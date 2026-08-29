#!/usr/bin/env python3
"""Generate compact, analysis-friendly JSONL files for the Hugging Face dataset."""

from __future__ import annotations

import json
import re
import sys
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
        environment = environment_for(task_path)
        records[name] = {
            "task_name": name,
            "category": task_path.parent.name,
            "instruction_path": str((task_path / "instruction.md").relative_to(ROOT)),
            "task_path": str(task_path.relative_to(ROOT)),
            "difficulty": task_config.get("metadata", {}).get("difficulty"),
            "environment_file": environment.get("file"),
            "environment_cluster": environment.get("cluster", []),
            "network_mode": environment.get("network_mode"),
            "control_node": environment.get("control_node"),
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


def summary_records() -> list[dict[str, Any]]:
    path = ROOT / "results-summary.md"
    records = []
    for line in path.read_text().splitlines():
        match = re.match(r"\|\s*(\d+)\s*\|(.+)\|", line)
        if not match:
            continue
        fields = [field.strip() for field in match.group(2).split("|")]
        if len(fields) != 9 or fields[0] == "Task":
            continue
        def number(value: str) -> float | None:
            return None if value == "—" else float(value)

        def percent(value: str) -> float | None:
            return None if value == "—" else float(value.rstrip("%"))

        records.append(
            {
                "row": int(match.group(1)),
                "task": fields[0],
                "environment": fields[1],
                "runs": int(fields[2]),
                "full_passes": fields[3],
                "best_score": number(fields[4]),
                "evaluation_coverage_percent": percent(fields[5]),
                "operational_hygiene_percent": percent(fields[6]),
                "provisioning_time": fields[7],
                "mean_duration": fields[8],
            }
        )
    return records


def main() -> int:
    task_map, tasks = task_records()
    jobs: dict[tuple[str, str], dict[str, Any]] = {}
    analyses: list[dict[str, Any]] = []

    for result_path in sorted(JOBS.glob("*/*/*/result.json")):
        task_name = result_path.parts[-4]
        job_name = result_path.parts[-3]
        trial_name = result_path.parts[-2]
        result = load_json(result_path)
        task = task_map.get(task_name, {})
        report_path = result_path.parent / "verifier" / "evaluation-report.json"
        report = load_json(report_path)
        exception = result.get("exception_info") or {}
        if not isinstance(exception, dict):
            exception = {"message": str(exception)}
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
        dimensions = dimension_analysis(report)
        incomplete = [item for item in dimensions if item.get("status") == "incomplete"]
        reasons = [
            f"{item['dimension']}: {reason}"
            for item in incomplete
            for reason in item.get("reasons", [])
        ]
        reasons = list(dict.fromkeys(reasons))
        analysis = redact(report.get("overall_summary")) or "No evaluator analysis was recorded."
        if reasons:
            analysis = f"{analysis} Reasons for incomplete evaluation: {'; '.join(reasons[:4])}"
        elif exception:
            analysis = "The trial ended before a complete evaluator analysis was recorded."
        analyses.append(
            {
                "task_name": task_name,
                "category": task.get("category"),
                "job_name": job_name,
                "trial_name": trial_name,
                "evaluation_complete": report.get("evaluation_complete"),
                "evaluation_coverage": report.get("evaluation_coverage"),
                "analysis": analysis,
                "report_path": str(report_path.relative_to(ROOT)) if report_path.is_file() else None,
            }
        )

    OUTPUT.mkdir(exist_ok=True)
    outputs = {
        "summary.jsonl": summary_records(),
        "tasks.jsonl": tasks,
        "jobs.jsonl": sorted(jobs.values(), key=lambda item: (item["task_name"], item["job_name"])),
        "evaluation-analysis.jsonl": sorted(analyses, key=lambda item: (item["task_name"], item["job_name"], item["trial_name"])),
    }
    for filename, records in outputs.items():
        path = OUTPUT / filename
        with path.open("w") as stream:
            for record in records:
                stream.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"wrote {len(records):4d} records to {path.relative_to(ROOT)}")
    print(f"indexed {len(task_map)} tasks, {len(jobs)} jobs, and {len(analyses)} evaluations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
