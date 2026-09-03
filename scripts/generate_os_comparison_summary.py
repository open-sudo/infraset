#!/usr/bin/env python3
"""Generate the OS comparison execution summary from recorded Harbor jobs."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).parent))

from generate_results_summary import (
    command_audit_stats,
    format_duration,
    metric,
    provision_time_ms,
    read_json,
    timestamp,
    trial_dirs,
)

JOBS = ROOT / "jobs"
TASKS = ROOT / "tasks" / "os-comparison"
OUTPUT = ROOT / "os-comparison-summary.md"
GITHUB_TREE = "https://github.com/open-sudo/infraset/tree/main/jobs"

OS_ORDER = [
    ("almalinux9",      "AlmaLinux 9"),
    ("alpine",          "Alpine Linux"),
    ("archlinux",       "Arch Linux"),
    ("centos-stream10", "CentOS Stream 10"),
    ("debian13",        "Debian 13"),
    ("rhel7",           "RHEL 7.9"),
    ("rhel8",           "RHEL 8.8"),
    ("rhel9",           "RHEL 9.8"),
    ("rhel10",          "RHEL 10.0"),
    ("ubuntu16",        "Ubuntu 16.04"),
    ("ubuntu24",        "Ubuntu 24.04"),
]

# OSes included in the cross-reference command table
CROSSREF_OS = [
    ("almalinux9",      "AlmaLinux 9"),
    ("alpine",          "Alpine"),
    ("archlinux",       "Arch"),
    ("centos-stream10", "CentOS S10"),
    ("debian13",        "Debian 13"),
    ("rhel7",           "RHEL 7.9"),
    ("rhel8",           "RHEL 8.8"),
    ("rhel9",           "RHEL 9.8"),
]

METRIC_NAMES = ("reward", "evaluation_coverage", "functionality", "operational_hygiene")


def os_anchor(label: str) -> str:
    return label.lower().replace(" ", "-").replace(".", "")


def job_dirs(task_dir: Path) -> list[Path]:
    return sorted(
        p for p in task_dir.iterdir()
        if p.is_dir() and (p / "result.json").is_file()
    )


def load_task(task_name: str) -> dict | None:
    task_dir = JOBS / task_name
    if not task_dir.exists():
        return None
    jobs = job_dirs(task_dir)
    if not jobs:
        return None

    reward_vals: list[float] = []
    coverage_vals: list[float] = []
    functionality_vals: list[float] = []
    hygiene_vals: list[float] = []
    exec_durations: list[float] = []
    prov_ms_vals: list[float] = []
    successful_commands = 0
    failed_commands = 0

    for job_dir in jobs:
        for trial_dir in trial_dirs(job_dir):
            result = read_json(trial_dir / "result.json")
            if result is None:
                continue
            vr = result.get("verifier_result") or {}
            rewards = vr.get("rewards") or {}
            rewards = rewards if isinstance(rewards, dict) else {}
            reward_vals.append(metric(rewards, "reward"))
            coverage_vals.append(metric(rewards, "evaluation_coverage"))
            functionality_vals.append(metric(rewards, "functionality"))
            hygiene_vals.append(metric(rewards, "operational_hygiene"))

            agent = result.get("agent_execution") or {}
            t0 = timestamp(agent.get("started_at"))
            t1 = timestamp(agent.get("finished_at"))
            if t0 and t1:
                exec_durations.append((t1 - t0).total_seconds())

            prov = provision_time_ms(trial_dir)
            if prov is not None:
                prov_ms_vals.append(prov)

            cmd = command_audit_stats(trial_dir)
            successful_commands += cmd["successful"]
            failed_commands += cmd["failed"]

    if not reward_vals:
        return None

    def avg(vals: list[float]) -> float:
        return sum(vals) / len(vals) if vals else 0.0

    return {
        "reward": avg(reward_vals),
        "coverage": avg(coverage_vals),
        "functionality": avg(functionality_vals),
        "hygiene": avg(hygiene_vals),
        "exec_seconds": avg(exec_durations),
        "prov_seconds": avg(prov_ms_vals) / 1000 if prov_ms_vals else None,
        "successful_commands": successful_commands,
        "failed_commands": failed_commands,
        "latest_job": jobs[-1].name,
    }


def fmt_prov(seconds: float | None) -> str:
    return f"{seconds:.2f}s" if seconds is not None else "—"


def get_commands(task_name: str) -> tuple[int, int] | None:
    task_dir = JOBS / task_name
    if not task_dir.exists():
        return None
    runs = sorted(p for p in task_dir.iterdir() if p.is_dir() and (p / "result.json").is_file())
    if not runs:
        return None
    s = f = 0
    for trial_dir in trial_dirs(runs[-1]):
        stats = command_audit_stats(trial_dir)
        s += stats["successful"]
        f += stats["failed"]
    return s, f


def build_crossref_table() -> list[str]:
    base_tasks = sorted(
        d.name.removesuffix("-almalinux9")
        for d in (TASKS / "almalinux9").iterdir() if d.is_dir()
    )
    cols = [label for _, label in CROSSREF_OS]
    lines = [
        "## Commands by task and OS\n",
        "Successful/failed executor commands per task per OS. "
        "`0/0` means the audit was captured but no managed-node commands were issued.\n",
        "| Task | " + " | ".join(cols) + " |",
        "|---|" + "|".join(["---:"] * len(CROSSREF_OS)) + "|",
    ]
    for task in base_tasks:
        cells = []
        for os_id, _ in CROSSREF_OS:
            result = get_commands(f"{task}-{os_id}")
            if result is None:
                cells.append("—")
            else:
                cells.append(f"{result[0]}/{result[1]}")
        lines.append("| " + task + " | " + " | ".join(cells) + " |")
    lines.append("")
    return lines


def build_summary() -> str:
    lines: list[str] = []

    lines.append("# OS Comparison: Task Execution Results\n")
    lines.append(
        "Results across 50 infrastructure tasks executed on each OS by an LLM agent "
        "(Codex / gpt-5.6-sol). Metrics are averages across recorded trials. "
        "`Reward` measures the supported outcome. `Hygiene` measures unnecessary mutations, "
        "attributable residue, and unrelated regression (1.000 = no problems found). "
        "Tasks without a job folder were not yet executed.\n"
    )

    lines.append("## Operating systems\n")
    for os_id, os_label in OS_ORDER:
        lines.append(f"- [{os_label}](#{os_anchor(os_label)})")
    lines.append("")

    lines.extend(build_crossref_table())

    for os_id, os_label in OS_ORDER:
        lines.append(f"## {os_label}\n")
        task_dirs = sorted(d for d in (TASKS / os_id).iterdir() if d.is_dir())
        total = len(task_dirs)
        executed = sum(1 for t in task_dirs if (JOBS / t.name).exists())
        lines.append(f"*{executed}/{total} tasks executed.*\n")
        lines.append(
            "| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |"
        )
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")

        for task_dir in task_dirs:
            task_name = task_dir.name
            display = task_name.removesuffix(f"-{os_id}")
            data = load_task(task_name)
            if data is None:
                lines.append(f"| {display} | — | — | — | — | — | — | — |")
            else:
                url = f"{GITHUB_TREE}/{task_name}/{data['latest_job']}"
                exec_t = format_duration(data["exec_seconds"]) if data["exec_seconds"] else "—"
                cmds = f"{data['successful_commands']}/{data['failed_commands']}"
                lines.append(
                    f"| [{display}]({url}) "
                    f"| {cmds} "
                    f"| {data['reward']:.3f} "
                    f"| {data['coverage']:.3f} "
                    f"| {data['functionality']:.3f} "
                    f"| {data['hygiene']:.3f} "
                    f"| {fmt_prov(data['prov_seconds'])} "
                    f"| {exec_t} |"
                )
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    content = build_summary()
    OUTPUT.write_text(content)
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
