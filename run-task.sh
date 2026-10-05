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
evaluator_model="${INFRASET_EVALUATOR_MODEL:-}"
evaluator_reasoning_effort="${INFRASET_EVALUATOR_REASONING_EFFORT:-}"
service_tier="${INFRASET_SERVICE_TIER:-fast}"
agent_name="${INFRASET_AGENT_NAME:-claude-code}"
jobs_root="${INFRASET_JOBS_DIR:-$script_dir/jobs}"
transport="${INFRASET_TRANSPORT:-trentina}"
execution_mode="${INFRASET_EXECUTION_MODE:-interactive}"
skip_existing=0
n_attempts="${INFRASET_N_ATTEMPTS:-1}"
parallel_limit="${INFRASET_PARALLEL:-1}"
# Fallback for a task that declares no [agent] timeout_sec of its own. A task
# that declares one wins: task.toml is what the runtime enforces and this
# kwarg is ignored for it. Observed directly -- a task asking for 1200 stopped
# at 1200 and one asking for 1800 stopped at 1800, both while this was set to
# 2100. To give a generated task more time, change its catalog entry and
# regenerate rather than setting this. Every generated task now asks for 2400,
# which matches the Antrieb cluster lease, so a task that runs its budget out
# leaves the verifier nothing to inspect; raise the lease before relying on
# the full window.
agent_timeout_sec="${INFRASET_AGENT_TIMEOUT_SEC:-2400}"

usage() {
  printf '%s\n' \
    "Usage: $0 [OPTIONS] TASK_OR_FOLDER [TASK_OR_FOLDER ...]" \
    "" \
    "Run one InfraSet task, or every task found recursively below a folder." \
    "Several tasks and folders may be given at once, so a shell glob that" \
    "expands to many task directories works directly:" \
    "" \
    "  $0 ./tasks/4523/*" \
    "" \
    "A path named more than once, whether directly or by way of a folder that" \
    "contains it, runs once." \
    "" \
    "Options:" \
    "  -j, --parallel N       Tasks to run concurrently (default: $parallel_limit)" \
    "  -k, --n-attempts N     Sequential trials for each task (default: $n_attempts)" \
    "      --agent-name NAME  Host agent backend (default: $agent_name)" \
    "      --model MODEL      Model passed to the selected host agent (default: $model)" \
    "      --reasoning-effort LEVEL  Agent reasoning effort (default: $reasoning_effort)" \
    "      --evaluator-model MODEL  Independent evaluator model (default: main model)" \
    "      --evaluator-reasoning-effort LEVEL  Independent evaluator reasoning effort (default: main level)" \
    "      --service-tier TIER  Codex service tier (default: $service_tier)" \
    "      --transport NAME   Execution transport: direct or trentina (default: $transport)." \
    "      --mode MODE        Executor mode: interactive or batch (default: $execution_mode)." \
    "      --skip-existing    Skip completed tasks with matching settings and task revision." \
    "  -m, --match GLOB       Keep only tasks whose directory name matches GLOB." \
    "                         Repeatable; a task matching any GLOB is kept." \
    "                         Quote it so the shell leaves it alone:" \
    "                           $0 -m '*-bash-*' ./tasks/4523" \
    "  -h, --help             Show this help" \
    "" \
    "Trials for the same task never overlap. Up to --parallel different tasks" \
    "may run at the same time." \
    "" \
    "Environment equivalents: INFRASET_PARALLEL, INFRASET_N_ATTEMPTS," \
    "and INFRASET_TRANSPORT. Results are written below" \
    "jobs/<id>/<timestamp>/<usecase>-<language>-<os>-<id>." \
    "Task layout: tasks/<id>/<usecase>-<language>-<os>-<id>." \
    "The scenario folder supplies the ID; every task in it must carry that ID." \
    "INFRASET_AGENT_TIMEOUT_SEC sets the executor timeout (default:" \
    "$agent_timeout_sec) only for a task that declares no [agent] timeout_sec." \
    "A task that declares one wins, so change the task, or its catalog entry," \
    "to give it more time. Keep either below the Antrieb cluster lease." \
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

declare -a input_args=()
declare -a match_globs=()
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
    --agent-name)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      agent_name="$2"
      shift 2
      ;;
    --agent-name=*)
      agent_name="${1#*=}"
      shift
      ;;
    --model)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      model="$2"
      shift 2
      ;;
    --model=*)
      model="${1#*=}"
      shift
      ;;
    --reasoning-effort)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      reasoning_effort="$2"
      shift 2
      ;;
    --reasoning-effort=*)
      reasoning_effort="${1#*=}"
      shift
      ;;
    --evaluator-model)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      evaluator_model="$2"
      shift 2
      ;;
    --evaluator-model=*)
      evaluator_model="${1#*=}"
      shift
      ;;
    --evaluator-reasoning-effort)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      evaluator_reasoning_effort="$2"
      shift 2
      ;;
    --evaluator-reasoning-effort=*)
      evaluator_reasoning_effort="${1#*=}"
      shift
      ;;
    --service-tier)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      service_tier="$2"
      shift 2
      ;;
    --service-tier=*)
      service_tier="${1#*=}"
      shift
      ;;
    --transport)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      transport="$2"
      shift 2
      ;;
    --transport=*)
      transport="${1#*=}"
      shift
      ;;
    --mode)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      execution_mode="$2"
      shift 2
      ;;
    --mode=*)
      execution_mode="${1#*=}"
      shift
      ;;
    --skip-existing)
      skip_existing=1
      shift
      ;;
    --match|-m)
      if [[ $# -lt 2 ]]; then
        printf 'Option %s requires a value.\n' "$1" >&2
        usage
        exit 2
      fi
      match_globs+=("$2")
      shift 2
      ;;
    --match=*)
      match_globs+=("${1#*=}")
      shift
      ;;
    --)
      shift
      while [[ $# -gt 0 ]]; do
        input_args+=("$1")
        shift
      done
      ;;
    -*)
      printf 'Unknown option: %s\n' "$1" >&2
      usage
      exit 2
      ;;
    *)
      input_args+=("$1")
      shift
      ;;
  esac
