#!/usr/bin/env python3
"""Generate the public InfraSet execution summary from recorded Harbor jobs."""

from __future__ import annotations

import ast
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
JOBS = ROOT / "jobs"
OUTPUT = ROOT / "results-summary.md"
DATA_OUTPUT = ROOT / "data" / "execution-summary.jsonl"
GITHUB_BLOB = "https://github.com/open-sudo/infraset/blob/main"


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
    clusters = []
    for item in value:
        label = str(item)
        match = re.fullmatch(r"(.+?)\s+x(\d+)", label)
        clusters.append(f"{match.group(2)} {match.group(1)}" if match else label)
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


def command_audit_paths(trial_dir: Path) -> tuple[list[Path], str]:
    canonical = trial_dir / "agent" / "executor-commands.jsonl"
    if canonical.is_file():
        return [canonical], "available"
    attempts = sorted(
        (trial_dir / "agent" / "attempts").glob("*/executor-commands.jsonl")
    )
    if attempts:
        return attempts, "attempt_fallback"
    return [], "unavailable"


def command_audit_stats(trial_dir: Path) -> dict[str, Any]:
    paths, status = command_audit_paths(trial_dir)
    requested: set[str] = set()
    terminal: set[str] = set()
    successful = failed = anonymous = 0
    for path in paths:
        for line in path.read_text(errors="replace").splitlines():
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(record, dict):
                continue
            command_id = record.get("command_id")
            if not isinstance(command_id, str) or not command_id:
                anonymous += 1
                command_id = f"anonymous-{anonymous}"
            outcome = record.get("outcome")
            if outcome == "requested":
                requested.add(command_id)
                continue
            terminal.add(command_id)
            return_code = record.get("return_code")
            if outcome == "completed" and return_code == 0:
                successful += 1
            elif outcome == "completed" and isinstance(return_code, int):
                failed += 1
    return {
        "status": status,
        "issued": len(requested | terminal),
        "successful": successful,
        "failed": failed,
        "unfinished": len(requested - terminal),
    }


def command_display(
    successful: int,
    failed: int,
    issued: int,
    available_trials: int,
    unavailable_trials: int,
) -> str:
    if available_trials == 0:
        return "audit unavailable"
    if successful == 0 and failed == 0:
        value = "0/0 (none issued)" if issued == 0 else "0/0 (no terminal result)"
    else:
        value = f"{successful}/{failed}"
    if unavailable_trials:
        value += f"; {unavailable_trials} audit unavailable"
    return value


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
    issued_commands = 0
    available_command_audits = 0
    unavailable_command_audits = 0
    execution_durations: list[float] = []
    provisioning: list[float] = []

    for directory, result in trials:
        rewards = result.get("verifier_result", {}).get("rewards", {})
        rewards = rewards if isinstance(rewards, dict) else {}
        for name in (
            "reward",
            "evaluation_coverage",
            "functionality",
            "operational_hygiene",
        ):
            metrics[name].append(metric(rewards, name))

        agent_execution = result.get("agent_execution", {})
        agent_execution = agent_execution if isinstance(agent_execution, dict) else {}
        started = timestamp(agent_execution.get("started_at"))
        finished = timestamp(agent_execution.get("finished_at"))
        if started is not None and finished is not None:
            execution_durations.append((finished - started).total_seconds())

        provisioned = provision_time_ms(directory)
        if provisioned is not None:
            provisioning.append(provisioned)

        command_stats = command_audit_stats(directory)
        successful_commands += command_stats["successful"]
        failed_commands += command_stats["failed"]
        issued_commands += command_stats["issued"]
        if command_stats["status"] == "unavailable":
            unavailable_command_audits += 1
        else:
            available_command_audits += 1

    return {
        "task": task_dir.name,
        "_analysis_url": (
            f"{GITHUB_BLOB}/jobs/{task_dir.name}/{jobs[-1].name}/analysis.md"
        ),
        "environment": environment(jobs[-1]),
        "commands": command_display(
            successful_commands,
            failed_commands,
            issued_commands,
            available_command_audits,
            unavailable_command_audits,
        ),
        "_successful_commands": successful_commands,
        "_failed_commands": failed_commands,
        **{name: mean(values) for name, values in metrics.items()},
        "provisioning_seconds": mean(provisioning) / 1000,
        "execution_seconds": mean(execution_durations),
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
        "| Task | Environment | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for record in values:
        task_link = f"[{record['task']}]({record['_analysis_url']})"
        lines.append(
            "| {task_link} | {environment} | "
            "{commands} | "
            "{reward:.3f} | {evaluation_coverage:.3f} | {functionality:.3f} | "
            "{operational_hygiene:.3f} | "
            "{provisioning_seconds:.2f}s | {execution_time} |".format(
                **record,
                task_link=task_link,
                execution_time=format_duration(record["execution_seconds"]),
            )
        )
    return "\n".join(lines)


def main() -> int:
    values = records()
    successful = sum(record["_successful_commands"] for record in values)
    failed = sum(record["_failed_commands"] for record in values)
    content = f"""{read_intro()}

## Execution summary

This table summarizes the recorded [jobs](https://github.com/open-sudo/infraset/tree/main/jobs). Metrics and times are averages across recorded trials. `Commands` reports successful/failed executor commands read directly from the provider-captured audit. Unfinished or indeterminate command records are excluded from both values. `0/0 (none issued)` means an audit was captured but contains no command request; `audit unavailable` means no canonical or per-attempt audit artifact exists. A failed command records an unsuccessful attempt; it does not by itself mean that the final task outcome failed.

`Reward` measures the supported outcome. `Operational hygiene` measures unnecessary mutations during execution, attributable residue, and unrelated regression. A hygiene score of `1.000` means the verifier found none of these problems; `0.000` means the execution received no hygiene credit.

The current dataset contains {len(values)} tasks and {successful + failed} completed executor commands: {successful} successful and {failed} failed.

{summary_table(values)}
"""
    OUTPUT.write_text(content)
    DATA_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with DATA_OUTPUT.open("w") as stream:
        for record in values:
            dataset_record = {
                key: value for key, value in record.items() if not key.startswith("_")
            }
            stream.write(json.dumps(dataset_record, ensure_ascii=False) + "\n")
    print(f"wrote {len(values)} task rows to {OUTPUT.relative_to(ROOT)}")
    print(f"wrote {len(values)} task records to {DATA_OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
