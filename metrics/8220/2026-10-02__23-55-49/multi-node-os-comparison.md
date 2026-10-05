# multi-node-os-comparison: command execution summary

Scope: `8220/2026-10-02__23-55-49`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | — | [32/4](../../../jobs/8220/2026-10-02__23-55-49/shared-nfs-storage-bash-ubuntu7-8220) |
| centralized-log-collector | — | — | — | — | — | — | — | — | [28/3](../../../jobs/8220/2026-10-02__23-55-49/centralized-log-collector-bash-ubuntu7-8220) |
| ssh-controller-access | — | — | — | — | — | — | — | — | [18/8](../../../jobs/8220/2026-10-02__23-55-49/ssh-controller-access-bash-ubuntu7-8220) |
| internal-ca-tls | — | — | — | — | — | — | — | — | [42/11](../../../jobs/8220/2026-10-02__23-55-49/internal-ca-tls-bash-ubuntu7-8220) |
| internal-time-sync | — | — | — | — | — | — | — | — | [77/4](../../../jobs/8220/2026-10-02__23-55-49/internal-time-sync-bash-ubuntu7-8220) |
| load-balanced-web-tier | — | — | — | — | — | — | — | — | [33/7](../../../jobs/8220/2026-10-02__23-55-49/load-balanced-web-tier-bash-ubuntu7-8220) |
| network-scoped-firewall | — | — | — | — | — | — | — | — | [35/9](../../../jobs/8220/2026-10-02__23-55-49/network-scoped-firewall-bash-ubuntu7-8220) |
| config-sync | — | — | — | — | — | — | — | — | [22/4](../../../jobs/8220/2026-10-02__23-55-49/config-sync-bash-ubuntu7-8220) |
| scheduled-backup | — | — | — | — | — | — | — | — | [21/2](../../../jobs/8220/2026-10-02__23-55-49/scheduled-backup-bash-ubuntu7-8220) |
| internal-dns-resolution | — | — | — | — | — | — | — | — | [29/5](../../../jobs/8220/2026-10-02__23-55-49/internal-dns-resolution-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 33.7/5.7 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | — | [4m 48s](../../../jobs/8220/2026-10-02__23-55-49/shared-nfs-storage-bash-ubuntu7-8220) |
| centralized-log-collector | — | — | — | — | — | — | — | — | [4m 15s](../../../jobs/8220/2026-10-02__23-55-49/centralized-log-collector-bash-ubuntu7-8220) |
| ssh-controller-access | — | — | — | — | — | — | — | — | [4m 09s](../../../jobs/8220/2026-10-02__23-55-49/ssh-controller-access-bash-ubuntu7-8220) |
| internal-ca-tls | — | — | — | — | — | — | — | — | [9m 07s](../../../jobs/8220/2026-10-02__23-55-49/internal-ca-tls-bash-ubuntu7-8220) |
| internal-time-sync | — | — | — | — | — | — | — | — | [17m 02s](../../../jobs/8220/2026-10-02__23-55-49/internal-time-sync-bash-ubuntu7-8220) |
| load-balanced-web-tier | — | — | — | — | — | — | — | — | [4m 08s](../../../jobs/8220/2026-10-02__23-55-49/load-balanced-web-tier-bash-ubuntu7-8220) |
| network-scoped-firewall | — | — | — | — | — | — | — | — | [5m 09s](../../../jobs/8220/2026-10-02__23-55-49/network-scoped-firewall-bash-ubuntu7-8220) |
| config-sync | — | — | — | — | — | — | — | — | [5m 09s](../../../jobs/8220/2026-10-02__23-55-49/config-sync-bash-ubuntu7-8220) |
| scheduled-backup | — | — | — | — | — | — | — | — | [3m 58s](../../../jobs/8220/2026-10-02__23-55-49/scheduled-backup-bash-ubuntu7-8220) |
| internal-dns-resolution | — | — | — | — | — | — | — | — | [4m 08s](../../../jobs/8220/2026-10-02__23-55-49/internal-dns-resolution-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 6m 11s |

Cluster provisioning is not a meaningful part of these times: median 572 ms across 40 clusters, about 0.26% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/shared-nfs-storage-bash-ubuntu7-8220) |
| centralized-log-collector | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8220/2026-10-02__23-55-49/centralized-log-collector-bash-ubuntu7-8220) |
| ssh-controller-access | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/ssh-controller-access-bash-ubuntu7-8220) |
| internal-ca-tls | — | — | — | — | — | — | — | — | [0.840](../../../jobs/8220/2026-10-02__23-55-49/internal-ca-tls-bash-ubuntu7-8220) |
| internal-time-sync | — | — | — | — | — | — | — | — | [0.740](../../../jobs/8220/2026-10-02__23-55-49/internal-time-sync-bash-ubuntu7-8220) |
| load-balanced-web-tier | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/load-balanced-web-tier-bash-ubuntu7-8220) |
| network-scoped-firewall | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/network-scoped-firewall-bash-ubuntu7-8220) |
| config-sync | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/config-sync-bash-ubuntu7-8220) |
| scheduled-backup | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8220/2026-10-02__23-55-49/scheduled-backup-bash-ubuntu7-8220) |
| internal-dns-resolution | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8220/2026-10-02__23-55-49/internal-dns-resolution-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 0.940 |
