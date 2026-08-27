#!/usr/bin/env python3
"""Generate compact, analysis-friendly JSONL files for the Hugging Face dataset."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

import tomllib


ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "tasks"
JOBS = ROOT / "jobs"
OUTPUT = ROOT / "data"


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def redact(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    value = re.sub(r"ant_[A-Za-z0-9_-]+", "ant_[REDACTED]", value)
    value = re.sub(r"hvs\.[A-Za-z0-9_-]+", "hvs.[REDACTED]", value)
    value = re.sub(
        r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----.*?-----END (?:[A-Z]+ )?PRIVATE KEY-----",
        "[PRIVATE KEY REDACTED]",
        value,
        flags=re.DOTALL,
    )
    return value


def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def duration_seconds(start: Any, finish: Any) -> float | None:
    begin = parse_time(start)
    end = parse_time(finish)
    if begin is None or end is None:
        return None
    return round((end - begin).total_seconds(), 3)


def environment_for(task_path: Path) -> dict[str, Any]:
    for name in ("harbor_antrieb.toml", "infraset.toml"):
        path = task_path / "environment" / name
        if path.is_file():
            try:
                parsed = tomllib.loads(path.read_text())
            except (OSError, tomllib.TOMLDecodeError):
                return {}
            return {
                "file": str(path.relative_to(ROOT)),
                "cluster": parsed.get("cluster", []),
                "network_mode": parsed.get("network_mode"),
                "control_node": parsed.get("control_node"),
                "initialize": parsed.get("initialize", []),
            }
    return {}


def task_records() -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    records: dict[str, dict[str, Any]] = {}
    for task_path in sorted(p for p in TASKS.glob("*/*") if p.is_dir()):
        task_file = task_path / "task.toml"
        if not task_file.is_file():
            continue
        try:
            task_config = tomllib.loads(task_file.read_text())
        except (OSError, tomllib.TOMLDecodeError):
            continue
        name = task_path.name
        records[name] = {
            "task_name": name,
            "category": task_path.parent.name,
            "instruction_path": str((task_path / "instruction.md").relative_to(ROOT)),
            "task_path": str(task_path.relative_to(ROOT)),
            "metadata": task_config.get("metadata", {}),
            "environment": environment_for(task_path),
        }
    return records, list(records.values())


def dimension_analysis(report: dict[str, Any]) -> list[dict[str, Any]]:
    dimensions = report.get("dimensions", {})
    if not isinstance(dimensions, dict):
        return []
    analyses = []
    for name, dimension in dimensions.items():
        if not isinstance(dimension, dict):
            continue
        coverage = dimension.get("coverage")
        score = dimension.get("score")
        reasons: list[str] = []
        for assertion in dimension.get("assertions", []):
            if not isinstance(assertion, dict):
                continue
            status = assertion.get("status")
            if status not in (None, "pass"):
                reason = assertion.get("summary") or f"assertion status: {status}"
                reasons.append(str(reason))
            for failure in assertion.get("failures", []):
                if failure:
                    reasons.append(str(failure))
            for limitation in assertion.get("limitations", []):
                if limitation:
                    reasons.append(f"limitation: {limitation}")
        if coverage is not None and coverage < 1:
            reasons.append(
                f"coverage was {coverage:.3f}; some authored assertions were not evaluated"
            )
        if not reasons and score is not None and score < 100:
            reasons.append(f"dimension score was {score:.1f} despite complete evaluation")
        analyses.append(
            {
                "dimension": name,
                "score": score,
                "coverage": coverage,
                "evaluated_points": dimension.get("evaluated_points"),
                "selected_points": dimension.get("selected_points"),
                "status": "complete" if coverage == 1 else "incomplete",
                "reasons": [redact(reason) for reason in dict.fromkeys(reasons)],
            }
        )
    return analyses


def provisioning_time_ms(trial_path: Path) -> int | None:
    payload = load_json(trial_path.parent / "provision-response.json")
    content = payload.get("content", [])
    if not isinstance(content, list):
        return None
    for item in content:
        if not isinstance(item, dict):
            continue
        try:
            response = json.loads(item.get("text", ""))
        except (TypeError, json.JSONDecodeError):
            continue
        if isinstance(response, dict) and isinstance(response.get("provision_time_ms"), (int, float)):
            return int(response["provision_time_ms"])
    return None


def main() -> int:
    task_map, tasks = task_records()
    jobs: dict[tuple[str, str], dict[str, Any]] = {}
    trials: list[dict[str, Any]] = []
    analyses: list[dict[str, Any]] = []
    task_trial_counts: defaultdict[str, int] = defaultdict(int)

    for result_path in sorted(JOBS.glob("*/*/*/result.json")):
        task_name = result_path.parts[-4]
        job_name = result_path.parts[-3]
        trial_name = result_path.parts[-2]
        result = load_json(result_path)
        task = task_map.get(task_name, {})
        rewards = ((result.get("verifier_result") or {}).get("rewards") or {})
        report_path = result_path.parent / "verifier" / "evaluation-report.json"
        report = load_json(report_path)
        exception = result.get("exception_info") or {}
        if not isinstance(exception, dict):
            exception = {"message": str(exception)}
        metrics = {
            key: rewards.get(key)
            for key in (
                "reward",
                "evaluation_coverage",
                "evaluation_complete",
                "functionality",
                "operational_hygiene",
                "publication_eligible",
            )
            if key in rewards
        }
        trial = {
            "task_name": task_name,
            "category": task.get("category"),
            "job_name": job_name,
            "trial_name": trial_name,
            "started_at": result.get("started_at"),
            "finished_at": result.get("finished_at"),
            "duration_seconds": duration_seconds(result.get("started_at"), result.get("finished_at")),
            "provisioning_time_ms": provisioning_time_ms(result_path),
            "model": ((result.get("agent_info") or {}).get("model_info") or {}).get("name"),
            "model_provider": ((result.get("agent_info") or {}).get("model_info") or {}).get("provider"),
            "metrics": metrics,
            "exception": {
                "type": exception.get("type") or exception.get("exception_type"),
                "message": redact(exception.get("message") or exception.get("exception_message")),
            }
            if exception
            else None,
            "result_path": str(result_path.relative_to(ROOT)),
            "instruction_path": task.get("instruction_path"),
            "environment": task.get("environment", {}),
        }
        trials.append(trial)
        task_trial_counts[task_name] += 1
        key = (task_name, job_name)
        jobs.setdefault(
            key,
            {
                "task_name": task_name,
                "category": task.get("category"),
                "job_name": job_name,
                "trial_count": 0,
                "job_path": str(result_path.parents[1].relative_to(ROOT)),
            },
        )
        jobs[key]["trial_count"] += 1
        analyses.append(
            {
                "task_name": task_name,
                "category": task.get("category"),
                "job_name": job_name,
                "trial_name": trial_name,
                "evaluation_complete": report.get("evaluation_complete"),
                "evaluation_coverage": report.get("evaluation_coverage"),
                "overall_summary": redact(report.get("overall_summary")),
                "dimensions": dimension_analysis(report),
                "exception": trial["exception"],
                "report_path": str(report_path.relative_to(ROOT)) if report_path.is_file() else None,
            }
        )

    OUTPUT.mkdir(exist_ok=True)
    outputs = {
        "tasks.jsonl": tasks,
        "jobs.jsonl": sorted(jobs.values(), key=lambda item: (item["task_name"], item["job_name"])),
        "trials.jsonl": sorted(trials, key=lambda item: (item["task_name"], item["job_name"], item["trial_name"])),
        "evaluation-analysis.jsonl": sorted(analyses, key=lambda item: (item["task_name"], item["job_name"], item["trial_name"])),
    }
    for filename, records in outputs.items():
        path = OUTPUT / filename
        with path.open("w") as stream:
            for record in records:
                stream.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
        print(f"wrote {len(records):4d} records to {path.relative_to(ROOT)}")
    print(f"indexed {len(task_map)} tasks and {len(trials)} trials")
    return 0


if __name__ == "__main__":
    sys.exit(main())
