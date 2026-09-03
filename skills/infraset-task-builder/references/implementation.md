# InfraSet Task Implementation

## Contents

- Layout
- Antrieb references and topology
- Preparation and baselines
- Runtime integration
- Validation

## Layout

Choose a directory from the initial state and complexity:

```text
${HOME}/infraset/tasks/greenfield/<slug>/
${HOME}/infraset/tasks/brownfield/<slug>/
${HOME}/infraset/tasks/complex/greenfield/<slug>/
${HOME}/infraset/tasks/complex/brownfield/<slug>/
${HOME}/infraset/tasks/os-comparison/<os>/<slug>-<os>/
```

Use `os-comparison/` only for a controlled matrix in which the same public request
is instantiated on multiple operating systems. Keep each task family's
`instruction.md` identical across the matrix and vary only the environment and any
strictly necessary platform initialization. Include the OS ID in every concrete
task directory name because task and job names are globally unique.

Create:

```text
instruction.md
task.toml
environment/harbor_antrieb.toml
tests/test.sh
```

Add preparation only when enabled:

```text
prepare/setup.toml
prepare/baseline.toml
prepare/prompt.md        # AI preparation only
```

Do not create task-specific `verifier/checks.toml` or `verifier/judge.toml`. The
executor collects task-specific evidence and the shared verifier scores it. Preserve
legacy verifier files during an unrelated task revision unless migration or removal
is explicitly requested.

Keep `tests/test.sh` as Harbor's fail-closed sentinel:

```sh
#!/bin/sh
echo "InfraSet requires the configured Harbor-Antrieb verifier." >&2
exit 1
```

## Antrieb references and topology

Use the Antrieb MCP `search` tool to retrieve each authoritative reference by exact
name before authoring topology. Read `antrieb/primer` for every task. Read
`antrieb/networking-primer` for custom networks or NICs and the relevant image
reference for specialized appliances. This is metadata discovery; do not provision a
cluster during static task generation.

Define the environment in `environment/harbor_antrieb.toml`:

```toml
cluster = ["ubuntu24.04 x3"]
base_runbooks = ["antrieb/primer"]
control_node = "node1"
endpoint = "https://antrieb.sh/mcp"
```

Include every reference used during authoring in `base_runbooks`. Do not include
scenario runbooks. For custom networks, verify CIDRs, reserved addresses, gateways,
DHCP ranges, node placement, service addresses, and NIC mappings against the primer.
Never copy a transient address from another run.

Use only currently available images. Do not add Docker or Compose files. Declare
`max_clusters` only when the scenario intentionally permits fresh executor attempts;
do not use retries to hide unreliable preparation.

## Preparation and baselines

Leave preparation disabled for greenfield tasks.

For deterministic brownfield state:

```toml
[prepare]
enabled = true
mode = "static"
setup = "prepare/setup.toml"
baseline = "prepare/baseline.toml"
```

Put idempotent or safely repeatable mutations in `[[steps]]`. Put facts needed for
later preservation or regression scoring in `[[observations]]`. Mark an observation
required only when scoring cannot be fair without it.

Baseline observations should capture durable facts, not transient noise. Record the
content, ownership, service state, policy, or application data that the task requires
the executor to preserve. Global collectors may capture generic before-and-after
hygiene such as temporary-file residue, but they cannot reconstruct missing
task-specific brownfield facts.

Use AI preparation only when deterministic setup cannot represent the scenario.
Keep preparer model selection out of task files and finish AI preparation with a
deterministic baseline.

## Runtime integration

The provider imports are:

```text
harbor_antrieb.agent:AntriebHostAgent
harbor_antrieb.environment:AntriebEnvironment
harbor_antrieb.verifier:AntriebVerifier
```

The shared executor contract requires the executor to perform final validation
and identify provider-captured command evidence for the requested outcomes. The
shared verifier then determines reward and confidence from the public problem,
topology, baseline, complete executor trace, selected evidence, and universal static
observations. Do not duplicate this contract in `instruction.md`. Task-local static
verifier files are not runtime inputs.

Every provider exec call exposes `NODE_NAME`, `NODE_IP`, and `CLUSTER_HOSTS`.
`node1` and similar values select managed exec targets but are not in-cluster DNS
names. Public protocol identities belong in the task only when they are genuine
business requirements.

Run a task through the repository runner:

```bash
${HOME}/infraset/run-task.sh \
  ${HOME}/infraset/tasks/<category>/<slug>
```

The runner supplies models, agent, provider, verifier, credentials, lifecycle, and
output location. Do not hardcode them in task files.

## Validation

Validate the evidence-based task artifacts:

```bash
uv run --isolated --no-project \
  --with-editable "${HOME}/harbor-antrieb" \
  python "${HOME}/infraset/skills/infraset-task-builder/scripts/validate_example.py" \
  --task-only --strict "${HOME}/infraset/tasks/<category>/<slug>"
git -C "${HOME}/infraset" diff --check
```

Without a local provider checkout, replace `--with-editable` with:

```text
--with "harbor-antrieb @ git+https://github.com/open-sudo/harbor-antrieb.git"
```

Static validation checks schemas and authoring policy. It does not prove that the
executor will complete the task or collect sufficient evidence. Do not launch a
cluster unless the user explicitly authorizes execution.
