#!/usr/bin/env python3
"""Reproduce command fail rates by Linux release and network OS."""

from __future__ import annotations

from collections import defaultdict

try:
    from .common import (
        category,
        command_audits,
        command_counts,
        node_components,
        task_name,
    )
except ImportError:
    from common import (
        category,
        command_audits,
        command_counts,
        node_components,
        task_name,
    )


LINUX_LABELS = {
    "rhel7.9": "RHEL 7.9",
    "rhel9.8": "RHEL 9.8",
    "rhel10.0": "RHEL 10.0",
    "ubuntu16.04": "Ubuntu 16.04",
    "ubuntu24.04": "Ubuntu 24.04",
}
NETWORK_CATEGORIES = {
    "sonic-networking": ("sonic", "SONiC"),
    "openwrt-networking": ("openwrt", "OpenWrt"),
    "opnsense-networking": ("opnsense", "OPNsense"),
    "vyos-networking": ("vyos", "VyOS"),
}


def _add(target: list[int], values: dict[str, int]) -> None:
    target[0] += values["requested"]
    target[1] += values["on_node"]
    target[2] += values["failed"]


def rates() -> tuple[
    list[tuple[str, int, int, int, float]],
    list[tuple[str, int, int, int, float]],
]:
    linux: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
    network: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
    for audit in command_audits():
        group = category(audit)
        if group == "single-node-os-comparison" and not task_name(audit).startswith(
            "file-integrity-baseline"
        ):
            component = next(iter(node_components(audit).values()))
            if component in LINUX_LABELS:
                _add(linux[component], command_counts(audit, {component}))
        if group in NETWORK_CATEGORIES:
            component, _ = NETWORK_CATEGORIES[group]
            _add(network[component], command_counts(audit, {component}))

    def rows(values, labels):
        result = []
        for component, (requested, on_node, failed) in values.items():
            result.append(
                (
                    labels[component],
                    requested,
                    on_node,
                    failed,
                    100 * failed / on_node,
                )
            )
        return result

    linux_rows = rows(linux, LINUX_LABELS)
    network_labels = {
        component: label for component, label in NETWORK_CATEGORIES.values()
    }
    network_rows = rows(network, network_labels)
    linux_order = {label: index for index, label in enumerate(LINUX_LABELS.values())}
    network_order = {
        label: index for index, (_, label) in enumerate(NETWORK_CATEGORIES.values())
    }
    linux_rows.sort(key=lambda row: linux_order[row[0]])
    network_rows.sort(key=lambda row: network_order[row[0]])
    return linux_rows, network_rows


def main() -> None:
    linux, network = rates()
    for title, values in (("Linux releases", linux), ("Network operating systems", network)):
        print(title)
        print("| Component | Requests | On-node results | Failed | Rate |")
        print("|---|---:|---:|---:|---:|")
        for label, requested, on_node, failed, rate in values:
            print(
                f"| {label} | {requested:,} | {on_node:,} | {failed:,} "
                f"| {rate:.1f}% |"
            )
        print()


if __name__ == "__main__":
    main()
