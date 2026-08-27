#!/usr/bin/env python3
"""Validate one generated InfraSet example without contacting Antrieb."""

from __future__ import annotations

import argparse
import re
import stat
import sys
import tomllib
from pathlib import Path
from typing import Any


REQUIRED_FILES = (
    "instruction.md",
    "task.toml",
    "environment/harbor_antrieb.toml",
    "verifier/judge.toml",
    "verifier/checks.toml",
    "tests/test.sh",
)
HARNESS_TERMS = re.compile(
    r"\b(?:harbor|antrieb|mcp|cluster lifecycle|do not|don't|must not|never)\b",
    re.IGNORECASE,
)
BASE_RUNBOOK = re.compile(r"antrieb/(?:primer|[a-z0-9-]+-(?:primer|reference))")


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
            if not isinstance(count, int) or count < 1:
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

    for relative in REQUIRED_FILES:
        if not (task_dir / relative).is_file():
            errors.append(f"missing required file: {relative}")

    instruction_path = task_dir / "instruction.md"
    if instruction_path.is_file():
        instruction = instruction_path.read_text()
        if not instruction.strip():
            errors.append("instruction.md is empty")
        if not re.search(r"\breboot(?:ed|s|ing)?\b", instruction, re.IGNORECASE):
            errors.append("instruction.md must state reboot persistence explicitly")
        matches = sorted(
            {match.group(0) for match in HARNESS_TERMS.finditer(instruction)}
        )
        if matches:
            errors.append(
                "instruction.md contains harness/prohibitive language: "
                + ", ".join(matches)
            )

    task_config = load_toml(task_dir / "task.toml", errors)
    if task_config and not task_config.get("schema_version"):
        errors.append("task.toml is missing schema_version")
    environment_config = load_toml(
        task_dir / "environment" / "harbor_antrieb.toml", errors
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

    judge_path = task_dir / "verifier" / "judge.toml"
    judge = load_toml(judge_path, errors)
    dimensions = judge.get("dimensions", {})
    if not isinstance(dimensions, dict) or not dimensions:
        errors.append("verifier/judge.toml needs dimensions")
        dimensions = {}
    weights = [
        config.get("weight")
        for config in dimensions.values()
        if isinstance(config, dict)
    ]
    if len(weights) != len(dimensions) or any(
        not isinstance(weight, (int, float)) or weight <= 0 for weight in weights
    ):
        errors.append("every dimension needs a positive numeric weight")
    elif not 0.999 <= sum(weights) <= 1.001:
        errors.append(f"dimension weights must total 1.0, got {sum(weights)}")
    valid_nodes = (
        {f"node{index}" for index in range(1, count + 1)}
        if count is not None
        else set()
    )
    for key in ("agent", "model"):
        if judge.get(key):
            warnings.append(
                f"verifier/judge.toml hardcodes {key}; prefer a verifier kwarg"
            )

    semantic_path = task_dir / "verifier" / "checks.toml"
    if semantic_path.is_file():
        semantic = load_toml(semantic_path, errors)
        if semantic.get("schema_version") != 1:
            errors.append("verifier/checks.toml schema_version must be 1")
        semantic_probes = semantic.get("probes", [])
        if not isinstance(semantic_probes, list) or not semantic_probes:
            errors.append(
                "verifier/checks.toml needs at least one [[probes]] entry"
            )
            semantic_probes = []
        probe_ids: set[str] = set()
        probe_levels: dict[str, int] = {}
        for index, probe in enumerate(semantic_probes, start=1):
            label = f"semantic probes[{index}]"
            if not isinstance(probe, dict):
                errors.append(f"{label} must be a table")
                continue
            probe_id = probe.get("id")
            if (
                not isinstance(probe_id, str)
                or re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", probe_id) is None
            ):
                errors.append(f"{label} needs a safe unique id")
            elif probe_id in probe_ids:
                errors.append(f"duplicate semantic probe id: {probe_id}")
            else:
                probe_ids.add(probe_id)
            level = probe.get("level", 1)
            if (
                not isinstance(level, int)
                or isinstance(level, bool)
                or not 1 <= level <= 10
            ):
                errors.append(f"{label} level must be an integer from 1 to 10")
            elif isinstance(probe_id, str):
                probe_levels[probe_id] = level
            targets = probe.get("targets")
            if (
                not isinstance(targets, list)
                or not targets
                or not all(isinstance(node, str) for node in targets)
            ):
                errors.append(f"{label} needs a non-empty targets list")
            elif len(targets) != len(set(targets)):
                errors.append(f"{label} targets must not contain duplicates")
            elif valid_nodes and not set(targets) <= valid_nodes:
                errors.append(f"{label} references unknown nodes: {targets}")
            effect = probe.get("effect", "read_only")
            if effect not in {
                "read_only",
                "evaluator_owned_data",
                "controlled_failure",
                "reboot",
            }:
                errors.append(f"{label} has unsupported effect: {effect!r}")
            elif (
                effect == "controlled_failure" and isinstance(level, int) and level < 6
            ):
                errors.append(f"{label} controlled failure must be level 6 or higher")
            elif effect == "reboot" and isinstance(level, int) and level < 8:
                errors.append(f"{label} reboot must be level 8 or higher")
            if effect != "read_only" and not probe.get("cleanup"):
                errors.append(f"{label} mutating probe must define cleanup")
            max_exec_calls = probe.get("max_exec_calls", 3)
            if (
                not isinstance(max_exec_calls, int)
                or isinstance(max_exec_calls, bool)
                or not 1 <= max_exec_calls <= 16
            ):
                errors.append(f"{label} max_exec_calls must be from 1 to 16")
            for field in ("procedure",):
                if not isinstance(probe.get(field), str) or not probe[field].strip():
                    errors.append(f"{label} needs {field}")
        if semantic_probes and not any(
            isinstance(probe, dict) and probe.get("level", 1) == 1
            for probe in semantic_probes
        ):
            errors.append("semantic verification needs at least one level-1 probe")

        semantic_assertions = semantic.get("assertions", [])
        if not isinstance(semantic_assertions, list) or not semantic_assertions:
            errors.append(
                "verifier/checks.toml needs at least one [[assertions]] entry"
            )
            semantic_assertions = []
        assertion_ids: set[str] = set()
        assertion_probes: dict[str, str] = {}
        assertion_requirements: dict[str, list[str]] = {}
        used_probes: set[str] = set()
        for index, assertion in enumerate(semantic_assertions, start=1):
            label = f"semantic assertions[{index}]"
            if not isinstance(assertion, dict):
                errors.append(f"{label} must be a table")
                continue
            assertion_id = assertion.get("id")
            if (
                not isinstance(assertion_id, str)
                or re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", assertion_id) is None
            ):
                errors.append(f"{label} needs a safe unique id")
            elif assertion_id in assertion_ids:
                errors.append(f"duplicate semantic assertion id: {assertion_id}")
            else:
                assertion_ids.add(assertion_id)
            probe_id = assertion.get("probe")
            if not isinstance(probe_id, str) or probe_id not in probe_ids:
                errors.append(f"{label} references an unknown probe")
            else:
                used_probes.add(probe_id)
                if isinstance(assertion_id, str):
                    assertion_probes[assertion_id] = probe_id
            if assertion.get("dimension") not in dimensions:
                errors.append(f"{label} references an unknown dimension")
            points = assertion.get("points", 1)
            if (
                not isinstance(points, (int, float))
                or isinstance(points, bool)
                or points <= 0
            ):
                errors.append(f"{label} points must be positive")
            if not isinstance(assertion.get("critical", False), bool):
                errors.append(f"{label} critical must be a boolean")
            requires = assertion.get("requires", [])
            if not isinstance(requires, list) or not all(
                isinstance(required, str) for required in requires
            ):
                errors.append(f"{label} requires must be a list of assertion ids")
                requires = []
            elif len(requires) != len(set(requires)):
                errors.append(f"{label} prerequisites must not contain duplicates")
            if isinstance(assertion_id, str):
                assertion_requirements[assertion_id] = requires
                if assertion_id in requires:
                    errors.append(f"{label} cannot require itself")
            for field in ("pass_condition", "fail_condition"):
                if (
                    not isinstance(assertion.get(field), str)
                    or not assertion[field].strip()
                ):
                    errors.append(f"{label} needs {field}")

        unused_probes = sorted(probe_ids - used_probes)
        if unused_probes:
            errors.append(f"semantic probes have no assertions: {unused_probes}")
        for assertion_id, requires in assertion_requirements.items():
            unknown = sorted(set(requires) - assertion_ids)
            if unknown:
                errors.append(
                    f"semantic assertion {assertion_id!r} references unknown "
                    f"prerequisites: {unknown}"
                )
            assertion_probe = assertion_probes.get(assertion_id)
            assertion_level = probe_levels.get(assertion_probe or "")
            later = sorted(
                required
                for required in requires
                if assertion_level is not None
                and (required_probe := assertion_probes.get(required)) is not None
                and probe_levels.get(required_probe, assertion_level) > assertion_level
            )
            if later:
                errors.append(
                    f"semantic assertion {assertion_id!r} requires deeper "
                    f"assertions: {later}"
                )

        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(assertion_id: str) -> None:
            if assertion_id in visited:
                return
            if assertion_id in visiting:
                errors.append("semantic assertion prerequisites contain a cycle")
                return
            visiting.add(assertion_id)
            for required in assertion_requirements.get(assertion_id, []):
                if required in assertion_requirements:
                    visit(required)
            visiting.remove(assertion_id)
            visited.add(assertion_id)

        for assertion_id in assertion_requirements:
            visit(assertion_id)

    sentinel = task_dir / "tests" / "test.sh"
    if sentinel.is_file() and not sentinel.stat().st_mode & stat.S_IXUSR:
        warnings.append("tests/test.sh is not executable")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task_dir", type=Path)
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
