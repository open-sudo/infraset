---
name: infraset-task-builder
description: Create or revise InfraSet infrastructure tasks backed by Antrieb-managed nodes. Use for task design, topology, preparation, semantic evaluation, validation, and runnable commands. Tasks are stored outside the Harbor checkout under ~/infraset/tasks.
---

# InfraSet Task Builder

Create or revise one task under `${HOME}/infraset/tasks`. The Harbor host is the
execution host: it runs the Harbor CLI, InfraSet executor, and semantic verifier.
The Harbor checkout is not the task storage location. Managed nodes come from
Antrieb, and the host-side components access them through the InfraSet bridge.

## Workflow

1. Read the Harbor checkout's `AGENTS.md`, `packages/infraset/README.md`, and the
   closest existing task under `${HOME}/infraset/tasks`.
2. Read `antrieb/primer` plus every relevant networking or appliance reference
   before selecting images, networks, addresses, NICs, gateways, or lifecycle
   behavior. If an authoritative primer is unavailable, stop rather than guess.
3. Choose `greenfield` or `brownfield`.
4. Read `references/task-authoring.md` and write a concise outcome-based
   `instruction.md`.
5. Read `references/implementation.md` and create the task under
   `${HOME}/infraset/tasks/{greenfield,brownfield}/...`.
6. Read `references/evaluation.md` and create semantic probes and atomic assertions
   in `verifier/checks.toml`, with dimensions and weights in
   `verifier/judge.toml`.
7. Validate without contacting Antrieb:

   ```bash
   cd "$HOME/harbor"
   uv run --package infraset python \
     "$HOME/infraset/skills/infraset-task-builder/scripts/validate_example.py" \
     "$HOME/infraset/tasks/<category>/<task-name>"
   uv run --package infraset pytest packages/infraset/tests/unit -q
   git diff --check
   ```

8. Report the task path, preparation mode, evaluation coverage, limitations, and
   the command using `$HOME/infraset/run-task.sh`. Do not launch a live cluster
   unless explicitly requested.

## Constraints


- Use `InfraSetHostAgent`, `InfraSetEnvironment`, `InfraSetVerifier`, and the
  existing Python exec bridge; do not create task-local runtime implementations.
- Keep model, agent, verifier, and credential selection in run-time configuration.
- Keep Antrieb tokens and credentials on the Harbor host.
- Keep provider lifecycle outside the executor.
- Include in `base_runbooks` the primers and appliance references read during
  authoring. Do not include scenario runbooks.
- Verify addresses, gateways, DHCP ranges, NIC mappings, image capabilities, and
  reboot behavior against the authoritative primers.
