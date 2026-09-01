#!/usr/bin/env bash

set -euo pipefail
export ANTRIEB_TOKEN=ant_pCcC_8WFtcCT3FW28rAFe2A65Qw6d0AK2m4lETF9i4c
export HARBOR_ANTRIEB_INITIALIZE_CREDENTIALS_FILE=~/rehl-credentials.txt

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
provider_requirement="${INFRASET_PROVIDER_REQUIREMENT:-harbor-antrieb @ git+https://github.com/open-sudo/harbor-antrieb.git}"
harbor_requirement="${HARBOR_REQUIREMENT:-harbor @ git+https://github.com/open-sudo/harbor.git}"
model="${INFRASET_MODEL:-gpt-5.6-sol}"
reasoning_effort="${INFRASET_REASONING_EFFORT:-max}"
service_tier="${INFRASET_SERVICE_TIER:-fast}"
agent_name="${INFRASET_AGENT_NAME:-codex}"
jobs_root="${INFRASET_JOBS_DIR:-$script_dir/jobs}"
n_attempts="${INFRASET_N_ATTEMPTS:-1}"
task_parallel="${INFRASET_TASK_PARALLEL:-1}"
parallel_limit="${INFRASET_PARALLEL:-1}"

usage() {
  printf '%s\n' \
    "Usage: $0 [OPTIONS] TASK_OR_FOLDER" \
    "" \
    "Run one InfraSet task, or every task found recursively below a folder." \
    "" \
    "Options:" \
    "  -j, --parallel N       Total concurrent trial budget (default: $parallel_limit)" \
    "  -k, --n-attempts N     Trials to run for each task (default: $n_attempts)" \
    "  -n, --task-parallel N  Concurrent trials within one task (default: $task_parallel)" \
    "  -h, --help             Show this help" \
    "" \
    "A running task consumes min(n-attempts, task-parallel) slots. The outer" \
    "scheduler starts only as many tasks as fit within --parallel." \
    "" \
    "Environment equivalents: INFRASET_PARALLEL, INFRASET_N_ATTEMPTS," \
    "INFRASET_TASK_PARALLEL." >&2
}

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

input_arg=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --help|-h)
      usage
      exit 0
      ;;
    --parallel|-j)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      parallel_limit="$2"
      shift 2
      ;;
    --parallel=*)
      parallel_limit="${1#*=}"
      shift
      ;;
    --n-attempts|-k)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      n_attempts="$2"
      shift 2
      ;;
    --n-attempts=*)
      n_attempts="${1#*=}"
      shift
      ;;
    --task-parallel|--n-concurrent|-n)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      task_parallel="$2"
      shift 2
      ;;
    --task-parallel=*|--n-concurrent=*)
      task_parallel="${1#*=}"
      shift
      ;;
    --)
      shift
      if [[ $# -ne 1 || -n "$input_arg" ]]; then
        usage
        exit 2
      fi
      input_arg="$1"
      shift
      ;;
    -*)
      printf 'Unknown option: %s\n' "$1" >&2
      usage
      exit 2
      ;;
    *)
      if [[ -n "$input_arg" ]]; then
        usage
        exit 2
      fi
      input_arg="$1"
      shift
      ;;
  esac
done

if [[ -z "$input_arg" ]]; then
  usage
  exit 2
fi

for value_name in parallel_limit n_attempts task_parallel; do
  value="${!value_name}"
  if [[ ! "$value" =~ ^[1-9][0-9]*$ ]]; then
    printf '%s must be a positive integer: %s\n' "$value_name" "$value" >&2
    exit 2
  fi
done

if [[ ! -e "$input_arg" ]]; then
  printf 'Task or folder does not exist: %s\n' "$input_arg" >&2
  exit 2
fi

input_path="$(realpath "$input_arg")"
declare -a task_paths=()
if [[ -f "$input_path/task.toml" ]]; then
  task_paths+=("$input_path")
elif [[ -d "$input_path" ]]; then
  while IFS= read -r -d '' task_file; do
    task_paths+=("$(dirname "$task_file")")
  done < <(find "$input_path" -type f -name task.toml -print0 | sort -z)
fi

