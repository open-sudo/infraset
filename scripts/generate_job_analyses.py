#!/usr/bin/env python3
"""Generate a human-readable verification analysis in every recorded job root."""

from __future__ import annotations

import argparse
import html
import json
import re
import tomllib
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JOBS = ROOT / "jobs"
JOB_NAME = re.compile(r"^\d{4}-\d{2}-\d{2}__\d{2}-\d{2}-\d{2}$")


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def elapsed(start: Any, finish: Any) -> float | None:
    started = parse_time(start)
    finished = parse_time(finish)
    if started is None or finished is None:
        return None
    try:
        return (finished - started).total_seconds()
    except TypeError:
        return None


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


def score(value: Any) -> str:
    if isinstance(value, bool):
        return "1.000" if value else "0.000"
    if isinstance(value, (int, float)):
        return f"{float(value):.3f}"
    return "not available"


def numeric(value: Any) -> float | None:
    if isinstance(value, bool):
        return float(value)
    if isinstance(value, (int, float)):
        return float(value)
    return None


def markdown_text(value: Any) -> str:
    text = str(value if value is not None else "")
    return " ".join(text.split())


def table_text(value: Any) -> str:
    return markdown_text(value).replace("|", "\\|").replace("`", "'")


def quote_markdown(text: str) -> list[str]:
    lines: list[str] = []
    for line in text.strip().splitlines():
        lines.append(f"> {line}" if line else ">")
    return lines or ["> Task instruction was unavailable."]


def format_cluster_entry(value: Any) -> str:
    label = str(value)
    match = re.fullmatch(r"(.+?)\s+x(\d+)", label)
    return f"{match.group(2)} {match.group(1)}" if match else f"1 {label}"


def environment_details(job_dir: Path) -> tuple[str, str, str]:
    try:
        value = tomllib.loads((job_dir / "environment.toml").read_text())
    except (OSError, tomllib.TOMLDecodeError):
        return "not recorded", "not recorded", "not recorded"
    cluster = value.get("cluster", [])
    cluster_text = (
        " + ".join(format_cluster_entry(item) for item in cluster)
        if isinstance(cluster, list) and cluster
        else "not recorded"
    )
    networks = value.get("networks", [])
    network_names = [
        str(item.get("name"))
        for item in networks
        if isinstance(item, dict) and item.get("name") is not None
    ]
    network_text = ", ".join(network_names) if network_names else "provider default"
    control = value.get("control_node")
    return cluster_text, network_text, str(control) if control else "not recorded"


def provision_time_ms(trial_dir: Path) -> float | None:
    payload = read_json(trial_dir / "provision-response.json")
    if payload is None:
        return None
    for item in payload.get("content", []):
        if not isinstance(item, dict) or item.get("type") != "text":
            continue
        raw = item.get("text")
        if not isinstance(raw, str):
            continue
        try:
            response = json.loads(raw)
        except json.JSONDecodeError:
            continue
        value = response.get("provision_time_ms")
        if isinstance(value, (int, float)):
            return float(value)
    return None


def trial_dirs(job_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in job_dir.iterdir()
        if path.is_dir()
        and (path / "result.json").is_file()
        and (path / "config.json").is_file()
    )


def job_dirs(jobs_dir: Path) -> list[Path]:
    values: list[Path] = []
    for task_dir in sorted(path for path in jobs_dir.iterdir() if path.is_dir()):
        for path in sorted(item for item in task_dir.iterdir() if item.is_dir()):
            if JOB_NAME.fullmatch(path.name) and (path / "result.json").is_file():
                values.append(path)
    return values


def command_audit_paths(trial_dir: Path) -> tuple[list[Path], str]:
    canonical = trial_dir / "agent" / "executor-commands.jsonl"
    if canonical.is_file():
        return [canonical], "available"
    attempts = sorted(
        (trial_dir / "agent" / "attempts").glob("*/executor-commands.jsonl")
    )
    if attempts:
        return attempts, "attempt_fallback"
    return [], "unavailable"


