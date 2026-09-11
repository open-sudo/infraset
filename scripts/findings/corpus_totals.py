#!/usr/bin/env python3
"""Reproduce the article's corpus, VM, pass, and hygiene totals."""

from __future__ import annotations

from collections import defaultdict
from math import floor

try:
    from .common import (
        category,
        command_audits,
        audit_records,
        job_dir,
        job_records,
        provisioned_node_count,
        rewards,
    )
except ImportError:
    from common import (
        category,
        command_audits,
        audit_records,
        job_dir,
        job_records,
        provisioned_node_count,
        rewards,
    )


CATEGORY_LABELS = {
    "vyos-opnsense-networking": "vyos-opnsense (cross-vendor)",
}


def main() -> None:
    jobs = list(job_records())
    audits = list(command_audits())
    command_job_dirs = {job_dir(audit) for audit in audits}

    provisioned = []
    for directory, _ in jobs:
        count = provisioned_node_count(directory)
        if count is None:
            raise SystemExit(f"missing provisioning node list: {directory}")
        provisioned.append((directory, count))

    command_requests = 0
    passed = 0
    by_category: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    hygiene_values: list[float] = []
    for audit in audits:
        requests = sum(
            record.get("outcome") == "requested" for record in audit_records(audit)
        )
        command_requests += requests
        reward = rewards(audit)
        is_pass = reward.get("reward") == 1.0
        passed += is_pass
        row = by_category[category(audit)]
        row[0] += 1
        row[1] += is_pass
        hygiene = reward.get("operational_hygiene")
        if isinstance(hygiene, (int, float)):
            hygiene_values.append(float(hygiene))

    vm_total = sum(count for _, count in provisioned)
    llm_vms = sum(count for directory, count in provisioned if directory in command_job_dirs)
    platform_vms = vm_total - llm_vms
    failed = len(audits) - passed
    platform_failures = len(jobs) - len(command_job_dirs)
    missing_hygiene = len(audits) - len(hygiene_values)
    observed_clean = sum(value == 1.0 for value in hygiene_values)
    clean_or_assumed = observed_clean + missing_hygiene
    mean_hygiene = (sum(hygiene_values) + missing_hygiene) / len(audits)

    print(f"Provisioning attempts: {len(jobs):,}")
    print(f"VMs created: {vm_total:,}")
    print(f"LLM runs: {len(audits):,}")
    print(f"VMs in LLM runs: {llm_vms:,}")
    print(f"Pre-command failures: {platform_failures:,}")
    print(f"VMs in pre-command failures: {platform_vms:,}")
    print(f"Command requests: {command_requests:,}")
    print(f"Passed: {passed:,}")
    print(f"Failed: {failed:,}")
    print(f"Pass rate: {100 * passed / len(audits):.1f}%")
    print(f"Hygiene values present: {len(hygiene_values):,}")
    print(f"Clean or assumed clean: {clean_or_assumed:,}")
    print(f"Residue: {len(audits) - clean_or_assumed:,}")
    print(f"Residue rate: {100 * (len(audits) - clean_or_assumed) / len(audits):.1f}%")
    print(f"Mean hygiene, missing values assumed clean: {mean_hygiene:.3f}")
    print()
    print("| Category | Runs | Passed | Rate |")
    print("|---|---:|---:|---:|")
    for name, (runs, category_passed) in sorted(
        by_category.items(), key=lambda item: (-item[1][1] / item[1][0], item[0])
    ):
        label = CATEGORY_LABELS.get(name, name)
        rate = floor(100 * category_passed / runs + 0.5)
        print(
            f"| {label} | {runs:,} | {category_passed:,} "
            f"| {rate}% |"
        )


if __name__ == "__main__":
    main()
