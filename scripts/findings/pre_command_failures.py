#!/usr/bin/env python3
"""Count clusters where the LLM issued no command."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from .common import ROOT, audit_records, job_records, provision_payload
except ImportError:
    from common import ROOT, audit_records, job_records, provision_payload


def command_audits(directory: Path) -> list[Path]:
    return sorted(directory.glob("*/agent/executor-commands.jsonl"))


def issued_command(directory: Path) -> bool:
    return any(
        record.get("outcome") == "requested"
        for audit in command_audits(directory)
        for record in audit_records(audit)
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count provisioned clusters with no recorded LLM command request."
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="list the affected job directories and cluster IDs",
    )
    args = parser.parse_args()

    cluster_ids: set[str] = set()
    failures: list[tuple[Path, str, str]] = []

    for directory, _ in job_records():
        payload = provision_payload(directory)
        if payload is None:
            raise SystemExit(f"missing provisioning response: {directory}")

        cluster_id = payload.get("session_id")
        if not isinstance(cluster_id, str) or not cluster_id:
            raise SystemExit(f"missing cluster session ID: {directory}")
        if cluster_id in cluster_ids:
            raise SystemExit(f"duplicate cluster session ID: {cluster_id}")
        cluster_ids.add(cluster_id)

        if issued_command(directory):
            continue

        reason = "empty command log" if command_audits(directory) else "no command log"
        failures.append((directory, cluster_id, reason))

    print(f"Clusters: {len(cluster_ids):,}")
    print(f"Clusters that issued an LLM command: {len(cluster_ids) - len(failures):,}")
    print(f"Failed before the first LLM command: {len(failures):,}")

    if args.list:
        print()
        for directory, cluster_id, reason in failures:
            print(f"{directory.relative_to(ROOT)}\t{cluster_id}\t{reason}")


if __name__ == "__main__":
    main()
