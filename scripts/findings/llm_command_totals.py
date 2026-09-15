#!/usr/bin/env python3
"""Count all commands issued by the LLM across the dataset."""

from __future__ import annotations

try:
    from .common import audit_records, command_audits
except ImportError:
    from common import audit_records, command_audits


def main() -> None:
    audits = list(command_audits())
    total_commands = 0
    command_bearing_runs = 0

    for audit in audits:
        command_ids: set[str] = set()

        for record in audit_records(audit):
            if record.get("outcome") != "requested":
                continue

            command_id = record.get("command_id")
            if not isinstance(command_id, str) or not command_id:
                raise SystemExit(f"command request without an ID: {audit}")
            if command_id in command_ids:
                raise SystemExit(
                    f"duplicate command request ID {command_id!r}: {audit}"
                )
            command_ids.add(command_id)

        total_commands += len(command_ids)
        command_bearing_runs += bool(command_ids)

    print(f"Command logs examined: {len(audits):,}")
    print(f"Runs with at least one command: {command_bearing_runs:,}")
    print(f"Commands issued by the LLM: {total_commands:,}")


if __name__ == "__main__":
    main()
