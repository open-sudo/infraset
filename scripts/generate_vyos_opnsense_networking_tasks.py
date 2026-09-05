#!/usr/bin/env python3
"""Generate the vyos-opnsense-networking task matrix from its catalog.

Two different network appliances face each other in every task: VyOS on one
side, OPNsense on the other, with Linux nodes behind them carrying the
workload. Only the operating system of those workload nodes varies across the
matrix, so what the matrix measures is how the same cross-vendor outcome is
reached with different hosts behind the routers.

The pairing is deliberate on the transport axis. VyOS reaches its exec channel
over vsock and cannot be locked out by its own configuration; OPNsense reaches
it over SSH and can be, the moment a filter reload lands without a rule for the
management path. Pairing the two means half the topology stays reachable even
when the other half is mid-mistake, which is why this pairing is preferred to
putting two SSH-transport appliances in one cluster.

Both platforms default to refusing forwarded traffic, so every path across the
pair has to be opened on both sides. That is the property most of these
families are built around.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and earlier
    import tomli as tomllib


REPOSITORY = Path(__file__).resolve().parents[1]
MATRIX_ROOT = REPOSITORY / "tasks" / "vyos-opnsense-networking"
CATALOG_PATH = MATRIX_ROOT / "catalog.toml"

EXPECTED_SYSTEMS = 8
EXPECTED_TASKS = 10

# Appliance order fixes node identity: node1 is VyOS and node2 is OPNsense in
# every task, so an instruction naming a node names the same platform on every
# operating system in the matrix.
APPLIANCES = ("vyos", "opnsense")

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

# Each topology is a (networks_block, nics_block) pair of pre-formatted TOML,
# shared by every operating system in the matrix for that task. Every node
# carries the always-on mgmt network first, so it lands on the first interface
# and the OPNsense management path survives a filter reload. The task-specific
# networks carry no egress and no platform DHCP, leaving addressing on them to
# the executor.
TOPOLOGIES: dict[str, tuple[str, str]] = {
    # One transit network between the two routers, one private network and one
    # workload behind each.
    "dual-site": (
        """
        [[networks]]
        name = "mgmt"
        dhcp = true
        egress = true

        [[networks]]
        name = "transit"
        dhcp = false
        egress = false

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
        node1 = [{ net = "mgmt" }, { net = "transit" }, { net = "lan-a" }]
        node2 = [{ net = "mgmt" }, { net = "transit" }, { net = "lan-b" }]
        node3 = [{ net = "mgmt" }, { net = "lan-a" }]
        node4 = [{ net = "mgmt" }, { net = "lan-b" }]
        """,
    ),
    # The same pair joined by two independent transit networks, so one can be
    # taken out of service or chosen deliberately per flow.
    "dual-path": (
        """
        [[networks]]
        name = "mgmt"
        dhcp = true
        egress = true

        [[networks]]
        name = "transit-a"
        dhcp = false
        egress = false

        [[networks]]
        name = "transit-b"
        dhcp = false
        egress = false

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
        node1 = [{ net = "mgmt" }, { net = "transit-a" }, { net = "transit-b" }, { net = "lan-a" }]
        node2 = [{ net = "mgmt" }, { net = "transit-a" }, { net = "transit-b" }, { net = "lan-b" }]
        node3 = [{ net = "mgmt" }, { net = "lan-a" }]
        node4 = [{ net = "mgmt" }, { net = "lan-b" }]
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
    if len(systems) != EXPECTED_SYSTEMS:
        raise ValueError(
            f"expected {EXPECTED_SYSTEMS} operating systems, found {len(systems)}"
        )
    if len(tasks) != EXPECTED_TASKS:
        raise ValueError(f"expected {EXPECTED_TASKS} task families, found {len(tasks)}")

    os_ids = [item.get("id") for item in systems if isinstance(item, dict)]
    slugs = [item.get("slug") for item in tasks if isinstance(item, dict)]
    numbers = [item.get("number") for item in tasks if isinstance(item, dict)]
    if len(set(os_ids)) != EXPECTED_SYSTEMS:
        raise ValueError("operating-system IDs must be unique")
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
        topology = task.get("topology")
        if topology not in TOPOLOGIES:
            raise ValueError(
                f"task {task.get('slug')!r} has unknown topology {topology!r}"
            )
        appliances = task.get("appliances")
        linux_nodes = task.get("linux_nodes")
        # Both platforms are always present: the pairing is the point.
        if appliances != len(APPLIANCES):
            raise ValueError(
                f"task {task.get('slug')!r} needs appliances = {len(APPLIANCES)}"
            )
        if not isinstance(linux_nodes, int) or linux_nodes < 1:
            raise ValueError(f"task {task.get('slug')!r} needs linux_nodes >= 1")
        # The nics block must cover exactly the nodes the cluster provisions.
        _, nics_block = TOPOLOGIES[topology]
        declared = sum(
            1 for line in nics_block.splitlines() if line.strip().startswith("node")
        )
        if declared != appliances + linux_nodes:
            raise ValueError(
                f"task {task.get('slug')!r} topology {topology!r} declares {declared} "
                f"nodes but the cluster provisions {appliances + linux_nodes}"
            )
        control_node = task.get("control_node")
        if not isinstance(control_node, str) or not control_node.startswith("node"):
            raise ValueError(f"task {task.get('slug')!r} needs a node control_node")
        # Keep the control node on a workload: the appliances come first.
        if int(control_node.removeprefix("node")) <= appliances:
            raise ValueError(
                f"task {task.get('slug')!r} control_node {control_node!r} is an appliance"
            )
    return systems, tasks


def cluster_entries(system: dict, task: dict) -> str:
    linux_nodes = task["linux_nodes"]
    image = system["image"]
    linux = image if linux_nodes == 1 else f"{image} x{linux_nodes}"
    entries = [f'"{name}"' for name in APPLIANCES] + [f'"{linux}"']
    return "[" + ", ".join(entries) + "]"


def environment_text(system: dict, task: dict) -> str:
    lines = [f"cluster = {cluster_entries(system, task)}"]
    if system.get("rhsm"):
        lines.append('initialize = ["rhsm"]')
    lines.extend(
        [
            "base_runbooks = [",
            '  "antrieb/primer",',
            '  "antrieb/networking-primer",',
            '  "antrieb/vyos-reference",',
            '  "antrieb/opnsense-reference",',
            "]",
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
    raise SystemExit(0 if generate() == EXPECTED_SYSTEMS * EXPECTED_TASKS else 1)
