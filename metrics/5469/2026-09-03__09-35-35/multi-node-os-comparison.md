# multi-node-os-comparison: command execution summary

Scope: `5469/2026-09-03__09-35-35`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [26/3](../../../jobs/5469/2026-09-03__09-35-35/shared-nfs-storage-bash-ubuntu24-5469/analysis.md) |
| centralized-log-collector | — | — | — | — | — | — | — | [22/5](../../../jobs/5469/2026-09-03__09-35-35/centralized-log-collector-bash-ubuntu24-5469/analysis.md) |
| ssh-controller-access | — | — | — | — | — | — | — | [29/10](../../../jobs/5469/2026-09-03__09-35-35/ssh-controller-access-bash-ubuntu24-5469/analysis.md) |
| internal-ca-tls | — | — | — | — | — | — | — | [34/1](../../../jobs/5469/2026-09-03__09-35-35/internal-ca-tls-bash-ubuntu24-5469/analysis.md) |
| internal-time-sync | — | — | — | — | — | — | — | [24/0](../../../jobs/5469/2026-09-03__09-35-35/internal-time-sync-bash-ubuntu24-5469/analysis.md) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [25/0](../../../jobs/5469/2026-09-03__09-35-35/load-balanced-web-tier-bash-ubuntu24-5469/analysis.md) |
| network-scoped-firewall | — | — | — | — | — | — | — | [31/1](../../../jobs/5469/2026-09-03__09-35-35/network-scoped-firewall-bash-ubuntu24-5469/analysis.md) |
| config-sync | — | — | — | — | — | — | — | [30/9](../../../jobs/5469/2026-09-03__09-35-35/config-sync-bash-ubuntu24-5469/analysis.md) |
| scheduled-backup | — | — | — | — | — | — | — | [32/3](../../../jobs/5469/2026-09-03__09-35-35/scheduled-backup-bash-ubuntu24-5469/analysis.md) |
| internal-dns-resolution | — | — | — | — | — | — | — | [23/1](../../../jobs/5469/2026-09-03__09-35-35/internal-dns-resolution-bash-ubuntu24-5469/analysis.md) |
| **Average** | — | — | — | — | — | — | — | 27.6/3.3 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [3m 16s](../../../jobs/5469/2026-09-03__09-35-35/shared-nfs-storage-bash-ubuntu24-5469/analysis.md) |
| centralized-log-collector | — | — | — | — | — | — | — | [4m 23s](../../../jobs/5469/2026-09-03__09-35-35/centralized-log-collector-bash-ubuntu24-5469/analysis.md) |
| ssh-controller-access | — | — | — | — | — | — | — | [4m 33s](../../../jobs/5469/2026-09-03__09-35-35/ssh-controller-access-bash-ubuntu24-5469/analysis.md) |
| internal-ca-tls | — | — | — | — | — | — | — | [4m 30s](../../../jobs/5469/2026-09-03__09-35-35/internal-ca-tls-bash-ubuntu24-5469/analysis.md) |
| internal-time-sync | — | — | — | — | — | — | — | [3m 40s](../../../jobs/5469/2026-09-03__09-35-35/internal-time-sync-bash-ubuntu24-5469/analysis.md) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [3m 00s](../../../jobs/5469/2026-09-03__09-35-35/load-balanced-web-tier-bash-ubuntu24-5469/analysis.md) |
| network-scoped-firewall | — | — | — | — | — | — | — | [3m 28s](../../../jobs/5469/2026-09-03__09-35-35/network-scoped-firewall-bash-ubuntu24-5469/analysis.md) |
| config-sync | — | — | — | — | — | — | — | [12m 04s](../../../jobs/5469/2026-09-03__09-35-35/config-sync-bash-ubuntu24-5469/analysis.md) |
| scheduled-backup | — | — | — | — | — | — | — | [5m 31s](../../../jobs/5469/2026-09-03__09-35-35/scheduled-backup-bash-ubuntu24-5469/analysis.md) |
| internal-dns-resolution | — | — | — | — | — | — | — | [3m 19s](../../../jobs/5469/2026-09-03__09-35-35/internal-dns-resolution-bash-ubuntu24-5469/analysis.md) |
| **Average** | — | — | — | — | — | — | — | 4m 46s |

Cluster provisioning is not a meaningful part of these times: median 878 ms across 10 clusters, about 0.36% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [0.850](../../../jobs/5469/2026-09-03__09-35-35/shared-nfs-storage-bash-ubuntu24-5469/analysis.md) |
| centralized-log-collector | — | — | — | — | — | — | — | [0.850](../../../jobs/5469/2026-09-03__09-35-35/centralized-log-collector-bash-ubuntu24-5469/analysis.md) |
| ssh-controller-access | — | — | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__09-35-35/ssh-controller-access-bash-ubuntu24-5469/analysis.md) |
| internal-ca-tls | — | — | — | — | — | — | — | [0.900](../../../jobs/5469/2026-09-03__09-35-35/internal-ca-tls-bash-ubuntu24-5469/analysis.md) |
| internal-time-sync | — | — | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__09-35-35/internal-time-sync-bash-ubuntu24-5469/analysis.md) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__09-35-35/load-balanced-web-tier-bash-ubuntu24-5469/analysis.md) |
| network-scoped-firewall | — | — | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__09-35-35/network-scoped-firewall-bash-ubuntu24-5469/analysis.md) |
| config-sync | — | — | — | — | — | — | — | [0.820](../../../jobs/5469/2026-09-03__09-35-35/config-sync-bash-ubuntu24-5469/analysis.md) |
| scheduled-backup | — | — | — | — | — | — | — | [0.850](../../../jobs/5469/2026-09-03__09-35-35/scheduled-backup-bash-ubuntu24-5469/analysis.md) |
| internal-dns-resolution | — | — | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__09-35-35/internal-dns-resolution-bash-ubuntu24-5469/analysis.md) |
| **Average** | — | — | — | — | — | — | — | 0.902 |
