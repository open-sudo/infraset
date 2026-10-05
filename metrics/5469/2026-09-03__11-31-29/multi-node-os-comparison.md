# multi-node-os-comparison: command execution summary

Scope: `5469/2026-09-03__11-31-29`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | [28/3](../../../jobs/5469/2026-09-03__11-31-29/shared-nfs-storage-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| centralized-log-collector | — | — | [38/7](../../../jobs/5469/2026-09-03__11-31-29/centralized-log-collector-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| ssh-controller-access | — | — | [18/4](../../../jobs/5469/2026-09-03__11-31-29/ssh-controller-access-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| internal-ca-tls | — | — | [28/3](../../../jobs/5469/2026-09-03__11-31-29/internal-ca-tls-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| internal-time-sync | — | — | [25/0](../../../jobs/5469/2026-09-03__11-31-29/internal-time-sync-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| load-balanced-web-tier | — | — | [42/3](../../../jobs/5469/2026-09-03__11-31-29/load-balanced-web-tier-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| network-scoped-firewall | — | — | [31/1](../../../jobs/5469/2026-09-03__11-31-29/network-scoped-firewall-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| config-sync | — | — | [24/3](../../../jobs/5469/2026-09-03__11-31-29/config-sync-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| scheduled-backup | — | — | [26/2](../../../jobs/5469/2026-09-03__11-31-29/scheduled-backup-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| internal-dns-resolution | — | — | [25/1](../../../jobs/5469/2026-09-03__11-31-29/internal-dns-resolution-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| **Average** | — | — | 28.5/2.7 | — | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | [3m 26s](../../../jobs/5469/2026-09-03__11-31-29/shared-nfs-storage-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| centralized-log-collector | — | — | [5m 05s](../../../jobs/5469/2026-09-03__11-31-29/centralized-log-collector-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| ssh-controller-access | — | — | [3m 16s](../../../jobs/5469/2026-09-03__11-31-29/ssh-controller-access-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| internal-ca-tls | — | — | [4m 06s](../../../jobs/5469/2026-09-03__11-31-29/internal-ca-tls-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| internal-time-sync | — | — | [3m 21s](../../../jobs/5469/2026-09-03__11-31-29/internal-time-sync-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| load-balanced-web-tier | — | — | [5m 06s](../../../jobs/5469/2026-09-03__11-31-29/load-balanced-web-tier-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| network-scoped-firewall | — | — | [4m 41s](../../../jobs/5469/2026-09-03__11-31-29/network-scoped-firewall-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| config-sync | — | — | [10m 39s](../../../jobs/5469/2026-09-03__11-31-29/config-sync-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| scheduled-backup | — | — | [3m 53s](../../../jobs/5469/2026-09-03__11-31-29/scheduled-backup-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| internal-dns-resolution | — | — | [3m 06s](../../../jobs/5469/2026-09-03__11-31-29/internal-dns-resolution-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| **Average** | — | — | 4m 40s | — | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 1534 ms across 10 clusters, about 0.64% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | [0.820](../../../jobs/5469/2026-09-03__11-31-29/shared-nfs-storage-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| centralized-log-collector | — | — | [0.850](../../../jobs/5469/2026-09-03__11-31-29/centralized-log-collector-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| ssh-controller-access | — | — | [0.920](../../../jobs/5469/2026-09-03__11-31-29/ssh-controller-access-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| internal-ca-tls | — | — | [0.900](../../../jobs/5469/2026-09-03__11-31-29/internal-ca-tls-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| internal-time-sync | — | — | [0.850](../../../jobs/5469/2026-09-03__11-31-29/internal-time-sync-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| load-balanced-web-tier | — | — | [0.900](../../../jobs/5469/2026-09-03__11-31-29/load-balanced-web-tier-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| network-scoped-firewall | — | — | [0.850](../../../jobs/5469/2026-09-03__11-31-29/network-scoped-firewall-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| config-sync | — | — | [0.900](../../../jobs/5469/2026-09-03__11-31-29/config-sync-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| scheduled-backup | — | — | [0.930](../../../jobs/5469/2026-09-03__11-31-29/scheduled-backup-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| internal-dns-resolution | — | — | [0.930](../../../jobs/5469/2026-09-03__11-31-29/internal-dns-resolution-bash-centos-stream10-5469/analysis.md) | — | — | — | — | — |
| **Average** | — | — | 0.885 | — | — | — | — | — |