if [[ ${#task_paths[@]} -eq 0 ]]; then
  printf 'No InfraSet tasks containing task.toml were found under: %s\n' "$input_path" >&2
  exit 2
fi

declare -A task_names_seen=()
declare -A environment_files=()
for task_path in "${task_paths[@]}"; do
  task_name="$(basename "$task_path")"
  if [[ -n "${task_names_seen[$task_name]+present}" ]]; then
    printf 'Duplicate task name %s found in %s and %s\n' \
      "$task_name" "${task_names_seen[$task_name]}" "$task_path" >&2
    exit 2
  fi
  task_names_seen["$task_name"]="$task_path"

  if [[ ! -f "$task_path/instruction.md" ]]; then
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
  environment_files["$task_path"]="$environment_file"
done

validator="$script_dir/skills/infraset-task-builder/scripts/validate_example.py"
if [[ ! -f "$validator" ]]; then
  printf 'InfraSet task validator does not exist: %s\n' "$validator" >&2
  exit 2
fi
if [[ -n "${INFRASET_PROVIDER_DIR:-}" ]]; then
  if [[ ! -f "$INFRASET_PROVIDER_DIR/pyproject.toml" ]]; then
    printf 'Harbor Antrieb provider does not exist: %s\n' "$INFRASET_PROVIDER_DIR" >&2
    exit 2
  fi
  validator_runner=(uv run --isolated --no-project --with-editable "$INFRASET_PROVIDER_DIR")
else
  validator_runner=(uv run --isolated --no-project --with "$provider_requirement")
fi

job_name="${INFRASET_JOB_NAME:-$(date '+%Y-%m-%d__%H-%M-%S')}"

"${validator_runner[@]}" bash -c '
validator="$1"
shift
for task_path in "$@"; do
  python "$validator" --task-only "$task_path" || exit
done
' _ "$validator" "${task_paths[@]}"

if [[ -n "${HARBOR_DIR:-}" ]]; then
  if [[ ! -d "$HARBOR_DIR" ]]; then
    printf 'Harbor checkout does not exist: %s\n' "$HARBOR_DIR" >&2
    exit 2
  fi
  if [[ -n "${INFRASET_PROVIDER_DIR:-}" ]]; then
    runner=(uv run --isolated --directory "$HARBOR_DIR" --with-editable "$HARBOR_DIR" --with-editable "$INFRASET_PROVIDER_DIR" harbor run)
  else
    runner=(uv run --isolated --refresh-package harbor-antrieb --directory "$HARBOR_DIR" --with-editable "$HARBOR_DIR" --with "$provider_requirement" harbor run)
  fi
elif [[ -n "${INFRASET_PROVIDER_DIR:-}" ]]; then
  runner=(uv run --isolated --no-project --refresh-package harbor --with "$harbor_requirement" --with-editable "$INFRASET_PROVIDER_DIR" harbor run)
else
  runner=(uv run --isolated --no-project --refresh-package harbor --refresh-package harbor-antrieb --with "$harbor_requirement" --with "$provider_requirement" harbor run)
fi

effective_task_parallel="$task_parallel"
if (( effective_task_parallel > n_attempts )); then
  effective_task_parallel="$n_attempts"
fi
if (( effective_task_parallel > parallel_limit )); then
  effective_task_parallel="$parallel_limit"
fi

task_slots="$effective_task_parallel"
max_active_tasks=$((parallel_limit / task_slots))

printf 'Tasks: %s; attempts per task: %s; per-task concurrency: %s; total concurrency budget: %s\n' \
  "${#task_paths[@]}" "$n_attempts" "$effective_task_parallel" "$parallel_limit"

for task_path in "${task_paths[@]}"; do
  task_name="$(basename "$task_path")"
  job_dir="$jobs_root/$task_name/$job_name"
  mkdir -p "$job_dir"
  cp "$task_path/instruction.md" "$job_dir/instruction.md"
  cp "${environment_files[$task_path]}" "$job_dir/environment.toml"
done

run_one_task() {
  local task_path="$1"
  local task_name
  local jobs_dir
  task_name="$(basename "$task_path")"
  jobs_dir="$jobs_root/$task_name"

  printf '[%s] Starting (%s attempt(s), %s concurrent)\n' \
    "$task_name" "$n_attempts" "$effective_task_parallel"

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
    --verifier-kwarg minimum_coverage=1.0 \
    --n-attempts "$n_attempts" \
    --n-concurrent "$effective_task_parallel"
}

declare -a active_pids=()
declare -a failed_tasks=()
declare -A task_by_pid=()
completed_tasks=0

remove_active_pid() {
  local completed_pid="$1"
  local pid
  local -a remaining=()
  for pid in "${active_pids[@]}"; do
    if [[ "$pid" != "$completed_pid" ]]; then
      remaining+=("$pid")
    fi
  done
  active_pids=("${remaining[@]}")
}

wait_for_one_task() {
  local completed_pid=""
  local task_path
  local task_name
  local status

  if wait -n -p completed_pid "${active_pids[@]}"; then
    status=0
  else
    status=$?
  fi

  task_path="${task_by_pid[$completed_pid]}"
  task_name="$(basename "$task_path")"
  unset 'task_by_pid[$completed_pid]'
  remove_active_pid "$completed_pid"
  completed_tasks=$((completed_tasks + 1))

  if (( status == 0 )); then
    printf '[%s] Completed successfully\n' "$task_name"
  else
    printf '[%s] Failed with exit code %s\n' "$task_name" "$status" >&2
    failed_tasks+=("$task_name")
  fi
}

terminate_active_tasks() {
  local pid
  trap - INT TERM
  for pid in "${active_pids[@]}"; do
    kill "$pid" 2>/dev/null || true
  done
  for pid in "${active_pids[@]}"; do
    wait "$pid" 2>/dev/null || true
  done
  exit 130
}
trap terminate_active_tasks INT TERM

for task_path in "${task_paths[@]}"; do
  while (( ${#active_pids[@]} >= max_active_tasks )); do
    wait_for_one_task
  done

  (run_one_task "$task_path") &
  pid=$!
  active_pids+=("$pid")
  task_by_pid["$pid"]="$task_path"
done

while (( ${#active_pids[@]} > 0 )); do
  wait_for_one_task
done

trap - INT TERM
if (( ${#failed_tasks[@]} > 0 )); then
  printf 'Completed %s task(s); %s failed: %s\n' \
    "$completed_tasks" "${#failed_tasks[@]}" "${failed_tasks[*]}" >&2
  exit 1
fi

printf 'Completed %s task(s) successfully.\n' "$completed_tasks"
