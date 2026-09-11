#!/usr/bin/env python3
"""Shared readers for calculations used by the findings article."""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path
from typing import Any, Iterator


ROOT = Path(__file__).resolve().parents[2]
TRANSPORT_FAILURE = re.compile(
    r"connection reset by peer"
    r"|connection timed out"
    r"|closed by remote host"
    r"|exec stream closed",
    re.IGNORECASE,
)


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def job_records() -> Iterator[tuple[Path, dict[str, Any]]]:
    """Yield job directories and their aggregate Harbor result."""
    for path in sorted(ROOT.glob("jobs/**/result.json")):
        value = read_json(path)
        if value is not None and "n_total_trials" in value:
            yield path.parent, value


def command_audits() -> Iterator[Path]:
    """Yield the canonical executor audit for every command-bearing run."""
    yield from sorted(ROOT.glob("jobs/**/agent/executor-commands.jsonl"))


def cluster_components(job_dir: Path) -> list[str]:
    """Expand a job's cluster declaration into one component per node."""
    line = next(
        row.split("=", 1)[1].strip()
        for row in (job_dir / "environment.toml").read_text().splitlines()
        if row.strip().startswith("cluster =")
    )
    declaration = ast.literal_eval(line)
    components: list[str] = []
    for item in declaration:
        match = re.fullmatch(r"(.+?)\s+x(\d+)", str(item))
        if match:
            components.extend([match.group(1)] * int(match.group(2)))
        else:
            components.append(str(item))
    return components


def cluster_size(job_dir: Path) -> int:
    return len(cluster_components(job_dir))


def trial_dir(audit: Path) -> Path:
    return audit.parent.parent


def job_dir(audit: Path) -> Path:
    return trial_dir(audit).parent


def category(audit: Path) -> str:
    return audit.relative_to(ROOT / "jobs").parts[0]


def task_name(audit: Path) -> str:
    return job_dir(audit).parent.name


def trial_result(audit: Path) -> dict[str, Any] | None:
    return read_json(trial_dir(audit) / "result.json")


def rewards(audit: Path) -> dict[str, Any]:
    result = trial_result(audit) or {}
    verifier = result.get("verifier_result") or {}
    value = verifier.get("rewards") or {}
    return value if isinstance(value, dict) else {}


def audit_records(audit: Path) -> Iterator[dict[str, Any]]:
    for line in audit.read_text(errors="replace").splitlines():
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            yield value


def is_transport_failure(record: dict[str, Any]) -> bool:
    return any(
        isinstance(record.get(field), str)
        and TRANSPORT_FAILURE.search(record[field])
        for field in ("stderr", "error")
    )


def node_components(audit: Path) -> dict[str, str]:
    """Map node names to components in declared provisioning order."""
    return {
        f"node{index}": component
        for index, component in enumerate(cluster_components(job_dir(audit)), 1)
    }


def provision_payload(job_dir: Path) -> dict[str, Any] | None:
    responses = sorted(job_dir.glob("*/provision-response.json"))
    if len(responses) != 1:
        return None
    outer = read_json(responses[0]) or {}
    for item in outer.get("content", []):
        if not isinstance(item, dict) or not isinstance(item.get("text"), str):
            continue
        try:
            value = json.loads(item["text"])
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            return value
    return None


def provisioned_node_count(job_dir: Path) -> int | None:
    payload = provision_payload(job_dir)
    nodes = (payload or {}).get("nodes")
    return len(nodes) if isinstance(nodes, list) else None


def command_counts(
    audit: Path,
    components: set[str] | None = None,
) -> dict[str, int]:
    """Count requests and terminal outcomes, optionally on selected components.

    Transport failures caused by reboot transitions are tracked separately.
    """
    mapping = node_components(audit)
    requested: set[str] = set()
    successful: set[str] = set()
    failed: set[str] = set()
    transport: set[str] = set()
    for record in audit_records(audit):
        if components is not None and mapping.get(record.get("node")) not in components:
            continue
        command_id = record.get("command_id")
        if not isinstance(command_id, str) or not command_id:
            continue
        if record.get("outcome") == "requested":
            requested.add(command_id)
            continue
        if record.get("outcome") != "completed":
            continue
        return_code = record.get("return_code")
        if not isinstance(return_code, int):
            continue
        if return_code == 0:
            successful.add(command_id)
        elif is_transport_failure(record):
            transport.add(command_id)
        else:
            failed.add(command_id)
    return {
        "requested": len(requested),
        "successful": len(successful),
        "failed": len(failed),
        "on_node": len(successful | failed),
        "transport": len(transport),
        "unfinished": len(requested - successful - failed - transport),
    }
