# multi-node-os-comparison: command execution summary

Scope: `5469/2026-09-29__19-46-01`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [25/4](../../../jobs/5469/2026-09-29__19-46-01/shared-nfs-storage-bash-ubuntu24-5469) |
| centralized-log-collector | — | — | — | — | — | — | — | [32/0](../../../jobs/5469/2026-09-29__19-46-01/centralized-log-collector-bash-ubuntu24-5469) |
| ssh-controller-access | — | — | — | — | — | — | — | [31/7](../../../jobs/5469/2026-09-29__19-46-01/ssh-controller-access-bash-ubuntu24-5469) |
| internal-ca-tls | — | — | — | — | — | — | — | [30/1](../../../jobs/5469/2026-09-29__19-46-01/internal-ca-tls-bash-ubuntu24-5469) |
| internal-time-sync | — | — | — | — | — | — | — | [23/0](../../../jobs/5469/2026-09-29__19-46-01/internal-time-sync-bash-ubuntu24-5469) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [23/0](../../../jobs/5469/2026-09-29__19-46-01/load-balanced-web-tier-bash-ubuntu24-5469) |
| network-scoped-firewall | — | — | — | — | — | — | — | [29/3](../../../jobs/5469/2026-09-29__19-46-01/network-scoped-firewall-bash-ubuntu24-5469) |
| config-sync | — | — | — | — | — | — | — | [28/3](../../../jobs/5469/2026-09-29__19-46-01/config-sync-bash-ubuntu24-5469) |
| scheduled-backup | — | — | — | — | — | — | — | [29/2](../../../jobs/5469/2026-09-29__19-46-01/scheduled-backup-bash-ubuntu24-5469) |
| internal-dns-resolution | — | — | — | — | — | — | — | [26/1](../../../jobs/5469/2026-09-29__19-46-01/internal-dns-resolution-bash-ubuntu24-5469) |
| **Average** | — | — | — | — | — | — | — | 27.6/2.1 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [3m 14s](../../../jobs/5469/2026-09-29__19-46-01/shared-nfs-storage-bash-ubuntu24-5469) |
| centralized-log-collector | — | — | — | — | — | — | — | [4m 08s](../../../jobs/5469/2026-09-29__19-46-01/centralized-log-collector-bash-ubuntu24-5469) |
| ssh-controller-access | — | — | — | — | — | — | — | [4m 41s](../../../jobs/5469/2026-09-29__19-46-01/ssh-controller-access-bash-ubuntu24-5469) |
| internal-ca-tls | — | — | — | — | — | — | — | [3m 37s](../../../jobs/5469/2026-09-29__19-46-01/internal-ca-tls-bash-ubuntu24-5469) |
| internal-time-sync | — | — | — | — | — | — | — | [2m 59s](../../../jobs/5469/2026-09-29__19-46-01/internal-time-sync-bash-ubuntu24-5469) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [3m 56s](../../../jobs/5469/2026-09-29__19-46-01/load-balanced-web-tier-bash-ubuntu24-5469) |
| network-scoped-firewall | — | — | — | — | — | — | — | [3m 47s](../../../jobs/5469/2026-09-29__19-46-01/network-scoped-firewall-bash-ubuntu24-5469) |
| config-sync | — | — | — | — | — | — | — | [10m 15s](../../../jobs/5469/2026-09-29__19-46-01/config-sync-bash-ubuntu24-5469) |
| scheduled-backup | — | — | — | — | — | — | — | [4m 13s](../../../jobs/5469/2026-09-29__19-46-01/scheduled-backup-bash-ubuntu24-5469) |
| internal-dns-resolution | — | — | — | — | — | — | — | [3m 38s](../../../jobs/5469/2026-09-29__19-46-01/internal-dns-resolution-bash-ubuntu24-5469) |
| **Average** | — | — | — | — | — | — | — | 4m 27s |

Cluster provisioning is not a meaningful part of these times: median 1282 ms across 10 clusters, about 0.60% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-29__19-46-01/shared-nfs-storage-bash-ubuntu24-5469) |
| centralized-log-collector | — | — | — | — | — | — | — | [0.970](../../../jobs/5469/2026-09-29__19-46-01/centralized-log-collector-bash-ubuntu24-5469) |
| ssh-controller-access | — | — | — | — | — | — | — | [0.900](../../../jobs/5469/2026-09-29__19-46-01/ssh-controller-access-bash-ubuntu24-5469) |
| internal-ca-tls | — | — | — | — | — | — | — | [0.750](../../../jobs/5469/2026-09-29__19-46-01/internal-ca-tls-bash-ubuntu24-5469) |
| internal-time-sync | — | — | — | — | — | — | — | [0.900](../../../jobs/5469/2026-09-29__19-46-01/internal-time-sync-bash-ubuntu24-5469) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [0.970](../../../jobs/5469/2026-09-29__19-46-01/load-balanced-web-tier-bash-ubuntu24-5469) |
| network-scoped-firewall | — | — | — | — | — | — | — | [0.550](../../../jobs/5469/2026-09-29__19-46-01/network-scoped-firewall-bash-ubuntu24-5469) |
| config-sync | — | — | — | — | — | — | — | [0.880](../../../jobs/5469/2026-09-29__19-46-01/config-sync-bash-ubuntu24-5469) |
| scheduled-backup | — | — | — | — | — | — | — | [0.900](../../../jobs/5469/2026-09-29__19-46-01/scheduled-backup-bash-ubuntu24-5469) |
| internal-dns-resolution | — | — | — | — | — | — | — | [0.920](../../../jobs/5469/2026-09-29__19-46-01/internal-dns-resolution-bash-ubuntu24-5469) |
| **Average** | — | — | — | — | — | — | — | 0.869 |
