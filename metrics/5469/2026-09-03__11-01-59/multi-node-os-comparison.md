# multi-node-os-comparison: command execution summary

Scope: `5469/2026-09-03__11-01-59`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | [24/3](../../../jobs/5469/2026-09-03__11-01-59/shared-nfs-storage-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| centralized-log-collector | — | [30/2](../../../jobs/5469/2026-09-03__11-01-59/centralized-log-collector-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| ssh-controller-access | — | [28/0](../../../jobs/5469/2026-09-03__11-01-59/ssh-controller-access-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| internal-ca-tls | — | [25/1](../../../jobs/5469/2026-09-03__11-01-59/internal-ca-tls-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| internal-time-sync | — | [29/1](../../../jobs/5469/2026-09-03__11-01-59/internal-time-sync-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| load-balanced-web-tier | — | [36/1](../../../jobs/5469/2026-09-03__11-01-59/load-balanced-web-tier-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| network-scoped-firewall | — | [34/0](../../../jobs/5469/2026-09-03__11-01-59/network-scoped-firewall-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| config-sync | — | [42/3](../../../jobs/5469/2026-09-03__11-01-59/config-sync-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| scheduled-backup | — | [26/1](../../../jobs/5469/2026-09-03__11-01-59/scheduled-backup-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| internal-dns-resolution | — | [24/2](../../../jobs/5469/2026-09-03__11-01-59/internal-dns-resolution-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| **Average** | — | 29.8/1.4 | — | — | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | [5m 46s](../../../jobs/5469/2026-09-03__11-01-59/shared-nfs-storage-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| centralized-log-collector | — | [5m 34s](../../../jobs/5469/2026-09-03__11-01-59/centralized-log-collector-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| ssh-controller-access | — | [2m 44s](../../../jobs/5469/2026-09-03__11-01-59/ssh-controller-access-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| internal-ca-tls | — | [3m 42s](../../../jobs/5469/2026-09-03__11-01-59/internal-ca-tls-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| internal-time-sync | — | [4m 13s](../../../jobs/5469/2026-09-03__11-01-59/internal-time-sync-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| load-balanced-web-tier | — | [3m 58s](../../../jobs/5469/2026-09-03__11-01-59/load-balanced-web-tier-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| network-scoped-firewall | — | [4m 17s](../../../jobs/5469/2026-09-03__11-01-59/network-scoped-firewall-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| config-sync | — | [15m 46s](../../../jobs/5469/2026-09-03__11-01-59/config-sync-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| scheduled-backup | — | [3m 04s](../../../jobs/5469/2026-09-03__11-01-59/scheduled-backup-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| internal-dns-resolution | — | [5m 54s](../../../jobs/5469/2026-09-03__11-01-59/internal-dns-resolution-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| **Average** | — | 5m 30s | — | — | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 1000 ms across 10 clusters, about 0.37% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | [0.930](../../../jobs/5469/2026-09-03__11-01-59/shared-nfs-storage-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| centralized-log-collector | — | [0.850](../../../jobs/5469/2026-09-03__11-01-59/centralized-log-collector-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| ssh-controller-access | — | [0.820](../../../jobs/5469/2026-09-03__11-01-59/ssh-controller-access-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| internal-ca-tls | — | [0.970](../../../jobs/5469/2026-09-03__11-01-59/internal-ca-tls-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| internal-time-sync | — | [0.800](../../../jobs/5469/2026-09-03__11-01-59/internal-time-sync-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| load-balanced-web-tier | — | [0.820](../../../jobs/5469/2026-09-03__11-01-59/load-balanced-web-tier-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| network-scoped-firewall | — | [0.880](../../../jobs/5469/2026-09-03__11-01-59/network-scoped-firewall-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| config-sync | — | [0.850](../../../jobs/5469/2026-09-03__11-01-59/config-sync-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| scheduled-backup | — | [0.900](../../../jobs/5469/2026-09-03__11-01-59/scheduled-backup-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| internal-dns-resolution | — | [0.930](../../../jobs/5469/2026-09-03__11-01-59/internal-dns-resolution-bash-almalinux9-5469/analysis.md) | — | — | — | — | — | — |
| **Average** | — | 0.875 | — | — | — | — | — | — |
