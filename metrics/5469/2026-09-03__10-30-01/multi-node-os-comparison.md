# multi-node-os-comparison: command execution summary

Scope: `5469/2026-09-03__10-30-01`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | [32/6](../../../jobs/5469/2026-09-03__10-30-01/shared-nfs-storage-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| centralized-log-collector | [31/3](../../../jobs/5469/2026-09-03__10-30-01/centralized-log-collector-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| ssh-controller-access | [31/7](../../../jobs/5469/2026-09-03__10-30-01/ssh-controller-access-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| internal-ca-tls | [31/6](../../../jobs/5469/2026-09-03__10-30-01/internal-ca-tls-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| internal-time-sync | [19/0](../../../jobs/5469/2026-09-03__10-30-01/internal-time-sync-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| load-balanced-web-tier | [38/0](../../../jobs/5469/2026-09-03__10-30-01/load-balanced-web-tier-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| network-scoped-firewall | [34/4](../../../jobs/5469/2026-09-03__10-30-01/network-scoped-firewall-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| config-sync | [32/3](../../../jobs/5469/2026-09-03__10-30-01/config-sync-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| scheduled-backup | [28/3](../../../jobs/5469/2026-09-03__10-30-01/scheduled-backup-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| internal-dns-resolution | [18/2](../../../jobs/5469/2026-09-03__10-30-01/internal-dns-resolution-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| **Average** | 29.4/3.4 | — | — | — | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | [5m 23s](../../../jobs/5469/2026-09-03__10-30-01/shared-nfs-storage-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| centralized-log-collector | [5m 52s](../../../jobs/5469/2026-09-03__10-30-01/centralized-log-collector-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| ssh-controller-access | [4m 45s](../../../jobs/5469/2026-09-03__10-30-01/ssh-controller-access-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| internal-ca-tls | [8m 50s](../../../jobs/5469/2026-09-03__10-30-01/internal-ca-tls-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| internal-time-sync | [3m 55s](../../../jobs/5469/2026-09-03__10-30-01/internal-time-sync-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| load-balanced-web-tier | [5m 57s](../../../jobs/5469/2026-09-03__10-30-01/load-balanced-web-tier-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| network-scoped-firewall | [5m 19s](../../../jobs/5469/2026-09-03__10-30-01/network-scoped-firewall-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| config-sync | [12m 16s](../../../jobs/5469/2026-09-03__10-30-01/config-sync-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| scheduled-backup | [4m 04s](../../../jobs/5469/2026-09-03__10-30-01/scheduled-backup-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| internal-dns-resolution | [2m 59s](../../../jobs/5469/2026-09-03__10-30-01/internal-dns-resolution-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| **Average** | 5m 56s | — | — | — | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 742 ms across 10 clusters, about 0.24% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | [0.850](../../../jobs/5469/2026-09-03__10-30-01/shared-nfs-storage-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| centralized-log-collector | [0.900](../../../jobs/5469/2026-09-03__10-30-01/centralized-log-collector-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| ssh-controller-access | [0.900](../../../jobs/5469/2026-09-03__10-30-01/ssh-controller-access-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| internal-ca-tls | [0.750](../../../jobs/5469/2026-09-03__10-30-01/internal-ca-tls-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| internal-time-sync | [0.900](../../../jobs/5469/2026-09-03__10-30-01/internal-time-sync-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| load-balanced-web-tier | [0.900](../../../jobs/5469/2026-09-03__10-30-01/load-balanced-web-tier-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| network-scoped-firewall | [0.800](../../../jobs/5469/2026-09-03__10-30-01/network-scoped-firewall-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| config-sync | [0.700](../../../jobs/5469/2026-09-03__10-30-01/config-sync-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| scheduled-backup | [0.850](../../../jobs/5469/2026-09-03__10-30-01/scheduled-backup-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| internal-dns-resolution | [0.900](../../../jobs/5469/2026-09-03__10-30-01/internal-dns-resolution-bash-alpine-5469/analysis.md) | — | — | — | — | — | — | — |
| **Average** | 0.845 | — | — | — | — | — | — | — |
