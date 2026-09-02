# Evidence-Based Verification Contract

InfraSet uses one global verification workflow. Tasks do not prescribe probe
commands. The executor demonstrates the implementation it created; the verifier
independently determines the score from captured evidence and a small set of
universal static observations.

## Inputs

The verifier receives:

- The public problem statement.
- The authored topology and managed node roles.
- Preparation and initial-state baselines when present.
- The complete provider-captured executor command trace.
- The executor's references to final evidence commands.
- Universal static observations collected before or after execution.

The executor's prose summary is a claim, not evidence.

## Executor evidence

The global executor prompt, not `instruction.md`, requires a final evidence phase.
The executor should:

1. Finish implementation and cleanup before collecting final evidence.
2. Validate each explicit outcome with ordinary administrator commands appropriate
   to the implementation it actually created.
3. Prefer externally observable product behavior over internal representation.
4. Identify the provider-captured command events that support each requirement.
5. Include contradictory and failed final checks rather than concealing them.
6. Avoid printing credentials, private keys, tokens, or unrelated sensitive data.

An executor-generated `echo`, copied claim, or synthetic status message does not
prove the underlying state. Evidence must include the real command, managed target,
return code, bounded stdout and stderr, and capture time. Commands executed before a
later configuration mutation may be stale and must be treated accordingly.

Missing evidence is not automatically task failure. It lowers coverage and
confidence or makes the affected outcome indeterminate.

## Bounded resilience validation

A requirement concerning availability, failover, restart, reboot, recovery,
resynchronization, or healing cannot be fully established from steady-state
configuration alone. When such behavior is explicitly required, the executor must
perform the smallest safe, reversible disruption needed to demonstrate it:

1. Capture direct evidence of the healthy baseline.
2. Disrupt one representative service, member, or node at a time.
3. Preserve quorum and retain an independent recovery path.
4. Exercise and capture the required behavior while the disruption is active.
5. Restore the affected component, wait for recovery, and capture the final healthy
   state and current data.
6. Reference provider-captured command IDs from the healthy, disrupted, and recovered
   phases in the final evidence for that requirement.

Prefer service-level interruption when it adequately represents the required
failure. Reboot a node only when reboot behavior is explicit or a service-level test
cannot establish the outcome. Never power off a node, sever the management path, or
perform a disruption the executor cannot reverse. Do not exhaustively disrupt every
interchangeable member unless the task distinguishes their roles.

If the provider or harness cannot safely perform the required transition, capture
the limitation and all available supporting evidence, then leave the outcome
indeterminate. Do not substitute redundancy metadata, service enablement, restart
policy, topology, or expected product behavior for observed proof.

## Universal static collection

The verifier may run or receive a fixed, platform-aware set of deterministic
collectors. These collectors must not encode task-specific implementation choices.
Examples include:

- Baseline-relative `/tmp` and other temporary-file residue.
- Task-related failed service units where a service manager exists.
- Interrupted package-manager state.
- Executor command success and failure counts.
- Harness, preparer, executor, and verifier cleanup status.
- Brownfield baseline differences supplied by preparation.

Do not penalize a nonempty temporary directory. Compare before and after state,
attribute additions to the responsible phase, and exclude known harness, preparer,
and verifier-owned artifacts. Unsupported collectors are not applicable; they are
not failures.

Static collectors are read-only unless they remove their own bounded temporary state.
They must not troubleshoot, repair, reboot, stop services, or invent task-specific
tests.

## Process hygiene

Operational hygiene covers execution conduct as well as final-state cleanliness. The
verifier reviews every terminal executor command and identifies commands that may
have changed managed-system state. Each mutation must have a clear, evidence-supported
role in satisfying a material task outcome, establishing a necessary prerequisite,
collecting bounded final evidence, or restoring and cleaning temporary state.

A mutation with no clear causal connection to one of those purposes is an unnecessary
mutation. This includes troubleshooting experiments that did not contribute to the
final solution, even if they were later reverted. A bounded, low-risk mutation that
was fully restored warrants less concern than one that was retained, broad,
destructive, or weakened security controls. Read-only discovery, unsuccessful
commands without evidence of a state change, competent implementation choices, and
corrective cleanup are not hygiene defects. When mutation or contribution cannot be
determined from the trace, record a limitation instead of speculating.

Every unnecessary mutation cited by the verifier must reference its captured executor
command ID and say whether the resulting state remained or was reverted. This is a
global evaluation rule; do not disclose it as an extra requirement in a task's public
instruction.

## Scoring

The verifier determines:

- `reward`: how fully the supported evidence satisfies the requested outcome.
- `confidence`: how complete, direct, current, and trustworthy the evidence is.
- `evaluation_coverage`: how much of the requested outcome was conclusively assessed.
- `operational_hygiene`: whether the command timeline, applicable global collectors,
  and baselines show unnecessary mutations, attributable residue, or unrelated
  regression.
- Per-requirement `satisfied`, `partially_satisfied`, `not_satisfied`, or
  `indeterminate` findings with evidence links.

Use these semantics:

- **Satisfied:** captured evidence directly establishes the requirement.
- **Partially satisfied:** captured evidence establishes only part of the outcome.
- **Not satisfied:** valid captured evidence conclusively contradicts the requirement.
- **Indeterminate:** evidence is missing, stale, ambiguous, malformed, unsupported,
  or insufficient to distinguish task failure from collection failure.

For behavioral resilience requirements, score direct before/during/after proof as
`satisfied`, supporting configuration without the transition as at most
`partially_satisfied`, inability to perform or observe a safe transition as
`indeterminate`, and an observed behavioral failure as `not_satisfied`.

Do not turn a verifier limitation into executor failure. Do not infer arbitrary
values, endpoints, identities, paths, or expected state. Every scored fact must come
from the public task, live provider metadata captured in the trace, a documented
platform invariant, preparation baseline, or verifier-owned global observation.

The verifier may use an LLM to interpret the bounded evidence and assign the score,
but it does not receive a live troubleshooting loop. It must not invent or execute
task-specific follow-up commands after seeing the result.

## Task-builder responsibilities

The task builder must ensure that:

1. Every business value affecting functionality appears in the public request or
   authored topology.
2. Brownfield preservation and regression claims have sufficient baseline data.
3. Requested outcomes can be demonstrated through normal administrative evidence.
4. Equivalent competent implementations can produce acceptable evidence.
5. No hidden task-specific acceptance checklist is required.
6. Global hygiene checks remain attribution-aware and platform-appropriate.
7. Explicit resilience outcomes can be exercised through a bounded, reversible
   transition supported by the authored topology.

Do not create task-specific `checks.toml`, `judge.toml`, verifier prompts, or probe
scripts. Verification policy belongs to the shared runtime; task facts and baselines
belong to the task.
