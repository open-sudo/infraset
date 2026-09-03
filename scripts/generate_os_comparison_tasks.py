#!/usr/bin/env python3
"""Generate the single-node OS comparison task matrix from its catalog."""

from __future__ import annotations

import shutil
import textwrap
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and earlier
    import tomli as tomllib


REPOSITORY = Path(__file__).resolve().parents[1]
MATRIX_ROOT = REPOSITORY / "tasks" / "os-comparison"
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
timeout_sec = 900

[verifier]
timeout_sec = 1200
environment_mode = "shared"

[environment]
network_mode = "public"
"""


PREPARATIONS: dict[str, tuple[str, str]] = {
    "inventory-data": (
        """
        set -eu
        install -d -o root -g root -m 0755 /srv/inventory/data
        printf '%s\n' 'sku-1001,keyboard,12' 'sku-1002,display,7' > /srv/inventory/data/records.csv
        printf '%s\n' '{"site":"north","generation":4}' > /srv/inventory/data/config.json
        chown -R root:root /srv/inventory
        chmod 0755 /srv/inventory /srv/inventory/data
        chmod 0644 /srv/inventory/data/records.csv /srv/inventory/data/config.json
        """,
        """
        set -eu
        find /srv/inventory/data -type f -print0 | sort -z | xargs -0 sha256sum
        stat -c '%U:%G:%a:%n' /srv/inventory /srv/inventory/data /srv/inventory/data/records.csv /srv/inventory/data/config.json
        """,
    ),
    "restore-data": (
        """
        set -eu
        install -d -o root -g root -m 0755 /srv/inventory/data /var/backups/inventory
        printf '%s\n' '{"site":"north","generation":"damaged"}' > /srv/inventory/data/config.json
        printf '%s\n' 'current-file-must-remain' > /srv/inventory/data/current.txt
        restore_source=/var/tmp/os-comparison-restore-source
        rm -rf "$restore_source"
        install -d -m 0700 "$restore_source"
        printf '%s\n' '{"site":"north","generation":4}' > "$restore_source/config.json"
        tar -czf /var/backups/inventory/inventory-20260901.tar.gz -C "$restore_source" config.json
        rm -rf "$restore_source"
        chmod 0644 /srv/inventory/data/config.json /srv/inventory/data/current.txt
        chmod 0600 /var/backups/inventory/inventory-20260901.tar.gz
        """,
        """
        set -eu
        printf 'current='; sha256sum /srv/inventory/data/current.txt
        printf 'damaged='; sha256sum /srv/inventory/data/config.json
        printf 'backup='; tar -xOf /var/backups/inventory/inventory-20260901.tar.gz config.json | sha256sum
        """,
    ),
    "temporary-files": (
        """
        set -eu
        install -d -o root -g root -m 1777 /var/tmp/inventory
        printf '%s\n' expired > /var/tmp/inventory/expired.tmp
        printf '%s\n' current > /var/tmp/inventory/current.tmp
        touch -t 202001010000 /var/tmp/inventory/expired.tmp
        touch /var/tmp/inventory/current.tmp
        """,
        """
        set -eu
        stat -c '%Y:%a:%n' /var/tmp/inventory/expired.tmp /var/tmp/inventory/current.tmp
        """,
    ),
    "application-log": (
        """
        set -eu
        install -d -o root -g root -m 0755 /var/log/inventory
        printf '%s\n' 'inventory service started' 'inventory initial record count: 2' > /var/log/inventory/app.log
        chmod 0644 /var/log/inventory/app.log
        """,
        """
        set -eu
        sha256sum /var/log/inventory/app.log
        stat -c '%U:%G:%a:%n' /var/log/inventory/app.log
        """,
    ),
    "audit-target": (
        """
        set -eu
        printf '%s\n' 'inventory_mode=production' > /etc/inventory.conf
        chown root:root /etc/inventory.conf
        chmod 0644 /etc/inventory.conf
        """,
        """
        set -eu
        sha256sum /etc/inventory.conf
        stat -c '%U:%G:%a:%n' /etc/inventory.conf
        """,
    ),
    "maintenance-command": (
        """
        set -eu
        cat > /usr/local/bin/inventory-maintenance <<'SCRIPT'
        #!/bin/sh
        printf 'inventory maintenance completed at %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
        SCRIPT
        chown root:root /usr/local/bin/inventory-maintenance
        chmod 0755 /usr/local/bin/inventory-maintenance
        """,
        """
        set -eu
        sha256sum /usr/local/bin/inventory-maintenance
        stat -c '%U:%G:%a:%n' /usr/local/bin/inventory-maintenance
        """,
    ),
    "service-worker": (
        """
        set -eu
        cat > /usr/local/bin/os-comparison-worker <<'SCRIPT'
        #!/bin/sh
        trap 'exit 0' TERM INT
        while :; do sleep 30; done
        SCRIPT
        chown root:root /usr/local/bin/os-comparison-worker
        chmod 0755 /usr/local/bin/os-comparison-worker
        """,
        """
        set -eu
        sha256sum /usr/local/bin/os-comparison-worker
        stat -c '%U:%G:%a:%n' /usr/local/bin/os-comparison-worker
        """,
    ),
    "flaky-worker": (
        """
        set -eu
        cat > /usr/local/bin/os-comparison-flaky-worker <<'SCRIPT'
        #!/bin/sh
        state=/var/tmp/os-comparison-flaky-worker-failed
        if test ! -e "$state"; then
          : > "$state"
          exit 1
        fi
        trap 'exit 0' TERM INT
        while :; do sleep 30; done
        SCRIPT
        rm -f /var/tmp/os-comparison-flaky-worker-failed
        chown root:root /usr/local/bin/os-comparison-flaky-worker
        chmod 0755 /usr/local/bin/os-comparison-flaky-worker
        """,
        """
        set -eu
        sha256sum /usr/local/bin/os-comparison-flaky-worker
        test ! -e /var/tmp/os-comparison-flaky-worker-failed
        """,
    ),
    "dependent-workers": (
        """
        set -eu
        cat > /usr/local/bin/inventory-database <<'SCRIPT'
        #!/bin/sh
        : > /var/tmp/inventory-database-ready
        trap 'rm -f /var/tmp/inventory-database-ready; exit 0' TERM INT
        while :; do sleep 30; done
        SCRIPT
        cat > /usr/local/bin/inventory-api <<'SCRIPT'
        #!/bin/sh
        test -e /var/tmp/inventory-database-ready
        trap 'exit 0' TERM INT
        while :; do sleep 30; done
        SCRIPT
        rm -f /var/tmp/inventory-database-ready
        chown root:root /usr/local/bin/inventory-database /usr/local/bin/inventory-api
        chmod 0755 /usr/local/bin/inventory-database /usr/local/bin/inventory-api
        """,
        """
        set -eu
        sha256sum /usr/local/bin/inventory-database /usr/local/bin/inventory-api
        test ! -e /var/tmp/inventory-database-ready
        """,
    ),
    "resource-worker": (
        """
        set -eu
        cat > /usr/local/bin/os-comparison-resource-worker <<'SCRIPT'
        #!/bin/sh
        trap 'exit 0' TERM INT
        while :; do :; done
        SCRIPT
        chown root:root /usr/local/bin/os-comparison-resource-worker
        chmod 0755 /usr/local/bin/os-comparison-resource-worker
        """,
        """
        set -eu
        sha256sum /usr/local/bin/os-comparison-resource-worker
        stat -c '%U:%G:%a:%n' /usr/local/bin/os-comparison-resource-worker
        """,
    ),
    "graceful-worker": (
        """
        set -eu
        cat > /usr/local/bin/os-comparison-graceful-worker <<'SCRIPT'
        #!/bin/sh
        marker=/var/tmp/os-comparison-graceful-stop
        trap 'printf "%s\n" graceful > "$marker"; exit 0' TERM INT
        while :; do sleep 30; done
        SCRIPT
        rm -f /var/tmp/os-comparison-graceful-stop
        chown root:root /usr/local/bin/os-comparison-graceful-worker
        chmod 0755 /usr/local/bin/os-comparison-graceful-worker
        """,
        """
        set -eu
        sha256sum /usr/local/bin/os-comparison-graceful-worker
        test ! -e /var/tmp/os-comparison-graceful-stop
        """,
    ),
}


def clean_block(value: str) -> str:
    return textwrap.dedent(value).strip() + "\n"


def quoted_command(value: str) -> str:
    command = clean_block(value)
    if "'''" in command:
        raise ValueError("generated shell command contains a TOML delimiter")
    return "'''\n" + command + "'''"


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
    if len(systems) != 11:
        raise ValueError(f"expected 11 operating systems, found {len(systems)}")
    if len(tasks) != 50:
        raise ValueError(f"expected 50 task families, found {len(tasks)}")

    os_ids = [item.get("id") for item in systems if isinstance(item, dict)]
    slugs = [item.get("slug") for item in tasks if isinstance(item, dict)]
    numbers = [item.get("number") for item in tasks if isinstance(item, dict)]
    if len(os_ids) != 11 or len(set(os_ids)) != 11:
        raise ValueError("operating-system IDs must be unique")
    if len(slugs) != 50 or len(set(slugs)) != 50:
        raise ValueError("task slugs must be unique")
    if numbers != list(range(1, 51)):
        raise ValueError("task numbers must be consecutive from 1 through 50")
    for task in tasks:
        profile = task.get("preparation")
        if profile is not None and profile not in PREPARATIONS:
            raise ValueError(f"unknown preparation profile: {profile}")
    return systems, tasks


def environment_text(system: dict, prepared: bool) -> str:
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
    if prepared:
        lines.extend(
            [
                "",
                "[prepare]",
                "enabled = true",
                'mode = "static"',
                'setup = "prepare/setup.toml"',
                'baseline = "prepare/baseline.toml"',
                "timeout_sec = 180",
            ]
        )
    return "\n".join(lines) + "\n"


def preparation_text(profile: str) -> tuple[str, str]:
    setup_command, baseline_command = PREPARATIONS[profile]
    setup = (
        "timeout_sec = 180\n\n"
        "[[steps]]\n"
        f'id = "prepare-{profile}"\n'
        "stage = 10\n"
        'node = "node1"\n'
        f"command = {quoted_command(setup_command)}\n"
    )
    baseline = (
        "timeout_sec = 120\n\n"
        "[[observations]]\n"
        f'id = "prepared-{profile}"\n'
        "stage = 10\n"
        'node = "node1"\n'
        f"command = {quoted_command(baseline_command)}\n"
        "required = true\n"
    )
    return setup, baseline


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
            profile = task.get("preparation")

            write(task_root / "instruction.md", instruction)
            write(
                task_root / "task.toml",
                TASK_CONFIG.format(difficulty=task["difficulty"]),
            )
            write(
                task_root / "environment" / "harbor_antrieb.toml",
                environment_text(system, profile is not None),
            )
            write(task_root / "tests" / "test.sh", SENTINEL, 0o755)

            prepare_root = task_root / "prepare"
            if profile is not None:
                setup, baseline = preparation_text(profile)
                write(prepare_root / "setup.toml", setup)
                write(prepare_root / "baseline.toml", baseline)
            elif prepare_root.exists():
                shutil.rmtree(prepare_root)

            generated += 1

    print(
        f"Generated {generated} tasks from {len(tasks)} task families across "
        f"{len(systems)} operating systems in {MATRIX_ROOT}"
    )
    return generated


if __name__ == "__main__":
    raise SystemExit(0 if generate() == 550 else 1)
