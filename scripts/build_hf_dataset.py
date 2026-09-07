#!/usr/bin/env python3
"""Flatten the InfraSet job tree into Parquet tables for Hugging Face.

The published tree keeps every artifact a run produced, which is what makes the
dataset auditable but not queryable. This script derives three flat tables from
it so the traces can be mined without walking 31k files:

  runs      one row per scored run, with the verifier's six metrics
  commands  one row per command the executor issued, with output
  tasks     one row per authored task definition

Nothing is redacted or truncated. The tables are a view over the tree, not a
replacement for it.
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and earlier
    import tomli as tomllib

REPOSITORY = Path(__file__).resolve().parents[1]
JOBS_ROOT = REPOSITORY / "jobs"
TASKS_ROOT = REPOSITORY / "tasks"
OUTPUT_ROOT = REPOSITORY / "data"

METRICS = (
    "reward",
    "functionality",
    "evaluation_coverage",
    "operational_hygiene",
    "confidence",
    "evaluation_complete",
)


def parse_timestamp(value: str) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).replace(tzinfo=None)
    except ValueError:
        return None


def run_identity(command_log: Path) -> dict[str, str]:
    """Derive category, image, task family and run id from the job path.

    Job paths are <jobs>/<category>/<image>/<task>/<timestamp>/<cluster>/agent/…
    """
    parts = command_log.relative_to(JOBS_ROOT).parts
    category, image, task, stamp, cluster = parts[0], parts[1], parts[2], parts[3], parts[4]
    return {
        "run_id": f"{category}/{image}/{task}/{stamp}/{cluster}",
        "category": category,
        "image": image,
        "task": task,
        "started_at_dir": stamp,
    }


def read_rewards(job_dir: Path) -> dict[str, float | None]:
    result = job_dir / "result.json"
    if not result.exists():
        return {name: None for name in METRICS}
    try:
        payload = json.loads(result.read_text())
    except (json.JSONDecodeError, OSError):
        return {name: None for name in METRICS}
    rewards = (payload.get("verifier_result") or {}).get("rewards") or {}
    return {name: rewards.get(name) for name in METRICS}


def load_commands(command_log: Path) -> list[dict]:
    """Merge the audit log's requested/completed pair into one row per command.

    The log writes two records per command sharing a command_id: the request,
    which carries the issue time, and the completion, which carries the return
    code and output.
    """
    requested: dict[str, dict] = {}
    order: list[str] = []
    completed: dict[str, dict] = {}
    for line in command_log.read_text(errors="replace").splitlines():
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        command_id = record.get("command_id")
        if not command_id:
            continue
        if record.get("outcome") == "requested":
            if command_id not in requested:
                order.append(command_id)
            requested[command_id] = record
        elif record.get("outcome") == "completed":
            completed[command_id] = record

    rows = []
    for sequence, command_id in enumerate(order, start=1):
        issue = requested[command_id]
        done = completed.get(command_id, {})
        rows.append(
            {
                "command_id": command_id,
                "sequence": sequence,
                "node": issue.get("node"),
                "command": issue.get("command"),
                "issued_at": parse_timestamp(issue.get("timestamp") or ""),
                "return_code": done.get("return_code"),
                "duration_ms": done.get("duration_ms"),
                "stdout": done.get("stdout"),
                "stderr": done.get("stderr"),
                "executor_attempt": issue.get("executor_attempt"),
                "completed": command_id in completed,
            }
        )
    return rows


def build_runs_and_commands() -> tuple[list[dict], list[dict]]:
    runs: list[dict] = []
    commands: list[dict] = []
    for command_log in sorted(JOBS_ROOT.rglob("agent/executor-commands.jsonl")):
        if "/attempts/" in str(command_log):
            continue
        identity = run_identity(command_log)
        job_dir = command_log.parents[1]
        rows = load_commands(command_log)

        stamps = [row["issued_at"] for row in rows if row["issued_at"]]
        duration = (max(stamps) - min(stamps)).total_seconds() if len(stamps) > 1 else None

        runs.append(
            {
                **identity,
                **read_rewards(job_dir),
                "command_count": len(rows),
                "node_count": len({row["node"] for row in rows if row["node"]}),
                "first_command_at": min(stamps) if stamps else None,
                "last_command_at": max(stamps) if stamps else None,
                "wall_seconds": duration,
            }
        )
        for row in rows:
            commands.append({"run_id": identity["run_id"], **row})
    return runs, commands


def build_tasks() -> list[dict]:
    tasks: list[dict] = []
    for instruction in sorted(TASKS_ROOT.rglob("instruction.md")):
        task_dir = instruction.parent
        parts = task_dir.relative_to(TASKS_ROOT).parts
        config: dict = {}
        config_path = task_dir / "task.toml"
        if config_path.exists():
            try:
                with config_path.open("rb") as handle:
                    config = tomllib.load(handle)
            except Exception:
                config = {}
        environment = ""
        environment_path = task_dir / "environment" / "harbor_antrieb.toml"
        if environment_path.exists():
            environment = environment_path.read_text(errors="replace")
        cluster = re.search(r"^cluster\s*=\s*(.+)$", environment, re.M)
        control = re.search(r'^control_node\s*=\s*"([^"]+)"', environment, re.M)
        tasks.append(
            {
                "task_path": str(task_dir.relative_to(REPOSITORY)),
                "category": parts[0],
                "image_dir": parts[1] if len(parts) > 2 else None,
                "slug": task_dir.name,
                "difficulty": (config.get("metadata") or {}).get("difficulty"),
                "agent_timeout_sec": (config.get("agent") or {}).get("timeout_sec"),
                "verifier_timeout_sec": (config.get("verifier") or {}).get("timeout_sec"),
                "instruction": instruction.read_text(errors="replace"),
                "cluster": cluster.group(1).strip() if cluster else None,
                "control_node": control.group(1) if control else None,
                "environment_toml": environment,
            }
        )
    return tasks


def write_table(rows: list[dict], name: str) -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    table = pa.Table.from_pylist(rows)
    destination = OUTPUT_ROOT / f"{name}.parquet"
    pq.write_table(table, destination, compression="zstd")
    size_mb = destination.stat().st_size / 1024 / 1024
    print(f"  {name:9} {len(rows):7} rows  {size_mb:6.1f} MB  {destination.relative_to(REPOSITORY)}")


def main() -> int:
    print("Building Parquet tables from the job tree")
    runs, commands = build_runs_and_commands()
    tasks = build_tasks()
    write_table(runs, "runs")
    write_table(commands, "commands")
    write_table(tasks, "tasks")
    scored = sum(1 for run in runs if run["reward"] is not None)
    print(f"\n{len(runs)} runs ({scored} scored), {len(commands)} commands, {len(tasks)} tasks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
