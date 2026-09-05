#!/usr/bin/env python3
"""Generate the openwrt-networking task matrix from its catalog.

The network appliance is fixed (OpenWrt) and only the operating system of the
Linux nodes behind it varies. A task may declare more than one appliance, so
the cluster and control node are derived per task from the catalog.

OpenWrt's exec transport is SSH rather than vsock, so a firewall reload that
moves the management interface into a restrictive zone can cost control-plane
access to the appliance itself. Every topology therefore puts the always-on
`mgmt` network first, making it `eth0` on every node, and the OpenWrt reference
carried in `base_runbooks` documents the rule that has to be staged before the
first reload.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and earlier
    import tomli as tomllib


REPOSITORY = Path(__file__).resolve().parents[1]
MATRIX_ROOT = REPOSITORY / "tasks" / "openwrt-networking"
CATALOG_PATH = MATRIX_ROOT / "catalog.toml"

EXPECTED_SYSTEMS = 8
EXPECTED_TASKS = 10

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

# Each topology is a (networks_block, nics_block) pair of pre-formatted TOML,
# shared by every operating system in the matrix for that task. Every node
# carries the always-on mgmt network so a broken data plane never costs
# control-plane reachability; the task-specific networks carry no egress.
# mgmt is listed first on every node so it lands on eth0.
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
    # One shared link that the executor must carry tagged VLANs over.
    "trunk": (
        """
        [[networks]]
        name = "mgmt"
        dhcp = true
        egress = true

        [[networks]]
        name = "trunk"
        dhcp = false
        egress = false
        """,
        """
        [nics]
        node1 = [{ net = "mgmt" }, { net = "trunk" }]
        node2 = [{ net = "mgmt" }, { net = "trunk" }]
        node3 = [{ net = "mgmt" }, { net = "trunk" }]
        """,
    ),
    # Two routers, each owning one private network, meeting on a transit link.
    # Neither private network is reachable from the other without a tunnel.
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
    # Two routers sharing one private network with a single client, so a
    # shared address can move between them while the client keeps using it.
    "redundant-gateway": (
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
        topology = task.get("topology")
        if topology not in TOPOLOGIES:
            raise ValueError(
                f"task {task.get('slug')!r} has unknown topology {topology!r}"
            )
        appliances = task.get("appliances")
        linux_nodes = task.get("linux_nodes")
        if not isinstance(appliances, int) or appliances < 1:
            raise ValueError(f"task {task.get('slug')!r} needs appliances >= 1")
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
        # Keep the control node on a Linux system: the appliances come first.
        if int(control_node.removeprefix("node")) <= appliances:
            raise ValueError(
                f"task {task.get('slug')!r} control_node {control_node!r} is an appliance"
            )
    return systems, tasks


def cluster_entries(system: dict, task: dict) -> str:
    appliances = task["appliances"]
    linux_nodes = task["linux_nodes"]
    openwrt = "openwrt" if appliances == 1 else f"openwrt x{appliances}"
    image = system["image"]
    linux = image if linux_nodes == 1 else f"{image} x{linux_nodes}"
    return f'["{openwrt}", "{linux}"]'


def environment_text(system: dict, task: dict) -> str:
    lines = [f"cluster = {cluster_entries(system, task)}"]
    if system.get("rhsm"):
        lines.append('initialize = ["rhsm"]')
    lines.extend(
        [
            "base_runbooks = [",
            '  "antrieb/primer",',
            '  "antrieb/networking-primer",',
            '  "antrieb/openwrt-reference",',
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
    raise SystemExit(0 if generate() == EXPECTED_SYSTEMS * EXPECTED_TASKS else 1)
