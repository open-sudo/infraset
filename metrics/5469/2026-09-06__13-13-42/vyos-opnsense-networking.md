# vyos-opnsense-networking: command execution summary

Scope: `5469/2026-09-06__13-13-42`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| transit-firewall-pair | — | — | — | — | — | — | — | — |
| published-service-two-hops | — | — | — | — | — | — | — | — |
| double-nat-path | — | — | — | — | — | — | — | — |
| ipsec-vendor-interop | — | — | — | — | — | — | — | — |
| wireguard-vendor-interop | — | — | — | — | — | — | — | — |
| split-dns-authority | — | — | — | — | — | — | — | — |
| dhcp-per-segment-gateway | — | — | — | — | — | — | — | — |
| firewall-log-correlation | — | — | — | — | — | — | — | — |
| redundant-path-failover | — | — | — | — | — | — | — | — |
| policy-based-egress | — | — | — | — | — | — | — | [108/10](../../../jobs/5469/2026-09-06__13-13-42/policy-based-egress-bash-ubuntu24-5469/analysis.md) |
| **Average** | — | — | — | — | — | — | — | 108.0/10.0 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| transit-firewall-pair | — | — | — | — | — | — | — | — |
| published-service-two-hops | — | — | — | — | — | — | — | — |
| double-nat-path | — | — | — | — | — | — | — | — |
| ipsec-vendor-interop | — | — | — | — | — | — | — | — |
| wireguard-vendor-interop | — | — | — | — | — | — | — | — |
| split-dns-authority | — | — | — | — | — | — | — | — |
| dhcp-per-segment-gateway | — | — | — | — | — | — | — | — |
| firewall-log-correlation | — | — | — | — | — | — | — | — |
| redundant-path-failover | — | — | — | — | — | — | — | — |
| policy-based-egress | — | — | — | — | — | — | — | [13m 20s](../../../jobs/5469/2026-09-06__13-13-42/policy-based-egress-bash-ubuntu24-5469/analysis.md) |
| **Average** | — | — | — | — | — | — | — | 13m 20s |

Cluster provisioning is not a meaningful part of these times: median 1595 ms across 1 clusters, about 0.20% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| transit-firewall-pair | — | — | — | — | — | — | — | — |
| published-service-two-hops | — | — | — | — | — | — | — | — |
| double-nat-path | — | — | — | — | — | — | — | — |
| ipsec-vendor-interop | — | — | — | — | — | — | — | — |
| wireguard-vendor-interop | — | — | — | — | — | — | — | — |
| split-dns-authority | — | — | — | — | — | — | — | — |
| dhcp-per-segment-gateway | — | — | — | — | — | — | — | — |
| firewall-log-correlation | — | — | — | — | — | — | — | — |
| redundant-path-failover | — | — | — | — | — | — | — | — |
| policy-based-egress | — | — | — | — | — | — | — | [0.700](../../../jobs/5469/2026-09-06__13-13-42/policy-based-egress-bash-ubuntu24-5469/analysis.md) |
| **Average** | — | — | — | — | — | — | — | 0.700 |
