#!/usr/bin/env python3
"""Count explicit external repository URLs and DNS failures by run."""

from __future__ import annotations

import re
from collections import defaultdict
from urllib.parse import urlsplit

try:
    from .common import ROOT, audit_records, command_audits, node_components, trial_dir
except ImportError:
    from common import ROOT, audit_records, command_audits, node_components, trial_dir


URL = re.compile(r"https?://[^\s\"'<>|]+", re.IGNORECASE)
REPOSITORY_PATH = (
    r"/etc/(?:yum\.repos\.d/[^\s;&|]+|apt/sources\.list(?:\.d/[^\s;&|]+)?|"
    r"apk/repositories|zypp/repos\.d/[^\s;&|]+|pacman\.conf)"
)
REPOSITORY_COMMAND = re.compile(
    r"\b(?:add-apt-repository|apt-add-repository)\b"
    r"|\b(?:dnf|yum)-config-manager\b[^\n]*(?:--add-repo|addrepo)"
    r"|\bzypper\b[^\n]*(?:addrepo|\bar\b)",
    re.IGNORECASE,
)
REPOSITORY_WRITE = re.compile(
    rf"\btee\b[^\n;]*{REPOSITORY_PATH}"
    rf"|>{1,2}\s*{REPOSITORY_PATH}"
    rf"|\b(?:cp|mv|install)\b[^\n;]*{REPOSITORY_PATH}"
    rf"|\bsed\b[^\n;]*\s-i(?:\s|$)[^\n;]*{REPOSITORY_PATH}"
    rf"|\b(?:curl|wget)\b[^\n;]*(?:\s-o\s+|--output(?:=|\s+)){REPOSITORY_PATH}",
    re.IGNORECASE,
)
DNS_FAILURE = re.compile(
    r"could not resolve(?: host)?"
    r"|couldn't resolve(?: host)?"
    r"|temporary failure (?:in name resolution|resolving)"
    r"|name or service not known"
    r"|no address associated with hostname"
    r"|failed to resolve",
    re.IGNORECASE,
)
DISTRO_REPOSITORIES = {
    "almalinux9": ("almalinux.org",),
    "alpine": ("alpinelinux.org",),
    "archlinux": ("archlinux.org",),
    "centos-stream10": ("centos.org",),
    "rhel7.9": ("redhat.com",),
    "rhel9.8": ("redhat.com",),
    "rhel10.0": ("redhat.com",),
    "ubuntu16.04": ("ubuntu.com",),
    "ubuntu24.04": ("ubuntu.com",),
}


def repository_configuration(command: str) -> bool:
    """Return whether a command attempts an explicit repository change."""
    return bool(REPOSITORY_COMMAND.search(command) or REPOSITORY_WRITE.search(command))


def hosts(command: str) -> set[str]:
    result = set()
    for match in URL.finditer(command):
        hostname = urlsplit(match.group().rstrip("),.;]")).hostname
        if (
            hostname
            and "$" not in hostname
            and "%" not in hostname
            and hostname not in {"localhost"}
        ):
            result.add(hostname.lower())
    return result


def external(hostname: str, component: str | None) -> bool:
    """Exclude distribution-operated, local, and placeholder repositories."""
    return not (
        hostname.endswith(DISTRO_REPOSITORIES.get(component or "", ()))
        or "example" in hostname
    )


def main() -> None:
    configured_runs: dict[str, set[str]] = {}
    failed_runs: dict[str, set[str]] = {}
    by_host: dict[str, set[str]] = defaultdict(set)
    failed_by_host: dict[str, set[str]] = defaultdict(set)

    for audit in command_audits():
        run = str(trial_dir(audit).relative_to(ROOT))
        records = list(audit_records(audit))
        components = node_components(audit)
        configured = set()
        for record in records:
            command = record.get("command")
            if record.get("outcome") != "requested" or not isinstance(command, str):
                continue
            if repository_configuration(command):
                component = components.get(record.get("node"))
                configured.update(
                    hostname
                    for hostname in hosts(command)
                    if external(hostname, component)
                )
        if not configured:
            continue

        configured_runs[run] = configured
        for hostname in configured:
            by_host[hostname].add(run)

        failed = set()
        for record in records:
            if record.get("outcome") != "completed":
                continue
            output = "\n".join(
                value
                for field in ("stdout", "stderr", "error")
                if isinstance((value := record.get(field)), str)
            )
            if not DNS_FAILURE.search(output):
                continue
            lowered = output.lower()
            failed.update(hostname for hostname in configured if hostname in lowered)
        if failed:
            failed_runs[run] = failed
            for hostname in failed:
                failed_by_host[hostname].add(run)

    total = len(configured_runs)
    failed = len(failed_runs)
    print(f"Runs with an explicit external repository URL: {total:,}")
    print(f"Runs with a configured hostname that failed DNS: {failed:,}")
    print(f"Rate: {100 * failed / total:.1f}%")
    print()
    print("| Host | Runs | Runs with DNS failure |")
    print("|---|---:|---:|")
    for hostname in sorted(by_host, key=lambda item: (-len(by_host[item]), item)):
        print(
            f"| {hostname} | {len(by_host[hostname]):,} "
            f"| {len(failed_by_host[hostname]):,} |"
        )
    print()
    print("Runs with DNS failures:")
    for run, hostnames in sorted(failed_runs.items()):
        print(f"{run}: {', '.join(sorted(hostnames))}")
    print()
    print("All repository-URL runs:")
    for run, hostnames in sorted(configured_runs.items()):
        print(f"{run}: {', '.join(sorted(hostnames))}")


if __name__ == "__main__":
    main()
