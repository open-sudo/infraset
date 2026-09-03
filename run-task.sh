#!/usr/bin/env bash

set -euo pipefail

credentials_file="${CREDENTIALS_FILE:-$HOME/credentials.env}"
if [[ ! -f "$credentials_file" || ! -r "$credentials_file" ]]; then
  printf 'Credentials file is not a readable regular file: %s\n' "$credentials_file" >&2
  exit 2
fi
credentials_file="$(realpath "$credentials_file")"

credentials_mode="$(stat -c '%a' "$credentials_file")"
if (( (8#$credentials_mode & 8#077) != 0 )); then
  printf 'Credentials file must not be group/world accessible: %s\n' "$credentials_file" >&2
  exit 2
fi

credential_value() {
  local requested_key="$1"
  local path="$2"
  local line key first last
  local value=""
  local found=0
  while IFS= read -r line || [[ -n "$line" ]]; do
    line="${line%$'\r'}"
    line="${line#"${line%%[![:space:]]*}"}"
    line="${line%"${line##*[![:space:]]}"}"
    if [[ -z "$line" || "$line" == \#* ]]; then
      continue
    fi
    if [[ ! "$line" =~ ^(export[[:space:]]+)?([A-Za-z_][A-Za-z0-9_]*)[[:space:]]*=(.*)$ ]]; then
      printf 'Malformed credential assignment in %s\n' "$path" >&2
      return 1
    fi
    key="${BASH_REMATCH[2]}"
    if [[ "$key" != "$requested_key" ]]; then
      continue
    fi
    value="${BASH_REMATCH[3]}"
    if (( found )); then
      printf 'Duplicate credential key %s in %s\n' "$requested_key" "$path" >&2
      return 1
    fi
    value="${value#"${value%%[![:space:]]*}"}"
    value="${value%"${value##*[![:space:]]}"}"
    if (( ${#value} >= 2 )); then
      first="${value:0:1}"
      last="${value: -1}"
      if [[ ( "$first" == "'" && "$last" == "'" ) \
        || ( "$first" == '"' && "$last" == '"' ) ]]; then
        value="${value:1:${#value}-2}"
      fi
    fi
    found=1
  done < "$path"
  if (( ! found )) || [[ -z "$value" ]]; then
    printf 'Credentials file does not define a nonempty %s: %s\n' \
      "$requested_key" "$path" >&2
    return 1
  fi
  printf '%s' "$value"
}

ANTRIEB_TOKEN="$(credential_value ANTRIEB_TOKEN "$credentials_file")"
export ANTRIEB_TOKEN
export CREDENTIALS_FILE="$credentials_file"

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
provider_requirement="${INFRASET_PROVIDER_REQUIREMENT:-harbor-antrieb @ git+https://github.com/open-sudo/harbor-antrieb.git}"
harbor_requirement="${HARBOR_REQUIREMENT:-harbor @ git+https://github.com/open-sudo/harbor.git}"
model="${INFRASET_MODEL:-claude-sonnet-5}"
reasoning_effort="${INFRASET_REASONING_EFFORT:-medium}"
service_tier="${INFRASET_SERVICE_TIER:-fast}"
agent_name="${INFRASET_AGENT_NAME:-claude-code}"
jobs_root="${INFRASET_JOBS_DIR:-$script_dir/jobs}"
n_attempts="${INFRASET_N_ATTEMPTS:-1}"
parallel_limit="${INFRASET_PARALLEL:-1}"

usage() {
  printf '%s\n' \
    "Usage: $0 [OPTIONS] TASK_OR_FOLDER" \
    "" \
    "Run one InfraSet task, or every task found recursively below a folder." \
    "" \
    "Options:" \
    "  -j, --parallel N       Tasks to run concurrently (default: $parallel_limit)" \
    "  -k, --n-attempts N     Sequential trials for each task (default: $n_attempts)" \
    "  -h, --help             Show this help" \
    "" \
    "Trials for the same task never overlap. Up to --parallel different tasks" \
    "may run at the same time." \
    "" \
    "Environment equivalents: INFRASET_PARALLEL and INFRASET_N_ATTEMPTS." \
    "Set CREDENTIALS_FILE to override the default credentials file at" \
    "\$HOME/credentials.env." >&2
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

for value_name in parallel_limit n_attempts; do
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

max_active_tasks="$parallel_limit"

task_jobs_dir() {
  local task_path="$1"
  local tasks_root="$script_dir/tasks"
  if [[ "$task_path" == "$tasks_root/"* ]]; then
    printf '%s/%s' "$jobs_root" "${task_path#$tasks_root/}"
  else
    printf '%s/%s' "$jobs_root" "$(basename "$task_path")"
  fi
}

printf 'Tasks: %s; sequential trials per task: %s; concurrent tasks: %s\n' \
  "${#task_paths[@]}" "$n_attempts" "$parallel_limit"

for task_path in "${task_paths[@]}"; do
  job_dir="$(task_jobs_dir "$task_path")/$job_name"
  mkdir -p "$job_dir"
  cp "$task_path/instruction.md" "$job_dir/instruction.md"
  cp "${environment_files[$task_path]}" "$job_dir/environment.toml"
done

run_one_task() {
  local task_path="$1"
  local task_name
  local jobs_dir
  task_name="$(basename "$task_path")"
  jobs_dir="$(task_jobs_dir "$task_path")"

  printf '[%s] Starting (%s sequential trial(s))\n' \
    "$task_name" "$n_attempts"

  local -a agent_kwargs=(
    --agent-kwarg agent_name="$agent_name"
    --agent-kwarg reasoning_effort="$reasoning_effort"
    --agent-kwarg diagnostic_agent="$agent_name"
    --agent-kwarg diagnostic_model="$model"
    --agent-kwarg diagnostic_reasoning_effort="$reasoning_effort"
  )
  local -a verifier_kwargs=(
    --verifier-kwarg agent="$agent_name"
    --verifier-kwarg model="$model"
    --verifier-kwarg reasoning_effort="$reasoning_effort"
    --verifier-kwarg minimum_coverage=1.0
  )
  if [[ "$agent_name" == "codex" && -n "$service_tier" ]]; then
    agent_kwargs+=(--agent-kwarg service_tier="$service_tier")
    verifier_kwargs+=(--verifier-kwarg service_tier="$service_tier")
  fi

  exec "${runner[@]}" \
    --yes \
    --path "$task_path" \
    --jobs-dir "$jobs_dir" \
    --job-name "$job_name" \
    --agent harbor_antrieb.agent:AntriebHostAgent \
    --model "$model" \
    "${agent_kwargs[@]}" \
    --env harbor_antrieb.environment:AntriebEnvironment \
    --verifier harbor_antrieb.verifier:AntriebVerifier \
    "${verifier_kwargs[@]}" \
    --n-attempts "$n_attempts" \
    --n-concurrent 1
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
