#!/usr/bin/env python3
"""Count the clusters and virtual machines created for the dataset."""

from __future__ import annotations

try:
    from .common import job_records, provision_payload
except ImportError:
    from common import job_records, provision_payload


def main() -> None:
    cluster_ids: set[str] = set()
    virtual_machines = 0

    for directory, _ in job_records():
        payload = provision_payload(directory)
        if payload is None:
            raise SystemExit(f"missing provisioning response: {directory}")

        cluster_id = payload.get("session_id")
        nodes = payload.get("nodes")
        if not isinstance(cluster_id, str) or not cluster_id:
            raise SystemExit(f"missing cluster session ID: {directory}")
        if cluster_id in cluster_ids:
            raise SystemExit(f"duplicate cluster session ID: {cluster_id}")
        if not isinstance(nodes, list) or not nodes:
            raise SystemExit(f"missing provisioning node list: {directory}")

        cluster_ids.add(cluster_id)
        virtual_machines += len(nodes)

    print(f"Clusters: {len(cluster_ids):,}")
    print(f"Virtual machines: {virtual_machines:,}")


if __name__ == "__main__":
    main()
