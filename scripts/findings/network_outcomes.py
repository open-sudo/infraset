#!/usr/bin/env python3
"""Compare network-OS command failures with end-to-end task outcomes."""

from __future__ import annotations

from collections import defaultdict

try:
    from .common import category, command_audits, command_counts, rewards
except ImportError:
    from common import category, command_audits, command_counts, rewards


NETWORK_COMPONENTS = {"openwrt", "opnsense", "sonic", "vyos"}
NETWORK_CATEGORIES = {
    "openwrt-networking",
    "opnsense-networking",
    "sonic-networking",
    "vyos-networking",
    "vyos-opnsense-networking",
}


def main() -> None:
    categories: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    cohorts: dict[bool, dict[str, int]] = defaultdict(
        lambda: {"runs": 0, "on_node": 0, "failed": 0, "zero_failed": 0}
    )
    for audit in command_audits():
        group = category(audit)
        if group not in NETWORK_CATEGORIES:
            continue
        passed = rewards(audit).get("reward") == 1.0
        categories[group][0] += 1
        categories[group][1] += passed
        counts = command_counts(audit, NETWORK_COMPONENTS)
        cohort = cohorts[passed]
        cohort["runs"] += 1
        cohort["on_node"] += counts["on_node"]
        cohort["failed"] += counts["failed"]
        cohort["zero_failed"] += counts["failed"] == 0

    print("| Category | Runs | Passed | Failed |")
    print("|---|---:|---:|---:|")
    for group, (runs, passed) in sorted(categories.items()):
        print(f"| {group} | {runs:,} | {passed:,} | {runs - passed:,} |")
    print()
    print("| Outcome | Runs | On-node results | Failed results | Rate | Zero failed results |")
    print("|---|---:|---:|---:|---:|---:|")
    for passed in (True, False):
        row = cohorts[passed]
        rate = 100 * row["failed"] / row["on_node"]
        print(
            f"| {'Passed' if passed else 'Failed'} | {row['runs']:,} "
            f"| {row['on_node']:,} | {row['failed']:,} | {rate:.1f}% "
            f"| {row['zero_failed']:,} |"
        )


if __name__ == "__main__":
    main()
