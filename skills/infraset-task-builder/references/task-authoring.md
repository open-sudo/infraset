# Candidate Task Authoring

## Goal

Write a concise performance-based certification task. Measure whether the executor
can administer infrastructure, not whether it can translate a supplied recipe into
commands.

## State publicly

- Required operational end state.
- Node topology and service roles.
- Exact identities, names, ports, paths, protocols, content, and data when they are
  genuine product requirements.
- Intended clients or access boundary when reachability matters.
- Availability or failure-tolerance outcome when it is part of the service contract.
- Explicit persistence: the configuration and service must remain operational after
  reboot.

Use short positive requirements. Describe what must be true, not how to make it true.

## Leave implicit

A competent administrator must independently handle:

- Distribution-appropriate packages, repositories, and service management.
- Boot enablement and persistent configuration.
- SELinux, AppArmor, firewalld, UFW, or the platform's applicable controls.
- Authentication, authorization, ownership, permissions, and least privilege.
- Necessary network exposure and removal of unintended listeners.
- Validation, troubleshooting, safe recovery, and cleanup.
- Preservation of unrelated state.

Do not turn these expectations into candidate instructions. Test them privately.

## Exclude from the public task

- Commands, procedural steps, package-manager instructions, and verification recipes.
- Implementation-specific configuration directives unless the implementation itself
  is the requested product requirement.
- Lists of prohibited actions or cleanup hints.
- Harbor, InfraSet, Antrieb, MCP, credentials, lifecycle, or evaluator mechanics.
- Details copied from private checks.

The shared executor prompt and restricted bridge enforce harness boundaries. They do
not belong in `instruction.md`.

## Fair hiddenness

Hide professional implications, not arbitrary business requirements.

It is fair to require an administrator to infer that a nonstandard HTTP port needs an
SELinux label, an effective firewall rule, boot enablement, safe permissions, and no
unnecessary default listener. It is not fair to secretly require a particular
database name, username, network, algorithm, or mount point unless the public outcome
defines it.

State failure behavior when it changes the promised service. For example, a
load-balanced service that must remain available after one backend fails needs that
availability outcome in the task. Recovery mechanics and secure implementation can
remain private checks.

## Self-review

Before finalizing `instruction.md`, confirm:

1. A candidate cannot pass merely by copying implementation bullets into commands.
2. Multiple secure implementations can satisfy the wording.
3. Every exact value in the prompt affects an observable business outcome.
4. Every hidden requirement is either normal platform competence or publicly implied
   by the requested outcome.
5. Persistence is explicit.
6. The text contains no harness instructions or prohibition list.

## Example abstraction

Too procedural:

> Install Nginx, edit its configuration, open the firewall, label port 6700 with
> SELinux, enable the service, and test it with curl.

Appropriate:

> Configure the distribution-supported Nginx service on node1 and node2. Each node
> must provide a successful HTTP response at `/` over TCP port 6700. The configuration
> and service must remain operational after both nodes are rebooted.