def command_audit(trial_dir: Path) -> dict[str, Any]:
    paths, status = command_audit_paths(trial_dir)
    records: dict[str, dict[str, Any]] = {}
    order: list[str] = []
    anonymous = 0
    malformed = 0
    for path in paths:
        attempt: int | None = None
        if path.parent.parent.name == "attempts":
            try:
                attempt = int(path.parent.name)
            except ValueError:
                pass
        try:
            lines = path.read_text(errors="replace").splitlines()
        except OSError:
            continue
        for line in lines:
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                malformed += 1
                continue
            if not isinstance(item, dict):
                malformed += 1
                continue
            command_id = item.get("command_id")
            if not isinstance(command_id, str) or not command_id:
                anonymous += 1
                command_id = f"legacy-command-{anonymous:04d}"
            item = {**item, "command_id": command_id}
            if attempt is not None:
                item.setdefault("executor_attempt", attempt)
            if command_id not in records:
                order.append(command_id)
                records[command_id] = item
            elif item.get("outcome") != "requested":
                records[command_id] = {**records[command_id], **item}

    for command_id in order:
        if records[command_id].get("outcome") == "requested":
            records[command_id] = {
                **records[command_id],
                "outcome": "unfinished",
                "return_code": None,
                "error": "No terminal command record was captured.",
            }
    timeline = [records[command_id] for command_id in order]
    successful = sum(
        item.get("outcome") == "completed" and item.get("return_code") == 0
        for item in timeline
    )
    failed = sum(
        item.get("outcome") == "completed"
        and isinstance(item.get("return_code"), int)
        and item.get("return_code") != 0
        for item in timeline
    )
    return {
        "status": status,
        "paths": paths,
        "records": records,
        "timeline": timeline,
        "successful": successful,
        "failed": failed,
        "issued": len(timeline),
        "malformed": malformed,
    }


def command_display(audit: dict[str, Any]) -> str:
    if audit["status"] == "unavailable":
        return "audit unavailable"
    if audit["issued"] == 0:
        return "0/0 (none issued)"
    if audit["successful"] == 0 and audit["failed"] == 0:
        return "0/0 (no terminal result)"
    return f"{audit['successful']}/{audit['failed']}"


def observation_records(trial_dir: Path) -> dict[str, dict[str, Any]]:
    payload = read_json(trial_dir / "verifier" / "global-observations.json") or {}
    records: dict[str, dict[str, Any]] = {}
    for phase_name in ("before_prepare", "after_prepare", "after_executor"):
        phase = payload.get(phase_name, {})
        if not isinstance(phase, dict):
            continue
        for node in phase.get("nodes", []):
            if not isinstance(node, dict):
                continue
            for item in node.get("observations", []):
                if not isinstance(item, dict) or not isinstance(item.get("id"), str):
                    continue
                records[item["id"]] = {**item, "node": node.get("name")}
    return records


def command_summary(command: Any) -> str:
    if not isinstance(command, str) or not command.strip():
        return "command text unavailable"
    lines = [line.strip() for line in command.splitlines() if line.strip()]
    skip = re.compile(
        r"^(set\s+-|(?:export\s+)?[A-Za-z_][A-Za-z0-9_]*=|printf\b|echo\b|#|[A-Z0-9_]+$)"
    )
    preferred = re.compile(
        r"\b(systemctl|curl|wget|dig|nsupdate|mysql|mariadb|psql|redis-cli|"
        r"openssl|ss\b|ip\b|nft\b|iptables|firewall-cmd|podman|docker|"
        r"kubectl|vtysh|birdc|wg\b|mount|showmount|rpcinfo|journalctl|"
        r"named-check|dnssec-|etcdctl|minio|mc\b|haproxy|nginx|test\b|"
        r"stat\b|getent|ping|nc\b|grep\b|awk\b|find\b|install\b|dnf\b|"
        r"yum\b|apt\b|apk\b|pacman\b)"
    )
    candidates = [line for line in lines if not skip.search(line)] or lines
    selected = next(
        (line for line in candidates if preferred.search(line)), candidates[0]
    )
    selected = re.sub(r"\s+", " ", selected)
    if re.search(
        r"(?i)(/root/[^ ]*password|BEGIN [A-Z ]*PRIVATE KEY|"
        r"(?:PASSWORD|PASSWD|TOKEN|SECRET|PRIVATE_KEY)[A-Z0-9_]*\s*=)",
        selected,
    ):
        return "credential-handling command (sensitive arguments omitted)"
    selected = re.sub(
        r"(?i)(--(?:password|pass|token|secret)(?:=|\s+))(?:\"[^\"]*\"|'[^']*'|\S+)",
        r"\1[redacted]",
        selected,
    )
    selected = re.sub(
        r"[A-Za-z0-9+/]{160,}={0,2}", "[encoded content omitted]", selected
    )
    return selected[:217] + ("..." if len(selected) > 217 else "")


