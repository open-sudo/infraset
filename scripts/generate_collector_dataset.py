#!/usr/bin/env python3
"""Flatten lifecycle collector artifacts into a Hugging Face-friendly JSONL split."""

from __future__ import annotations

import argparse
import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JOBS = ROOT / "jobs"
DEFAULT_OUTPUT = ROOT / "data" / "collector-observations.jsonl"
PHASES = ("before_prepare", "after_prepare", "after_executor")


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def base_row(
    *,
    task: str,
    job: str,
    trial: str,
    attempt: int,
    cluster_number: int,
    prepare_enabled: str,
    phase: str,
    phase_status: str,
    lifecycle_outcome: str,
    captured_at: str,
    source_path: str,
) -> dict[str, Any]:
    return {
        "task": task,
        "job": job,
        "trial": trial,
        "collector_attempt": attempt,
        "cluster_number": cluster_number,
        "prepare_enabled": prepare_enabled,
        "phase": phase,
        "phase_status": phase_status,
        "lifecycle_outcome": lifecycle_outcome,
        "captured_at": captured_at,
        "node": "",
        "image": "",
        "observation_id": "",
        "observation_description": "",
        "observation_status": "",
        "return_code": None,
        "duration_ms": None,
        "stdout": "",
        "stderr": "",
        "error": "",
        "source_path": source_path,
    }


def snapshot_rows(
    phase_row: dict[str, Any], snapshot: dict[str, Any]
) -> Iterable[dict[str, Any]]:
    found = False
    for node in snapshot.get("nodes", []):
        if not isinstance(node, dict):
            continue
        image = node.get("image", {})
        image_ani = image.get("ani") if isinstance(image, dict) else None
        for observation in node.get("observations", []):
            if not isinstance(observation, dict):
                continue
            found = True
            yield {
                **phase_row,
                "node": str(node.get("name", "")),
                "image": str(image_ani) if image_ani is not None else "",
                "observation_id": str(observation.get("id", "")),
                "observation_description": str(
                    observation.get("description", "")
                ),
                "observation_status": str(observation.get("status", "")),
                "return_code": (
                    observation.get("return_code")
                    if isinstance(observation.get("return_code"), int)
                    else None
                ),
                "duration_ms": (
                    observation.get("duration_ms")
                    if isinstance(observation.get("duration_ms"), int)
                    else None
                ),
                "stdout": (
                    str(observation.get("stdout"))
                    if observation.get("stdout") is not None
                    else ""
                ),
                "stderr": (
                    str(observation.get("stderr"))
                    if observation.get("stderr") is not None
                    else ""
                ),
                "error": (
                    str(observation.get("error"))
                    if observation.get("error") is not None
                    else ""
                ),
            }
    if not found:
        limitations = snapshot.get("limitations", [])
        yield {
            **phase_row,
            "observation_id": f"collector:{phase_row['phase']}",
            "observation_description": "Lifecycle snapshot availability.",
            "observation_status": "unavailable",
            "error": "; ".join(str(item) for item in limitations),
        }


def collector_rows(
    trial_dir: Path, *, task: str, job: str, trial: str
) -> Iterable[dict[str, Any]]:
    attempts_dir = trial_dir / "collector" / "attempts"
    if not attempts_dir.is_dir():
        yield from legacy_rows(trial_dir, task=task, job=job, trial=trial)
        return
    for attempt_dir in sorted(path for path in attempts_dir.iterdir() if path.is_dir()):
        manifest = read_json(attempt_dir / "manifest.json") or {}
        attempt_value = manifest.get("attempt")
        attempt = attempt_value if isinstance(attempt_value, int) else 0
        cluster_value = manifest.get("cluster_number")
        cluster_number = cluster_value if isinstance(cluster_value, int) else 0
        prepare_value = manifest.get("prepare_enabled")
        prepare_enabled = (
            str(prepare_value).lower()
            if isinstance(prepare_value, bool)
            else "unknown"
        )
        phases = manifest.get("phases", {})
        phases = phases if isinstance(phases, dict) else {}
        for phase in PHASES:
            phase_record = phases.get(phase, {})
            phase_record = phase_record if isinstance(phase_record, dict) else {}
            same_as = phase_record.get("same_as")
            same_as = same_as if isinstance(same_as, str) else None
            if same_as is not None:
                # A disabled preparer deliberately collapses this phase into the
                # before-prepare snapshot; do not duplicate every observation.
                continue
            path_value = phase_record.get("path")
            snapshot_path = (
                trial_dir / path_value
                if isinstance(path_value, str)
                else attempt_dir
                / "snapshots"
                / f"{phase.replace('_', '-')}.json"
            )
            snapshot = read_json(snapshot_path)
            captured_at = (
                snapshot.get("captured_at") if snapshot is not None else None
            )
            source = (
                display_path(snapshot_path)
                if snapshot_path.exists()
                else display_path(attempt_dir / "manifest.json")
            )
            row = base_row(
                task=task,
                job=job,
                trial=trial,
                attempt=attempt,
                cluster_number=cluster_number,
                prepare_enabled=prepare_enabled,
                phase=phase,
                phase_status=str(phase_record.get("status", "missing")),
                lifecycle_outcome=(
                    str(phase_record.get("lifecycle_outcome"))
                    if phase_record.get("lifecycle_outcome") is not None
                    else "unknown"
                ),
                captured_at=str(captured_at) if captured_at is not None else "",
                source_path=source,
            )
            if snapshot is None:
                yield {
                    **row,
                    "observation_id": f"collector:{phase}",
                    "observation_description": "Lifecycle snapshot availability.",
                    "observation_status": "unavailable",
                    "error": "The lifecycle snapshot file was unavailable.",
                }
            else:
                yield from snapshot_rows(row, snapshot)


def legacy_rows(
    trial_dir: Path, *, task: str, job: str, trial: str
) -> Iterable[dict[str, Any]]:
    legacy = (
        ("after_prepare", trial_dir / "environment-baseline.json"),
        ("after_executor", trial_dir / "verifier" / "environment-post.json"),
    )
    for phase, path in legacy:
        snapshot = read_json(path)
        if snapshot is None:
            continue
        row = base_row(
            task=task,
            job=job,
            trial=trial,
            attempt=0,
            cluster_number=0,
            prepare_enabled="unknown",
            phase=phase,
            phase_status="legacy",
            lifecycle_outcome="unknown",
            captured_at=(
                str(snapshot.get("captured_at"))
                if snapshot.get("captured_at") is not None
                else ""
            ),
            source_path=display_path(path),
        )
        yield from snapshot_rows(row, snapshot)


def rows(jobs_dir: Path) -> Iterable[dict[str, Any]]:
    for task_dir in sorted(path for path in jobs_dir.iterdir() if path.is_dir()):
        for job_dir in sorted(path for path in task_dir.iterdir() if path.is_dir()):
            for trial_dir in sorted(path for path in job_dir.iterdir() if path.is_dir()):
                if not (trial_dir / "config.json").is_file():
                    continue
                yield from collector_rows(
                    trial_dir,
                    task=task_dir.name,
                    job=job_dir.name,
                    trial=trial_dir.name,
                )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=Path, default=DEFAULT_JOBS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with args.output.open("w") as stream:
        for record in rows(args.jobs):
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
    print(f"wrote {count} collector records to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
