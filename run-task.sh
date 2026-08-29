#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
provider_requirement="${INFRASET_PROVIDER_REQUIREMENT:-harbor-antrieb @ git+https://github.com/open-sudo/harbor-antrieb.git}"
harbor_requirement="${HARBOR_REQUIREMENT:-harbor @ git+https://github.com/open-sudo/harbor.git}"
model="${INFRASET_MODEL:-gpt-5.6-sol}"
reasoning_effort="${INFRASET_REASONING_EFFORT:-max}"
service_tier="${INFRASET_SERVICE_TIER:-fast}"
agent_name="${INFRASET_AGENT_NAME:-codex}"
verification_level="${INFRASET_VERIFICATION_LEVEL:-5}"
jobs_root="${INFRASET_JOBS_DIR:-$script_dir/jobs}"

# Development checkouts are authoritative when Harbor, the provider, and this
# runner are cloned next to one another. This keeps local task runs on the same
# coordinated revisions instead of silently mixing GitHub and PyPI releases.
workspace_dir="$(dirname "$script_dir")"
if [[ -z "${HARBOR_DIR:-}" \
  && -z "${INFRASET_PROVIDER_DIR:-}" \
  && -f "$workspace_dir/harbor/pyproject.toml" \
  && -f "$workspace_dir/harbor-antrieb/pyproject.toml" ]]; then
  HARBOR_DIR="$workspace_dir/harbor"
  INFRASET_PROVIDER_DIR="$workspace_dir/harbor-antrieb"
fi

if [[ $# -ne 1 ]]; then
  printf 'Usage: %s /path/to/harbor_antrieb/task\n' "$0" >&2
  exit 2
fi

task_path="$(realpath "$1")"
if [[ ! -f "$task_path/task.toml" ]]; then
  printf 'InfraSet task does not contain task.toml: %s\n' "$task_path" >&2
  exit 2
fi

task_name="$(basename "$task_path")"
job_name="${INFRASET_JOB_NAME:-$(date '+%Y-%m-%d__%H-%M-%S')}"
jobs_dir="$jobs_root/$task_name"
job_dir="$jobs_dir/$job_name"
mkdir -p "$job_dir"

if [[ -f "$task_path/instruction.md" ]]; then
  cp "$task_path/instruction.md" "$job_dir/instruction.md"
else
  printf 'InfraSet task does not contain instruction.md: %s\n' "$task_path" >&2
  exit 2
fi

environment_file=""
for candidate in \
  "$task_path/environment/harbor_antrieb.toml" \
  "$task_path/environment/infraset.toml"; do
  if [[ -f "$candidate" ]]; then
    environment_file="$candidate"
    break
  fi
done

if [[ -z "$environment_file" ]]; then
  printf 'InfraSet task does not contain an environment definition: %s\n' "$task_path" >&2
  exit 2
fi
cp "$environment_file" "$job_dir/environment.toml"

if [[ -n "${HARBOR_DIR:-}" ]]; then
  if [[ ! -d "$HARBOR_DIR" ]]; then
    printf 'Harbor checkout does not exist: %s\n' "$HARBOR_DIR" >&2
    exit 2
  fi
  if [[ -n "${INFRASET_PROVIDER_DIR:-}" ]]; then
    if [[ ! -f "$INFRASET_PROVIDER_DIR/pyproject.toml" ]]; then
      printf 'Harbor Antrieb provider does not exist: %s\n' "$INFRASET_PROVIDER_DIR" >&2
      exit 2
    fi
    runner=(uv run --directory "$HARBOR_DIR" --with "$HARBOR_DIR" --with "$INFRASET_PROVIDER_DIR" harbor run)
  else
    runner=(uv run --directory "$HARBOR_DIR" --with "$HARBOR_DIR" --with "$provider_requirement" harbor run)
  fi
elif [[ -n "${INFRASET_PROVIDER_DIR:-}" ]]; then
  if [[ ! -f "$INFRASET_PROVIDER_DIR/pyproject.toml" ]]; then
    printf 'Harbor Antrieb provider does not exist: %s\n' "$INFRASET_PROVIDER_DIR" >&2
    exit 2
  fi
  runner=(uv run --no-project --with "$harbor_requirement" --with "$INFRASET_PROVIDER_DIR" harbor run)
else
  runner=(uv run --no-project --with "$harbor_requirement" --with "$provider_requirement" harbor run)
fi

exec "${runner[@]}" \
  --yes \
  --path "$task_path" \
  --jobs-dir "$jobs_dir" \
  --job-name "$job_name" \
  --agent harbor_antrieb.agent:AntriebHostAgent \
  --model "$model" \
  --agent-kwarg agent_name="$agent_name" \
  --agent-kwarg reasoning_effort="$reasoning_effort" \
  --agent-kwarg service_tier="$service_tier" \
  --agent-kwarg diagnostic_agent=codex \
  --agent-kwarg diagnostic_model="$model" \
  --agent-kwarg diagnostic_reasoning_effort="$reasoning_effort" \
  --env harbor_antrieb.environment:AntriebEnvironment \
  --verifier harbor_antrieb.verifier:AntriebVerifier \
  --verifier-kwarg agent="$agent_name" \
  --verifier-kwarg model="$model" \
  --verifier-kwarg reasoning_effort="$reasoning_effort" \
  --verifier-kwarg service_tier="$service_tier" \
  --verifier-kwarg level="$verification_level" \
  --verifier-kwarg minimum_coverage=1.0 \
  --n-attempts 3 \
  --n-concurrent 1
