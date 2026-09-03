# multi-node-os-comparison: command execution summary

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Task names link to that run's analysis. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [shared-nfs-storage](jobs/multi-node-os-comparison/alpine/shared-nfs-storage-alpine/2026-09-03__10-30-01/analysis.md) | 32/11 | 24/7 | 28/7 | 26/12 | 29/8 | 33/9 | 41/5 | 26/5 |
| [centralized-log-collector](jobs/multi-node-os-comparison/alpine/centralized-log-collector-alpine/2026-09-03__10-30-01/analysis.md) | 31/7 | 30/3 | 38/14 | 29/6 | 24/7 | 29/8 | 28/4 | 22/9 |
| [ssh-controller-access](jobs/multi-node-os-comparison/alpine/ssh-controller-access-alpine/2026-09-03__10-30-01/analysis.md) | 31/11 | 28/3 | 18/10 | 32/8 | 24/5 | 33/11 | 17/8 | 29/14 |
| [internal-ca-tls](jobs/multi-node-os-comparison/alpine/internal-ca-tls-alpine/2026-09-03__10-30-01/analysis.md) | 31/29 | 25/4 | 28/9 | 33/8 | 34/7 | 0/0 | 31/7 | 34/4 |
| [internal-time-sync](jobs/multi-node-os-comparison/alpine/internal-time-sync-alpine/2026-09-03__10-30-01/analysis.md) | 19/14 | 29/3 | 25/4 | 18/5 | 27/5 | 33/6 | 23/6 | 24/3 |
| [load-balanced-web-tier](jobs/multi-node-os-comparison/alpine/load-balanced-web-tier-alpine/2026-09-03__10-30-01/analysis.md) | 38/13 | 36/7 | 42/8 | 32/8 | 32/12 | 42/6 | 32/1 | 25/4 |
| [network-scoped-firewall](jobs/multi-node-os-comparison/alpine/network-scoped-firewall-alpine/2026-09-03__10-30-01/analysis.md) | 34/22 | 34/5 | 31/4 | 34/14 | 27/11 | 39/8 | 25/6 | 31/4 |
| [config-sync](jobs/multi-node-os-comparison/alpine/config-sync-alpine/2026-09-03__10-30-01/analysis.md) | 32/22 | 42/5 | 24/7 | 35/2 | 28/8 | 27/8 | 29/5 | 30/13 |
| [scheduled-backup](jobs/multi-node-os-comparison/alpine/scheduled-backup-alpine/2026-09-03__10-30-01/analysis.md) | 28/25 | 26/3 | 26/7 | 22/7 | 27/8 | 25/7 | 24/6 | 32/7 |
| [internal-dns-resolution](jobs/multi-node-os-comparison/alpine/internal-dns-resolution-alpine/2026-09-03__10-30-01/analysis.md) | 18/16 | 24/4 | 25/10 | 26/8 | 29/8 | 0/0 | 20/5 | 23/3 |
