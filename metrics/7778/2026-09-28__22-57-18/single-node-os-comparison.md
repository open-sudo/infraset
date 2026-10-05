# single-node-os-comparison: command execution summary

Scope: `7778/2026-09-28__22-57-18`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | [21/7](../../../jobs/7778/2026-09-28__22-57-18/account-resource-limits-ansible-ubuntu24-7778) |
| application-log-rotation | — | — | — | — | — | — | — | [25/7](../../../jobs/7778/2026-09-28__22-57-18/application-log-rotation-ansible-ubuntu24-7778) |
| custom-ca-trust | — | — | — | — | — | — | — | [16/2](../../../jobs/7778/2026-09-28__22-57-18/custom-ca-trust-ansible-ubuntu24-7778) |
| host-firewall-baseline | — | — | — | — | — | — | — | [33/2](../../../jobs/7778/2026-09-28__22-57-18/host-firewall-baseline-ansible-ubuntu24-7778) |
| kernel-network-hardening | — | — | — | — | — | — | — | [22/4](../../../jobs/7778/2026-09-28__22-57-18/kernel-network-hardening-ansible-ubuntu24-7778) |
| repair-application-permissions | — | — | — | — | — | — | — | [19/3](../../../jobs/7778/2026-09-28__22-57-18/repair-application-permissions-ansible-ubuntu24-7778) |
| scheduled-maintenance | — | — | — | — | — | — | — | [31/9](../../../jobs/7778/2026-09-28__22-57-18/scheduled-maintenance-ansible-ubuntu24-7778) |
| ssh-key-only | — | — | — | — | — | — | — | [30/6](../../../jobs/7778/2026-09-28__22-57-18/ssh-key-only-ansible-ubuntu24-7778) |
| sticky-drop-directory | — | — | — | — | — | — | — | [24/4](../../../jobs/7778/2026-09-28__22-57-18/sticky-drop-directory-ansible-ubuntu24-7778) |
| unprivileged-service | — | — | — | — | — | — | — | [16/0](../../../jobs/7778/2026-09-28__22-57-18/unprivileged-service-ansible-ubuntu24-7778) |
| mandatory-access-control-port | — | — | — | — | — | — | — | [17/4](../../../jobs/7778/2026-09-28__22-57-18/mandatory-access-control-port-ansible-ubuntu24-7778) |
| kernel-module-blacklist | — | — | — | — | — | — | — | [22/8](../../../jobs/7778/2026-09-28__22-57-18/kernel-module-blacklist-ansible-ubuntu24-7778) |
| boot-kernel-parameter | — | — | — | — | — | — | — | [21/6](../../../jobs/7778/2026-09-28__22-57-18/boot-kernel-parameter-ansible-ubuntu24-7778) |
| mount-option-hardening | — | — | — | — | — | — | — | [31/3](../../../jobs/7778/2026-09-28__22-57-18/mount-option-hardening-ansible-ubuntu24-7778) |
| service-sandboxing | — | — | — | — | — | — | — | [16/1](../../../jobs/7778/2026-09-28__22-57-18/service-sandboxing-ansible-ubuntu24-7778) |
| password-complexity-policy | — | — | — | — | — | — | — | [35/9](../../../jobs/7778/2026-09-28__22-57-18/password-complexity-policy-ansible-ubuntu24-7778) |
| sudo-command-logging | — | — | — | — | — | — | — | [17/2](../../../jobs/7778/2026-09-28__22-57-18/sudo-command-logging-ansible-ubuntu24-7778) |
| cron-access-control | — | — | — | — | — | — | — | [27/6](../../../jobs/7778/2026-09-28__22-57-18/cron-access-control-ansible-ubuntu24-7778) |
| ssh-host-certificate | — | — | — | — | — | — | — | [26/4](../../../jobs/7778/2026-09-28__22-57-18/ssh-host-certificate-ansible-ubuntu24-7778) |
| disk-quota | — | — | — | — | — | — | — | [18/2](../../../jobs/7778/2026-09-28__22-57-18/disk-quota-ansible-ubuntu24-7778) |
| encrypted-volume | — | — | — | — | — | — | — | [17/3](../../../jobs/7778/2026-09-28__22-57-18/encrypted-volume-ansible-ubuntu24-7778) |
| lvm-extend | — | — | — | — | — | — | — | [30/6](../../../jobs/7778/2026-09-28__22-57-18/lvm-extend-ansible-ubuntu24-7778) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | [56/11](../../../jobs/7778/2026-09-28__22-57-18/filesystem-snapshot-rollback-ansible-ubuntu24-7778) |
| zram-swap | — | — | — | — | — | — | — | [28/7](../../../jobs/7778/2026-09-28__22-57-18/zram-swap-ansible-ubuntu24-7778) |
| package-version-hold | — | — | — | — | — | — | — | [30/2](../../../jobs/7778/2026-09-28__22-57-18/package-version-hold-ansible-ubuntu24-7778) |
| local-package-repository | — | — | — | — | — | — | — | [30/3](../../../jobs/7778/2026-09-28__22-57-18/local-package-repository-ansible-ubuntu24-7778) |
| oom-protection | — | — | — | — | — | — | — | [33/3](../../../jobs/7778/2026-09-28__22-57-18/oom-protection-ansible-ubuntu24-7778) |
| rootless-container-service | — | — | — | — | — | — | — | [30/6](../../../jobs/7778/2026-09-28__22-57-18/rootless-container-service-ansible-ubuntu24-7778) |
| certificate-rotation | — | — | — | — | — | — | — | [32/6](../../../jobs/7778/2026-09-28__22-57-18/certificate-rotation-ansible-ubuntu24-7778) |
| file-integrity-baseline | — | — | — | — | — | — | — | [37/1](../../../jobs/7778/2026-09-28__22-57-18/file-integrity-baseline-ansible-ubuntu24-7778) |
| **Average** | — | — | — | — | — | — | — | 26.3/4.6 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | [3m 51s](../../../jobs/7778/2026-09-28__22-57-18/account-resource-limits-ansible-ubuntu24-7778) |
| application-log-rotation | — | — | — | — | — | — | — | [4m 12s](../../../jobs/7778/2026-09-28__22-57-18/application-log-rotation-ansible-ubuntu24-7778) |
| custom-ca-trust | — | — | — | — | — | — | — | [3m 26s](../../../jobs/7778/2026-09-28__22-57-18/custom-ca-trust-ansible-ubuntu24-7778) |
| host-firewall-baseline | — | — | — | — | — | — | — | [4m 51s](../../../jobs/7778/2026-09-28__22-57-18/host-firewall-baseline-ansible-ubuntu24-7778) |
| kernel-network-hardening | — | — | — | — | — | — | — | [3m 27s](../../../jobs/7778/2026-09-28__22-57-18/kernel-network-hardening-ansible-ubuntu24-7778) |
| repair-application-permissions | — | — | — | — | — | — | — | [3m 07s](../../../jobs/7778/2026-09-28__22-57-18/repair-application-permissions-ansible-ubuntu24-7778) |
| scheduled-maintenance | — | — | — | — | — | — | — | [3m 48s](../../../jobs/7778/2026-09-28__22-57-18/scheduled-maintenance-ansible-ubuntu24-7778) |
| ssh-key-only | — | — | — | — | — | — | — | [3m 40s](../../../jobs/7778/2026-09-28__22-57-18/ssh-key-only-ansible-ubuntu24-7778) |
| sticky-drop-directory | — | — | — | — | — | — | — | [4m 02s](../../../jobs/7778/2026-09-28__22-57-18/sticky-drop-directory-ansible-ubuntu24-7778) |
| unprivileged-service | — | — | — | — | — | — | — | [2m 34s](../../../jobs/7778/2026-09-28__22-57-18/unprivileged-service-ansible-ubuntu24-7778) |
| mandatory-access-control-port | — | — | — | — | — | — | — | [4m 42s](../../../jobs/7778/2026-09-28__22-57-18/mandatory-access-control-port-ansible-ubuntu24-7778) |
| kernel-module-blacklist | — | — | — | — | — | — | — | [4m 22s](../../../jobs/7778/2026-09-28__22-57-18/kernel-module-blacklist-ansible-ubuntu24-7778) |
| boot-kernel-parameter | — | — | — | — | — | — | — | [4m 34s](../../../jobs/7778/2026-09-28__22-57-18/boot-kernel-parameter-ansible-ubuntu24-7778) |
| mount-option-hardening | — | — | — | — | — | — | — | [3m 59s](../../../jobs/7778/2026-09-28__22-57-18/mount-option-hardening-ansible-ubuntu24-7778) |
| service-sandboxing | — | — | — | — | — | — | — | [4m 20s](../../../jobs/7778/2026-09-28__22-57-18/service-sandboxing-ansible-ubuntu24-7778) |
| password-complexity-policy | — | — | — | — | — | — | — | [9m 00s](../../../jobs/7778/2026-09-28__22-57-18/password-complexity-policy-ansible-ubuntu24-7778) |
| sudo-command-logging | — | — | — | — | — | — | — | [3m 58s](../../../jobs/7778/2026-09-28__22-57-18/sudo-command-logging-ansible-ubuntu24-7778) |
| cron-access-control | — | — | — | — | — | — | — | [4m 08s](../../../jobs/7778/2026-09-28__22-57-18/cron-access-control-ansible-ubuntu24-7778) |
| ssh-host-certificate | — | — | — | — | — | — | — | [4m 00s](../../../jobs/7778/2026-09-28__22-57-18/ssh-host-certificate-ansible-ubuntu24-7778) |
| disk-quota | — | — | — | — | — | — | — | [4m 56s](../../../jobs/7778/2026-09-28__22-57-18/disk-quota-ansible-ubuntu24-7778) |
| encrypted-volume | — | — | — | — | — | — | — | [3m 59s](../../../jobs/7778/2026-09-28__22-57-18/encrypted-volume-ansible-ubuntu24-7778) |
| lvm-extend | — | — | — | — | — | — | — | [5m 03s](../../../jobs/7778/2026-09-28__22-57-18/lvm-extend-ansible-ubuntu24-7778) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | [16m 04s](../../../jobs/7778/2026-09-28__22-57-18/filesystem-snapshot-rollback-ansible-ubuntu24-7778) |
| zram-swap | — | — | — | — | — | — | — | [6m 42s](../../../jobs/7778/2026-09-28__22-57-18/zram-swap-ansible-ubuntu24-7778) |
| package-version-hold | — | — | — | — | — | — | — | [4m 47s](../../../jobs/7778/2026-09-28__22-57-18/package-version-hold-ansible-ubuntu24-7778) |
| local-package-repository | — | — | — | — | — | — | — | [5m 42s](../../../jobs/7778/2026-09-28__22-57-18/local-package-repository-ansible-ubuntu24-7778) |
| oom-protection | — | — | — | — | — | — | — | [4m 25s](../../../jobs/7778/2026-09-28__22-57-18/oom-protection-ansible-ubuntu24-7778) |
| rootless-container-service | — | — | — | — | — | — | — | [5m 13s](../../../jobs/7778/2026-09-28__22-57-18/rootless-container-service-ansible-ubuntu24-7778) |
| certificate-rotation | — | — | — | — | — | — | — | [7m 21s](../../../jobs/7778/2026-09-28__22-57-18/certificate-rotation-ansible-ubuntu24-7778) |
| file-integrity-baseline | — | — | — | — | — | — | — | [19m 57s](../../../jobs/7778/2026-09-28__22-57-18/file-integrity-baseline-ansible-ubuntu24-7778) |
| **Average** | — | — | — | — | — | — | — | 5m 28s |

