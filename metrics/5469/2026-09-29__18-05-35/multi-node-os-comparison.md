# multi-node-os-comparison: command execution summary

Scope: `5469/2026-09-29__18-05-35`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [22/4](../../../jobs/5469/2026-09-29__18-05-35/shared-nfs-storage-bash-rhel7-5469) | — | — | — | — |
| centralized-log-collector | — | — | — | [15/4](../../../jobs/5469/2026-09-29__18-05-35/centralized-log-collector-bash-rhel7-5469) | — | — | — | — |
| ssh-controller-access | — | — | — | [16/2](../../../jobs/5469/2026-09-29__18-05-35/ssh-controller-access-bash-rhel7-5469) | — | — | — | — |
| internal-ca-tls | — | — | — | [27/8](../../../jobs/5469/2026-09-29__18-05-35/internal-ca-tls-bash-rhel7-5469) | — | — | — | — |
| internal-time-sync | — | — | — | [13/2](../../../jobs/5469/2026-09-29__18-05-35/internal-time-sync-bash-rhel7-5469) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [29/7](../../../jobs/5469/2026-09-29__18-05-35/load-balanced-web-tier-bash-rhel7-5469) | — | — | — | — |
| network-scoped-firewall | — | — | — | [32/4](../../../jobs/5469/2026-09-29__18-05-35/network-scoped-firewall-bash-rhel7-5469) | — | — | — | — |
| config-sync | — | — | — | [33/3](../../../jobs/5469/2026-09-29__18-05-35/config-sync-bash-rhel7-5469) | — | — | — | — |
| scheduled-backup | — | — | — | [19/1](../../../jobs/5469/2026-09-29__18-05-35/scheduled-backup-bash-rhel7-5469) | — | — | — | — |
| internal-dns-resolution | — | — | — | [17/8](../../../jobs/5469/2026-09-29__18-05-35/internal-dns-resolution-bash-rhel7-5469) | — | — | — | — |
| **Average** | — | — | — | 22.3/4.3 | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [8m 15s](../../../jobs/5469/2026-09-29__18-05-35/shared-nfs-storage-bash-rhel7-5469) | — | — | — | — |
| centralized-log-collector | — | — | — | [6m 03s](../../../jobs/5469/2026-09-29__18-05-35/centralized-log-collector-bash-rhel7-5469) | — | — | — | — |
| ssh-controller-access | — | — | — | [5m 38s](../../../jobs/5469/2026-09-29__18-05-35/ssh-controller-access-bash-rhel7-5469) | — | — | — | — |
| internal-ca-tls | — | — | — | [14m 37s](../../../jobs/5469/2026-09-29__18-05-35/internal-ca-tls-bash-rhel7-5469) | — | — | — | — |
| internal-time-sync | — | — | — | [5m 36s](../../../jobs/5469/2026-09-29__18-05-35/internal-time-sync-bash-rhel7-5469) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [8m 59s](../../../jobs/5469/2026-09-29__18-05-35/load-balanced-web-tier-bash-rhel7-5469) | — | — | — | — |
| network-scoped-firewall | — | — | — | [7m 54s](../../../jobs/5469/2026-09-29__18-05-35/network-scoped-firewall-bash-rhel7-5469) | — | — | — | — |
| config-sync | — | — | — | [16m 22s](../../../jobs/5469/2026-09-29__18-05-35/config-sync-bash-rhel7-5469) | — | — | — | — |
| scheduled-backup | — | — | — | [5m 14s](../../../jobs/5469/2026-09-29__18-05-35/scheduled-backup-bash-rhel7-5469) | — | — | — | — |
| internal-dns-resolution | — | — | — | [8m 28s](../../../jobs/5469/2026-09-29__18-05-35/internal-dns-resolution-bash-rhel7-5469) | — | — | — | — |
| **Average** | — | — | — | 8m 43s | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 779 ms across 10 clusters, about 0.21% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [0.700](../../../jobs/5469/2026-09-29__18-05-35/shared-nfs-storage-bash-rhel7-5469) | — | — | — | — |
| centralized-log-collector | — | — | — | [0.900](../../../jobs/5469/2026-09-29__18-05-35/centralized-log-collector-bash-rhel7-5469) | — | — | — | — |
| ssh-controller-access | — | — | — | [0.800](../../../jobs/5469/2026-09-29__18-05-35/ssh-controller-access-bash-rhel7-5469) | — | — | — | — |
| internal-ca-tls | — | — | — | [0.780](../../../jobs/5469/2026-09-29__18-05-35/internal-ca-tls-bash-rhel7-5469) | — | — | — | — |
| internal-time-sync | — | — | — | [0.900](../../../jobs/5469/2026-09-29__18-05-35/internal-time-sync-bash-rhel7-5469) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [0.900](../../../jobs/5469/2026-09-29__18-05-35/load-balanced-web-tier-bash-rhel7-5469) | — | — | — | — |
| network-scoped-firewall | — | — | — | [0.800](../../../jobs/5469/2026-09-29__18-05-35/network-scoped-firewall-bash-rhel7-5469) | — | — | — | — |
| config-sync | — | — | — | [0.850](../../../jobs/5469/2026-09-29__18-05-35/config-sync-bash-rhel7-5469) | — | — | — | — |
| scheduled-backup | — | — | — | [0.950](../../../jobs/5469/2026-09-29__18-05-35/scheduled-backup-bash-rhel7-5469) | — | — | — | — |
| internal-dns-resolution | — | — | — | [0.850](../../../jobs/5469/2026-09-29__18-05-35/internal-dns-resolution-bash-rhel7-5469) | — | — | — | — |
| **Average** | — | — | — | 0.843 | — | — | — | — |
