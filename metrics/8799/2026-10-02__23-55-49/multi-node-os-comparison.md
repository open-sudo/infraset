# multi-node-os-comparison: command execution summary

Scope: `8799/2026-10-02__23-55-49`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | — | [38/7](../../../jobs/8799/2026-10-02__23-55-49/shared-nfs-storage-bash-centos5-8799) |
| centralized-log-collector | — | — | — | — | — | — | — | — | [36/9](../../../jobs/8799/2026-10-02__23-55-49/centralized-log-collector-bash-centos5-8799) |
| ssh-controller-access | — | — | — | — | — | — | — | — | [34/6](../../../jobs/8799/2026-10-02__23-55-49/ssh-controller-access-bash-centos5-8799) |
| internal-ca-tls | — | — | — | — | — | — | — | — | [39/10](../../../jobs/8799/2026-10-02__23-55-49/internal-ca-tls-bash-centos5-8799) |
| internal-time-sync | — | — | — | — | — | — | — | — | [46/8](../../../jobs/8799/2026-10-02__23-55-49/internal-time-sync-bash-centos5-8799) |
| load-balanced-web-tier | — | — | — | — | — | — | — | — | [49/6](../../../jobs/8799/2026-10-02__23-55-49/load-balanced-web-tier-bash-centos5-8799) |
| network-scoped-firewall | — | — | — | — | — | — | — | — | [38/6](../../../jobs/8799/2026-10-02__23-55-49/network-scoped-firewall-bash-centos5-8799) |
| config-sync | — | — | — | — | — | — | — | — | [33/6](../../../jobs/8799/2026-10-02__23-55-49/config-sync-bash-centos5-8799) |
| scheduled-backup | — | — | — | — | — | — | — | — | [18/7](../../../jobs/8799/2026-10-02__23-55-49/scheduled-backup-bash-centos5-8799) |
| internal-dns-resolution | — | — | — | — | — | — | — | — | [17/6](../../../jobs/8799/2026-10-02__23-55-49/internal-dns-resolution-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 34.8/7.1 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | — | [7m 58s](../../../jobs/8799/2026-10-02__23-55-49/shared-nfs-storage-bash-centos5-8799) |
| centralized-log-collector | — | — | — | — | — | — | — | — | [7m 42s](../../../jobs/8799/2026-10-02__23-55-49/centralized-log-collector-bash-centos5-8799) |
| ssh-controller-access | — | — | — | — | — | — | — | — | [7m 56s](../../../jobs/8799/2026-10-02__23-55-49/ssh-controller-access-bash-centos5-8799) |
| internal-ca-tls | — | — | — | — | — | — | — | — | [10m 14s](../../../jobs/8799/2026-10-02__23-55-49/internal-ca-tls-bash-centos5-8799) |
| internal-time-sync | — | — | — | — | — | — | — | — | [14m 40s](../../../jobs/8799/2026-10-02__23-55-49/internal-time-sync-bash-centos5-8799) |
| load-balanced-web-tier | — | — | — | — | — | — | — | — | [8m 24s](../../../jobs/8799/2026-10-02__23-55-49/load-balanced-web-tier-bash-centos5-8799) |
| network-scoped-firewall | — | — | — | — | — | — | — | — | [9m 12s](../../../jobs/8799/2026-10-02__23-55-49/network-scoped-firewall-bash-centos5-8799) |
| config-sync | — | — | — | — | — | — | — | — | [9m 45s](../../../jobs/8799/2026-10-02__23-55-49/config-sync-bash-centos5-8799) |
| scheduled-backup | — | — | — | — | — | — | — | — | [7m 35s](../../../jobs/8799/2026-10-02__23-55-49/scheduled-backup-bash-centos5-8799) |
| internal-dns-resolution | — | — | — | — | — | — | — | — | [8m 58s](../../../jobs/8799/2026-10-02__23-55-49/internal-dns-resolution-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 9m 14s |

Cluster provisioning is not a meaningful part of these times: median 734 ms across 40 clusters, about 0.22% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-02__23-55-49/shared-nfs-storage-bash-centos5-8799) |
| centralized-log-collector | — | — | — | — | — | — | — | — | [0.840](../../../jobs/8799/2026-10-02__23-55-49/centralized-log-collector-bash-centos5-8799) |
| ssh-controller-access | — | — | — | — | — | — | — | — | [0.840](../../../jobs/8799/2026-10-02__23-55-49/ssh-controller-access-bash-centos5-8799) |
| internal-ca-tls | — | — | — | — | — | — | — | — | [0.760](../../../jobs/8799/2026-10-02__23-55-49/internal-ca-tls-bash-centos5-8799) |
| internal-time-sync | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8799/2026-10-02__23-55-49/internal-time-sync-bash-centos5-8799) |
| load-balanced-web-tier | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8799/2026-10-02__23-55-49/load-balanced-web-tier-bash-centos5-8799) |
| network-scoped-firewall | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8799/2026-10-02__23-55-49/network-scoped-firewall-bash-centos5-8799) |
| config-sync | — | — | — | — | — | — | — | — | [0.760](../../../jobs/8799/2026-10-02__23-55-49/config-sync-bash-centos5-8799) |
| scheduled-backup | — | — | — | — | — | — | — | — | [0.880](../../../jobs/8799/2026-10-02__23-55-49/scheduled-backup-bash-centos5-8799) |
| internal-dns-resolution | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8799/2026-10-02__23-55-49/internal-dns-resolution-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 0.880 |
