# Workplace Task Authoring

## Contents

- Goal
- Public requirements
- Professional expectations
- Evidence-ready outcomes
- Excluded content
- Fair scoring boundary
- Self-review
- Example

## Goal

Write an infrastructure request as a human operator, manager, or customer would
assign it. InfraSet measures how an LLM handles human requests on real systems; it
does not measure translation of a supplied acceptance checklist into commands.

Avoid over-contracting. State the job and the facts a human would actually supply.
The verifier scores the public problem using executor-collected evidence, topology,
preparation baselines, and universal static observations. There is no private list of
task-specific acceptance commands.

## Public requirements

Include:

- The requested operational outcome.
- The systems and roles a human would identify.
- Exact identities, names, ports, paths, protocols, content, and data when they are
  genuine business requirements.
- The intended client or access boundary when reachability matters.
- Unusual availability, migration, compatibility, or preservation behavior when it
  materially defines the request.

Use concise ordinary language. Describe what the human wants, not how to implement
or verify it. Include a constraint only when it distinguishes this scenario from
competent normal administration or materially changes the requested outcome.

Refer to managed systems as `node1`, `node2`, and so on. These are stable task-facing
selectors, not promises about hostnames or internal DNS. Never include literal IP
addresses; transient addresses are discovered at execution time.

## Professional expectations

A competent administrator normally handles:

- Distribution-appropriate packages, repositories, and service management.
- Boot enablement and persistence.
- Applicable SELinux, AppArmor, firewall, and host-security controls.
- Authentication, authorization, ownership, permissions, and least privilege.
- Necessary exposure and removal of unintended listeners.
- Validation, troubleshooting, safe recovery, and cleanup.
- Preservation of unrelated state.

Do not restate all of these as task requirements. The global verifier may consider
documented platform invariants and universal hygiene observations. An implicit
professional expectation may affect hygiene or confidence, but it must not smuggle
an arbitrary business value into the score.

## Evidence-ready outcomes

Write requirements whose effects can be demonstrated through normal final validation
by the executor. Good evidence comes from service clients, effective configuration,
service managers, protocol responses, data queries, and other externally observable
state. Do not force a particular proof command or implementation representation.

The executor is globally instructed to collect evidence after completing the work.
Do not add evidence-collection instructions to `instruction.md`.

For brownfield preservation requirements, ensure preparation records the exact facts
needed for a fair before-and-after comparison. If a fact cannot be reconstructed from
the public task, live environment, or baseline, leave it unscored rather than hiding
it from the executor.

## Excluded content

- Commands, procedural steps, package-manager instructions, and verification recipes.
- Implementation-specific directives unless that implementation is itself required.
- Lists of prohibited actions or cleanup hints.
- Harbor, InfraSet, Antrieb, MCP, evidence IDs, credentials, lifecycle, or scoring
  mechanics.
- Values introduced only to make evaluation convenient.

## Fair scoring boundary

Every task-specific fact that can affect functionality must be traceable to the
public request, topology, or preparation baseline. The global verifier may additionally
apply documented platform invariants and baseline-relative hygiene checks.

It is fair to expect an administrator to preserve enforcing SELinux on a RHEL system,
enable a requested persistent service, avoid unrelated failed units, and clean up its
own troubleshooting residue. It is not fair to require a hidden database name,
username, address, algorithm, mount point, or serialization choice.

Real workplace requests can be incomplete. Let the executor discover facts that a
human would discover from the systems. State facts that require a business decision,
or leave the corresponding outcome indeterminate and unscored.

## Self-review

Confirm that:

1. The text sounds like a plausible human request.
2. It states the job rather than an acceptance checklist.
3. Multiple competent and secure implementations can satisfy it.
4. Every exact value affects a real observable outcome.
5. Every task-specific scored fact is public or baseline-backed.
6. The outcome can be demonstrated without assuming a private implementation shape.
7. Brownfield preservation claims have sufficient baseline evidence.
8. The text contains no harness or evidence-collection instructions.
9. It uses node selectors rather than literal IP addresses.

## Example

Too procedural:

> Install Nginx, edit its configuration, open the firewall, label port 6700 with
> SELinux, enable the service, and test it with curl.

Appropriate:

> Configure Nginx on node1 and node2 to serve the application at `/` over TCP port
> 6700.
