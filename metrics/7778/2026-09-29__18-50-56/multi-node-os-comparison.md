# multi-node-os-comparison: command execution summary

Scope: `7778/2026-09-29__18-50-56`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [43/7](../../../jobs/7778/2026-09-29__18-50-56/shared-nfs-storage-ansible-ubuntu24-7778) |
| centralized-log-collector | — | — | — | — | — | — | — | [47/5](../../../jobs/7778/2026-09-29__18-50-56/centralized-log-collector-ansible-ubuntu24-7778) |
| ssh-controller-access | — | — | — | — | — | — | — | [31/1](../../../jobs/7778/2026-09-29__18-50-56/ssh-controller-access-ansible-ubuntu24-7778) |
| internal-ca-tls | — | — | — | — | — | — | — | [34/3](../../../jobs/7778/2026-09-29__18-50-56/internal-ca-tls-ansible-ubuntu24-7778) |
| internal-time-sync | — | — | — | — | — | — | — | [34/8](../../../jobs/7778/2026-09-29__18-50-56/internal-time-sync-ansible-ubuntu24-7778) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [46/6](../../../jobs/7778/2026-09-29__18-50-56/load-balanced-web-tier-ansible-ubuntu24-7778) |
| network-scoped-firewall | — | — | — | — | — | — | — | [44/4](../../../jobs/7778/2026-09-29__18-50-56/network-scoped-firewall-ansible-ubuntu24-7778) |
| config-sync | — | — | — | — | — | — | — | [46/6](../../../jobs/7778/2026-09-29__18-50-56/config-sync-ansible-ubuntu24-7778) |
| scheduled-backup | — | — | — | — | — | — | — | [49/8](../../../jobs/7778/2026-09-29__18-50-56/scheduled-backup-ansible-ubuntu24-7778) |
| internal-dns-resolution | — | — | — | — | — | — | — | [40/12](../../../jobs/7778/2026-09-29__18-50-56/internal-dns-resolution-ansible-ubuntu24-7778) |
| **Average** | — | — | — | — | — | — | — | 41.4/6.0 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [5m 07s](../../../jobs/7778/2026-09-29__18-50-56/shared-nfs-storage-ansible-ubuntu24-7778) |
| centralized-log-collector | — | — | — | — | — | — | — | [7m 18s](../../../jobs/7778/2026-09-29__18-50-56/centralized-log-collector-ansible-ubuntu24-7778) |
| ssh-controller-access | — | — | — | — | — | — | — | [6m 20s](../../../jobs/7778/2026-09-29__18-50-56/ssh-controller-access-ansible-ubuntu24-7778) |
| internal-ca-tls | — | — | — | — | — | — | — | [6m 23s](../../../jobs/7778/2026-09-29__18-50-56/internal-ca-tls-ansible-ubuntu24-7778) |
| internal-time-sync | — | — | — | — | — | — | — | [4m 13s](../../../jobs/7778/2026-09-29__18-50-56/internal-time-sync-ansible-ubuntu24-7778) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [6m 20s](../../../jobs/7778/2026-09-29__18-50-56/load-balanced-web-tier-ansible-ubuntu24-7778) |
| network-scoped-firewall | — | — | — | — | — | — | — | [4m 55s](../../../jobs/7778/2026-09-29__18-50-56/network-scoped-firewall-ansible-ubuntu24-7778) |
| config-sync | — | — | — | — | — | — | — | [11m 28s](../../../jobs/7778/2026-09-29__18-50-56/config-sync-ansible-ubuntu24-7778) |
| scheduled-backup | — | — | — | — | — | — | — | [6m 21s](../../../jobs/7778/2026-09-29__18-50-56/scheduled-backup-ansible-ubuntu24-7778) |
| internal-dns-resolution | — | — | — | — | — | — | — | [6m 05s](../../../jobs/7778/2026-09-29__18-50-56/internal-dns-resolution-ansible-ubuntu24-7778) |
| **Average** | — | — | — | — | — | — | — | 6m 27s |

Cluster provisioning is not a meaningful part of these times: median 1404 ms across 10 clusters, about 0.38% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [0.850](../../../jobs/7778/2026-09-29__18-50-56/shared-nfs-storage-ansible-ubuntu24-7778) |
| centralized-log-collector | — | — | — | — | — | — | — | [0.850](../../../jobs/7778/2026-09-29__18-50-56/centralized-log-collector-ansible-ubuntu24-7778) |
| ssh-controller-access | — | — | — | — | — | — | — | [0.950](../../../jobs/7778/2026-09-29__18-50-56/ssh-controller-access-ansible-ubuntu24-7778) |
| internal-ca-tls | — | — | — | — | — | — | — | [0.900](../../../jobs/7778/2026-09-29__18-50-56/internal-ca-tls-ansible-ubuntu24-7778) |
| internal-time-sync | — | — | — | — | — | — | — | [0.950](../../../jobs/7778/2026-09-29__18-50-56/internal-time-sync-ansible-ubuntu24-7778) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [0.850](../../../jobs/7778/2026-09-29__18-50-56/load-balanced-web-tier-ansible-ubuntu24-7778) |
| network-scoped-firewall | — | — | — | — | — | — | — | [0.850](../../../jobs/7778/2026-09-29__18-50-56/network-scoped-firewall-ansible-ubuntu24-7778) |
| config-sync | — | — | — | — | — | — | — | [0.920](../../../jobs/7778/2026-09-29__18-50-56/config-sync-ansible-ubuntu24-7778) |
| scheduled-backup | — | — | — | — | — | — | — | [0.920](../../../jobs/7778/2026-09-29__18-50-56/scheduled-backup-ansible-ubuntu24-7778) |
| internal-dns-resolution | — | — | — | — | — | — | — | [0.900](../../../jobs/7778/2026-09-29__18-50-56/internal-dns-resolution-ansible-ubuntu24-7778) |
| **Average** | — | — | — | — | — | — | — | 0.894 |
