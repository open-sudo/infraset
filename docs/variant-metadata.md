# Scenarios and task variant metadata

A scenario is a collection of tasks. Its persistent four-digit ID belongs to the
collection, not to an execution. Transport, model, and other execution parameters
belong to a timestamped job batch. The identical task sets previously named
vanilla-luna (5782) and trentina (7292) now share scenario 5782. Other collections
remain separate.

```text
tasks/5782/                         # shared direct / Trentina task set
  scenario.toml
  centralized-log-collector-bash-rhel7-5782/
    variant.toml
    instruction.md
    task.toml
    environment/harbor_antrieb.toml

tasks/5469/                         # former vanilla collection
  scenario.toml
  centralized-log-collector-bash-rhel7-5469/
    variant.toml
    ...
```

All tasks are direct children of their scenario folder. Task folder names are
`<usecase>-<language>-<os>-<id>`. Every task in a scenario carries the same ID.
The [scenario directory](../tasks/README.md) lists the collection-to-ID mapping.
Catalogs and collection notes are preserved under each scenario's `_collection/`.
The full historical task-path mapping is saved in `data/scenario-layout.json`.

## Running tasks

```bash
./run-task.sh --transport trentina tasks/5782
./run-task.sh --transport direct tasks/5469/centralized-log-collector-bash-rhel7-5469
```

`run-task.sh` reads each task's ID from its immediate parent folder, validates the
name and metadata, and writes results under:

```text
jobs/5469/<timestamp>/centralized-log-collector-bash-rhel7-5469/
```

There is no `--id` option, and `INFRASET_ID` is not used. Executions do not generate
IDs. When creating a new scenario, assign an unused four-digit ID once; retain it
for all tasks and subsequent runs. The runner supports several scenario folders
in one invocation and preserves the ID of each task.

## Task descriptor

Every task includes `variant.toml`. It is the descriptive source for search,
database ingestion, and a use-case index. `task.toml` remains Harbor's runtime
configuration. Metadata does not add requirements to the prompt or change scoring.

```toml
schema_version = 1
id = "5469"
usecase = "centralized-log-collector"
title = "Centralized log collector"
description = "Forward application logs from a client to a persistent central collector."
category = "multi-node-os-comparison"
tags = ["logging", "syslog"]
language = "bash"
os = "rhel7"
difficulty = "hard"

[prompt]
path = "instruction.md"
sha256 = "<64-character SHA-256 of the exact instruction.md bytes>"

[environment]
images = ["rhel7.9"]
node_count = 2
initial_state = "greenfield"
```

- `schema_version`: metadata format version, currently integer `1`.
- `id`: scenario ID as a string. It must match the parent folder and task suffix.
- `usecase`: stable lowercase slug grouping tasks by operational objective. The
  same use case may appear in many scenarios; it does not determine the scenario ID.
- `title`, `description`: searchable prose. Initial values were derived from task
  names and the first prose paragraph of each prompt and can be curated.
- `category`, `tags`: category slug and a nonempty list of unique tag slugs.
- `language`: implementation language/tool, such as `bash` or `ansible`.
- `os`: target OS label, such as `ubuntu7` or `centos-stream10`; bespoke
  heterogeneous scenarios use `mixed`.
- `difficulty`: `easy`, `medium`, `hard`, or `expert`, matching `task.toml`.
- `prompt`: relative prompt path and exact-byte SHA-256 for detecting changes.
- `environment`: distinct image selectors, total node count including controllers,
  and initial state according to preparation settings.

The runner copies the descriptor into each job and appends the actual run settings:

```toml
[run]
id = "5469"
execution_mode = "interactive"
transport = "direct"
```

Task descriptors must not contain `[run]`. In job snapshots, `run.id` and the
top-level `id` both identify the source scenario. Timestamps distinguish reruns.
For indexing, group scenarios by `id`, use cases by `usecase`, and task variants
by `(id, usecase, language, os)`. A prompt checksum alone is not a unique task key.

## Authoring and indexing

Author the descriptor with the task. Keep the scenario ID stable. Update the
prompt checksum and environment facts when their source files change.

```bash
python3.11 scripts/variant_metadata.py check
python3.11 scripts/variant_metadata.py check tasks/5782
python3.11 scripts/variant_metadata.py index > /tmp/infraset-task-index.jsonl
```

