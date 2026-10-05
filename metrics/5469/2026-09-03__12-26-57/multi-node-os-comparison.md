# multi-node-os-comparison: command execution summary

Scope: `5469/2026-09-03__12-26-57`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [26/8](../../../jobs/5469/2026-09-03__12-26-57/shared-nfs-storage-bash-rhel7-5469/analysis.md) | — | — | — | — |
| centralized-log-collector | — | — | — | [29/4](../../../jobs/5469/2026-09-03__12-26-57/centralized-log-collector-bash-rhel7-5469/analysis.md) | — | — | — | — |
| ssh-controller-access | — | — | — | [32/3](../../../jobs/5469/2026-09-03__12-26-57/ssh-controller-access-bash-rhel7-5469/analysis.md) | — | — | — | — |
| internal-ca-tls | — | — | — | [33/6](../../../jobs/5469/2026-09-03__12-26-57/internal-ca-tls-bash-rhel7-5469/analysis.md) | — | — | — | — |
| internal-time-sync | — | — | — | [18/1](../../../jobs/5469/2026-09-03__12-26-57/internal-time-sync-bash-rhel7-5469/analysis.md) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [32/1](../../../jobs/5469/2026-09-03__12-26-57/load-balanced-web-tier-bash-rhel7-5469/analysis.md) | — | — | — | — |
| network-scoped-firewall | — | — | — | [34/7](../../../jobs/5469/2026-09-03__12-26-57/network-scoped-firewall-bash-rhel7-5469/analysis.md) | — | — | — | — |
| config-sync | — | — | — | [35/0](../../../jobs/5469/2026-09-03__12-26-57/config-sync-bash-rhel7-5469/analysis.md) | — | — | — | — |
| scheduled-backup | — | — | — | [22/1](../../../jobs/5469/2026-09-03__12-26-57/scheduled-backup-bash-rhel7-5469/analysis.md) | — | — | — | — |
| internal-dns-resolution | — | — | — | [26/6](../../../jobs/5469/2026-09-03__12-26-57/internal-dns-resolution-bash-rhel7-5469/analysis.md) | — | — | — | — |
| **Average** | — | — | — | 28.7/3.7 | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [8m 59s](../../../jobs/5469/2026-09-03__12-26-57/shared-nfs-storage-bash-rhel7-5469/analysis.md) | — | — | — | — |
| centralized-log-collector | — | — | — | [7m 15s](../../../jobs/5469/2026-09-03__12-26-57/centralized-log-collector-bash-rhel7-5469/analysis.md) | — | — | — | — |
| ssh-controller-access | — | — | — | [6m 27s](../../../jobs/5469/2026-09-03__12-26-57/ssh-controller-access-bash-rhel7-5469/analysis.md) | — | — | — | — |
| internal-ca-tls | — | — | — | [6m 38s](../../../jobs/5469/2026-09-03__12-26-57/internal-ca-tls-bash-rhel7-5469/analysis.md) | — | — | — | — |
| internal-time-sync | — | — | — | [5m 10s](../../../jobs/5469/2026-09-03__12-26-57/internal-time-sync-bash-rhel7-5469/analysis.md) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [5m 35s](../../../jobs/5469/2026-09-03__12-26-57/load-balanced-web-tier-bash-rhel7-5469/analysis.md) | — | — | — | — |
| network-scoped-firewall | — | — | — | [11m 26s](../../../jobs/5469/2026-09-03__12-26-57/network-scoped-firewall-bash-rhel7-5469/analysis.md) | — | — | — | — |
| config-sync | — | — | — | [15m 04s](../../../jobs/5469/2026-09-03__12-26-57/config-sync-bash-rhel7-5469/analysis.md) | — | — | — | — |
| scheduled-backup | — | — | — | [5m 34s](../../../jobs/5469/2026-09-03__12-26-57/scheduled-backup-bash-rhel7-5469/analysis.md) | — | — | — | — |
| internal-dns-resolution | — | — | — | [10m 21s](../../../jobs/5469/2026-09-03__12-26-57/internal-dns-resolution-bash-rhel7-5469/analysis.md) | — | — | — | — |
| **Average** | — | — | — | 8m 15s | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 692 ms across 10 clusters, about 0.16% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [0.850](../../../jobs/5469/2026-09-03__12-26-57/shared-nfs-storage-bash-rhel7-5469/analysis.md) | — | — | — | — |
| centralized-log-collector | — | — | — | [0.900](../../../jobs/5469/2026-09-03__12-26-57/centralized-log-collector-bash-rhel7-5469/analysis.md) | — | — | — | — |
| ssh-controller-access | — | — | — | [0.900](../../../jobs/5469/2026-09-03__12-26-57/ssh-controller-access-bash-rhel7-5469/analysis.md) | — | — | — | — |
| internal-ca-tls | — | — | — | [0.900](../../../jobs/5469/2026-09-03__12-26-57/internal-ca-tls-bash-rhel7-5469/analysis.md) | — | — | — | — |
| internal-time-sync | — | — | — | [0.900](../../../jobs/5469/2026-09-03__12-26-57/internal-time-sync-bash-rhel7-5469/analysis.md) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [0.950](../../../jobs/5469/2026-09-03__12-26-57/load-balanced-web-tier-bash-rhel7-5469/analysis.md) | — | — | — | — |
| network-scoped-firewall | — | — | — | [0.800](../../../jobs/5469/2026-09-03__12-26-57/network-scoped-firewall-bash-rhel7-5469/analysis.md) | — | — | — | — |
| config-sync | — | — | — | [0.850](../../../jobs/5469/2026-09-03__12-26-57/config-sync-bash-rhel7-5469/analysis.md) | — | — | — | — |
| scheduled-backup | — | — | — | [0.900](../../../jobs/5469/2026-09-03__12-26-57/scheduled-backup-bash-rhel7-5469/analysis.md) | — | — | — | — |
| internal-dns-resolution | — | — | — | [0.600](../../../jobs/5469/2026-09-03__12-26-57/internal-dns-resolution-bash-rhel7-5469/analysis.md) | — | — | — | — |
| **Average** | — | — | — | 0.855 | — | — | — | — |
