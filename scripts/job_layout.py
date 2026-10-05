"""Shared discovery for InfraSet job layouts."""

from __future__ import annotations

import json
import re
import tomllib
from functools import lru_cache
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


RUN_NAME = re.compile(r"^\d{4}-\d{2}-\d{2}__\d{2}-\d{2}-\d{2}$")


@lru_cache(maxsize=None)
def _migration_paths(jobs_root: Path) -> dict:
    path = jobs_root.parent / 'data/job-layout.json'
    return json.loads(path.read_text())['jobs'] if path.is_file() else {}


def resolve_job_path(path: Path, jobs_root: Path) -> Path:
    """Resolve a saved pre-migration job or trial path without rewriting history."""
    parts = path.relative_to(jobs_root).parts
    mapping = _migration_paths(jobs_root)
    for length in range(len(parts), 0, -1):
        key = '/'.join(parts[:length])
        if key in mapping:
            return jobs_root / mapping[key] / Path(*parts[length:])
    return path


@dataclass(frozen=True)
class JobLocation:
    runner: str
    run_name: str
    task_parts: tuple[str, ...]

    @property
    def category(self) -> str:
        return self.task_parts[0]

    @property
    def task_name(self) -> str:
        return self.task_parts[-1]


def iter_job_dirs(jobs_root: Path) -> Iterator[Path]:
    """Yield Harbor aggregate-job directories under either supported layout."""
    for result_path in sorted(jobs_root.rglob("result.json")):
        try:
            payload = json.loads(result_path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(payload, dict) and "n_total_trials" in payload:
            yield result_path.parent


def job_location(job_dir: Path, jobs_root: Path) -> JobLocation:
    """Describe a job under the task/date layout or older layouts."""
    parts = job_dir.relative_to(jobs_root).parts
    metadata_path = job_dir / 'variant.toml'
    if metadata_path.is_file():
        metadata = tomllib.loads(metadata_path.read_text())
        scenario_id = metadata.get('id', '')
        # Also support callers scoped to jobs/<id> or jobs/<id>/<timestamp>.
        if (job_dir.parent.parent.name == scenario_id
                and job_dir.name.endswith('-' + scenario_id)):
            return JobLocation(
                runner=scenario_id,
                run_name=job_dir.parent.name,
                task_parts=(metadata['category'], metadata['os'], job_dir.name),
            )
    if len(parts) == 2 and RUN_NAME.fullmatch(parts[-1]):
        metadata_path = job_dir / 'variant.toml'
        if metadata_path.is_file():
            metadata = tomllib.loads(metadata_path.read_text())
            scenario_id = metadata.get('id', '')
            if scenario_id and parts[0].endswith('-' + scenario_id):
                return JobLocation(
                    runner=scenario_id,
                    run_name=parts[-1],
                    task_parts=(metadata['category'], metadata['os'], parts[0]),
                )
    if RUN_NAME.fullmatch(jobs_root.name) and parts:
        return JobLocation(
            runner=jobs_root.parent.name,
            run_name=jobs_root.name,
            task_parts=parts,
        )
    if len(parts) >= 2 and RUN_NAME.fullmatch(parts[0]):
        return JobLocation(
            runner=jobs_root.name,
            run_name=parts[0],
            task_parts=parts[1:],
        )
    if len(parts) >= 2 and RUN_NAME.fullmatch(parts[1]):
        return JobLocation(
            runner=jobs_root.name,
            run_name=parts[1],
            task_parts=(parts[0], *parts[2:]),
        )
    if len(parts) >= 3 and RUN_NAME.fullmatch(parts[2]):
        return JobLocation(
            runner=parts[0],
            run_name=parts[2],
            task_parts=(parts[1], *parts[3:]),
        )
    if len(parts) >= 3 and RUN_NAME.fullmatch(parts[1]):
        return JobLocation(
            runner=parts[0],
            run_name=parts[1],
            task_parts=parts[2:],
        )
    if len(parts) >= 2 and RUN_NAME.fullmatch(parts[-1]):
        return JobLocation(
            runner="vanilla",
            run_name=parts[-1],
            task_parts=parts[:-1],
        )
    raise ValueError(f"unrecognized InfraSet job path: {job_dir}")
