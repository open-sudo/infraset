#!/usr/bin/env python3
"""Validate one evidence-based InfraSet task without contacting Antrieb."""

from __future__ import annotations

import argparse
import ipaddress
import re
import stat
import sys
from pathlib import Path
from typing import Any

import tomllib

try:
    from harbor.models.task.config import TaskConfig
    from harbor_antrieb.config import AntriebDefinition
    from harbor_antrieb.static_preparer import (
        StaticBaselineConfig,
        StaticSetupConfig,
    )
    from pydantic import ValidationError
except ModuleNotFoundError as exc:  # pragma: no cover - exercised by CLI packaging
    TaskConfig = None  # type: ignore[assignment,misc]
    AntriebDefinition = None  # type: ignore[assignment,misc]
    StaticBaselineConfig = None  # type: ignore[assignment,misc]
    StaticSetupConfig = None  # type: ignore[assignment,misc]
    ValidationError = ValueError  # type: ignore[assignment,misc]
    MODEL_IMPORT_ERROR: ModuleNotFoundError | None = exc
else:
    MODEL_IMPORT_ERROR = None


CORE_REQUIRED_FILES = (
    "instruction.md",
    "task.toml",
    "environment/harbor_antrieb.toml",
    "tests/test.sh",
)
LEGACY_VERIFIER_FILES = (
    "verifier/judge.toml",
    "verifier/checks.toml",
)
HARNESS_TERMS = re.compile(
    r"\b(?:harbor|antrieb|mcp|cluster lifecycle|do not|don't|must not|never)\b",
    re.IGNORECASE,
)
BASE_RUNBOOK = re.compile(r"antrieb/(?:primer|[a-z0-9-]+-(?:primer|reference))")
IP_CANDIDATE = re.compile(
    r"(?<![A-Za-z0-9_])(?:"
    r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
    r"|(?:[0-9A-Fa-f]{0,4}:){2,7}[0-9A-Fa-f]{0,4}"
    r")(?:/[0-9]{1,3})?(?![A-Za-z0-9_])"
)


def literal_ips(text: str) -> list[str]:
    found: set[str] = set()
    for match in IP_CANDIDATE.finditer(text):
        candidate = match.group(0)
        try:
            ipaddress.ip_interface(candidate)
        except ValueError:
            continue
        found.add(candidate)
    return sorted(found)


def validate_runtime_model(
    model: Any,
    data: Any,
    label: str,
    errors: list[str],
) -> None:
    try:
        model.model_validate(data)
    except ValidationError as exc:
        errors.append(f"{label} does not match the current runtime schema: {exc}")


