#!/usr/bin/env python3
"""Generate the single-node-os-comparison task matrix from its catalog.

Single-node administration requests issued against eight general-purpose Linux
operating systems. One node, the same public instruction on every operating
system, and only the image varies.

The catalog carries two generations of task families in one matrix. The first
ten cover accounts, permissions, scheduling, and services, and four of them
prepare existing state before the executor starts. The remaining twenty cover
mandatory access control, boot and kernel configuration, storage management,
package pinning, and service confinement, and are greenfield. Families differ
in how long they need, so each one declares its own timeouts.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and earlier
    import tomli as tomllib


REPOSITORY = Path(__file__).resolve().parents[1]
MATRIX_ROOT = REPOSITORY / "tasks" / "single-node-os-comparison"
CATALOG_PATH = MATRIX_ROOT / "catalog.toml"

EXPECTED_SYSTEMS = 8
EXPECTED_TASKS = 30

SENTINEL = """#!/bin/sh
echo "InfraSet requires the configured Harbor-Antrieb verifier." >&2
exit 1
"""

TASK_CONFIG = """schema_version = "1.4"

[metadata]
author_name = "InfraSet"
difficulty = "{difficulty}"
category = "infrastructure"

[agent]
timeout_sec = {agent_timeout_sec}

[verifier]
timeout_sec = {verifier_timeout_sec}
environment_mode = "shared"

[environment]
network_mode = "public"
"""

# The four brownfield families share one preparation contract. Their setup and
# baseline files are maintained by hand in the task directories; this generator
# only declares them and never rewrites their contents.
PREPARE_BLOCK = """
[prepare]
enabled = true
mode = "static"
setup = "prepare/setup.toml"
baseline = "prepare/baseline.toml"
timeout_sec = 180
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
    if len(systems) != EXPECTED_SYSTEMS:
        raise ValueError(
            f"expected {EXPECTED_SYSTEMS} operating systems, found {len(systems)}"
        )
    if len(tasks) != EXPECTED_TASKS:
        raise ValueError(
            f"expected {EXPECTED_TASKS} task families, found {len(tasks)}"
        )

    os_ids = [item.get("id") for item in systems if isinstance(item, dict)]
    slugs = [item.get("slug") for item in tasks if isinstance(item, dict)]
    numbers = [item.get("number") for item in tasks if isinstance(item, dict)]
    if len(set(os_ids)) != EXPECTED_SYSTEMS:
        raise ValueError("operating-system IDs must be unique")
    # Task directory names are globally unique in InfraSet, so a slug reused
    # between families would collide once the matrix is generated.
    if len(set(slugs)) != EXPECTED_TASKS:
        raise ValueError("task slugs must be unique")
    if numbers != list(range(1, EXPECTED_TASKS + 1)):
        raise ValueError(
            f"task numbers must be consecutive from 1 through {EXPECTED_TASKS}"
        )
    for task in tasks:
        if task.get("difficulty") not in {"easy", "medium", "hard"}:
            raise ValueError(f"task {task.get('slug')!r} has an unsupported difficulty")
        for key in ("agent_timeout_sec", "verifier_timeout_sec"):
            if not isinstance(task.get(key), int):
                raise ValueError(f"task {task.get('slug')!r} is missing {key}")
    return systems, tasks


def environment_text(system: dict, task: dict) -> str:
    lines = [f'cluster = ["{system["image"]}"]']
    if system.get("rhsm"):
        lines.append('initialize = ["rhsm"]')
    lines.extend(
        [
            'base_runbooks = ["antrieb/primer"]',
            'control_node = "node1"',
            'endpoint = "https://antrieb.sh/mcp"',
        ]
    )
    text = "\n".join(lines) + "\n"
    if task.get("prepare"):
        text += PREPARE_BLOCK
    return text


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
                TASK_CONFIG.format(
                    difficulty=task["difficulty"],
                    agent_timeout_sec=task["agent_timeout_sec"],
                    verifier_timeout_sec=task["verifier_timeout_sec"],
                ),
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
    raise SystemExit(
        0 if generate() == EXPECTED_SYSTEMS * EXPECTED_TASKS else 1
    )
