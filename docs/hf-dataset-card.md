---
license: apache-2.0
pretty_name: "InfraSet: LLM-Executed Infrastructure Tasks"
language:
  - en
tags:
  - infrastructure
  - system-administration
  - agents
  - traces
  - linux
  - networking
  - observability
size_categories:
  - 10K<n<100K
configs:
  - config_name: runs
    data_files: data/runs.parquet
  - config_name: commands
    data_files: data/commands.parquet
  - config_name: tasks
    data_files: data/tasks.parquet
---

# InfraSet

An open dataset of LLM-executed infrastructure tasks. Every task ran on a
disposable cluster of full virtual machines, and every command the model issued
was recorded, along with what came back and what state was left behind.

- Recorded runs, commands, virtual machines, and authored tasks across single-host
  administration, multi-node services, stateful clusters, and four network operating systems
- **8 releases across 5 distributions**: Alpine, AlmaLinux 9, CentOS Stream 10,
  RHEL 7.9 / 9.8 / 10.0, Ubuntu 16.04 / 24.04
- **4 network platforms**: VyOS, OpenWrt, SONiC, OPNsense

Clusters were provisioned through [Antrieb](https://antrieb.sh) and executed with
the [Harbor](https://github.com/harbor-framework/harbor) framework. The full
source tree, including every raw artifact, is at
[github.com/open-sudo/infraset](https://github.com/open-sudo/infraset).

## Results

Start with **[single-node-os-comparison.md](metrics/single-node-os-comparison.md)**.
It is the widest comparison in the set: the same 30 tasks executed on all eight
releases, with command success and failure counts, completion time and operational
hygiene side by side, and every cell linking to the analysis for that run.

The remaining categories are summarised the same way.

| Category | Summary |
|---|---|
| Single-host administration | [single-node-os-comparison.md](metrics/single-node-os-comparison.md) |
| Multi-node services | [multi-node-os-comparison.md](metrics/multi-node-os-comparison.md) |
| Stateful clusters | [clustered-services.md](metrics/clustered-services.md) |
| VyOS | [vyos-networking.md](metrics/vyos-networking.md) |
| OpenWrt | [openwrt-networking.md](metrics/openwrt-networking.md) |
| SONiC | [sonic-networking.md](metrics/sonic-networking.md) |
| OPNsense | [opnsense-networking.md](metrics/opnsense-networking.md) |
| VyOS and OPNsense cross-vendor | [vyos-opnsense-networking.md](metrics/vyos-opnsense-networking.md) |
| Cluster provisioning | [cluster-provisioning-performance.md](metrics/cluster-provisioning-performance.md) |

## Tables

Three flat views over the job tree, for querying without walking the raw artifacts.

```python
from datasets import load_dataset

runs     = load_dataset("infraset/infraset", "runs")
commands = load_dataset("infraset/infraset", "commands")
tasks    = load_dataset("infraset/infraset", "tasks")
```

### `runs`

One row per execution, with the verifier's metrics.

| Field | Notes |
|---|---|
| `run_id` | `category/image/task/timestamp/cluster` |
| `category`, `image`, `task` | e.g. `clustered-services`, `rhel9`, `etcd-cluster-rhel9` |
| `reward` | Overall score, 0 to 1 |
| `functionality` | Fraction of the task's material outcomes satisfied |
| `operational_hygiene` | Penalises residue, unrelated mutation and collateral damage |
| `evaluation_coverage`, `evaluation_complete` | How much of the task the verifier could assess |
| `confidence` | Verifier's confidence in its own verdict |
| `command_count`, `node_count` | Size of the run |
| `first_command_at`, `last_command_at`, `wall_seconds` | Timing |

Runs with a null `reward` were executed but not scored.

### `commands`

One row per command the executor issued, joined to `runs` on `run_id`. The
underlying audit log writes two records per command, a request and a completion;
they are merged here, so the row count is the true command count.

| Field | Notes |
|---|---|
| `run_id`, `command_id`, `sequence` | `sequence` is issue order within the run |
| `node` | Managed node selector, e.g. `node1` |
| `command` | Exactly what was issued |
| `return_code`, `duration_ms` | Result |
| `stdout`, `stderr` | Full output, not truncated |
| `completed` | False when a command was issued but never returned |

### `tasks`

One row per authored task, including the instruction the model was given.

| Field | Notes |
|---|---|
| `task_path`, `category`, `slug`, `image_dir` | Location and identity |
| `instruction` | The plain-language objective, verbatim |
| `difficulty` | `easy`, `medium` or `hard` |
| `cluster`, `control_node`, `environment_toml` | Topology and node specification |
| `agent_timeout_sec`, `verifier_timeout_sec` | Limits the run was given |

## How runs were produced

Each run received a disposable cluster and a plain-language objective. The model
chose its own approach; nothing prescribed the commands. After finishing, it ran a
provider-wide restart protocol, rebooting each node and demonstrating that
services and data recovered.

An independent verifier then scored the run from captured evidence alone, with no
access to the live systems. It derives the task's material outcomes from the
public instruction and classifies each one, citing evidence.

**The executor and the verifier are both LLMs.** Every run here was executed by
Claude Sonnet 5 at medium reasoning effort, and scored by an LLM verifier. Command
counts, timings and return codes are direct observations; the scores are
judgments. Treat them accordingly.

## What is in the traces

Nothing is redacted or truncated. The traces contain whatever the model typed,
including credentials and key material it generated during a run: private keys,
certificates, cluster cookies and passwords.

All of it is ephemeral. The keys were generated on disposable virtual machines
that were destroyed when the run ended, none is reused across runs, and none
grants access to anything that still exists. They are published intact because
removing them would break the very traces the dataset exists to support: a
question like "does the model leave key material behind, and where" cannot be
answered from a redacted log.

## Known limitations

- **One model, one setting.** Nothing here says how a different model, or the same
  model at a different reasoning effort, behaves.
- **Two images execute as non-root.** RHEL 7.9 and Ubuntu 16.04 run as a normal
  user with `sudo -n`; the rest execute as root. Any old-versus-new comparison
  carries that confound.
- **Scores are LLM judgments.** See above. The raw evidence is published so they
  can be checked rather than trusted.
- **The restart protocol is applied to every task**, independent of its
  instruction, so the corpus may push the model toward durable configuration more
  than an ad-hoc request would.

## Citation

```bibtex
@misc{infraset2026,
  title  = {InfraSet: An Open Dataset of LLM-Executed Infrastructure Tasks},
  author = {InfraSet},
  year   = {2026},
  url    = {https://huggingface.co/datasets/infraset/infraset}
}
```

Apache 2.0. Contributions welcome: new tasks, new executions, or a re-reading of
the data.