def error_excerpt(record: dict[str, Any]) -> str:
    raw = "\n".join(
        str(record.get(name, "")) for name in ("stderr", "stdout") if record.get(name)
    )
    if not raw.strip():
        return "No error text was captured."
    sensitive = re.compile(
        r"(?i)(password|passwd|secret|token|authorization|private[ _-]?key|api[ _-]?key)"
    )
    interesting = re.compile(
        r"(?i)(error|failed|failure|invalid|unknown|missing|denied|timeout|timed out|"
        r"not found|unreachable|refused|reset|syntax|exit|expired|cannot|couldn't)"
    )
    lines = []
    for line in raw.splitlines():
        clean = markdown_text(line)
        if not clean or sensitive.search(clean):
            continue
        if interesting.search(clean):
            lines.append(clean)
    if not lines:
        lines = [
            markdown_text(line)
            for line in raw.splitlines()
            if line.strip() and not sensitive.search(line)
        ]
    excerpt = "; ".join(lines[-2:]) if lines else "Sensitive error output was omitted."
    return excerpt[:317] + ("..." if len(excerpt) > 317 else "")


def failed_commands(commands: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    values = []
    for record in commands.values():
        return_code = record.get("return_code")
        if isinstance(return_code, int) and return_code != 0:
            values.append(record)
    return sorted(values, key=lambda item: str(item.get("timestamp", "")))


def evidence_ids(report: dict[str, Any]) -> list[str]:
    values: list[str] = []
    for requirement in report.get("requirements", []):
        if not isinstance(requirement, dict):
            continue
        for item in requirement.get("evidence_ids", []):
            if isinstance(item, str) and item not in values:
                values.append(item)
    hygiene = report.get("operational_hygiene", {})
    if isinstance(hygiene, dict):
        for item in hygiene.get("evidence_ids", []):
            if isinstance(item, str) and item not in values:
                values.append(item)
    return values


def evidence_description(
    evidence_id: str,
    commands: dict[str, dict[str, Any]],
    observations: dict[str, dict[str, Any]],
) -> tuple[str, str]:
    command = commands.get(evidence_id)
    if command is not None:
        node = command.get("node", "unknown node")
        rc = command.get("return_code")
        source = f"executor command on {node}, return code {rc}"
        return source, command_summary(command.get("command"))
    observation = observations.get(evidence_id)
    if observation is not None:
        node = observation.get("node", "unknown node")
        status = observation.get("status", "unknown")
        rc = observation.get("return_code")
        source = f"global observation on {node}, {status}, return code {rc}"
        description = observation.get("description") or evidence_id.rsplit(":", 1)[-1]
        return source, markdown_text(description)
    return (
        "unresolved reference",
        "The cited identifier was not found in the recorded command or global-observation artifacts.",
    )


def report_reward(report: dict[str, Any], result: dict[str, Any]) -> float | None:
    value = numeric(report.get("reward"))
    if value is not None:
        return value
    rewards = (result.get("verifier_result") or {}).get("rewards", {})
    if isinstance(rewards, dict):
        return numeric(rewards.get("reward"))
    return None


def report_hygiene(report: dict[str, Any]) -> float | None:
    hygiene = report.get("operational_hygiene")
    if isinstance(hygiene, dict):
        return numeric(hygiene.get("score"))
    return numeric(hygiene)


def verdict(report: dict[str, Any], result: dict[str, Any]) -> str:
    exception = result.get("exception_info")
    reward = report_reward(report, result)
    coverage = numeric(report.get("evaluation_coverage"))
    functionality = numeric(report.get("functionality"))
    complete = report.get("evaluation_complete")
    if (
        exception is None
        and reward is not None
        and reward >= 0.9995
        and coverage is not None
        and coverage >= 0.9995
        and functionality is not None
        and functionality >= 0.9995
        and complete is True
    ):
        return "full success"
    if exception is not None or reward is None:
        return "not successfully evaluated"
    if reward <= 0.0005 and (functionality or 0.0) <= 0.0005:
        return "unsuccessful"
    return "partial success"


def model_name(result: dict[str, Any]) -> str:
    agent = result.get("agent_info", {})
    if not isinstance(agent, dict):
        return "not recorded"
    model = agent.get("model_info", {})
    if not isinstance(model, dict):
        return "not recorded"
    return str(model.get("name") or "not recorded")


def requirement_lines(report: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    requirements = report.get("requirements", [])
    if not isinstance(requirements, list) or not requirements:
        return ["No per-requirement verifier findings were recorded."]
    labels = {
        "satisfied": "Satisfied",
        "partially_satisfied": "Partially satisfied",
        "not_satisfied": "Not satisfied",
        "indeterminate": "Indeterminate",
    }
    for item in requirements:
        if not isinstance(item, dict):
            continue
        identifier = markdown_text(item.get("id") or "requirement")
        status = str(item.get("status") or "unknown")
        requirement = markdown_text(
            item.get("requirement") or "Requirement text unavailable."
        )
        summary = markdown_text(item.get("summary") or "No explanation was recorded.")
        refs = [
            str(value)
            for value in item.get("evidence_ids", [])
            if isinstance(value, str)
        ]
        lines.extend(
            [
                f"- **{identifier} — {labels.get(status, status.replace('_', ' ').title())}:** {requirement}",
                f"  - **Why:** {summary}",
                "  - **Recorded evidence:** "
                + (", ".join(f"`{value}`" for value in refs) if refs else "none cited"),
            ]
        )
    return lines


def trial_metrics(
    trial_dir: Path,
    result: dict[str, Any],
    report: dict[str, Any],
    audit: dict[str, Any],
) -> dict[str, Any]:
    provisioned = provision_time_ms(trial_dir)
    return {
        "verdict": verdict(report, result),
        "reward": report_reward(report, result),
        "coverage": numeric(report.get("evaluation_coverage")),
        "functionality": numeric(report.get("functionality")),
        "hygiene": report_hygiene(report),
        "confidence": numeric(report.get("confidence")),
        "successful_commands": audit["successful"],
        "failed_commands": audit["failed"],
        "commands_display": command_display(audit),
        "command_audit_status": audit["status"],
        "total_duration": elapsed(result.get("started_at"), result.get("finished_at")),
        "environment_duration": elapsed(
            (result.get("environment_setup") or {}).get("started_at"),
            (result.get("environment_setup") or {}).get("finished_at"),
        ),
        "executor_duration": elapsed(
            (result.get("agent_execution") or {}).get("started_at"),
            (result.get("agent_execution") or {}).get("finished_at"),
        ),
        "verifier_duration": elapsed(
            (result.get("verifier") or {}).get("started_at"),
            (result.get("verifier") or {}).get("finished_at"),
        ),
        "provision_ms": provisioned,
    }


def trial_section(trial_dir: Path) -> tuple[list[str], dict[str, Any]]:
    result = read_json(trial_dir / "result.json") or {}
    report = read_json(trial_dir / "verifier" / "evaluation-report.json") or {}
    audit = command_audit(trial_dir)
    commands = audit["records"]
    observations = observation_records(trial_dir)
    metrics = trial_metrics(trial_dir, result, report, audit)
    failures = failed_commands(commands)
    refs = evidence_ids(report)
    unresolved = [
        item for item in refs if item not in commands and item not in observations
    ]
    lines = [
        f"## Trial `{trial_dir.name}`",
        "",
        f"**Verifier decision: {metrics['verdict'].title()}.** "
        + markdown_text(
            report.get("overall_summary")
            or "No overall verifier explanation was recorded."
        ),
        "",
        "| Reward | Coverage | Functionality | Hygiene | Confidence | Commands |",
        "|---:|---:|---:|---:|---:|---:|",
        f"| {score(metrics['reward'])} | {score(metrics['coverage'])} | "
        f"{score(metrics['functionality'])} | {score(metrics['hygiene'])} | "
        f"{score(metrics['confidence'])} | "
        f"{metrics['commands_display']} |",
        "",
        "### Why the verifier reached this decision",
        "",
        *requirement_lines(report),
        "",
        "### Operational hygiene",
        "",
    ]
    hygiene = report.get("operational_hygiene")
    if isinstance(hygiene, dict):
        lines.append(
            f"The verifier assigned hygiene **{score(hygiene.get('score'))}**. "
            + markdown_text(
                hygiene.get("summary") or "No hygiene explanation was recorded."
            )
        )
        hygiene_refs = [
            str(item)
            for item in hygiene.get("evidence_ids", [])
            if isinstance(item, str)
        ]
        if hygiene_refs:
            lines.extend(
                [
                    "",
                    "Hygiene evidence: "
                    + ", ".join(f"`{item}`" for item in hygiene_refs),
                ]
            )
    else:
        lines.append("Operational hygiene was not separately scored in this trial.")

    lines.extend(["", "### Evidence cited by the verifier", ""])
    if refs:
        lines.extend(
            [
                "| Evidence ID | Source | What it records |",
                "|---|---|---|",
            ]
        )
        for item in refs:
            source, description = evidence_description(item, commands, observations)
            lines.append(
                f"| `{table_text(item)}` | {table_text(source)} | {table_text(description)} |"
            )
    else:
        lines.append("The verifier did not cite any recorded evidence identifiers.")

    lines.extend(["", "### Comments and limitations", ""])
    comments: list[str] = []
    exception = result.get("exception_info")
    if isinstance(exception, dict):
        kind = markdown_text(exception.get("exception_type") or "Execution error")
        message = markdown_text(
            exception.get("exception_message") or "No exception message was recorded."
        )
        comments.append(f"**Execution exception:** {kind}: {message}")
    limitations = report.get("limitations", [])
    if isinstance(limitations, list):
        comments.extend(markdown_text(item) for item in limitations if item)
    if unresolved:
        comments.append(
            "The verifier cited unresolved evidence identifiers: "
            + ", ".join(f"`{item}`" for item in unresolved)
            + ". These references reduce the auditability of the decision."
        )
    if metrics["coverage"] is not None and metrics["coverage"] < 0.9995:
        comments.append(
            f"Only {metrics['coverage'] * 100:.1f}% of the requested outcome was conclusively evaluated."
        )
    if metrics["hygiene"] is not None and metrics["hygiene"] < 0.9995:
        comments.append(
            f"Operational hygiene was below a full pass ({metrics['hygiene']:.3f}); review the hygiene explanation above separately from functional success."
        )
    if metrics["confidence"] is not None and metrics["confidence"] < 0.9995:
        comments.append(
            f"Verifier confidence was {metrics['confidence']:.3f}; this is evidence confidence for this trial, not a repeatability estimate."
        )
    if not comments:
        comments.append(
            "The verifier recorded no explicit limitations. This establishes the captured trial outcome, not guaranteed success on every future execution."
        )
    lines.extend(f"- {item}" for item in comments)

    lines.extend(["", "### Failed executor commands", ""])
    if failures:
        lines.extend(
            [
                "A failed command is an unsuccessful attempt, not automatically a failed final outcome. The requirement findings above show whether the executor recovered.",
                "",
                "| Command ID | Node | Return code | Command | Recorded error |",
                "|---|---|---:|---|---|",
            ]
        )
        for item in failures:
            lines.append(
                "| `{}` | {} | {} | `{}` | {} |".format(
                    table_text(item.get("command_id", "unknown")),
                    table_text(item.get("node", "unknown")),
                    table_text(item.get("return_code", "unknown")),
                    table_text(command_summary(item.get("command"))),
                    table_text(error_excerpt(item)),
                )
            )
    else:
        lines.append("No failed executor commands were recorded.")

    if metrics["verdict"] != "full success":
        lines.extend(["", "### Complete executor command timeline", ""])
        if audit["status"] == "unavailable":
            lines.append(
                "The command audit is unavailable. No canonical or per-attempt "
                "audit artifact exists, so the executor timeline cannot be reconstructed."
            )
        elif not audit["timeline"]:
            lines.append(
                "The command audit was captured, but it is empty. The executor "
                "issued no managed-node commands."
            )
        else:
            lines.append(
                "The following is the complete provider-captured executor command "
                "timeline, in execution order. Commands are stored in redacted form."
            )
            for index, item in enumerate(audit["timeline"], 1):
                command = item.get("command")
                rendered_command = (
                    command if isinstance(command, str) and command else "(unavailable)"
                )
                summary = (
                    f"{index}. {item.get('command_id', 'unknown')} · "
                    f"{item.get('node', 'unknown')} · {item.get('outcome', 'unknown')}"
                )
                lines.extend(
                    [
                        "",
                        "<details>",
                        f"<summary>{html.escape(summary)}</summary>",
                        "",
                        f"- Attempt: `{table_text(item.get('executor_attempt', 'not recorded'))}`",
                        f"- Timestamp: `{table_text(item.get('timestamp', 'not recorded'))}`",
                        f"- Return code: `{table_text(item.get('return_code', 'not recorded'))}`",
                        f"- Duration: `{table_text(item.get('duration_ms', 'not recorded'))}` ms",
                        "",
                        f"<pre><code>{html.escape(rendered_command)}</code></pre>",
                        "",
                        "</details>",
                    ]
                )

    provision = metrics["provision_ms"]
    provision_text = (
        f"{provision / 1000:.3f}s" if provision is not None else "not recorded"
    )
    lines.extend(
        [
            "",
            "### Timing",
            "",
            f"- Total trial duration: **{format_duration(metrics['total_duration'])}**",
            f"- Environment setup: **{format_duration(metrics['environment_duration'])}**",
            f"- Antrieb provisioning response: **{provision_text}**",
            f"- Executor phase: **{format_duration(metrics['executor_duration'])}**",
            f"- Verifier phase: **{format_duration(metrics['verifier_duration'])}**",
            "",
            "### Trial artifacts",
            "",
            f"- [Trial result]({trial_dir.name}/result.json)",
        ]
    )
    if (trial_dir / "verifier" / "evaluation-report.json").is_file():
        lines.append(
            f"- [Verifier report]({trial_dir.name}/verifier/evaluation-report.json)"
        )
    for index, path in enumerate(audit["paths"], 1):
        relative = path.relative_to(trial_dir.parent)
        label = (
            "Executor command audit"
            if len(audit["paths"]) == 1
            else f"Executor command audit {index}"
        )
        lines.append(f"- [{label}]({relative.as_posix()})")
    if (trial_dir / "verifier" / "global-observations.json").is_file():
        lines.append(
            f"- [Global observations]({trial_dir.name}/verifier/global-observations.json)"
        )
    lines.append("")
    metrics["model"] = model_name(result)
    metrics["unresolved_evidence"] = len(unresolved)
    metrics["actual_failed_commands"] = len(failures)
    return lines, metrics


def job_outcome_text(metrics: list[dict[str, Any]]) -> str:
    counts = {
        name: sum(1 for item in metrics if item["verdict"] == name)
        for name in (
            "full success",
            "partial success",
            "unsuccessful",
            "not successfully evaluated",
        )
    }
    total = len(metrics)
    if counts["full success"] == total:
        if total == 1:
            return "The verifier treated the recorded trial as a full success. All requested outcomes were conclusively supported by the cited evidence."
        return (
            f"The verifier treated all {total} independently provisioned trials as full successes. "
            "The repeated result strengthens run-level repeatability, while still not guaranteeing future executions."
        )
    parts = [f"{value} {name}" for name, value in counts.items() if value]
    return (
        "The verifier did not produce a uniform full-success result across this job: "
        + ", ".join(parts)
        + ". The trial sections below explain the divergence."
    )


def generate_job(job_dir: Path) -> dict[str, Any]:
    root_result = read_json(job_dir / "result.json") or {}
    instruction = (job_dir / "instruction.md").read_text(errors="replace")
    cluster, networks, control = environment_details(job_dir)
    trials = trial_dirs(job_dir)
    trial_content: list[list[str]] = []
    trial_metrics_values: list[dict[str, Any]] = []
    for directory in trials:
        section, metrics = trial_section(directory)
        trial_content.append(section)
        trial_metrics_values.append(metrics)

    stats = root_result.get("stats", {})
    stats = stats if isinstance(stats, dict) else {}
    job_duration = elapsed(
        root_result.get("started_at"), root_result.get("finished_at")
    )
    models = sorted({item["model"] for item in trial_metrics_values})
    lines = [
        "<!-- Generated by scripts/generate_job_analyses.py. -->",
        f"# Verification analysis: {job_dir.parent.name}",
        "",
        f"Job: `{job_dir.name}`",
        "",
        "This report explains the verifier decisions recorded for this job. It interprets the saved evidence; it does not rerun the task or independently inspect the expired clusters.",
        "",
        "## Task",
        "",
        *quote_markdown(instruction),
        "",
        "## Environment",
        "",
        f"- Systems: **{cluster}**",
        f"- Networks: **{networks}**",
        f"- Control node: **{control}**",
        f"- Executor model: **{', '.join(models) if models else 'not recorded'}**",
        "",
        "## Job outcome",
        "",
        job_outcome_text(trial_metrics_values),
        "",
        f"The job contains **{len(trials)} {'trial' if len(trials) == 1 else 'trials'}**, completed in "
        f"**{format_duration(job_duration)}** with **{int(stats.get('n_errored_trials', 0) or 0)} "
        f"Harbor-reported errored {'trial' if int(stats.get('n_errored_trials', 0) or 0) == 1 else 'trials'}** "
        f"and **{int(stats.get('n_retries', 0) or 0)} "
        f"{'retry' if int(stats.get('n_retries', 0) or 0) == 1 else 'retries'}**.",
        "",
        "| Trial | Decision | Reward | Coverage | Functionality | Hygiene | Commands | Duration |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for directory, metrics in zip(trials, trial_metrics_values, strict=True):
        lines.append(
            f"| `{directory.name}` | {metrics['verdict'].title()} | {score(metrics['reward'])} | "
            f"{score(metrics['coverage'])} | {score(metrics['functionality'])} | "
            f"{score(metrics['hygiene'])} | {metrics['commands_display']} | "
            f"{format_duration(metrics['total_duration'])} |"
        )
    lines.append("")
    for section in trial_content:
        lines.extend(section)

    lines.extend(["## Overall comments for readers", ""])
    if len(trials) == 1:
        lines.append(
            "- This job contains one trial. Its evidence can establish what happened in that execution, but it cannot measure run-to-run variability."
        )
    else:
        verdicts = {item["verdict"] for item in trial_metrics_values}
        if len(verdicts) == 1:
            lines.append(
                f"- All {len(trials)} trials received the same `{next(iter(verdicts))}` classification, providing a useful repeatability check within this job."
            )
        else:
            lines.append(
                "- The trials diverged. Treat the successful and unsuccessful paths as separate evidence rather than relying only on their average score."
            )
    failed_total = sum(item["actual_failed_commands"] for item in trial_metrics_values)
    if failed_total:
        lines.append(
            f"- The executor audit contains {failed_total} failed command attempt(s). Review their surrounding trial findings before interpreting them as final task failures."
        )
    unresolved_total = sum(item["unresolved_evidence"] for item in trial_metrics_values)
    if unresolved_total:
        lines.append(
            f"- The verifier cited {unresolved_total} evidence reference(s) that could not be resolved from the saved command and global-observation artifacts."
        )
    lines.extend(
        [
            "- Scores describe the outcomes supported by these recorded executions; they are not a general claim that the model will always complete the task.",
            "",
            "## Job artifacts",
            "",
            "- [Task instruction](instruction.md)",
            "- [Environment definition](environment.toml)",
            "- [Aggregate job result](result.json)",
            "",
        ]
    )
    (job_dir / "analysis.md").write_text("\n".join(lines))
    return {
        "job": str(job_dir.relative_to(ROOT)),
        "trials": len(trials),
        "failed_commands": failed_total,
        "unresolved_evidence": unresolved_total,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=Path, default=DEFAULT_JOBS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    jobs = job_dirs(args.jobs)
    records = [generate_job(path) for path in jobs]
    print(
        "generated {} analyses for {} trials; {} failed command attempts; {} unresolved evidence references".format(
            len(records),
            sum(item["trials"] for item in records),
            sum(item["failed_commands"] for item in records),
            sum(item["unresolved_evidence"] for item in records),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