def load_toml(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        return tomllib.loads(path.read_text())
    except (OSError, tomllib.TOMLDecodeError) as exc:
        errors.append(f"{path}: {exc}")
        return {}


def cluster_node_count(cluster: object) -> int | None:
    if not isinstance(cluster, list) or not cluster:
        return None
    total = 0
    for item in cluster:
        if isinstance(item, str):
            match = re.search(r"\s+x(\d+)\s*$", item)
            total += int(match.group(1)) if match else 1
        elif isinstance(item, dict):
            count = item.get("count", 1)
            if not isinstance(count, int) or isinstance(count, bool) or count < 1:
                return None
            total += count
        else:
            return None
    return total


def validate(task_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not task_dir.is_dir():
        return [f"task directory does not exist: {task_dir}"], warnings
    if MODEL_IMPORT_ERROR is not None:
        return [
            (
                "harbor-antrieb is required for validation; run this script with "
                "`uv run --with-editable $HOME/harbor-antrieb` or "
                "`uv run --with 'harbor-antrieb @ git+https://github.com/"
                "open-sudo/harbor-antrieb.git'` "
                f"({MODEL_IMPORT_ERROR})"
            )
        ], warnings

    for relative in CORE_REQUIRED_FILES:
        if not (task_dir / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for relative in LEGACY_VERIFIER_FILES:
        if (task_dir / relative).is_file():
            warnings.append(
                f"{relative} is a retired task-local verifier artifact and is "
                "ignored by the evidence-based runtime"
            )

    instruction_path = task_dir / "instruction.md"
    if instruction_path.is_file():
        instruction = instruction_path.read_text()
        if not instruction.strip():
            errors.append("instruction.md is empty")
        public_ips = literal_ips(instruction)
        if public_ips:
            errors.append(
                "instruction.md must use node selectors instead of literal IP "
                f"addresses: {public_ips}"
            )
        matches = sorted(
            {match.group(0) for match in HARNESS_TERMS.finditer(instruction)}
        )
        if matches:
            errors.append(
                "instruction.md contains harness/prohibitive language: "
                + ", ".join(matches)
            )

    task_config = load_toml(task_dir / "task.toml", errors)
    if task_config:
        validate_runtime_model(TaskConfig, task_config, "task.toml", errors)
    if task_config and not task_config.get("schema_version"):
        errors.append("task.toml is missing schema_version")

    environment_config = load_toml(
        task_dir / "environment" / "harbor_antrieb.toml", errors
    )
    if environment_config:
        validate_runtime_model(
            AntriebDefinition,
            environment_config,
            "environment/harbor_antrieb.toml",
            errors,
        )
    count = cluster_node_count(environment_config.get("cluster"))
    if environment_config and count is None:
        errors.append("environment cluster must be a non-empty supported list")
    max_clusters = environment_config.get("max_clusters", 1)
    if (
        not isinstance(max_clusters, int)
        or isinstance(max_clusters, bool)
        or max_clusters < 1
    ):
        errors.append("environment max_clusters must be a positive integer")

    base_runbooks = environment_config.get("base_runbooks", ["antrieb/primer"])
    if not isinstance(base_runbooks, list) or not all(
        isinstance(name, str) for name in base_runbooks
    ):
        errors.append("environment base_runbooks must be a list of strings")
    else:
        if "antrieb/primer" not in base_runbooks:
            errors.append("environment base_runbooks must include antrieb/primer")
        if len(base_runbooks) != len(set(base_runbooks)):
            errors.append("environment base_runbooks must not contain duplicates")
        invalid_runbooks = [
            name for name in base_runbooks if BASE_RUNBOOK.fullmatch(name) is None
        ]
        if invalid_runbooks:
            errors.append(
                "environment base_runbooks may contain only Antrieb primers and "
                f"image references: {invalid_runbooks}"
            )

    control_node = environment_config.get("control_node")
    if count is not None and control_node not in {
        f"node{index}" for index in range(1, count + 1)
    }:
        errors.append(f"control_node {control_node!r} is outside the declared cluster")

    prepare = environment_config.get("prepare", {})
    if isinstance(prepare, dict) and prepare.get("enabled"):
        mode = prepare.get("mode", "static")
        baseline = task_dir / str(prepare.get("baseline", "prepare/baseline.toml"))
        if not baseline.is_file():
            errors.append(f"enabled preparation is missing baseline: {baseline}")
        if mode == "static":
            setup = task_dir / str(prepare.get("setup", "prepare/setup.toml"))
            if not setup.is_file():
                errors.append(f"static preparation is missing setup: {setup}")
            else:
                setup_config = load_toml(setup, errors)
                if setup_config:
                    validate_runtime_model(
                        StaticSetupConfig,
                        setup_config,
                        str(setup.relative_to(task_dir)),
                        errors,
                    )
        elif mode == "ai":
            prompt = task_dir / str(prepare.get("prompt", "prepare/prompt.md"))
            if not prompt.is_file():
                errors.append(f"AI preparation is missing prompt: {prompt}")
            for key in ("agent", "model"):
                if prepare.get(key):
                    warnings.append(
                        f"environment prepare.{key} is hardcoded; prefer a run-time kwarg"
                    )
        else:
            errors.append(f"unsupported preparation mode: {mode!r}")
        if baseline.is_file():
            baseline_config = load_toml(baseline, errors)
            if baseline_config:
                validate_runtime_model(
                    StaticBaselineConfig,
                    baseline_config,
                    str(baseline.relative_to(task_dir)),
                    errors,
                )

    sentinel = task_dir / "tests" / "test.sh"
    if sentinel.is_file() and not sentinel.stat().st_mode & stat.S_IXUSR:
        warnings.append("tests/test.sh is not executable")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task_dir", type=Path)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="retained for CLI compatibility; authoring-policy errors are strict",
    )
    parser.add_argument(
        "--task-only",
        action="store_true",
        help="retained for CLI compatibility; all validation is task-only",
    )
    args = parser.parse_args()
    errors, warnings = validate(args.task_dir.resolve())
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"OK: {args.task_dir} ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
