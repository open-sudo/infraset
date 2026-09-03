#!/usr/bin/env python3
"""Generate a task x OS command cross-reference summary for a job category.

Produces `<category>-summary.md` at the repository root. Each row is a task
(linking to the analysis.md of its latest recorded job run); each column is an
operating system / image that appears in that category. Cells report
successful/failed executor commands as "success/failure" for the latest job
run, so the table shows how many commands the executor needed per OS and how
many of them failed.

Usage:
    python scripts/generate_category_summary.py single-node-os-comparison
    python scripts/generate_category_summary.py multi-node-os-comparison
    python scripts/generate_category_summary.py mixed-os-scenarios
"""

from __future__ import annotations

import argparse
import json
import re
import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
JOBS = ROOT / "jobs"
TASKS = ROOT / "tasks"
JOB_NAME = re.compile(r"^\d{4}-\d{2}-\d{2}__\d{2}-\d{2}-\d{2}$")

IMAGE_LABELS = {
    "alpine": "Alpine Linux",
    "almalinux9": "AlmaLinux 9",
    "archlinux": "Arch Linux",
    "centos-stream10": "CentOS Stream 10",
    "debian13": "Debian 13",
    "rhel7.9": "RHEL 7.9",
    "rhel8.8": "RHEL 8.8",
    "rhel9.8": "RHEL 9.8",
    "rhel10.0": "RHEL 10.0",
    "ubuntu16.04": "Ubuntu 16.04",
    "ubuntu24.04": "Ubuntu 24.04",
    "vyos": "VyOS",
    "sonic": "SONiC",
}


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def read_toml(path: Path) -> dict[str, Any] | None:
    try:
        with path.open("rb") as handle:
            return tomllib.load(handle)
    except (OSError, tomllib.TOMLDecodeError):
        return None


def label_for(image: str) -> str:
    return IMAGE_LABELS.get(image, image)


def job_runs(task_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in task_dir.iterdir()
        if path.is_dir() and JOB_NAME.fullmatch(path.name) and (path / "result.json").is_file()
    )


def trial_dirs(job_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in job_dir.iterdir()
        if path.is_dir() and (path / "result.json").is_file() and (path / "config.json").is_file()
    )


def command_records(trial_dir: Path) -> list[dict[str, Any]]:
    canonical = trial_dir / "agent" / "executor-commands.jsonl"
    paths = [canonical] if canonical.is_file() else sorted(
        (trial_dir / "agent" / "attempts").glob("*/executor-commands.jsonl")
    )
    records: list[dict[str, Any]] = []
    for path in paths:
        for line in path.read_text(errors="replace").splitlines():
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(record, dict):
                records.append(record)
    return records


def command_stats(records: list[dict[str, Any]], node_filter: set[str] | None = None) -> tuple[int, int]:
    successful = failed = 0
    for record in records:
        if node_filter is not None and record.get("node") not in node_filter:
            continue
        if record.get("outcome") != "completed":
            continue
        return_code = record.get("return_code")
        if return_code == 0:
            successful += 1
        elif isinstance(return_code, int):
            failed += 1
    return successful, failed


def expand_cluster(cluster: list[Any]) -> list[str]:
    images: list[str] = []
    for entry in cluster:
        if not isinstance(entry, str):
            continue
        match = re.fullmatch(r"(\S+)\s+x(\d+)", entry.strip())
        if match:
            images.extend([match.group(1)] * int(match.group(2)))
        else:
            images.append(entry.strip())
    return images


def relative_link(path: Path) -> str:
    return str(path.relative_to(ROOT))


