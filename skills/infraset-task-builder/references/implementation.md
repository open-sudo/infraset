# InfraSet Task Implementation

## Standard layout

Choose the directory from the task's initial state and complexity:

```text
../infraset/tasks/greenfield/infraset-<slug>/
../infraset/tasks/brownfield/infraset-<slug>/
../infraset/tasks/complex/greenfield/infraset-<slug>/
../infraset/tasks/complex/brownfield/infraset-<slug>/
```

Use `greenfield` when preparation is disabled and the executor receives pristine
managed nodes. Use `brownfield` when task-authored preparation establishes existing
state and captures a baseline before execution. Do not place a task in `brownfield`
merely because the underlying image contains normal distribution defaults.

Use the matching `complex/` directory when a task combines tightly coupled
distributed services, consensus or replication with recovery/rejoin, specialized
appliances with several custom networks or NICs, or an empirically long workflow
that can consume most of the provider lease. Multiple nodes alone do not make a task
complex.

Within the selected directory, create:

```text
instruction.md
task.toml
environment/harbor_antrieb.toml
verifier/checks.toml
tests/test.sh
```

Add preparation files only when preparation is enabled:

```text
prepare/setup.toml
prepare/baseline.toml
prepare/prompt.md        # AI preparation only
```

Add `verifier/judge.toml` with semantic dimensions and weights. Do not create unused
directories or compatibility files.

## Task and environment

Use the current task schema and shared verifier environment mode. Follow the closest
existing example rather than copying stale values blindly.

Define managed topology in `environment/harbor_antrieb.toml`:

```toml
cluster = ["ubuntu24.04 x3"]
base_runbooks = ["antrieb/primer"]
control_node = "node1"
endpoint = "https://antrieb.sh/mcp"
```

Always include `antrieb/primer`. Add `antrieb/networking-primer` when the task
declares custom networks or NICs. Add an appliance reference such as
`antrieb/vyos-reference` for each specialized image. Do not add scenario runbooks:
the harness accepts only base primers and appliance references, reads them before
provisioning, and injects them transiently into host-side AI prompts.

Read those primers and references while authoring the task, before selecting the
topology or exact values. They are authoritative for provider-reserved addresses,
egress gateways, DHCP behavior, NIC attachment and naming, available image
capabilities, management access, reboot behavior, and other platform constraints.
Do not infer these conventions from an older example or merely list a runbook in
`base_runbooks` without reading it.

Create an address-allocation check for every custom network: record its CIDR,
provider gateway and reserved range, DHCP range, node addresses, service VIPs, and
published endpoints. Confirm that every address is unique, belongs to its intended
network, survives the declared lifecycle, and does not conflict with infrastructure
described by the primers. If an authoritative primer cannot be read, stop and report
the blocker instead of inventing a topology.

Tasks default to one executor cluster. For a task where learning from a failed or
expired attempt is part of the intended budget, declare a small explicit quota:

```toml
max_clusters = 3
```

Each retry uses an identically specified fresh cluster and repeats preparation. Do
not increase the quota merely to hide an unreliable image, preparer, or evaluator.
Increase `[agent].timeout_sec` enough to contain every cluster lease plus the
log-only postmortems.

Use Antrieb image names that are actually available in this repository/environment.
Do not add Docker or Compose files.

## Preparation decision

For a greenfield task, leave preparation disabled and omit preparation files.

For deterministic brownfield state:

```toml
[prepare]
enabled = true
mode = "static"
setup = "prepare/setup.toml"
baseline = "prepare/baseline.toml"
```

Put idempotent or safely repeatable mutations in staged `[[steps]]`. Capture facts
needed for later comparison as `[[observations]]`. Use required observations for
grading prerequisites and optional observations only for documented limitations.

Use AI preparation only when deterministic setup cannot represent the scenario.
Keep `agent` and `model` absent from task files and supply them with environment
kwargs at run time. AI preparation still ends with a static baseline.

## Executor and evaluator selection

Use these direct import paths:

```text
infraset.agent:InfraSetHostAgent
infraset.environment:InfraSetEnvironment
infraset.verifier:InfraSetVerifier
```

Semantic verification uses the cumulative `--verifier-kwarg level=<1-through-10>`.
Every task needs `verifier/judge.toml` with its semantic dimensions and weights.

Put shared shell prerequisites in the top-level `command_prelude`. Use it to select
an explicit client configuration and fail before assertions when the service being
queried is unavailable. Since the prelude runs on every target node, guard
controller-only setup with the managed `NODE_NAME` variable.

Keep the Harbor 0.21 fail-closed `tests/test.sh` sentinel required by task validation.
It must explain that the custom InfraSet verifier is required and exit nonzero.

## Fully expanded run command

Use Harbor's supported long options. The environment long option is `--env`.

```bash
uv run --package infraset harbor run \
  --path ../infraset/tasks/<category>/infraset-<slug> \
  --agent infraset.agent:InfraSetHostAgent \
  --model <executor-model> \
  --agent-kwarg agent_name=<executor-backend> \
  --agent-kwarg reasoning_effort=medium \
  --agent-kwarg diagnostic_agent=<postmortem-backend> \
  --agent-kwarg diagnostic_model=<postmortem-model> \
  --agent-kwarg diagnostic_reasoning_effort=medium \
  --env infraset.environment:InfraSetEnvironment \
  --verifier infraset.verifier:InfraSetVerifier \
  --verifier-kwarg level=<1-through-10>
```

Configure semantic evidence collection with deterministic assertion scoring:

```text
--verifier infraset.verifier:InfraSetVerifier
--verifier-kwarg agent=<evaluator-backend>
--verifier-kwarg model=<evaluator-model>
--verifier-kwarg reasoning_effort=low
--verifier-kwarg level=<1-through-10>
--verifier-kwarg minimum_coverage=1.0
```

Its task-owned `checks.toml` separates bounded `[[probes]]` from atomic
scored `[[assertions]]`. Evaluator limitations make only affected assertions
indeterminate. Runs below the minimum coverage omit the primary reward and are not
publication eligible.

For AI preparation, add:

```text
--environment-kwarg prepare_mode=ai
--environment-kwarg prepare_agent=<preparer-backend>
--environment-kwarg prepare_model=<preparer-model>
--environment-kwarg prepare_reasoning_effort=medium
```

The executor model remains Harbor's first-class `--model` value. Static preparation
uses no model; AI preparation receives its model through run-time kwargs.

## Validation

Run:

```bash
uv run --package infraset python \
  ../infraset/skills/infraset-task-builder/scripts/validate_example.py \
  ../infraset/tasks/<category>/infraset-<slug>
uv run --package infraset pytest packages/infraset/tests/unit -q
git diff --check
```

For Python changes, also follow the repository's Ruff and `ty` requirements. Never
launch a live cluster merely to validate generated files unless the user authorizes
the run.
