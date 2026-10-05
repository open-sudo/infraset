# multi-node-os-comparison: command execution summary

Scope: `5469/2026-09-03__11-57-11`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | [29/3](../../../jobs/5469/2026-09-03__11-57-11/shared-nfs-storage-bash-rhel9-5469/analysis.md) | — | — | — |
| centralized-log-collector | — | — | — | — | [24/1](../../../jobs/5469/2026-09-03__11-57-11/centralized-log-collector-bash-rhel9-5469/analysis.md) | — | — | — |
| ssh-controller-access | — | — | — | — | [24/0](../../../jobs/5469/2026-09-03__11-57-11/ssh-controller-access-bash-rhel9-5469/analysis.md) | — | — | — |
| internal-ca-tls | — | — | — | — | [34/3](../../../jobs/5469/2026-09-03__11-57-11/internal-ca-tls-bash-rhel9-5469/analysis.md) | — | — | — |
| internal-time-sync | — | — | — | — | [27/1](../../../jobs/5469/2026-09-03__11-57-11/internal-time-sync-bash-rhel9-5469/analysis.md) | — | — | — |
| load-balanced-web-tier | — | — | — | — | [32/3](../../../jobs/5469/2026-09-03__11-57-11/load-balanced-web-tier-bash-rhel9-5469/analysis.md) | — | — | — |
| network-scoped-firewall | — | — | — | — | [27/1](../../../jobs/5469/2026-09-03__11-57-11/network-scoped-firewall-bash-rhel9-5469/analysis.md) | — | — | — |
| config-sync | — | — | — | — | [28/2](../../../jobs/5469/2026-09-03__11-57-11/config-sync-bash-rhel9-5469/analysis.md) | — | — | — |
| scheduled-backup | — | — | — | — | [27/3](../../../jobs/5469/2026-09-03__11-57-11/scheduled-backup-bash-rhel9-5469/analysis.md) | — | — | — |
| internal-dns-resolution | — | — | — | — | [29/0](../../../jobs/5469/2026-09-03__11-57-11/internal-dns-resolution-bash-rhel9-5469/analysis.md) | — | — | — |
| **Average** | — | — | — | — | 28.1/1.7 | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | [3m 48s](../../../jobs/5469/2026-09-03__11-57-11/shared-nfs-storage-bash-rhel9-5469/analysis.md) | — | — | — |
| centralized-log-collector | — | — | — | — | [5m 02s](../../../jobs/5469/2026-09-03__11-57-11/centralized-log-collector-bash-rhel9-5469/analysis.md) | — | — | — |
| ssh-controller-access | — | — | — | — | [3m 54s](../../../jobs/5469/2026-09-03__11-57-11/ssh-controller-access-bash-rhel9-5469/analysis.md) | — | — | — |
| internal-ca-tls | — | — | — | — | [5m 52s](../../../jobs/5469/2026-09-03__11-57-11/internal-ca-tls-bash-rhel9-5469/analysis.md) | — | — | — |
| internal-time-sync | — | — | — | — | [5m 06s](../../../jobs/5469/2026-09-03__11-57-11/internal-time-sync-bash-rhel9-5469/analysis.md) | — | — | — |
| load-balanced-web-tier | — | — | — | — | [4m 43s](../../../jobs/5469/2026-09-03__11-57-11/load-balanced-web-tier-bash-rhel9-5469/analysis.md) | — | — | — |
| network-scoped-firewall | — | — | — | — | [4m 46s](../../../jobs/5469/2026-09-03__11-57-11/network-scoped-firewall-bash-rhel9-5469/analysis.md) | — | — | — |
| config-sync | — | — | — | — | [9m 53s](../../../jobs/5469/2026-09-03__11-57-11/config-sync-bash-rhel9-5469/analysis.md) | — | — | — |
| scheduled-backup | — | — | — | — | [4m 20s](../../../jobs/5469/2026-09-03__11-57-11/scheduled-backup-bash-rhel9-5469/analysis.md) | — | — | — |
| internal-dns-resolution | — | — | — | — | [5m 04s](../../../jobs/5469/2026-09-03__11-57-11/internal-dns-resolution-bash-rhel9-5469/analysis.md) | — | — | — |
| **Average** | — | — | — | — | 5m 15s | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 884 ms across 10 clusters, about 0.34% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | [0.880](../../../jobs/5469/2026-09-03__11-57-11/shared-nfs-storage-bash-rhel9-5469/analysis.md) | — | — | — |
| centralized-log-collector | — | — | — | — | [0.920](../../../jobs/5469/2026-09-03__11-57-11/centralized-log-collector-bash-rhel9-5469/analysis.md) | — | — | — |
| ssh-controller-access | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__11-57-11/ssh-controller-access-bash-rhel9-5469/analysis.md) | — | — | — |
| internal-ca-tls | — | — | — | — | [0.650](../../../jobs/5469/2026-09-03__11-57-11/internal-ca-tls-bash-rhel9-5469/analysis.md) | — | — | — |
| internal-time-sync | — | — | — | — | [0.900](../../../jobs/5469/2026-09-03__11-57-11/internal-time-sync-bash-rhel9-5469/analysis.md) | — | — | — |
| load-balanced-web-tier | — | — | — | — | [0.850](../../../jobs/5469/2026-09-03__11-57-11/load-balanced-web-tier-bash-rhel9-5469/analysis.md) | — | — | — |
| network-scoped-firewall | — | — | — | — | [0.750](../../../jobs/5469/2026-09-03__11-57-11/network-scoped-firewall-bash-rhel9-5469/analysis.md) | — | — | — |
| config-sync | — | — | — | — | [0.900](../../../jobs/5469/2026-09-03__11-57-11/config-sync-bash-rhel9-5469/analysis.md) | — | — | — |
| scheduled-backup | — | — | — | — | [0.600](../../../jobs/5469/2026-09-03__11-57-11/scheduled-backup-bash-rhel9-5469/analysis.md) | — | — | — |
| internal-dns-resolution | — | — | — | — | [0.900](../../../jobs/5469/2026-09-03__11-57-11/internal-dns-resolution-bash-rhel9-5469/analysis.md) | — | — | — |
| **Average** | — | — | — | — | 0.830 | — | — | — |
