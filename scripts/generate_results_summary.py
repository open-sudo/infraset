#!/usr/bin/env python3
"""Generate the public InfraSet execution summary from recorded Harbor jobs."""

from __future__ import annotations

import ast
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
JOBS = ROOT / "jobs"
OUTPUT = ROOT / "results-summary.md"
DATA_OUTPUT = ROOT / "data" / "execution-summary.jsonl"


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def timestamp(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def environment(job_dir: Path) -> str:
    path = job_dir / "environment.toml"
    try:
        cluster_line = next(
            line.split("=", 1)[1].strip()
            for line in path.read_text().splitlines()
            if line.strip().startswith("cluster =")
        )
        value = ast.literal_eval(cluster_line)
    except (OSError, StopIteration, SyntaxError, ValueError):
        return "—"
    if not isinstance(value, list):
        return "—"
    clusters = [str(item) for item in value]
    return " + ".join(clusters) if clusters else "—"


def provision_time_ms(trial_dir: Path) -> float | None:
    payload = read_json(trial_dir / "provision-response.json")
    if payload is None:
        return None
    for item in payload.get("content", []):
        if not isinstance(item, dict) or item.get("type") != "text":
            continue
        text = item.get("text")
        if not isinstance(text, str):
            continue
        try:
            response = json.loads(text)
        except json.JSONDecodeError:
            continue
        value = response.get("provision_time_ms")
        if isinstance(value, (int, float)):
            return float(value)
    return None


def trial_dirs(job_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in job_dir.iterdir()
        if path.is_dir()
        and (path / "config.json").is_file()
        and (path / "result.json").is_file()
    )


def job_dirs(task_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in task_dir.iterdir()
        if path.is_dir() and (path / "result.json").is_file()
    )


def metric(rewards: dict[str, Any], name: str) -> float:
    value = rewards.get(name)
    return float(value) if isinstance(value, (int, float)) else 0.0


def task_record(task_dir: Path) -> dict[str, Any] | None:
    jobs = job_dirs(task_dir)
    if not jobs:
        return None

    trials: list[tuple[Path, dict[str, Any]]] = []
    for job_dir in jobs:
        for directory in trial_dirs(job_dir):
            result = read_json(directory / "result.json")
            if result is not None:
                trials.append((directory, result))
    if not trials:
        return None

    metrics: dict[str, list[float]] = defaultdict(list)
    successful_commands = 0
    failed_commands = 0
    exceptions = 0
    execution_durations: list[float] = []
    provisioning: list[float] = []
    analysis = ""
    lowest_reward = 2.0

    for directory, result in trials:
        rewards = result.get("verifier_result", {}).get("rewards", {})
        rewards = rewards if isinstance(rewards, dict) else {}
        reward = metric(rewards, "reward")
        for name in (
            "reward",
            "confidence",
            "evaluation_complete",
            "evaluation_coverage",
            "functionality",
            "operational_hygiene",
            "publication_eligible",
        ):
            metrics[name].append(metric(rewards, name))

        if result.get("exception_info") is not None:
            exceptions += 1

        agent_execution = result.get("agent_execution", {})
        agent_execution = (
            agent_execution if isinstance(agent_execution, dict) else {}
        )
        started = timestamp(agent_execution.get("started_at"))
        finished = timestamp(agent_execution.get("finished_at"))
        if started is not None and finished is not None:
            execution_durations.append((finished - started).total_seconds())

        provisioned = provision_time_ms(directory)
        if provisioned is not None:
            provisioning.append(provisioned)

        report = read_json(directory / "verifier" / "evaluation-report.json") or {}
        if reward < lowest_reward and reward < 1.0:
            summary = report.get("overall_summary")
            if isinstance(summary, str) and summary.strip():
                analysis = summary.strip()
            else:
                exception = result.get("exception_info", {})
                exception = exception if isinstance(exception, dict) else {}
                exception_type = exception.get("exception_type")
                analysis = (
                    f"The trial ended with {exception_type}."
                    if isinstance(exception_type, str)
                    else "The recorded evidence did not support a full outcome."
                )
            lowest_reward = reward
        command_stats = report.get("command_stats", {})
        command_stats = command_stats if isinstance(command_stats, dict) else {}
        successful_commands += int(command_stats.get("successful", 0) or 0)
        failed_commands += int(command_stats.get("failed", 0) or 0)

    return {
        "task": task_dir.name,
        "environment": environment(jobs[-1]),
        "trials": len(trials),
        "exceptions": exceptions,
        "commands": f"{successful_commands}/{failed_commands}",
        **{name: mean(values) for name, values in metrics.items()},
        "provisioning_seconds": mean(provisioning) / 1000,
        "execution_seconds": mean(execution_durations),
        "analysis": analysis,
    }


def records() -> list[dict[str, Any]]:
    values = []
    for task_dir in sorted(path for path in JOBS.iterdir() if path.is_dir()):
        record = task_record(task_dir)
        if record is not None:
            values.append(record)
    return values


def format_duration(seconds: float) -> str:
    rounded = round(seconds)
    return f"{rounded // 60}m {rounded % 60:02d}s"


def read_intro() -> str:
    readme = (ROOT / "README.md").read_text()
    return readme.split("\n## What makes InfraSet different", 1)[0].rstrip()


def summary_table(values: list[dict[str, Any]]) -> str:
    lines = [
        "| Task | Environment | Trials | Exceptions | Commands | Reward | Confidence | Evaluation complete | Coverage | Functionality | Hygiene | Publishable | Provisioning time | Execution time | Analysis |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for record in values:
        lines.append(
            "| {task} | {environment} | {trials} | {exceptions} | "
            "{commands} | "
            "{reward:.3f} | {confidence:.3f} | {evaluation_complete:.3f} | "
            "{evaluation_coverage:.3f} | {functionality:.3f} | "
            "{operational_hygiene:.3f} | {publication_eligible:.3f} | "
            "{provisioning_seconds:.2f}s | {execution_time} | {analysis_text} |".format(
                **record,
                execution_time=format_duration(record["execution_seconds"]),
                analysis_text=(record["analysis"] or "—").replace("|", "\\|"),
            )
        )
    return "\n".join(lines)


def main() -> int:
    values = records()
    trials = sum(record["trials"] for record in values)
    successful = sum(int(record["commands"].split("/", 1)[0]) for record in values)
    failed = sum(int(record["commands"].split("/", 1)[1]) for record in values)
    content = f"""{read_intro()}

## Execution summary

This table summarizes the recorded [jobs](https://github.com/open-sudo/infraset/tree/main/jobs). Metrics and times are averages across recorded trials. `Commands` reports successful/failed executor commands from the provider-captured audit. Unfinished or indeterminate command records are excluded from both values. A failed command records an unsuccessful attempt; it does not by itself mean that the final task outcome failed.

`Reward` measures the supported outcome, while `Confidence` reflects the completeness and quality of its evidence. `Operational hygiene` measures attributable residue or unrelated regression found by applicable global checks. A hygiene score of `1.000` means all applicable checks passed; `0.000` means none passed.

The current dataset contains {len(values)} tasks, {trials} trials, and {successful + failed} completed executor commands: {successful} successful and {failed} failed.

{summary_table(values)}
"""
    OUTPUT.write_text(content)
    DATA_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with DATA_OUTPUT.open("w") as stream:
        for record in values:
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"wrote {len(values)} task rows to {OUTPUT.relative_to(ROOT)}")
    print(f"wrote {len(values)} task records to {DATA_OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
