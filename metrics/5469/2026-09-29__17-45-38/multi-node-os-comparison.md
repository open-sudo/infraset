# multi-node-os-comparison: command execution summary

Scope: `5469/2026-09-29__17-45-38`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [38/4](../../../jobs/5469/2026-09-29__17-45-38/shared-nfs-storage-bash-rhel7-5469) | — | — | — | — |
| centralized-log-collector | — | — | — | [24/10](../../../jobs/5469/2026-09-29__17-45-38/centralized-log-collector-bash-rhel7-5469) | — | — | — | — |
| ssh-controller-access | — | — | — | [29/6](../../../jobs/5469/2026-09-29__17-45-38/ssh-controller-access-bash-rhel7-5469) | — | — | — | — |
| internal-ca-tls | — | — | — | [27/2](../../../jobs/5469/2026-09-29__17-45-38/internal-ca-tls-bash-rhel7-5469) | — | — | — | — |
| internal-time-sync | — | — | — | [27/2](../../../jobs/5469/2026-09-29__17-45-38/internal-time-sync-bash-rhel7-5469) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [52/6](../../../jobs/5469/2026-09-29__17-45-38/load-balanced-web-tier-bash-rhel7-5469) | — | — | — | — |
| network-scoped-firewall | — | — | — | [42/6](../../../jobs/5469/2026-09-29__17-45-38/network-scoped-firewall-bash-rhel7-5469) | — | — | — | — |
| config-sync | — | — | — | [31/4](../../../jobs/5469/2026-09-29__17-45-38/config-sync-bash-rhel7-5469) | — | — | — | — |
| scheduled-backup | — | — | — | [25/4](../../../jobs/5469/2026-09-29__17-45-38/scheduled-backup-bash-rhel7-5469) | — | — | — | — |
| internal-dns-resolution | — | — | — | [37/4](../../../jobs/5469/2026-09-29__17-45-38/internal-dns-resolution-bash-rhel7-5469) | — | — | — | — |
| **Average** | — | — | — | 33.2/4.8 | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [11m 13s](../../../jobs/5469/2026-09-29__17-45-38/shared-nfs-storage-bash-rhel7-5469) | — | — | — | — |
| centralized-log-collector | — | — | — | [9m 07s](../../../jobs/5469/2026-09-29__17-45-38/centralized-log-collector-bash-rhel7-5469) | — | — | — | — |
| ssh-controller-access | — | — | — | [6m 04s](../../../jobs/5469/2026-09-29__17-45-38/ssh-controller-access-bash-rhel7-5469) | — | — | — | — |
| internal-ca-tls | — | — | — | [7m 20s](../../../jobs/5469/2026-09-29__17-45-38/internal-ca-tls-bash-rhel7-5469) | — | — | — | — |
| internal-time-sync | — | — | — | [6m 13s](../../../jobs/5469/2026-09-29__17-45-38/internal-time-sync-bash-rhel7-5469) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [13m 05s](../../../jobs/5469/2026-09-29__17-45-38/load-balanced-web-tier-bash-rhel7-5469) | — | — | — | — |
| network-scoped-firewall | — | — | — | [7m 28s](../../../jobs/5469/2026-09-29__17-45-38/network-scoped-firewall-bash-rhel7-5469) | — | — | — | — |
| config-sync | — | — | — | [11m 43s](../../../jobs/5469/2026-09-29__17-45-38/config-sync-bash-rhel7-5469) | — | — | — | — |
| scheduled-backup | — | — | — | [7m 13s](../../../jobs/5469/2026-09-29__17-45-38/scheduled-backup-bash-rhel7-5469) | — | — | — | — |
| internal-dns-resolution | — | — | — | [11m 05s](../../../jobs/5469/2026-09-29__17-45-38/internal-dns-resolution-bash-rhel7-5469) | — | — | — | — |
| **Average** | — | — | — | 9m 03s | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 1054 ms across 10 clusters, about 0.21% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [0.750](../../../jobs/5469/2026-09-29__17-45-38/shared-nfs-storage-bash-rhel7-5469) | — | — | — | — |
| centralized-log-collector | — | — | — | [0.850](../../../jobs/5469/2026-09-29__17-45-38/centralized-log-collector-bash-rhel7-5469) | — | — | — | — |
| ssh-controller-access | — | — | — | [0.850](../../../jobs/5469/2026-09-29__17-45-38/ssh-controller-access-bash-rhel7-5469) | — | — | — | — |
| internal-ca-tls | — | — | — | [0.900](../../../jobs/5469/2026-09-29__17-45-38/internal-ca-tls-bash-rhel7-5469) | — | — | — | — |
| internal-time-sync | — | — | — | [0.900](../../../jobs/5469/2026-09-29__17-45-38/internal-time-sync-bash-rhel7-5469) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [0.900](../../../jobs/5469/2026-09-29__17-45-38/load-balanced-web-tier-bash-rhel7-5469) | — | — | — | — |
| network-scoped-firewall | — | — | — | [0.850](../../../jobs/5469/2026-09-29__17-45-38/network-scoped-firewall-bash-rhel7-5469) | — | — | — | — |
| config-sync | — | — | — | [0.800](../../../jobs/5469/2026-09-29__17-45-38/config-sync-bash-rhel7-5469) | — | — | — | — |
| scheduled-backup | — | — | — | [0.650](../../../jobs/5469/2026-09-29__17-45-38/scheduled-backup-bash-rhel7-5469) | — | — | — | — |
| internal-dns-resolution | — | — | — | [0.820](../../../jobs/5469/2026-09-29__17-45-38/internal-dns-resolution-bash-rhel7-5469) | — | — | — | — |
| **Average** | — | — | — | 0.827 | — | — | — | — |
