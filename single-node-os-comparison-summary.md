# single-node-os-comparison: command execution summary

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Task names link to that run's analysis. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](jobs/single-node-os-comparison/alpine/account-resource-limits-alpine/2026-09-03__07-51-03/analysis.md) | 22/17 | 7/2 | 8/3 | 9/2 | 8/3 | 6/4 | 8/1 | 9/2 |
| [application-log-rotation](jobs/single-node-os-comparison/alpine/application-log-rotation-alpine/2026-09-03__07-51-03/analysis.md) | 19/10 | 10/2 | 11/3 | 12/5 | 12/4 | 12/3 | 12/3 | 12/3 |
| [custom-ca-trust](jobs/single-node-os-comparison/alpine/custom-ca-trust-alpine/2026-09-03__07-51-03/analysis.md) | 16/11 | 13/1 | 16/2 | 12/3 | 8/2 | 10/3 | 13/2 | 11/1 |
| [host-firewall-baseline](jobs/single-node-os-comparison/alpine/host-firewall-baseline-alpine/2026-09-03__07-51-03/analysis.md) | 11/7 | 15/2 | 10/3 | 18/6 | 14/3 | 14/5 | 10/1 | 12/2 |
| [kernel-network-hardening](jobs/single-node-os-comparison/alpine/kernel-network-hardening-alpine/2026-09-03__07-51-03/analysis.md) | 11/11 | 11/2 | 9/3 | 9/6 | 12/2 | 10/2 | 10/2 | 11/1 |
| [repair-application-permissions](jobs/single-node-os-comparison/alpine/repair-application-permissions-alpine/2026-09-03__07-51-03/analysis.md) | 10/14 | 9/3 | 12/4 | 12/5 | 14/4 | 13/5 | 11/5 | 12/3 |
| [scheduled-maintenance](jobs/single-node-os-comparison/alpine/scheduled-maintenance-alpine/2026-09-03__07-51-03/analysis.md) | 10/3 | 11/2 | 10/2 | 8/3 | 12/2 | 12/3 | 6/3 | 11/4 |
| [ssh-key-only](jobs/single-node-os-comparison/alpine/ssh-key-only-alpine/2026-09-03__07-51-03/analysis.md) | 16/6 | 17/1 | 15/2 | 17/7 | 10/2 | 19/3 | 11/3 | 19/4 |
| [sticky-drop-directory](jobs/single-node-os-comparison/alpine/sticky-drop-directory-alpine/2026-09-03__07-51-03/analysis.md) | 11/8 | 13/4 | 12/2 | 11/1 | 11/3 | 14/3 | 12/2 | 10/3 |
| [unprivileged-service](jobs/single-node-os-comparison/alpine/unprivileged-service-alpine/2026-09-03__07-51-03/analysis.md) | 10/17 | 9/1 | 9/2 | 11/4 | 9/3 | 8/3 | 11/3 | 10/1 |
