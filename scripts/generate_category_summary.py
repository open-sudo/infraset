#!/usr/bin/env python3
"""Generate a task x OS command cross-reference summary for a job category.

Produces `metrics/<scenario-id>/<timestamp>/<category>.md`; explicit aggregates
use `metrics/<scenario-id>/aggregate-<category>.md`. Each row is a task;
each column is an operating system / image that appears in that category.
For the catalog-driven matrices (single-node-os-comparison,
multi-node-os-comparison) the file has two tables built from each task's
latest recorded job run: successful/failed executor commands as
"success/failure", and how long that job run took to complete. Every cell
links to the analysis.md of the specific job run it describes.
mixed-os-scenarios only gets the commands table, since its tasks are bespoke
rather than a repeated matrix.

Usage:
    python scripts/generate_category_summary.py single-node-os-comparison
    python scripts/generate_category_summary.py --scenario 5469 --aggregate \
        multi-node-os-comparison
    python scripts/generate_category_summary.py --scenario 5782 \
        --run 2026-10-02__08-42-41 single-node-os-comparison
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import re
import tomllib
from datetime import datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from generate_provisioning_metrics import (  # noqa: E402
    samples as provisioning_samples,
    trial_share as provisioning_trial_share,
)
from job_layout import RUN_NAME, iter_job_dirs, job_location  # noqa: E402
from scenario_layout import collection_asset, collection_root

ROOT = Path(__file__).resolve().parents[1]
JOBS = ROOT / "jobs"
TASKS = ROOT / "tasks"

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


def trial_dirs(job_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in job_dir.iterdir()
        if path.is_dir()
        and (path / "result.json").is_file()
        and (path / "config.json").is_file()
    )


def command_records(trial_dir: Path) -> list[dict[str, Any]]:
    canonical = trial_dir / "agent" / "executor-commands.jsonl"
    paths = (
        [canonical]
        if canonical.is_file()
        else sorted(
            (trial_dir / "agent" / "attempts").glob("*/executor-commands.jsonl")
        )
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


# A command whose exec channel dropped never reached the managed node, so it
# says nothing about the operating system or the executor. These are dominated
# by the deliberate post-reboot liveness polling that the restart-evidence
# protocol requires: every poll issued while the node is still rebooting
# records one. Counting them as failures penalises whichever image is slowest
# to bring sshd back up, which is not what this table is measuring.
_TRANSPORT_FAILURE = re.compile(
    r"connection reset by peer"
    r"|connection timed out"
    r"|closed by remote host"
    r"|exec stream closed",
    re.IGNORECASE,
)


def is_transport_failure(record: dict[str, Any]) -> bool:
    """Report whether a non-zero command failed in transit rather than on the node."""
    for field in ("stderr", "error"):
        value = record.get(field)
        if isinstance(value, str) and _TRANSPORT_FAILURE.search(value):
            return True
    return False


def command_stats(
    records: list[dict[str, Any]], node_filter: set[str] | None = None
) -> tuple[int, int, int]:
    """Return (successful, failed, transport) counts for completed commands."""
    successful = failed = transport = 0
    for record in records:
        if node_filter is not None and record.get("node") not in node_filter:
            continue
        if record.get("outcome") != "completed":
            continue
        return_code = record.get("return_code")
        if return_code == 0:
            successful += 1
        elif isinstance(return_code, int):
            if is_transport_failure(record):
                transport += 1
            else:
                failed += 1
    return successful, failed, transport


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


def relative_link(path: Path, output_dir: Path) -> str:
    """Return a relative link from a generated metrics directory to a job path."""
    return os.path.relpath(path, output_dir)


def completed_jobs(category_roots: list[Path], category: str | None = None) -> dict[tuple[str, ...], Path]:
    """Index the latest completed job for each task path in the selected scope."""
    jobs: dict[tuple[str, ...], Path] = {}
    for category_root in category_roots:
        for result_path in sorted(category_root.rglob("result.json")):
            payload = read_json(result_path)
            if payload is None or "n_total_trials" not in payload:
                continue
            job_dir = result_path.parent
            metadata = read_toml(job_dir / 'variant.toml') or {}
            if category is not None and metadata.get('category') != category:
                continue
            # A Harbor aggregate result can exist even when provisioning failed
            # before a trial directory and provider response were recorded. Such
            # infrastructure failures must not replace a completed task result
            # or count against the runner.
            if not any(
                trial.is_dir() and (trial / "provision-response.json").is_file()
                for trial in job_dir.iterdir()
            ):
                continue
            key = (metadata['os'], f"{metadata['usecase']}-{metadata['os']}") if metadata else job_dir.relative_to(category_root).parts
            jobs[key] = job_dir
    return jobs


def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def trial_duration_seconds(trial_dir: Path) -> float | None:
    result = read_json(trial_dir / "result.json") or {}
    started = parse_time(result.get("started_at"))
    finished = parse_time(result.get("finished_at"))
    if started is None or finished is None:
        return None
    return (finished - started).total_seconds()


def trial_hygiene(trial_dir: Path) -> float | None:
    result = read_json(trial_dir / "result.json") or {}
    rewards = (result.get("verifier_result") or {}).get("rewards")
    if not isinstance(rewards, dict):
        return None
    value = rewards.get("operational_hygiene")
    return float(value) if isinstance(value, (int, float)) else None


def format_hygiene(value: float | None) -> str:
    return f"{value:.3f}" if value is not None else "not available"


def format_duration(seconds: float | None) -> str:
    if seconds is None:
        return "not recorded"
    rounded = max(0, round(seconds))
    hours, remainder = divmod(rounded, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours}h {minutes:02d}m {secs:02d}s"
    if minutes:
        return f"{minutes}m {secs:02d}s"
    return f"{secs}s"


def provisioning_note(jobs_root: Path) -> str:
    """One line placing cluster provisioning next to the completion times."""
    values = [elapsed for _, _, elapsed in provisioning_samples(jobs_root)]
    if not values:
        return ""
    share = provisioning_trial_share(jobs_root)
    note = (
        f"Cluster provisioning is not a meaningful part of these times: "
        f"median {statistics.median(values):.0f} ms across {len(values)} "
        f"clusters"
    )
    if share is not None:
        note += f", about {share:.2f}% of a trial's wall clock"
    return note + (
        ". See [cluster provisioning performance]"
        "(cluster-provisioning-performance.md).\n"
    )


def build_matrix_category(
    category: str,
    jobs_by_task: dict[tuple[str, ...], Path],
    output_dir: Path,
    provisioning_root: Path,
    scope_label: str,
) -> str:
    """single-node-os-comparison / multi-node-os-comparison: catalog-driven matrix."""
    catalog = read_toml(collection_asset('vanilla', f'{category}/catalog.toml'))
    if catalog is None:
        raise SystemExit(f"no catalog.toml found for {category}")
    systems = catalog.get("operating_systems", [])
    tasks = catalog.get("tasks", [])
    os_ids = [(item["id"], item.get("label", item["id"])) for item in systems]
    slugs = [item["slug"] for item in tasks]
    # Preserve catalog ordering while including newer tasks and legacy OS variants.
    for job in jobs_by_task.values():
        metadata = read_toml(job / 'variant.toml') or {}
        if metadata.get('usecase') and metadata['usecase'] not in slugs:
            slugs.append(metadata['usecase'])
        if metadata.get('os') and metadata['os'] not in {key for key, _ in os_ids}:
            os_ids.append((metadata['os'], label_for(metadata['os'])))

    cols = [label for _, label in os_ids]
    header = [
        "| Task | " + " | ".join(cols) + " |",
        "|---|" + "|".join(["---:"] * len(cols)) + "|",
    ]

    # cell_data[slug][os_id] = (link, successful, failed, avg_duration_seconds, avg_hygiene) or None
    cell_data: dict[
        str, dict[str, tuple[str, int, int, float | None, float | None] | None]
    ] = {}

    for slug in slugs:
        cell_data[slug] = {}
        for os_id, _ in os_ids:
            task_dir = jobs_by_task.get((os_id, f"{slug}-{os_id}"))
            if task_dir is None:
                cell_data[slug][os_id] = None
                continue
            latest = task_dir
            successful = failed = 0
            durations: list[float] = []
            hygiene_scores: list[float] = []
            for trial_dir in trial_dirs(latest):
                records = command_records(trial_dir)
                s, f, _transport = command_stats(records)
                successful += s
                failed += f
                duration = trial_duration_seconds(trial_dir)
                if duration is not None:
                    durations.append(duration)
                hygiene = trial_hygiene(trial_dir)
                if hygiene is not None:
                    hygiene_scores.append(hygiene)
            link = relative_link(latest / "analysis.md" if (latest / "analysis.md").is_file() else latest, output_dir)
            avg_duration = sum(durations) / len(durations) if durations else None
            avg_hygiene = (
                sum(hygiene_scores) / len(hygiene_scores) if hygiene_scores else None
            )
            cell_data[slug][os_id] = (
                link,
                successful,
                failed,
                avg_duration,
                avg_hygiene,
            )

    def column_averages() -> dict[
        str, tuple[float | None, float | None, float | None, float | None]
    ]:
        averages: dict[
            str, tuple[float | None, float | None, float | None, float | None]
        ] = {}
        for os_id, _ in os_ids:
            entries = [
                cell_data[slug][os_id]
                for slug in slugs
                if cell_data[slug][os_id] is not None
            ]
            if not entries:
                averages[os_id] = (None, None, None, None)
                continue
            avg_success = sum(e[1] for e in entries) / len(entries)
            avg_failed = sum(e[2] for e in entries) / len(entries)
            durations = [e[3] for e in entries if e[3] is not None]
            avg_duration = sum(durations) / len(durations) if durations else None
            hygiene_scores = [e[4] for e in entries if e[4] is not None]
            avg_hygiene = (
                sum(hygiene_scores) / len(hygiene_scores) if hygiene_scores else None
            )
            averages[os_id] = (avg_success, avg_failed, avg_duration, avg_hygiene)
        return averages

    averages = column_averages()

    commands_lines = [
        f"# {category}: command execution summary\n",
        f"Scope: `{scope_label}`.\n",
        "Successful/failed executor commands per task per OS, from each task's "
        "latest recorded job run. Each success/failure count links to the "
        "analysis for that specific job. `0/0` means the audit was captured "
        "but no managed-node commands were issued. `—` means the task has "
        "not been executed yet for that OS. The final **Average** row is the "
        "mean successful/failed count per OS across all tasks with a "
        "recorded run.\n",
        "Commands whose exec channel dropped (connection reset, connection "
        "timed out, closed by remote host, exec stream closed) are excluded "
        "from both counts: they never reached the node, and they are "
        "dominated by the deliberate post-reboot liveness polling that the "
        "restart-evidence protocol requires. Counting them would rank images "
        "by how slowly they bring sshd back up rather than by how the "
        "executor handled them.\n",
        *header,
    ]
    for slug in slugs:
        cells = []
        for os_id, _ in os_ids:
            data = cell_data[slug][os_id]
            cells.append("—" if data is None else f"[{data[1]}/{data[2]}]({data[0]})")
        commands_lines.append("| " + slug + " | " + " | ".join(cells) + " |")
    avg_cells = []
    for os_id, _ in os_ids:
        avg_success, avg_failed, _, _ = averages[os_id]
        avg_cells.append(
            "—" if avg_success is None else f"{avg_success:.1f}/{avg_failed:.1f}"
        )
    commands_lines.append("| **Average** | " + " | ".join(avg_cells) + " |")

    duration_lines = [
        "",
        "## Completion time\n",
        "Wall-clock time from job start to finish for the same latest recorded "
        "job run per task per OS (averaged across trials when a job ran more "
        "than one). Each duration links to the analysis for that specific "
        "job. `—` means the task has not been executed yet for that OS. The "
        "final **Average** row is the mean completion time per OS across all "
        "tasks with a recorded run.\n",
        *header,
    ]
    for slug in slugs:
        cells = []
        for os_id, _ in os_ids:
            data = cell_data[slug][os_id]
            cells.append(
                "—" if data is None else f"[{format_duration(data[3])}]({data[0]})"
            )
        duration_lines.append("| " + slug + " | " + " | ".join(cells) + " |")
    avg_cells = []
    for os_id, _ in os_ids:
        _, _, avg_duration, _ = averages[os_id]
        avg_cells.append(
            format_duration(avg_duration) if avg_duration is not None else "—"
        )
    duration_lines.append("| **Average** | " + " | ".join(avg_cells) + " |")
    duration_lines.append("")
    duration_lines.append(provisioning_note(provisioning_root))

    hygiene_lines = [
        "",
        "## Operational hygiene\n",
        "Operational-hygiene score (1.000 = no unnecessary mutations, "
        "attributable residue, or unrelated regression found) from the "
        "verifier's evaluation of the same latest recorded job run per task "
        "per OS, averaged across trials when a job ran more than one. Each "
        "score links to the analysis for that specific job. `—` means the "
        "task has not been executed yet for that OS, or the run has no "
        "recorded verifier score. The final **Average** row is the mean "
        "hygiene score per OS across all tasks with a recorded score.\n",
        *header,
    ]
    for slug in slugs:
        cells = []
        for os_id, _ in os_ids:
            data = cell_data[slug][os_id]
            if data is None or data[4] is None:
                cells.append("—")
            else:
                cells.append(f"[{format_hygiene(data[4])}]({data[0]})")
        hygiene_lines.append("| " + slug + " | " + " | ".join(cells) + " |")
    avg_cells = []
    for os_id, _ in os_ids:
        _, _, _, avg_hygiene = averages[os_id]
        avg_cells.append(
            format_hygiene(avg_hygiene) if avg_hygiene is not None else "—"
        )
    hygiene_lines.append("| **Average** | " + " | ".join(avg_cells) + " |")

    return "\n".join(commands_lines + duration_lines + hygiene_lines + [""])


def build_mixed_os_scenarios(
    jobs_by_task: dict[tuple[str, ...], Path],
    output_dir: Path,
    scope_label: str,
) -> str:
    """mixed-os-scenarios: bespoke per-task topology, no shared catalog."""
    task_data: list[tuple[str, str | None, dict[str, tuple[int, int]]]] = []
    seen_images: dict[str, None] = {}

    for task_parts, task_dir in sorted(jobs_by_task.items()):
        latest = task_dir
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
                s, f, _transport = command_stats(records, node_filter=nodes)
                successful += s
                failed += f
            per_image[image] = (successful, failed)

        link = relative_link(latest / "analysis.md" if (latest / "analysis.md").is_file() else latest, output_dir)
        task_data.append(("/".join(task_parts), link, per_image))

    image_order = sorted(seen_images, key=lambda image: label_for(image))
    cols = [label_for(image) for image in image_order]
    lines = [
        "# mixed-os-scenarios: command execution summary\n",
        f"Scope: `{scope_label}`.\n",
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
        help=(
            "Job category under jobs/. A category with a "
            "tasks/<category>/catalog.toml is rendered as a task x OS matrix; "
            "mixed-os-scenarios is rendered from its per-task topologies."
        ),
    )
    parser.add_argument(
        "--scenario", "--runner",
        dest="runner",
        default="5782",
        help="Scenario ID (default: 5782); --runner remains a compatibility alias.",
    )
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument(
        "--run",
        dest="run_name",
        help="Timestamped run to summarize (default: latest for the scenario).",
    )
    scope.add_argument(
        "--aggregate",
        action="store_true",
        help="Use the latest completed job per task across this scenario's runs (explicitly combines execution settings).",
    )
    args = parser.parse_args()

    args.runner = collection_root(args.runner).name
    runner_root = JOBS / args.runner
    available_run_names = sorted(
        {
            job_location(job_dir, JOBS).run_name
            for job_dir in iter_job_dirs(runner_root)
            if job_location(job_dir, JOBS).category == args.category
        }
    )
    if not available_run_names:
        raise SystemExit(f"no recorded runs for runner {args.runner!r}")

    if args.aggregate:
        category_roots = [
            runner_root / run_name
            for run_name in available_run_names
            if (runner_root / run_name).is_dir()
        ]
        scope_name = "aggregate"
        provisioning_root = runner_root
    else:
        if args.run_name:
            run_name = args.run_name
        else:
            category_runs = [
                run_name
                for run_name in available_run_names
                if (runner_root / run_name).is_dir()
            ]
            run_name = category_runs[-1] if category_runs else available_run_names[-1]
        category_root = runner_root / run_name
        category_roots = [category_root] if category_root.is_dir() else []
        scope_name = run_name
        provisioning_root = category_root

    if not category_roots:
        raise SystemExit(
            f"no recorded jobs for category {args.category!r} in "
            f"{args.runner}/{scope_name}"
        )

    output_dir = ROOT / "metrics" / args.runner
    if not args.aggregate:
        output_dir /= scope_name
    jobs_by_task = completed_jobs(category_roots, args.category)
    if not jobs_by_task:
        raise SystemExit(
            f"no completed jobs for category {args.category!r} in "
            f"{args.runner}/{scope_name}"
        )
    scope_label = f"{args.runner}/{scope_name}"

    if collection_asset('vanilla', f'{args.category}/catalog.toml').is_file():
        content = build_matrix_category(
            args.category,
            jobs_by_task,
            output_dir,
            provisioning_root,
            scope_label,
        )
    elif args.category == "mixed-os-scenarios":
        content = build_mixed_os_scenarios(jobs_by_task, output_dir, scope_label)
    else:
        raise SystemExit(
            f"category {args.category!r} has no catalog.toml and no bespoke builder"
        )

    output = output_dir / f"{'aggregate-' if args.aggregate else ''}{args.category}.md"
    output_dir.mkdir(parents=True, exist_ok=True)
    output.write_text(content)
    print(f"wrote {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
