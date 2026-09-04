#!/usr/bin/env python3
"""Generate the clustered-services task matrix from its catalog.

Each task family asks for a named stateful service in a clustered
configuration, and the operating system underneath it varies across the
matrix. Every node in a cluster runs the same image, so the comparison
stays focused on how the executor adapts the same clustering job to each
distribution's packages, service manager, and defaults.

Clusters use the provider's default network: the members need to reach
each other and the internet, which is exactly what it provides.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and earlier
    import tomli as tomllib


REPOSITORY = Path(__file__).resolve().parents[1]
MATRIX_ROOT = REPOSITORY / "tasks" / "clustered-services"
CATALOG_PATH = MATRIX_ROOT / "catalog.toml"

SENTINEL = """#!/bin/sh
echo "InfraSet requires the configured Harbor-Antrieb verifier." >&2
exit 1
"""

# Forming a cluster means installing and configuring a service on every
# member, which takes longer than the single-service tasks in the other
# matrices; the legacy images are slower again.
TASK_CONFIG = """schema_version = "1.4"

[metadata]
author_name = "InfraSet"
difficulty = "{difficulty}"
category = "infrastructure"

[agent]
timeout_sec = 2400

[verifier]
timeout_sec = 1800
environment_mode = "shared"

[environment]
network_mode = "public"
"""


def clean_block(value: str) -> str:
    return textwrap.dedent(value).strip() + "\n"


def write(path: Path, content: str, mode: int | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    if mode is not None:
        path.chmod(mode)


def validate_catalog(catalog: dict[str, object]) -> tuple[list[dict], list[dict]]:
    systems = catalog.get("operating_systems")
    tasks = catalog.get("tasks")
    if not isinstance(systems, list) or not isinstance(tasks, list):
        raise ValueError("catalog requires operating_systems and tasks arrays")
    if len(systems) != 8:
        raise ValueError(f"expected 8 operating systems, found {len(systems)}")
    if len(tasks) != 10:
        raise ValueError(f"expected 10 task families, found {len(tasks)}")

    os_ids = [item.get("id") for item in systems if isinstance(item, dict)]
    slugs = [item.get("slug") for item in tasks if isinstance(item, dict)]
    numbers = [item.get("number") for item in tasks if isinstance(item, dict)]
    if len(set(os_ids)) != 8:
        raise ValueError("operating-system IDs must be unique")
    if len(set(slugs)) != 10:
        raise ValueError("task slugs must be unique")
    if numbers != list(range(1, 11)):
        raise ValueError("task numbers must be consecutive from 1 through 10")

    for task in tasks:
        nodes = task.get("nodes")
        if not isinstance(nodes, int) or nodes < 3:
            raise ValueError(
                f"task {task.get('slug')!r} needs at least 3 nodes to form a cluster"
            )
        if task.get("difficulty") not in {"easy", "medium", "hard"}:
            raise ValueError(f"task {task.get('slug')!r} has an unsupported difficulty")
    return systems, tasks


def environment_text(system: dict, task: dict) -> str:
    image = system["image"]
    lines = [f'cluster = ["{image} x{task["nodes"]}"]']
    if system.get("rhsm"):
        lines.append('initialize = ["rhsm"]')
    lines.extend(
        [
            'base_runbooks = ["antrieb/primer"]',
            'control_node = "node1"',
            'endpoint = "https://antrieb.sh/mcp"',
        ]
    )
    return "\n".join(lines) + "\n"


def generate() -> int:
    with CATALOG_PATH.open("rb") as handle:
        systems, tasks = validate_catalog(tomllib.load(handle))

    generated = 0
    for system in systems:
        os_root = MATRIX_ROOT / system["id"]
        os_root.mkdir(parents=True, exist_ok=True)
        for task in tasks:
            task_root = os_root / f'{task["slug"]}-{system["id"]}'
            task_root.mkdir(parents=True, exist_ok=True)

            write(task_root / "instruction.md", clean_block(task["instruction"]))
            write(
                task_root / "task.toml",
                TASK_CONFIG.format(difficulty=task["difficulty"]),
            )
            write(
                task_root / "environment" / "harbor_antrieb.toml",
                environment_text(system, task),
            )
            write(task_root / "tests" / "test.sh", SENTINEL, 0o755)
            generated += 1

    print(
        f"Generated {generated} tasks from {len(tasks)} task families across "
        f"{len(systems)} operating systems in {MATRIX_ROOT}"
    )
    return generated


if __name__ == "__main__":
    raise SystemExit(0 if generate() == 80 else 1)
