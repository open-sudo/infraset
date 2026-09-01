---
name: infraset-task-builder
description: Create or revise complete InfraSet tasks backed by Antrieb-managed nodes, including realistic workplace instructions, topology, environment configuration, optional brownfield preparation and baselines, and evidence-ready verification design. Use for task authoring under ~/infraset/tasks and for reviewing whether executor-collected evidence and global verifier observations can fairly score a task.
---

# InfraSet Task Builder

Create or revise one complete InfraSet task. Treat the InfraSet repository as the
source of task definitions. Harbor supplies execution and `harbor-antrieb` supplies
the Antrieb integration. This skill targets the evidence-based executor and global
verifier contract below. Legacy task-local verifier artifacts are ignored by the
current runtime. Tasks do not live in Harbor.

## Scope

Own:

- `instruction.md`
- `task.toml`
- `environment/harbor_antrieb.toml`
- optional `prepare/` setup, prompt, and baseline files
- the fail-closed `tests/test.sh` sentinel
- the task's evidence and scoring boundary

Verification is part of task design, not a separate probe-authoring activity. The
executor collects task-specific evidence after doing the work. The global verifier
scores the public problem from provider-captured evidence and may collect a small,
fixed set of static observations such as baseline-relative temporary-file residue.
Do not generate task-specific `verifier/checks.toml` or `verifier/judge.toml` files.

## Workflow

1. Inspect repository guidance and a nearby validator-passing task. Resolve runtime
   questions against current `harbor-antrieb` models.
2. Retrieve `antrieb/primer` and every relevant networking or image reference through
   the Antrieb MCP `search` tool before choosing topology or platform behavior. Read
   the returned bodies; do not guess provider facts.
3. Normalize the idea into an operational objective, node roles, topology, initial
   state, and genuine business constraints. Ask only when a missing business choice
   materially changes the task and cannot be discovered from the systems.
4. Choose `greenfield` when no task-authored state is needed and `brownfield` when
   preparation creates existing state. Reserve `complex/` for tightly coupled or
   specialized recovery-heavy scenarios.
5. Read [references/task-authoring.md](references/task-authoring.md) and write a
   concise, realistic `instruction.md`.
6. Read [references/implementation.md](references/implementation.md) and create the
   topology, runtime configuration, preparation, baseline, and sentinel.
7. Read [references/verification-contract.md](references/verification-contract.md).
   Confirm that every scored business fact is public, every preservation claim has a
   baseline when needed, and an executor can demonstrate the requested outcome with
   ordinary final validation commands. Do not prescribe those commands.
8. Run the public validator with `--task-only --strict`. Do not provision a cluster
   unless the user explicitly asks for execution.
9. Report the task path, preparation mode, topology, evidence boundary, baseline
   coverage, and unresolved limitations.

## Hard constraints

- Generate tasks statically. Do not require an executor model to pass before a task
  can be recorded.
- Use standard Harbor and `harbor-antrieb` formats. Do not create task-local runtime
  implementations or verifier programs.
- Keep credentials, models, lifecycle, retries, evidence capture, and scoring in
  runtime configuration rather than task files.
- Do not over-contract the public task. State the operational objective, topology,
  and genuine scenario-specific constraints in ordinary human language.
- Do not hide arbitrary business requirements. The verifier may apply documented
  platform invariants and universal hygiene rules, but it must not score an
  undeclared hostname, address, port, path, identity, or expected value.
- Refer to systems with managed selectors such as `node1`, `node2`, and `node3`.
  These select managed exec targets; they are not hostnames or in-cluster DNS
  identities. Never place literal IP addresses in `instruction.md`.
- Treat `NODE_NAME`, `NODE_IP`, and `CLUSTER_HOSTS` as provider-injected runtime
  values. Never copy transient addresses from an earlier execution into task files.
- Prefer deterministic, idempotent preparation. Capture a baseline whenever scoring
  must distinguish prepared state from executor-caused changes.
- Design outcomes that can be evidenced externally. Do not require the verifier to
  infer success from a preferred implementation shape.
- Treat availability, failover, restart, reboot, recovery, resynchronization, and
  healing requirements as behavioral outcomes. Ensure each can be demonstrated by
  one bounded, reversible state transition. Do not treat configuration alone as
  proof, and do not put validation mechanics in the public instruction.
- Keep executor evidence collection out of `instruction.md`; the global executor
  contract requests it for every task.
- Preserve unrelated files and legacy verifier artifacts when revising an existing
  task unless the user explicitly requests their migration or removal.
- Include every Antrieb reference used while authoring in `base_runbooks`; include no
  scenario-specific runbook.
