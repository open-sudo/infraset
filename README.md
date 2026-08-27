# Testing LLMs on Infrastructure Work

**InfraSet** is a dataset of executable infrastructure tasks and LLM execution
traces. It helps answer questions such as:

- How do LLMs behave on end-of-life Linux distributions such as Ubuntu 16.04?
- How do they perform on full-system VMs and distributed environments?
- How do they operate in brownfield environments?
- How do they handle networks, routers, firewalls, and switches?
- How do they handle migrations between versions or distributions?

These questions matter to anyone considering LLMs for real infrastructure work.

InfraSet currently contains 48 tasks, and we hope the community will help expand it.
This repository contains the dataset: task definitions, task-building guidance,
and execution results. These execution results can also be explored on
[Hugging Face](https://huggingface.co/datasets/infraset/infraset).
[A summary of all recorded task executions](results-summary.md) provides a quick
overview of environments, run counts, scores, durations, and takeaways.
[Structured JSONL indexes](data/) provide task, job, trial, and evaluation-analysis
records for filtering and programmatic analysis.
[Harbor](https://github.com/harbor-framework/harbor) provides the execution
framework, [Antrieb](https://antrieb.sh/) provides the infrastructure, while
[`harbor-antrieb`](https://github.com/open-sudo/harbor-antrieb) connects Harbor
to Antrieb.

## What makes InfraSet different

- **It is not a leaderboard.** InfraSet explores infrastructure scenarios rather
  than focusing on comparing LLMs.
- **A rich testbed.** It includes multiple operating systems,
  full-system VMs, multi-node clusters, and networked infrastructure.
- **Rich execution data.** It publishes traces of what the LLM attempted, what
  happened, whether it recovered, and whether the result worked—not just scores.

## Testbed

Tasks run on disposable VMs, clusters, and networks provisioned through
[Antrieb](https://antrieb.sh/). A key benefit of Antrieb is the exceptionally
fast provisioning of VM-based testbeds. No access to your infrastructure is
required.

Environments can include:

- Current and end-of-life Linux distributions, including RHEL 7 through 10,
  AlmaLinux 9, Alpine, Arch, Debian 13, Ubuntu 16.04, and Ubuntu 24.04
- Single-node and multi-node systems
- Brownfield configurations and pre-existing state
- Routers, firewalls, and switches, including VyOS, OPNsense, OpenWrt, and SONiC
- Multi-network topologies and real service dependencies

## Execution traces

Published runs include the observable, redacted agent trajectory:

- Agent messages and tool calls
- Commands, output, and errors
- Failed and recovery attempts
- Final response and evaluator result

Each task is evaluated against the resulting infrastructure state, not merely the
LLM's final answer. Browse and download the published traces from the
[InfraSet Hugging Face dataset](https://huggingface.co/datasets/infraset/infraset).

## Running a task

Install `uv` and log in to the agent you want to use, such as Codex or Claude
Code. Create an API key in the [Antrieb dashboard](https://antrieb.sh/dash), then
export the Antrieb token:

```bash
export ANTRIEB_TOKEN='ant_XXXXXX'
```

Run a task from the repository root:

```bash
./run-task.sh ./tasks/greenfield/haproxy-nodejs-ubuntu16
```

The runner fetches Harbor and `harbor-antrieb` automatically. Results are stored
under `jobs/<task-name>/`.

## Creating a task

InfraSet includes a task-builder skill that allows a coding agent to turn a task
idea into a complete executable Harbor task.

1. Copy `./skills/infraset-task-builder` into a skills directory your coding
   agent can access.
2. Load the skill and describe the task you want to create.

For example:

> Create an OpenLDAP task with 50 service accounts used at various times during
> the past eight months. Identify accounts unused for 90 or more days and disable
> them.

The skill generates the task instructions, topology, preparation, and evaluation
files. Run the generated task with:

```bash
./run-task.sh ./tasks/<category>/<generated-task-name>
```

## Exploring results

Task definitions are in `tasks/`; execution results are in `jobs/`. The same
results are published in the [InfraSet Hugging Face dataset](https://huggingface.co/datasets/infraset/infraset),
which is the easiest place to browse or download them. Use your preferred
analysis tool to investigate:

- What did the LLM try first?
- Which assumptions were incorrect?
- Where did it recover successfully?
- Did the final change actually solve the problem?
- What would a human SRE need to verify before applying the fix?

For structured analysis, start with `data/trials.jsonl`. It contains one record
per trial, including the task, environment, model, duration, provisioning time,
evaluation metrics, and links to the full recorded result. The companion
`data/evaluation-analysis.jsonl` explains incomplete evaluation dimensions using
the evaluator's recorded assertion failures, limitations, and summaries.

Regenerate these indexes after adding or removing jobs:

```bash
uv run --with tomli python scripts/generate_hf_index.py
```

## Contributing

Contributions are welcome, including new operating systems, network topologies,
clustered environments, brownfield scenarios, troubleshooting tasks, evaluation
improvements, and analysis of existing execution traces.
