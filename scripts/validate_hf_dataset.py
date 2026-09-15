#!/usr/bin/env python3
"""Validate the queryable Hugging Face tables and dataset card."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import pyarrow.parquet as pq


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DEFAULT_CARD = ROOT / "docs" / "hf-dataset-card.md"

RUN_COLUMNS = {
    "run_id",
    "category",
    "image",
    "task",
    "started_at_dir",
    "reward",
    "functionality",
    "evaluation_coverage",
    "operational_hygiene",
    "confidence",
    "evaluation_complete",
    "command_count",
    "node_count",
    "first_command_at",
    "last_command_at",
    "wall_seconds",
}
COMMAND_COLUMNS = {
    "run_id",
    "command_id",
    "sequence",
    "node",
    "command",
    "issued_at",
    "return_code",
    "duration_ms",
    "stdout",
    "stderr",
    "executor_attempt",
    "completed",
}
TASK_COLUMNS = {
    "task_path",
    "category",
    "image_dir",
    "slug",
    "difficulty",
    "agent_timeout_sec",
    "verifier_timeout_sec",
    "instruction",
    "cluster",
    "control_node",
    "environment_toml",
}


def read_table(name: str, expected_columns: set[str]) -> list[dict]:
    path = DATA / f"{name}.parquet"
    table = pq.read_table(path)
    columns = set(table.column_names)
    if columns != expected_columns:
        missing = sorted(expected_columns - columns)
        extra = sorted(columns - expected_columns)
        raise ValueError(f"{path}: missing={missing}, extra={extra}")
    return table.to_pylist()


def unique(values: list[object], label: str) -> None:
    if len(values) != len(set(values)):
        raise ValueError(f"duplicate {label}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--card", type=Path, default=DEFAULT_CARD)
    args = parser.parse_args()

    runs = read_table("runs", RUN_COLUMNS)
    commands = read_table("commands", COMMAND_COLUMNS)
    tasks = read_table("tasks", TASK_COLUMNS)

    run_ids = [row["run_id"] for row in runs]
    unique(run_ids, "run ID")
    unique([row["task_path"] for row in tasks], "task path")
    unique(
        [(row["run_id"], row["command_id"]) for row in commands],
        "command ID within a run",
    )

    unknown_runs = sorted({row["run_id"] for row in commands} - set(run_ids))
    if unknown_runs:
        raise ValueError(f"commands refer to unknown runs: {unknown_runs}")

    commands_by_run = Counter(row["run_id"] for row in commands)
    mismatches = [
        row["run_id"]
        for row in runs
        if row["command_count"] != commands_by_run[row["run_id"]]
    ]
    if mismatches:
        raise ValueError(f"run command counts disagree: {mismatches}")
    if any(row["node_count"] < 1 for row in runs):
        raise ValueError("every run must contain at least one provisioned VM")

    passed = sum(row["reward"] == 1.0 for row in runs)
    failed = len(runs) - passed
    table_names = ("runs", "commands", "tasks")
    size_mb = (
        sum((DATA / f"{name}.parquet").stat().st_size for name in table_names)
        / 1_000_000
    )

    card = args.card.read_text()
    required_text = (
        "config_name: runs",
        "config_name: commands",
        "config_name: tasks",
        f"{len(runs):,} are counted as LLM runs: "
        f"{passed:,} passed and {failed:,} failed",
        f"{len(commands):,} commands",
        f"{len(tasks):,} task definitions",
        f"{size_mb:.1f} MB compressed",
    )
    missing = [text for text in required_text if text not in card]
    if missing:
        raise ValueError(f"dataset card is missing: {missing}")

    vm_count = sum(row["node_count"] for row in runs)
    print(
        f"HF dataset valid: {len(runs):,} runs "
        f"({passed:,} passed, {failed:,} failed), "
        f"{len(commands):,} commands, {len(tasks):,} tasks, "
        f"{vm_count:,} VMs in LLM runs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
