#!/usr/bin/env python3
"""Validate InfraSet's Hugging Face card and fixed-schema JSONL files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "data" / "execution-summary.jsonl"
COLLECTOR = ROOT / "data" / "collector-observations.jsonl"
DEFAULT_CARD = Path("/tmp/infraset-hf-card.md")

SUMMARY_KEYS = {
    "task",
    "environment",
    "commands",
    "reward",
    "evaluation_coverage",
    "functionality",
    "operational_hygiene",
    "provisioning_seconds",
    "execution_seconds",
}
COLLECTOR_KEYS = {
    "task",
    "job",
    "trial",
    "collector_attempt",
    "cluster_number",
    "prepare_enabled",
    "phase",
    "phase_status",
    "lifecycle_outcome",
    "captured_at",
    "node",
    "image",
    "observation_id",
    "observation_description",
    "observation_status",
    "return_code",
    "duration_ms",
    "stdout",
    "stderr",
    "error",
    "source_path",
}


def rows(path: Path, expected_keys: set[str]) -> list[dict[str, Any]]:
    result = []
    with path.open() as stream:
        for line_number, line in enumerate(stream, start=1):
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON") from exc
            if not isinstance(value, dict):
                raise TypeError(f"{path}:{line_number}: row is not an object")
            if set(value) != expected_keys:
                missing = sorted(expected_keys - set(value))
                extra = sorted(set(value) - expected_keys)
                raise ValueError(
                    f"{path}:{line_number}: schema mismatch; "
                    f"missing={missing}, extra={extra}"
                )
            result.append(value)
    if not result:
        raise ValueError(f"{path}: dataset is empty")
    return result


def validate_column_types(path: Path, values: list[dict[str, Any]]) -> None:
    for key in values[0]:
        types = {type(row[key]) for row in values if row[key] is not None}
        if len(types) > 1 and not types <= {int, float}:
            names = sorted(item.__name__ for item in types)
            raise TypeError(f"{path}: column {key!r} mixes types {names}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--card", type=Path, default=DEFAULT_CARD)
    args = parser.parse_args()

    summary = rows(SUMMARY, SUMMARY_KEYS)
    collector = rows(COLLECTOR, COLLECTOR_KEYS)
    validate_column_types(SUMMARY, summary)
    validate_column_types(COLLECTOR, collector)

    invalid_commands = [
        row["commands"]
        for row in summary
        if not isinstance(row["commands"], str)
        or re.fullmatch(
            r"(?:\d+/\d+(?: \((?:none issued|no terminal result)\))?"
            r"(?:; \d+ audit unavailable)?|audit unavailable)",
            row["commands"],
        )
        is None
    ]
    if invalid_commands:
        raise ValueError(
            "execution-summary commands must contain successful/failed counts or "
            "an explicit audit-availability state"
        )

    summary_tasks = [str(row["task"]) for row in summary]
    if len(summary_tasks) != len(set(summary_tasks)):
        raise ValueError("execution summary contains duplicate task rows")
    collector_tasks = {str(row["task"]) for row in collector}
    if set(summary_tasks) != collector_tasks:
        raise ValueError(
            "collector and execution-summary task sets differ: "
            f"summary_only={sorted(set(summary_tasks) - collector_tasks)}, "
            f"collector_only={sorted(collector_tasks - set(summary_tasks))}"
        )

    phases = {str(row["phase"]) for row in collector}
    unexpected_phases = phases - {
        "before_prepare",
        "after_prepare",
        "after_executor",
    }
    if unexpected_phases:
        raise ValueError(f"collector contains unknown phases: {unexpected_phases}")

    card = args.card.read_text()
    for required in (
        "config_name: execution-summary",
        "path: data/execution-summary.jsonl",
        "config_name: collector",
        "path: data/collector-observations.jsonl",
    ):
        if required not in card:
            raise ValueError(f"dataset card is missing {required!r}")

    print(
        f"HF dataset valid: {len(summary)} task summaries, "
        f"{len(collector)} collector observations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