done

if [[ ${#input_args[@]} -eq 0 ]]; then
  usage
  exit 2
fi

if [[ -z "$evaluator_model" ]]; then
  evaluator_model="$model"
fi
if [[ -z "$evaluator_reasoning_effort" ]]; then
  evaluator_reasoning_effort="$reasoning_effort"
fi

for value_name in parallel_limit n_attempts agent_timeout_sec; do
  value="${!value_name}"
  if [[ ! "$value" =~ ^[1-9][0-9]*$ ]]; then
    printf '%s must be a positive integer: %s\n' "$value_name" "$value" >&2
    exit 2
  fi
done

if [[ "$transport" != "direct" && "$transport" != "trentina" ]]; then
  printf 'Unsupported transport %s; expected direct or trentina.\n' "$transport" >&2
  exit 2
fi

if [[ "$execution_mode" != "interactive" && "$execution_mode" != "batch" ]]; then
  printf 'Unsupported execution mode %s; expected interactive or batch.\n' \
    "$execution_mode" >&2
  exit 2
fi
export INFRASET_EXECUTION_MODE="$execution_mode"

if [[ "$transport" == "trentina" ]]; then
    # Route only executor commands through Trentina. Provisioning, preparation,
    # collection, and teardown continue to use the direct Antrieb connection.
    export ANTRIEB_EXECUTOR_MCP_URL="${ANTRIEB_EXECUTOR_MCP_URL:-http://localhost:8019/gateway/infraset/mcp}"
    export ANTRIEB_EXECUTOR_TOKEN="${ANTRIEB_EXECUTOR_TOKEN:-somesecretstring}"
    export ANTRIEB_EXECUTOR_TOOL_PREFIX="${ANTRIEB_EXECUTOR_TOOL_PREFIX:-antrieb__}"
else
  # Route executor commands directly to Antrieb.
  unset ANTRIEB_EXECUTOR_MCP_URL
  unset ANTRIEB_EXECUTOR_TOKEN
  unset ANTRIEB_EXECUTOR_TOOL_PREFIX
fi

declare -a task_paths=()
declare -A task_paths_seen=()

# A task reached through several arguments, or through both a folder and its
# own path, is collected once and keeps the position of its first mention.
collect_task_path() {
  local candidate="$1"
  if [[ -n "${task_paths_seen[$candidate]+present}" ]]; then
    return 0
  fi
  task_paths_seen["$candidate"]=1
  task_paths+=("$candidate")
}

for input_arg in "${input_args[@]}"; do
  if [[ ! -e "$input_arg" ]]; then
    printf 'Task or folder does not exist: %s\n' "$input_arg" >&2
    exit 2
  fi
  input_path="$(realpath "$input_arg")"
  if [[ -f "$input_path/task.toml" ]]; then
    collect_task_path "$input_path"
  elif [[ -d "$input_path" ]]; then
    while IFS= read -r -d '' task_file; do
      collect_task_path "$(dirname "$task_file")"
    done < <(find "$input_path" -type f -name task.toml -print0 | sort -z)
  else
    printf 'Not an InfraSet task or folder: %s\n' "$input_arg" >&2
    exit 2
  fi
done

if [[ ${#task_paths[@]} -eq 0 ]]; then
  printf 'No InfraSet tasks containing task.toml were found under: %s\n' \
    "${input_args[*]}" >&2
  exit 2
fi

if [[ ${#match_globs[@]} -gt 0 ]]; then
  declare -a filtered_paths=()
  for task_path in "${task_paths[@]}"; do
    task_name="$(basename "$task_path")"
    for glob in "${match_globs[@]}"; do
      # shellcheck disable=SC2053  # the right side is a pattern on purpose
      if [[ "$task_name" == $glob ]]; then
        filtered_paths+=("$task_path")
        break
      fi
    done
  done
  if [[ ${#filtered_paths[@]} -eq 0 ]]; then
    printf 'No task directory name matched: %s\n' "${match_globs[*]}" >&2
    exit 2
  fi
  task_paths=("${filtered_paths[@]}")
fi

# A scenario owns the ID. Every task must be directly inside its scenario folder.
task_scenario_id() {
  local task_path="$1"
  local parent="${task_path%/*}"
  local scenario_id="${parent##*/}"
  if [[ ! "$scenario_id" =~ ^[1-9][0-9]{3}$ ]]; then
    printf 'Task must be inside a four-digit scenario folder: %s\n' "$task_path" >&2
    return 2
  fi
  if [[ "${task_path##*/}" != *-"$scenario_id" ]]; then
    printf 'Task name must end with its scenario ID %s: %s\n' "$scenario_id" "$task_path" >&2
    return 2
  fi
  printf '%s' "$scenario_id"
}

declare -A task_names_seen=()
declare -A result_names=()
declare -A scenario_ids=()
declare -A environment_files=()
for task_path in "${task_paths[@]}"; do
  scenario_ids["$task_path"]="$(task_scenario_id "$task_path")"
  task_name="${task_path##*/}"
  result_names["$task_path"]="$task_name"
  if [[ -n "${task_names_seen[$task_name]+present}" ]]; then
    printf 'Duplicate result folder %s found in %s and %s\n' \
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
if [[ ! "$job_name" =~ ^[A-Za-z0-9][A-Za-z0-9._-]*$ ]]; then
  printf 'INFRASET_JOB_NAME must be one path segment: %s\n' "$job_name" >&2
  exit 2
fi

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

task_job_dir() {
  local task_path="$1"
  printf '%s/%s/%s/%s' \
    "$jobs_root" "${scenario_ids[$task_path]}" "$job_name" "${result_names[$task_path]}"
}

execution_parameters=(
  --parameter "transport=$transport"
  --parameter "execution_mode=$execution_mode"
  --parameter "agent_name=$agent_name"
  --parameter "model=$model"
  --parameter "reasoning_effort=$reasoning_effort"
  --parameter "service_tier=$([[ "$agent_name" == codex ]] && printf '%s' "$service_tier" || true)"
  --parameter "evaluator_model=$evaluator_model"
  --parameter "evaluator_reasoning_effort=$evaluator_reasoning_effort"
  --parameter "agent_timeout_sec=$agent_timeout_sec"
  --parameter "n_attempts=$n_attempts"
  --parameter "parallel_limit=$parallel_limit"
  --parameter "harbor_requirement=$harbor_requirement"
  --parameter "provider_requirement=$provider_requirement"
  --harbor-dir "${HARBOR_DIR:-}"
  --provider-dir "${INFRASET_PROVIDER_DIR:-}"
)
if (( skip_existing )); then
  execution_parameters+=(--skip-existing)
fi
refresh_job_index() {
  if ! "${validator_runner[@]}" python "$script_dir/scripts/generate_job_index.py" \
      --jobs-root "$jobs_root" "$@"; then
    printf 'Warning: could not refresh %s/INDEX.md; regenerate with scripts/generate_job_index.py.\n' "$jobs_root" >&2
  fi
}

execution_paths="$("${validator_runner[@]}" python "$script_dir/scripts/execution_metadata.py" \
  --jobs-root "$jobs_root" --batch "$job_name" \
  "${execution_parameters[@]}" "${task_paths[@]}")"
if [[ -z "$execution_paths" ]]; then
  refresh_job_index
  exit 0
fi
mapfile -t task_paths <<< "$execution_paths"

printf 'Transport: %s; mode: %s; tasks: %s; sequential trials per task: %s; concurrent tasks: %s\n' \
  "$transport" "$execution_mode" "${#task_paths[@]}" "$n_attempts" "$parallel_limit"
printf 'Results: %s/<scenario-id>/%s/<task-name>\n' "$jobs_root" "$job_name"

for task_path in "${task_paths[@]}"; do
  job_dir="$(task_job_dir "$task_path")"
  mkdir -p "$job_dir"
  cp "$task_path/instruction.md" "$job_dir/instruction.md"
  cp "${environment_files[$task_path]}" "$job_dir/environment.toml"
  cp "$task_path/variant.toml" "$job_dir/variant.toml"
  printf '\n[run]\nid = "%s"\nexecution_mode = "%s"\ntransport = "%s"\n' \
    "${scenario_ids[$task_path]}" "$execution_mode" "$transport" >> "$job_dir/variant.toml"
done

refresh_job_index

run_one_task() {
  local task_path="$1"
  local task_name
  local job_dir
  local jobs_dir
  task_name="$(basename "$task_path")"
  job_dir="$(task_job_dir "$task_path")"
  jobs_dir="$(dirname "$job_dir")"
  # Pass this scenario's snapshotted prompt to this child only; preserve newlines.
  export INFRASET_EXECUTOR_PROMPT=""
  if [[ -f "$jobs_dir/prompt" ]]; then
    INFRASET_EXECUTOR_PROMPT="$(cat "$jobs_dir/prompt"; printf '.')"
    INFRASET_EXECUTOR_PROMPT="${INFRASET_EXECUTOR_PROMPT%.}"
  fi

  printf '[%s] Starting (%s sequential trial(s))\n' \
    "$task_name" "$n_attempts"

  local -a agent_kwargs=(
    --agent-kwarg agent_name="$agent_name"
    --agent-kwarg reasoning_effort="$reasoning_effort"
    --agent-kwarg timeout_sec="$agent_timeout_sec"
    --agent-kwarg execution_mode="$execution_mode"
    --agent-kwarg diagnostic_agent="$agent_name"
    --agent-kwarg diagnostic_model="$model"
    --agent-kwarg diagnostic_reasoning_effort="$reasoning_effort"
  )
  local -a verifier_kwargs=(
    --verifier-kwarg agent="$agent_name"
    --verifier-kwarg model="$evaluator_model"
    --verifier-kwarg reasoning_effort="$evaluator_reasoning_effort"
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
    --job-name "$task_name" \
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
    refresh_job_index --job "$(task_job_dir "$task_path")" --status finished --exit-code "$status"
    printf '[%s] Completed successfully\n' "$task_name"
  else
    printf '[%s] Failed with exit code %s\n' "$task_name" "$status" >&2
    failed_tasks+=("$task_name")
    refresh_job_index --job "$(task_job_dir "$task_path")" --status failed --exit-code "$status"
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
    refresh_job_index --job "$(task_job_dir "${task_by_pid[$pid]}")" --status interrupted --exit-code 130
  done
  exit 130
}
trap terminate_active_tasks INT TERM

for task_path in "${task_paths[@]}"; do
  while (( ${#active_pids[@]} >= max_active_tasks )); do
    wait_for_one_task
  done

  refresh_job_index --job "$(task_job_dir "$task_path")" --status running
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