The JSONL exporter includes structured metadata plus `task_path`, relative to the
selected root. It emits output only after every descriptor validates. The public
task validator also checks metadata before execution. `init` can initialize missing
descriptors for migrated tasks with a recorded historical path; for brand-new
tasks, author the descriptor explicitly. Initialization never overwrites a file.

## Historical jobs

Historical jobs use the same `jobs/<id>/<timestamp>/<task-name>-<id>/` layout.
All execution artifacts and original timestamps are preserved. The path migration
is recorded in `data/job-layout.json`; shared readers can resolve historical paths
through this mapping. Metadata references the source scenario and current task path.
Previously generated per-run IDs are retained as `backfill.previous_run_id` for
traceability. Prompt and environment facts come from saved job snapshots, while
`[backfill]` identifies fields inherited from the current task catalog.

```bash
python3.11 scripts/backfill_job_variants.py          # preview
python3.11 scripts/backfill_job_variants.py --write  # add or align descriptors
```

The backfill covers jobs with saved instructions and environments, including
incomplete jobs. Modes and transports absent from historical records remain
unspecified. It never generates scenario IDs and leaves already-aligned files
unchanged.

## Job batch layout

Tasks launched together share a timestamp folder within their scenario:

```text
jobs/5782/
  2026-10-04__12-00-00/
    centralized-log-collector-bash-rhel7-5782/
    centralized-log-collector-bash-rhel10-5782/
```

Each task folder contains its Harbor job, trials, saved instructions, environment,
and variant metadata. Each timestamp folder also contains `execution.toml`, with
resolved execution parameters, their fingerprint, and hashes of task inputs.
`--skip-existing` requires the same task, scenario, execution settings, task revision,
and completed attempt count. Changing transport, model, mode, or task inputs
therefore produces a new execution. Existing job folders are never overwritten. The timestamp is the batch label; Harbor's job name is the
full task name. The existing `INFRASET_JOB_NAME` override supplies the batch label.


The consolidated histories are:

- `jobs/5782/2026-10-01__19-16-34/`: 362 direct jobs.
- `jobs/5782/2026-10-02__08-42-41/`: 362 Trentina jobs.

Their manifests preserve recorded Harbor task digests and original scenario IDs.
Historical digests are not assumed equivalent to the new task-revision hashes,
so these historical batches do not trigger automatic skipping. Their transport
labels come from the confirmed execution history; other settings come from saved
job configs. New batches record hashes of task file contents and permissions,
excluding descriptive `variant.toml` metadata.

The former 7292 task copies are preserved in `data/scenario-archives/7292/`.
`data/scenario-consolidation.json` records the moves; the task and job layout
maps retain aliases for historical paths. Run either transport against the same
active task set:

```bash
./run-task.sh --transport direct tasks/5782
./run-task.sh --transport trentina tasks/5782
```


## Additional scenario prompt

A scenario may contain a UTF-8 file named `prompt`, alongside `scenario.toml`.
`run-task.sh` snapshots its contents to `jobs/<id>/<timestamp>/prompt` and passes
that text in `INFRASET_EXECUTOR_PROMPT` to the Harbor child process for each task.
`harbor_antrieb` appends it to the default executor prompt, including retries.
The task instruction, default executor instructions, and evaluator are unchanged.
Scenarios without a prompt pass an empty value, preventing inheritance from a
previous scenario or the calling shell. Do not put credentials in this file.

The execution manifest records `parameters.prompt_sha256`; changing the prompt
changes the configuration fingerprint and prevents `--skip-existing` from reusing
a run with different guidance. The generated job index links to the saved prompt.

Scenario `9038` copies all 100 RHEL10 tasks from `3922` and adds the administrator
policy in `tasks/9038/prompt`. Run it with `./run-task.sh tasks/9038`.
This requires the updated local `harbor-antrieb` provider (or a release containing
the `INFRASET_EXECUTOR_PROMPT` support).

Scenario `2935` copies the same 100 tasks from `9038` with prompt revision 2.
It adds reversion of unsuccessful troubleshooting changes, verification of the
intended user workflow after cleanup, and a final review of changes against the
initial state. Scenarios `3922` and `9038` remain unchanged for comparison.

The `2935` prompt also incorporates the ten curated operating rules, consolidated
with its existing guidance. Prompt changes are tracked by the execution hash;
the scenario ID and task definitions remain the same.