def build_matrix_category(category: str) -> str:
    """single-node-os-comparison / multi-node-os-comparison: catalog-driven matrix."""
    catalog = read_toml(TASKS / category / "catalog.toml")
    if catalog is None:
        raise SystemExit(f"no catalog.toml found for {category}")
    systems = catalog.get("operating_systems", [])
    tasks = catalog.get("tasks", [])
    os_ids = [(item["id"], item.get("label", item["id"])) for item in systems]
    slugs = [item["slug"] for item in tasks]

    category_jobs = JOBS / category
    cols = [label for _, label in os_ids]
    lines = [
        f"# {category}: command execution summary\n",
        "Successful/failed executor commands per task per OS, from each task's "
        "latest recorded job run. Task names link to that run's analysis. "
        "`0/0` means the audit was captured but no managed-node commands were "
        "issued. `—` means the task has not been executed yet for that OS.\n",
        "| Task | " + " | ".join(cols) + " |",
        "|---|" + "|".join(["---:"] * len(cols)) + "|",
    ]

    for slug in slugs:
        cells = []
        link_target: str | None = None
        for os_id, _ in os_ids:
            task_dir = category_jobs / os_id / f"{slug}-{os_id}"
            if not task_dir.is_dir():
                cells.append("—")
                continue
            runs = job_runs(task_dir)
            if not runs:
                cells.append("—")
                continue
            latest = runs[-1]
            successful = failed = 0
            for trial_dir in trial_dirs(latest):
                records = command_records(trial_dir)
                s, f = command_stats(records)
                successful += s
                failed += f
            cells.append(f"{successful}/{failed}")
            if link_target is None:
                link_target = relative_link(latest / "analysis.md")
        name_cell = f"[{slug}]({link_target})" if link_target else slug
        lines.append("| " + name_cell + " | " + " | ".join(cells) + " |")

    lines.append("")
    return "\n".join(lines)


def build_mixed_os_scenarios() -> str:
    """mixed-os-scenarios: bespoke per-task topology, no shared catalog."""
    category_jobs = JOBS / "mixed-os-scenarios"
    task_dirs = sorted(p for p in category_jobs.iterdir() if p.is_dir())

    task_data: list[tuple[str, str | None, dict[str, tuple[int, int]]]] = []
    seen_images: dict[str, None] = {}

    for task_dir in task_dirs:
        runs = job_runs(task_dir)
        if not runs:
            continue
        latest = runs[-1]
        env = read_toml(latest / "environment.toml") or {}
        images = expand_cluster(env.get("cluster", []))
        node_for_image: dict[str, set[str]] = {}
        for index, image in enumerate(images):
            node_for_image.setdefault(image, set()).add(f"node{index + 1}")
            seen_images.setdefault(image, None)

        per_image: dict[str, tuple[int, int]] = {}
        for image, nodes in node_for_image.items():
            successful = failed = 0
            for trial_dir in trial_dirs(latest):
                records = command_records(trial_dir)
                s, f = command_stats(records, node_filter=nodes)
                successful += s
                failed += f
            per_image[image] = (successful, failed)

        link = relative_link(latest / "analysis.md")
        task_data.append((task_dir.name, link, per_image))

    image_order = sorted(seen_images, key=lambda image: label_for(image))
    cols = [label_for(image) for image in image_order]
    lines = [
        "# mixed-os-scenarios: command execution summary\n",
        "Successful/failed executor commands per task per OS/image, from each "
        "task's latest recorded job run, split by which node(s) in that task's "
        "topology ran each image. Task names link to that run's analysis. "
        "Unlike the OS-comparison matrices, each mixed-os-scenarios task has "
        "its own bespoke topology, so most rows only populate the column(s) "
        "for the image(s) that task actually provisions; `—` means that "
        "image was not part of this task's topology.\n",
        "| Task | " + " | ".join(cols) + " |",
        "|---|" + "|".join(["---:"] * len(cols)) + "|",
    ]

    for name, link, per_image in task_data:
        cells = []
        for image in image_order:
            if image in per_image:
                s, f = per_image[image]
                cells.append(f"{s}/{f}")
            else:
                cells.append("—")
        name_cell = f"[{name}]({link})" if link else name
        lines.append("| " + name_cell + " | " + " | ".join(cells) + " |")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "category",
        choices=["single-node-os-comparison", "multi-node-os-comparison", "mixed-os-scenarios"],
    )
    args = parser.parse_args()

    if args.category == "mixed-os-scenarios":
        content = build_mixed_os_scenarios()
    else:
        content = build_matrix_category(args.category)

    output = ROOT / f"{args.category}-summary.md"
    output.write_text(content)
    print(f"wrote {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
