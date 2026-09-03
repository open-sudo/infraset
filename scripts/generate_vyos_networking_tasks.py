#!/usr/bin/env python3
"""Generate the vyos-networking task matrix from its catalog.

Every task in this matrix fixes the network appliance (a single VyOS
router as node1) and varies only the operating system of the two Linux
nodes behind it, mirroring single-node-os-comparison and
multi-node-os-comparison but with a router in front of the compared nodes
instead of a bare cluster.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and earlier
    import tomli as tomllib


REPOSITORY = Path(__file__).resolve().parents[1]
MATRIX_ROOT = REPOSITORY / "tasks" / "vyos-networking"
CATALOG_PATH = MATRIX_ROOT / "catalog.toml"

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
timeout_sec = 1200

[verifier]
timeout_sec = 1500
environment_mode = "shared"

[environment]
network_mode = "public"
"""

# Each topology is a (networks_block, nics_block) pair of pre-formatted TOML
# text, shared by every operating system in the matrix for that task.
TOPOLOGIES: dict[str, tuple[str, str]] = {
    "single-lan": (
        """
        [[networks]]
        name = "mgmt"
        dhcp = true
        egress = true

        [[networks]]
        name = "lan"
        dhcp = false
        egress = false
        """,
        """
        [nics]
        node1 = [{ net = "mgmt" }, { net = "lan" }]
        node2 = [{ net = "mgmt" }, { net = "lan" }]
        node3 = [{ net = "mgmt" }, { net = "lan" }]
        """,
    ),
    "dual-lan": (
        """
        [[networks]]
        name = "mgmt"
        dhcp = true
        egress = true

        [[networks]]
        name = "lan-a"
        dhcp = false
        egress = false

        [[networks]]
        name = "lan-b"
        dhcp = false
        egress = false
        """,
        """
        [nics]
        node1 = [{ net = "mgmt" }, { net = "lan-a" }, { net = "lan-b" }]
        node2 = [{ net = "mgmt" }, { net = "lan-a" }]
        node3 = [{ net = "mgmt" }, { net = "lan-b" }]
        """,
    ),
    "gateway-client": (
        """
        [[networks]]
        name = "mgmt"
        dhcp = true
        egress = true

        [[networks]]
        name = "lan"
        dhcp = false
        egress = false
        """,
        """
        [nics]
        node1 = [{ net = "mgmt" }, { net = "lan" }]
        node2 = [{ net = "mgmt" }, { net = "lan" }]
        node3 = [{ net = "mgmt" }]
        """,
    ),
}


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
    if len(tasks) != 5:
        raise ValueError(f"expected 5 task families, found {len(tasks)}")

    os_ids = [item.get("id") for item in systems if isinstance(item, dict)]
    slugs = [item.get("slug") for item in tasks if isinstance(item, dict)]
    numbers = [item.get("number") for item in tasks if isinstance(item, dict)]
    if len(os_ids) != 8 or len(set(os_ids)) != 8:
        raise ValueError("operating-system IDs must be unique")
    if len(slugs) != 5 or len(set(slugs)) != 5:
        raise ValueError("task slugs must be unique")
    if numbers != list(range(1, 6)):
        raise ValueError("task numbers must be consecutive from 1 through 5")
    for task in tasks:
        topology = task.get("topology")
        if topology not in TOPOLOGIES:
            raise ValueError(f"task {task.get('slug')!r} has unknown topology {topology!r}")
    return systems, tasks


def environment_text(system: dict, task: dict) -> str:
    image = system["image"]
    lines = [f'cluster = ["vyos", "{image} x2"]']
    if system.get("rhsm"):
        lines.append('initialize = ["rhsm"]')
    lines.extend(
        [
            'base_runbooks = [',
            '  "antrieb/primer",',
            '  "antrieb/networking-primer",',
            '  "antrieb/vyos-reference",',
            ']',
            f'control_node = "{task["control_node"]}"',
            'endpoint = "https://antrieb.sh/mcp"',
            "",
        ]
    )
    networks_block, nics_block = TOPOLOGIES[task["topology"]]
    lines.append(clean_block(networks_block))
    lines.append(clean_block(nics_block))
    return "\n".join(lines).rstrip() + "\n"


def generate() -> int:
    with CATALOG_PATH.open("rb") as handle:
        systems, tasks = validate_catalog(tomllib.load(handle))

    generated = 0
    for system in systems:
        os_root = MATRIX_ROOT / system["id"]
        os_root.mkdir(parents=True, exist_ok=True)
        for task in tasks:
            task_name = f'{task["slug"]}-{system["id"]}'
            task_root = os_root / task_name
            task_root.mkdir(parents=True, exist_ok=True)
            instruction = clean_block(task["instruction"])

            write(task_root / "instruction.md", instruction)
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
    raise SystemExit(0 if generate() == 40 else 1)
