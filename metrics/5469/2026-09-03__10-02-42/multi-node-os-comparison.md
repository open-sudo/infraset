# multi-node-os-comparison: command execution summary

Scope: `5469/2026-09-03__10-02-42`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | [41/5](../../../jobs/5469/2026-09-03__10-02-42/shared-nfs-storage-bash-ubuntu16-5469/analysis.md) | — |
| centralized-log-collector | — | — | — | — | — | — | [28/4](../../../jobs/5469/2026-09-03__10-02-42/centralized-log-collector-bash-ubuntu16-5469/analysis.md) | — |
| ssh-controller-access | — | — | — | — | — | — | [17/8](../../../jobs/5469/2026-09-03__10-02-42/ssh-controller-access-bash-ubuntu16-5469/analysis.md) | — |
| internal-ca-tls | — | — | — | — | — | — | [31/7](../../../jobs/5469/2026-09-03__10-02-42/internal-ca-tls-bash-ubuntu16-5469/analysis.md) | — |
| internal-time-sync | — | — | — | — | — | — | [23/4](../../../jobs/5469/2026-09-03__10-02-42/internal-time-sync-bash-ubuntu16-5469/analysis.md) | — |
| load-balanced-web-tier | — | — | — | — | — | — | [32/1](../../../jobs/5469/2026-09-03__10-02-42/load-balanced-web-tier-bash-ubuntu16-5469/analysis.md) | — |
| network-scoped-firewall | — | — | — | — | — | — | [25/3](../../../jobs/5469/2026-09-03__10-02-42/network-scoped-firewall-bash-ubuntu16-5469/analysis.md) | — |
| config-sync | — | — | — | — | — | — | [29/5](../../../jobs/5469/2026-09-03__10-02-42/config-sync-bash-ubuntu16-5469/analysis.md) | — |
| scheduled-backup | — | — | — | — | — | — | [24/6](../../../jobs/5469/2026-09-03__10-02-42/scheduled-backup-bash-ubuntu16-5469/analysis.md) | — |
| internal-dns-resolution | — | — | — | — | — | — | [20/5](../../../jobs/5469/2026-09-03__10-02-42/internal-dns-resolution-bash-ubuntu16-5469/analysis.md) | — |
| **Average** | — | — | — | — | — | — | 27.0/4.8 | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | [6m 37s](../../../jobs/5469/2026-09-03__10-02-42/shared-nfs-storage-bash-ubuntu16-5469/analysis.md) | — |
| centralized-log-collector | — | — | — | — | — | — | [4m 31s](../../../jobs/5469/2026-09-03__10-02-42/centralized-log-collector-bash-ubuntu16-5469/analysis.md) | — |
| ssh-controller-access | — | — | — | — | — | — | [2m 43s](../../../jobs/5469/2026-09-03__10-02-42/ssh-controller-access-bash-ubuntu16-5469/analysis.md) | — |
| internal-ca-tls | — | — | — | — | — | — | [4m 30s](../../../jobs/5469/2026-09-03__10-02-42/internal-ca-tls-bash-ubuntu16-5469/analysis.md) | — |
| internal-time-sync | — | — | — | — | — | — | [5m 16s](../../../jobs/5469/2026-09-03__10-02-42/internal-time-sync-bash-ubuntu16-5469/analysis.md) | — |
| load-balanced-web-tier | — | — | — | — | — | — | [3m 46s](../../../jobs/5469/2026-09-03__10-02-42/load-balanced-web-tier-bash-ubuntu16-5469/analysis.md) | — |
| network-scoped-firewall | — | — | — | — | — | — | [4m 27s](../../../jobs/5469/2026-09-03__10-02-42/network-scoped-firewall-bash-ubuntu16-5469/analysis.md) | — |
| config-sync | — | — | — | — | — | — | [9m 29s](../../../jobs/5469/2026-09-03__10-02-42/config-sync-bash-ubuntu16-5469/analysis.md) | — |
| scheduled-backup | — | — | — | — | — | — | [3m 44s](../../../jobs/5469/2026-09-03__10-02-42/scheduled-backup-bash-ubuntu16-5469/analysis.md) | — |
| internal-dns-resolution | — | — | — | — | — | — | [2m 48s](../../../jobs/5469/2026-09-03__10-02-42/internal-dns-resolution-bash-ubuntu16-5469/analysis.md) | — |
| **Average** | — | — | — | — | — | — | 4m 47s | — |

Cluster provisioning is not a meaningful part of these times: median 628 ms across 10 clusters, about 0.26% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__10-02-42/shared-nfs-storage-bash-ubuntu16-5469/analysis.md) | — |
| centralized-log-collector | — | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__10-02-42/centralized-log-collector-bash-ubuntu16-5469/analysis.md) | — |
| ssh-controller-access | — | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__10-02-42/ssh-controller-access-bash-ubuntu16-5469/analysis.md) | — |
| internal-ca-tls | — | — | — | — | — | — | [0.930](../../../jobs/5469/2026-09-03__10-02-42/internal-ca-tls-bash-ubuntu16-5469/analysis.md) | — |
| internal-time-sync | — | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__10-02-42/internal-time-sync-bash-ubuntu16-5469/analysis.md) | — |
| load-balanced-web-tier | — | — | — | — | — | — | [1.000](../../../jobs/5469/2026-09-03__10-02-42/load-balanced-web-tier-bash-ubuntu16-5469/analysis.md) | — |
| network-scoped-firewall | — | — | — | — | — | — | [0.850](../../../jobs/5469/2026-09-03__10-02-42/network-scoped-firewall-bash-ubuntu16-5469/analysis.md) | — |
| config-sync | — | — | — | — | — | — | [0.850](../../../jobs/5469/2026-09-03__10-02-42/config-sync-bash-ubuntu16-5469/analysis.md) | — |
| scheduled-backup | — | — | — | — | — | — | [0.600](../../../jobs/5469/2026-09-03__10-02-42/scheduled-backup-bash-ubuntu16-5469/analysis.md) | — |
| internal-dns-resolution | — | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__10-02-42/internal-dns-resolution-bash-ubuntu16-5469/analysis.md) | — |
| **Average** | — | — | — | — | — | — | 0.898 | — |
