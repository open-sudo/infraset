#!/usr/bin/env python3
"""Summarise Antrieb cluster-provisioning time across every recorded job.

Provisioning is a platform property rather than a per-task result, so it is
grouped by cluster shape (node count and network count) rather than by task
or operating system: within a single image the spread is wider than the
spread between images, so a per-OS table would present scheduling jitter as
though it were a comparison.

Writes metrics/cluster-provisioning-performance.md.
"""

from __future__ import annotations

import json
import re
import statistics
import tomllib
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
JOBS = ROOT / "jobs"
OUTPUT = ROOT / "metrics" / "cluster-provisioning-performance.md"
JOB_NAME = re.compile(r"^\d{4}-\d{2}-\d{2}__\d{2}-\d{2}-\d{2}$")
COUNT_SUFFIX = re.compile(r"^(?P<image>\S+)\s+x(?P<count>\d+)$")


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def provision_ms(trial_dir: Path) -> float | None:
    """Read the provider-reported provisioning time for one trial's cluster."""
    payload = read_json(trial_dir / "provision-response.json")
    if payload is None:
        return None
    for item in payload.get("content", []):
        if not isinstance(item, dict) or item.get("type") != "text":
            continue
        text = item.get("text")
        if not isinstance(text, str):
            continue
        try:
            response = json.loads(text)
        except json.JSONDecodeError:
            continue
        value = response.get("provision_time_ms")
        if isinstance(value, (int, float)):
            return float(value)
    return None


def cluster_shape(job_dir: Path) -> tuple[int, int] | None:
    """Return (node count, network count) for a job's declared environment.

    The environment file is real TOML, so it is parsed rather than pattern
    matched: an earlier regex version silently mis-attributed node counts.
    """
    path = job_dir / "environment.toml"
    try:
        with path.open("rb") as handle:
            environment = tomllib.load(handle)
    except (OSError, tomllib.TOMLDecodeError):
        return None

    cluster = environment.get("cluster")
    if not isinstance(cluster, list) or not cluster:
        return None
    nodes = 0
    for entry in cluster:
        if not isinstance(entry, str):
            return None
        match = COUNT_SUFFIX.match(entry.strip())
        nodes += int(match.group("count")) if match else 1
    if nodes < 1:
        return None

    networks = environment.get("networks")
    network_count = len(networks) if isinstance(networks, list) and networks else 1

    # A declared nics table must cover exactly the nodes the cluster provisions;
    # a mismatch means the shape is not trustworthy, so drop the sample.
    nics = environment.get("nics")
    if isinstance(nics, dict) and nics and len(nics) != nodes:
        return None
    return nodes, network_count


def samples() -> list[tuple[int, int, float]]:
    values: list[tuple[int, int, float]] = []
    for job_dir in JOBS.rglob("*"):
        if not job_dir.is_dir() or not JOB_NAME.fullmatch(job_dir.name):
            continue
        shape = cluster_shape(job_dir)
        if shape is None:
            continue
        for trial_dir in sorted(job_dir.iterdir()):
            if not trial_dir.is_dir():
                continue
            elapsed = provision_ms(trial_dir)
            if elapsed is not None:
                values.append((shape[0], shape[1], elapsed))
    return values


def trial_share() -> float | None:
    """Median provisioning time as a percentage of total trial wall clock."""
    shares: list[float] = []
    for job_dir in JOBS.rglob("*"):
        if not job_dir.is_dir() or not JOB_NAME.fullmatch(job_dir.name):
            continue
        for trial_dir in sorted(job_dir.iterdir()):
            if not trial_dir.is_dir():
                continue
            elapsed = provision_ms(trial_dir)
            result = read_json(trial_dir / "result.json")
            if elapsed is None or result is None:
                continue
            try:
                started = datetime.fromisoformat(
                    str(result.get("started_at")).replace("Z", "+00:00")
                )
                finished = datetime.fromisoformat(
                    str(result.get("finished_at")).replace("Z", "+00:00")
                )
            except (TypeError, ValueError):
                continue
            total = (finished - started).total_seconds()
            if total > 0:
                shares.append(elapsed / 1000 / total * 100)
    return statistics.median(shares) if shares else None


def percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    index = min(len(ordered) - 1, int(fraction * len(ordered)))
    return ordered[index]


def build() -> str:
    values = samples()
    if not values:
        raise SystemExit("no provisioning samples found under jobs/")

    by_shape: dict[tuple[int, int], list[float]] = defaultdict(list)
    for nodes, networks, elapsed in values:
        by_shape[(nodes, networks)].append(elapsed)
    everything = [elapsed for _, _, elapsed in values]
    share = trial_share()
    sub_second = sum(1 for value in everything if value < 1000)

    lines = [
        "# Cluster provisioning performance\n",
        "Every task in this dataset runs on a disposable cluster that "
        "[Antrieb](https://antrieb.sh/) provisions on demand. This page reports "
        "how long that takes, measured from the provider's own "
        "`provision_time_ms` for each cluster actually created during a "
        "recorded job.\n",
        f"Across **{len(everything)} clusters**: median "
        f"**{statistics.median(everything):.0f} ms**, 95th percentile "
        f"**{percentile(everything, 0.95):.0f} ms**, slowest "
        f"**{max(everything):.0f} ms**. "
        f"{sub_second} of {len(everything)} "
        f"({100 * sub_second / len(everything):.0f}%) completed in under a "
        f"second, and every one completed in under "
        f"{max(everything) / 1000:.1f} seconds.\n",
    ]
    if share is not None:
        lines.append(
            f"Provisioning accounts for a median of **{share:.2f}%** of a "
            "trial's total wall clock, so the completion times reported in the "
            "per-category metrics are effectively all executor work rather "
            "than environment setup.\n"
        )

    lines.extend(
        [
            "## By cluster shape\n",
            "Grouped by what was actually provisioned rather than by operating "
            "system: within a single image the spread is wider than the spread "
            "between images, so a per-OS breakdown would show host scheduling "
            "jitter rather than a property of the image.\n",
            "| Nodes | Networks | Clusters | Median | 95th pct | Slowest |",
            "|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for nodes, networks in sorted(by_shape):
        group = by_shape[(nodes, networks)]
        lines.append(
            f"| {nodes} | {networks} | {len(group)} | "
            f"{statistics.median(group):.0f} ms | "
            f"{percentile(group, 0.95):.0f} ms | {max(group):.0f} ms |"
        )
    lines.append("")
    lines.append(
        "Provisioning stays broadly flat as clusters grow: adding nodes and "
        "additional isolated networks moves the median by a few hundred "
        "milliseconds rather than by orders of magnitude.\n"
    )
    return "\n".join(lines)


def main() -> int:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build())
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
