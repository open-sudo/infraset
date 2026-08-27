# Private Evaluation Design

## Dimensions

Use applicable dimensions with weights totaling 1.0:

- `functionality`: requested behavior from the intended consumer.
- `security`: effective exposure, controls, authentication, authorization,
  permissions, and privilege.
- `persistence`: the complete functional and secure state after reboot.
- `resilience`: failure tolerance, recovery, synchronization, and rejoining when the
  service contract requires them.
- `operational_hygiene`: unnecessary or conflicting changes and residual artifacts.

Redistribute weight when a dimension is genuinely inapplicable. Do not manufacture a
resilience test for a nonredundant service.

## Check effective behavior

- Exercise the service from its intended client or another managed node when network
  availability matters; localhost alone is insufficient.
- Inspect runtime state as well as persistent configuration.
- Test every relevant node, role, direction, endpoint, and identity.
- Verify absence of unintended listeners and broad exposure.
- Confirm mandatory access controls remain enforcing and permit the service through
  the correct persistent mechanism.
- Confirm firewall runtime and persistent state and, where possible, actual allowed
  and denied network behavior.
- Check authentication, permissions, service identity, and least privilege.
- Prefer semantic or behavioral assertions over matching one exact file layout.

## Persistence and disruption

Reboot every relevant node, wait for it to return, then rerun functionality and
security checks. For redundant systems, inject a controlled failure, verify the
remaining service, restore the component, and verify clean recovery and rejoining.

Evaluator operations such as reboot, stop, start, and fault injection are setup
actions, not evidence of executor quality. They must not earn points. Ensure
cleanup and recovery run even when an earlier assertion fails.

Ensure recovery actions run even after a failed assertion so evaluation does not
leave the managed system unnecessarily damaged.

## Atomic evidence

Keep important assertions atomic enough to identify the failed property. A single
shell block may prepare context, but do not combine SELinux, firewall, listeners,
service status, and HTTP behavior into one opaque exit code when separate evidence is
practical.

Use retries only for state expected to converge after reboot or recovery. Avoid long
retries for permanent configuration failures.

## Verification depth

Semantic evaluation uses cumulative runtime levels 1 through 10. Level 1 should be
a small, non-destructive smoke suite; add controlled failures at level 6 or higher
and reboots at level 8 or higher. Create `verifier/checks.toml`.
Separate evidence collection from scoring. Define
ordered `[[probes]]` with a stable ID, cumulative level, target nodes, allowed effect,
command budget, procedure, and cleanup for every mutation. Then define atomic
`[[assertions]]` that reference one probe and declare a dimension, authored points,
optional criticality and prerequisites, and explicit pass/fail conditions. One probe
may support several assertions, but each assertion must represent only one operational
property. Keep level 1 to a few core functional probes and level 2 to high-value
functionality and security. Put controlled failures at level 6 or higher and reboots
at level 8 or higher.

The semantic evaluator executes probes and reports `pass`, `fail`, or `indeterminate` plus
concrete command evidence for every selected assertion. It never assigns scores. InfraSet
aggregates authored assertion points deterministically. Missing evidence,
command errors, expired access, ambiguous output, and unmet prerequisites are
evaluator limitations: they make only affected assertions indeterminate and reduce
coverage without penalizing the executor. Incomplete mutation cleanup makes every
assertion supported by that probe indeterminate.

Use assertion prerequisites only when the dependent property is genuinely impossible
to evaluate without the prerequisite. Do not form a dependency chain across otherwise
independent core outcomes: one failed discovery command must not suppress all remaining
checks. Where client names, credential locations, service layouts, or packaging may
vary, give the evaluator enough command budget to discover a working local mechanism
and attempt a fallback. A failed strategy should be diagnosed on that node rather than
repeated unchanged across every node.

The default minimum coverage is 1.0. Below the configured threshold, preserve the
dimension results and a provisional score for diagnosis, but omit the primary
`reward`, set `evaluation_complete = false`, and make the run ineligible for
publication. A lower threshold must be an explicit run-time policy decision through
`--verifier-kwarg minimum_coverage=<0-through-1>`.

Negative checks must fail closed. A connection error, missing client configuration,
authentication failure, or unavailable control plane is not proof that access was
denied. Establish prerequisites in `command_prelude` or explicitly before negating a
probe. Likewise, preserve and test the exit status of commands whose empty output is
used as evidence.

## Brownfield hygiene

Compare with the preparation baseline. Grade preservation of existing data,
accounts, packages, services, policies, and configuration rather than assuming a
pristine image. Distinguish intended changes from operational residue.

For greenfield tasks, inspect all relevant nodes for unnecessary users, credentials,
packages, services, firewall rules, listeners, temporary files, backups, debug
settings, and conflicting configuration.

## Scoring

- Weight outcomes by importance rather than number of commands.
- Do not give points to evaluator actions.
- Do not double-count one observation merely because it appears in several shell
  commands.
- Apply a clear critical-failure cap for severe nonfunctionality, unsafe exposure,
  disabled controls, data loss, or failed recovery.
- Make a perfect score mean the infrastructure is functional, secure, persistent,
  recoverable where applicable, and clean—not just that packages and processes exist.

## Fairness review

Before finalizing checks, confirm that:

1. Equivalent secure implementations can pass.
2. Every arbitrary product value is public.
3. Hidden checks represent normal operational competence.
4. Effective behavior is tested, not inferred only from configuration text.
5. Failure output identifies what actually broke.
6. Every scored assertion measures executor work.
