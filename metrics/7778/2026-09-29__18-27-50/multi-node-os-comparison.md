# multi-node-os-comparison: command execution summary

Scope: `7778/2026-09-29__18-27-50`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [55/15](../../../jobs/7778/2026-09-29__18-27-50/shared-nfs-storage-ansible-rhel7-7778) | — | — | — | — |
| centralized-log-collector | — | — | — | [47/14](../../../jobs/7778/2026-09-29__18-27-50/centralized-log-collector-ansible-rhel7-7778) | — | — | — | — |
| ssh-controller-access | — | — | — | [42/9](../../../jobs/7778/2026-09-29__18-27-50/ssh-controller-access-ansible-rhel7-7778) | — | — | — | — |
| internal-ca-tls | — | — | — | [57/5](../../../jobs/7778/2026-09-29__18-27-50/internal-ca-tls-ansible-rhel7-7778) | — | — | — | — |
| internal-time-sync | — | — | — | [35/7](../../../jobs/7778/2026-09-29__18-27-50/internal-time-sync-ansible-rhel7-7778) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [51/6](../../../jobs/7778/2026-09-29__18-27-50/load-balanced-web-tier-ansible-rhel7-7778) | — | — | — | — |
| network-scoped-firewall | — | — | — | [77/14](../../../jobs/7778/2026-09-29__18-27-50/network-scoped-firewall-ansible-rhel7-7778) | — | — | — | — |
| config-sync | — | — | — | [48/4](../../../jobs/7778/2026-09-29__18-27-50/config-sync-ansible-rhel7-7778) | — | — | — | — |
| scheduled-backup | — | — | — | [31/9](../../../jobs/7778/2026-09-29__18-27-50/scheduled-backup-ansible-rhel7-7778) | — | — | — | — |
| internal-dns-resolution | — | — | — | [47/10](../../../jobs/7778/2026-09-29__18-27-50/internal-dns-resolution-ansible-rhel7-7778) | — | — | — | — |
| **Average** | — | — | — | 49.0/9.3 | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [20m 18s](../../../jobs/7778/2026-09-29__18-27-50/shared-nfs-storage-ansible-rhel7-7778) | — | — | — | — |
| centralized-log-collector | — | — | — | [15m 33s](../../../jobs/7778/2026-09-29__18-27-50/centralized-log-collector-ansible-rhel7-7778) | — | — | — | — |
| ssh-controller-access | — | — | — | [11m 50s](../../../jobs/7778/2026-09-29__18-27-50/ssh-controller-access-ansible-rhel7-7778) | — | — | — | — |
| internal-ca-tls | — | — | — | [9m 41s](../../../jobs/7778/2026-09-29__18-27-50/internal-ca-tls-ansible-rhel7-7778) | — | — | — | — |
| internal-time-sync | — | — | — | [9m 37s](../../../jobs/7778/2026-09-29__18-27-50/internal-time-sync-ansible-rhel7-7778) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [9m 11s](../../../jobs/7778/2026-09-29__18-27-50/load-balanced-web-tier-ansible-rhel7-7778) | — | — | — | — |
| network-scoped-firewall | — | — | — | [15m 59s](../../../jobs/7778/2026-09-29__18-27-50/network-scoped-firewall-ansible-rhel7-7778) | — | — | — | — |
| config-sync | — | — | — | [14m 36s](../../../jobs/7778/2026-09-29__18-27-50/config-sync-ansible-rhel7-7778) | — | — | — | — |
| scheduled-backup | — | — | — | [7m 52s](../../../jobs/7778/2026-09-29__18-27-50/scheduled-backup-ansible-rhel7-7778) | — | — | — | — |
| internal-dns-resolution | — | — | — | [11m 32s](../../../jobs/7778/2026-09-29__18-27-50/internal-dns-resolution-ansible-rhel7-7778) | — | — | — | — |
| **Average** | — | — | — | 12m 37s | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 1268 ms across 10 clusters, about 0.20% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [0.700](../../../jobs/7778/2026-09-29__18-27-50/shared-nfs-storage-ansible-rhel7-7778) | — | — | — | — |
| centralized-log-collector | — | — | — | [0.800](../../../jobs/7778/2026-09-29__18-27-50/centralized-log-collector-ansible-rhel7-7778) | — | — | — | — |
| ssh-controller-access | — | — | — | [0.750](../../../jobs/7778/2026-09-29__18-27-50/ssh-controller-access-ansible-rhel7-7778) | — | — | — | — |
| internal-ca-tls | — | — | — | [0.750](../../../jobs/7778/2026-09-29__18-27-50/internal-ca-tls-ansible-rhel7-7778) | — | — | — | — |
| internal-time-sync | — | — | — | [0.850](../../../jobs/7778/2026-09-29__18-27-50/internal-time-sync-ansible-rhel7-7778) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [0.930](../../../jobs/7778/2026-09-29__18-27-50/load-balanced-web-tier-ansible-rhel7-7778) | — | — | — | — |
| network-scoped-firewall | — | — | — | [0.750](../../../jobs/7778/2026-09-29__18-27-50/network-scoped-firewall-ansible-rhel7-7778) | — | — | — | — |
| config-sync | — | — | — | [0.650](../../../jobs/7778/2026-09-29__18-27-50/config-sync-ansible-rhel7-7778) | — | — | — | — |
| scheduled-backup | — | — | — | [0.650](../../../jobs/7778/2026-09-29__18-27-50/scheduled-backup-ansible-rhel7-7778) | — | — | — | — |
| internal-dns-resolution | — | — | — | [0.850](../../../jobs/7778/2026-09-29__18-27-50/internal-dns-resolution-ansible-rhel7-7778) | — | — | — | — |
| **Average** | — | — | — | 0.768 | — | — | — | — |