Cluster provisioning is not a meaningful part of these times: median 999 ms across 30 clusters, about 0.40% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | [0.900](../../../jobs/7778/2026-09-28__22-57-18/account-resource-limits-ansible-ubuntu24-7778) |
| application-log-rotation | — | — | — | — | — | — | — | [0.800](../../../jobs/7778/2026-09-28__22-57-18/application-log-rotation-ansible-ubuntu24-7778) |
| custom-ca-trust | — | — | — | — | — | — | — | [0.950](../../../jobs/7778/2026-09-28__22-57-18/custom-ca-trust-ansible-ubuntu24-7778) |
| host-firewall-baseline | — | — | — | — | — | — | — | [0.930](../../../jobs/7778/2026-09-28__22-57-18/host-firewall-baseline-ansible-ubuntu24-7778) |
| kernel-network-hardening | — | — | — | — | — | — | — | [0.920](../../../jobs/7778/2026-09-28__22-57-18/kernel-network-hardening-ansible-ubuntu24-7778) |
| repair-application-permissions | — | — | — | — | — | — | — | [0.950](../../../jobs/7778/2026-09-28__22-57-18/repair-application-permissions-ansible-ubuntu24-7778) |
| scheduled-maintenance | — | — | — | — | — | — | — | [0.850](../../../jobs/7778/2026-09-28__22-57-18/scheduled-maintenance-ansible-ubuntu24-7778) |
| ssh-key-only | — | — | — | — | — | — | — | [0.750](../../../jobs/7778/2026-09-28__22-57-18/ssh-key-only-ansible-ubuntu24-7778) |
| sticky-drop-directory | — | — | — | — | — | — | — | [0.950](../../../jobs/7778/2026-09-28__22-57-18/sticky-drop-directory-ansible-ubuntu24-7778) |
| unprivileged-service | — | — | — | — | — | — | — | [0.850](../../../jobs/7778/2026-09-28__22-57-18/unprivileged-service-ansible-ubuntu24-7778) |
| mandatory-access-control-port | — | — | — | — | — | — | — | [0.950](../../../jobs/7778/2026-09-28__22-57-18/mandatory-access-control-port-ansible-ubuntu24-7778) |
| kernel-module-blacklist | — | — | — | — | — | — | — | [0.650](../../../jobs/7778/2026-09-28__22-57-18/kernel-module-blacklist-ansible-ubuntu24-7778) |
| boot-kernel-parameter | — | — | — | — | — | — | — | [0.820](../../../jobs/7778/2026-09-28__22-57-18/boot-kernel-parameter-ansible-ubuntu24-7778) |
| mount-option-hardening | — | — | — | — | — | — | — | [0.900](../../../jobs/7778/2026-09-28__22-57-18/mount-option-hardening-ansible-ubuntu24-7778) |
| service-sandboxing | — | — | — | — | — | — | — | [0.900](../../../jobs/7778/2026-09-28__22-57-18/service-sandboxing-ansible-ubuntu24-7778) |
| password-complexity-policy | — | — | — | — | — | — | — | [0.720](../../../jobs/7778/2026-09-28__22-57-18/password-complexity-policy-ansible-ubuntu24-7778) |
| sudo-command-logging | — | — | — | — | — | — | — | [0.780](../../../jobs/7778/2026-09-28__22-57-18/sudo-command-logging-ansible-ubuntu24-7778) |
| cron-access-control | — | — | — | — | — | — | — | [0.900](../../../jobs/7778/2026-09-28__22-57-18/cron-access-control-ansible-ubuntu24-7778) |
| ssh-host-certificate | — | — | — | — | — | — | — | [0.930](../../../jobs/7778/2026-09-28__22-57-18/ssh-host-certificate-ansible-ubuntu24-7778) |
| disk-quota | — | — | — | — | — | — | — | [0.850](../../../jobs/7778/2026-09-28__22-57-18/disk-quota-ansible-ubuntu24-7778) |
| encrypted-volume | — | — | — | — | — | — | — | [0.900](../../../jobs/7778/2026-09-28__22-57-18/encrypted-volume-ansible-ubuntu24-7778) |
| lvm-extend | — | — | — | — | — | — | — | [0.850](../../../jobs/7778/2026-09-28__22-57-18/lvm-extend-ansible-ubuntu24-7778) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | [0.800](../../../jobs/7778/2026-09-28__22-57-18/filesystem-snapshot-rollback-ansible-ubuntu24-7778) |
| zram-swap | — | — | — | — | — | — | — | [0.750](../../../jobs/7778/2026-09-28__22-57-18/zram-swap-ansible-ubuntu24-7778) |
| package-version-hold | — | — | — | — | — | — | — | [0.900](../../../jobs/7778/2026-09-28__22-57-18/package-version-hold-ansible-ubuntu24-7778) |
| local-package-repository | — | — | — | — | — | — | — | [0.800](../../../jobs/7778/2026-09-28__22-57-18/local-package-repository-ansible-ubuntu24-7778) |
| oom-protection | — | — | — | — | — | — | — | [0.800](../../../jobs/7778/2026-09-28__22-57-18/oom-protection-ansible-ubuntu24-7778) |
| rootless-container-service | — | — | — | — | — | — | — | [0.850](../../../jobs/7778/2026-09-28__22-57-18/rootless-container-service-ansible-ubuntu24-7778) |
| certificate-rotation | — | — | — | — | — | — | — | [0.850](../../../jobs/7778/2026-09-28__22-57-18/certificate-rotation-ansible-ubuntu24-7778) |
| file-integrity-baseline | — | — | — | — | — | — | — | [0.750](../../../jobs/7778/2026-09-28__22-57-18/file-integrity-baseline-ansible-ubuntu24-7778) |
| **Average** | — | — | — | — | — | — | — | 0.850 |
