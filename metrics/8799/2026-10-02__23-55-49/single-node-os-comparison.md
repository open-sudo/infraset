# single-node-os-comparison: command execution summary

Scope: `8799/2026-10-02__23-55-49`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — | [10/7](../../../jobs/8799/2026-10-02__23-55-49/account-resource-limits-bash-centos5-8799) |
| application-log-rotation | — | — | — | — | — | — | — | — | [14/7](../../../jobs/8799/2026-10-02__23-55-49/application-log-rotation-bash-centos5-8799) |
| custom-ca-trust | — | — | — | — | — | — | — | — | [17/5](../../../jobs/8799/2026-10-02__23-55-49/custom-ca-trust-bash-centos5-8799) |
| host-firewall-baseline | — | — | — | — | — | — | — | — | [12/7](../../../jobs/8799/2026-10-02__23-55-49/host-firewall-baseline-bash-centos5-8799) |
| kernel-network-hardening | — | — | — | — | — | — | — | — | [12/26](../../../jobs/8799/2026-10-02__23-55-49/kernel-network-hardening-bash-centos5-8799) |
| repair-application-permissions | — | — | — | — | — | — | — | — | [17/17](../../../jobs/8799/2026-10-02__23-55-49/repair-application-permissions-bash-centos5-8799) |
| scheduled-maintenance | — | — | — | — | — | — | — | — | [7/3](../../../jobs/8799/2026-10-02__23-55-49/scheduled-maintenance-bash-centos5-8799) |
| ssh-key-only | — | — | — | — | — | — | — | — | [11/12](../../../jobs/8799/2026-10-02__23-55-49/ssh-key-only-bash-centos5-8799) |
| sticky-drop-directory | — | — | — | — | — | — | — | — | [8/5](../../../jobs/8799/2026-10-02__23-55-49/sticky-drop-directory-bash-centos5-8799) |
| unprivileged-service | — | — | — | — | — | — | — | — | [14/5](../../../jobs/8799/2026-10-02__23-55-49/unprivileged-service-bash-centos5-8799) |
| mandatory-access-control-port | — | — | — | — | — | — | — | — | [17/6](../../../jobs/8799/2026-10-02__23-55-49/mandatory-access-control-port-bash-centos5-8799) |
| kernel-module-blacklist | — | — | — | — | — | — | — | — | [11/11](../../../jobs/8799/2026-10-02__23-55-49/kernel-module-blacklist-bash-centos5-8799) |
| boot-kernel-parameter | — | — | — | — | — | — | — | — | [10/5](../../../jobs/8799/2026-10-02__23-55-49/boot-kernel-parameter-bash-centos5-8799) |
| mount-option-hardening | — | — | — | — | — | — | — | — | [12/5](../../../jobs/8799/2026-10-02__23-55-49/mount-option-hardening-bash-centos5-8799) |
| service-sandboxing | — | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — | [31/25](../../../jobs/8799/2026-10-02__23-55-49/password-complexity-policy-bash-centos5-8799) |
| sudo-command-logging | — | — | — | — | — | — | — | — | [12/7](../../../jobs/8799/2026-10-02__23-55-49/sudo-command-logging-bash-centos5-8799) |
| cron-access-control | — | — | — | — | — | — | — | — | [10/5](../../../jobs/8799/2026-10-02__23-55-49/cron-access-control-bash-centos5-8799) |
| ssh-host-certificate | — | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — | [14/7](../../../jobs/8799/2026-10-02__23-55-49/disk-quota-bash-centos5-8799) |
| encrypted-volume | — | — | — | — | — | — | — | — | [19/8](../../../jobs/8799/2026-10-02__23-55-49/encrypted-volume-bash-centos5-8799) |
| lvm-extend | — | — | — | — | — | — | — | — | [13/20](../../../jobs/8799/2026-10-02__23-55-49/lvm-extend-bash-centos5-8799) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — | [12/7](../../../jobs/8799/2026-10-02__23-55-49/filesystem-snapshot-rollback-bash-centos5-8799) |
| zram-swap | — | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — | [15/8](../../../jobs/8799/2026-10-02__23-55-49/package-version-hold-bash-centos5-8799) |
| local-package-repository | — | — | — | — | — | — | — | — | [22/16](../../../jobs/8799/2026-10-02__23-55-49/local-package-repository-bash-centos5-8799) |
| oom-protection | — | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — | [24/21](../../../jobs/8799/2026-10-02__23-55-49/certificate-rotation-bash-centos5-8799) |
| file-integrity-baseline | — | — | — | — | — | — | — | — | [16/9](../../../jobs/8799/2026-10-02__23-55-49/file-integrity-baseline-bash-centos5-8799) |
| chroot-web-service | — | — | — | — | — | — | — | — | [13/4](../../../jobs/8799/2026-10-02__23-55-49/chroot-web-service-bash-centos5-8799) |
| persistent-swap | — | — | — | — | — | — | — | — | [14/4](../../../jobs/8799/2026-10-02__23-55-49/persistent-swap-bash-centos5-8799) |
| service-confinement | — | — | — | — | — | — | — | — | [24/7](../../../jobs/8799/2026-10-02__23-55-49/service-confinement-bash-centos5-8799) |
| service-resource-limits | — | — | — | — | — | — | — | — | [22/6](../../../jobs/8799/2026-10-02__23-55-49/service-resource-limits-bash-centos5-8799) |
| ssh-host-key-pinning | — | — | — | — | — | — | — | — | [15/8](../../../jobs/8799/2026-10-02__23-55-49/ssh-host-key-pinning-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 14.9/9.4 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — | [3m 34s](../../../jobs/8799/2026-10-02__23-55-49/account-resource-limits-bash-centos5-8799) |
| application-log-rotation | — | — | — | — | — | — | — | — | [30m 33s](../../../jobs/8799/2026-10-02__23-55-49/application-log-rotation-bash-centos5-8799) |
| custom-ca-trust | — | — | — | — | — | — | — | — | [4m 41s](../../../jobs/8799/2026-10-02__23-55-49/custom-ca-trust-bash-centos5-8799) |
| host-firewall-baseline | — | — | — | — | — | — | — | — | [5m 17s](../../../jobs/8799/2026-10-02__23-55-49/host-firewall-baseline-bash-centos5-8799) |
| kernel-network-hardening | — | — | — | — | — | — | — | — | [5m 57s](../../../jobs/8799/2026-10-02__23-55-49/kernel-network-hardening-bash-centos5-8799) |
| repair-application-permissions | — | — | — | — | — | — | — | — | [4m 55s](../../../jobs/8799/2026-10-02__23-55-49/repair-application-permissions-bash-centos5-8799) |
| scheduled-maintenance | — | — | — | — | — | — | — | — | [4m 57s](../../../jobs/8799/2026-10-02__23-55-49/scheduled-maintenance-bash-centos5-8799) |
| ssh-key-only | — | — | — | — | — | — | — | — | [4m 43s](../../../jobs/8799/2026-10-02__23-55-49/ssh-key-only-bash-centos5-8799) |
| sticky-drop-directory | — | — | — | — | — | — | — | — | [3m 39s](../../../jobs/8799/2026-10-02__23-55-49/sticky-drop-directory-bash-centos5-8799) |
| unprivileged-service | — | — | — | — | — | — | — | — | [5m 15s](../../../jobs/8799/2026-10-02__23-55-49/unprivileged-service-bash-centos5-8799) |
| mandatory-access-control-port | — | — | — | — | — | — | — | — | [5m 31s](../../../jobs/8799/2026-10-02__23-55-49/mandatory-access-control-port-bash-centos5-8799) |
| kernel-module-blacklist | — | — | — | — | — | — | — | — | [4m 05s](../../../jobs/8799/2026-10-02__23-55-49/kernel-module-blacklist-bash-centos5-8799) |
| boot-kernel-parameter | — | — | — | — | — | — | — | — | [4m 14s](../../../jobs/8799/2026-10-02__23-55-49/boot-kernel-parameter-bash-centos5-8799) |
| mount-option-hardening | — | — | — | — | — | — | — | — | [4m 30s](../../../jobs/8799/2026-10-02__23-55-49/mount-option-hardening-bash-centos5-8799) |
| service-sandboxing | — | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — | [13m 24s](../../../jobs/8799/2026-10-02__23-55-49/password-complexity-policy-bash-centos5-8799) |
| sudo-command-logging | — | — | — | — | — | — | — | — | [5m 04s](../../../jobs/8799/2026-10-02__23-55-49/sudo-command-logging-bash-centos5-8799) |
| cron-access-control | — | — | — | — | — | — | — | — | [4m 09s](../../../jobs/8799/2026-10-02__23-55-49/cron-access-control-bash-centos5-8799) |
| ssh-host-certificate | — | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — | [4m 34s](../../../jobs/8799/2026-10-02__23-55-49/disk-quota-bash-centos5-8799) |
| encrypted-volume | — | — | — | — | — | — | — | — | [5m 35s](../../../jobs/8799/2026-10-02__23-55-49/encrypted-volume-bash-centos5-8799) |
| lvm-extend | — | — | — | — | — | — | — | — | [4m 17s](../../../jobs/8799/2026-10-02__23-55-49/lvm-extend-bash-centos5-8799) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — | [25m 00s](../../../jobs/8799/2026-10-02__23-55-49/filesystem-snapshot-rollback-bash-centos5-8799) |
| zram-swap | — | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — | [4m 09s](../../../jobs/8799/2026-10-02__23-55-49/package-version-hold-bash-centos5-8799) |
| local-package-repository | — | — | — | — | — | — | — | — | [5m 23s](../../../jobs/8799/2026-10-02__23-55-49/local-package-repository-bash-centos5-8799) |
| oom-protection | — | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — | [5m 56s](../../../jobs/8799/2026-10-02__23-55-49/certificate-rotation-bash-centos5-8799) |
| file-integrity-baseline | — | — | — | — | — | — | — | — | [5m 21s](../../../jobs/8799/2026-10-02__23-55-49/file-integrity-baseline-bash-centos5-8799) |
| chroot-web-service | — | — | — | — | — | — | — | — | [5m 07s](../../../jobs/8799/2026-10-02__23-55-49/chroot-web-service-bash-centos5-8799) |
| persistent-swap | — | — | — | — | — | — | — | — | [4m 20s](../../../jobs/8799/2026-10-02__23-55-49/persistent-swap-bash-centos5-8799) |
| service-confinement | — | — | — | — | — | — | — | — | [6m 45s](../../../jobs/8799/2026-10-02__23-55-49/service-confinement-bash-centos5-8799) |
| service-resource-limits | — | — | — | — | — | — | — | — | [4m 39s](../../../jobs/8799/2026-10-02__23-55-49/service-resource-limits-bash-centos5-8799) |
| ssh-host-key-pinning | — | — | — | — | — | — | — | — | [4m 59s](../../../jobs/8799/2026-10-02__23-55-49/ssh-host-key-pinning-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 6m 41s |

Cluster provisioning is not a meaningful part of these times: median 734 ms across 40 clusters, about 0.22% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-02__23-55-49/account-resource-limits-bash-centos5-8799) |
| application-log-rotation | — | — | — | — | — | — | — | — | [0.780](../../../jobs/8799/2026-10-02__23-55-49/application-log-rotation-bash-centos5-8799) |
| custom-ca-trust | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-02__23-55-49/custom-ca-trust-bash-centos5-8799) |
| host-firewall-baseline | — | — | — | — | — | — | — | — | [0.860](../../../jobs/8799/2026-10-02__23-55-49/host-firewall-baseline-bash-centos5-8799) |
| kernel-network-hardening | — | — | — | — | — | — | — | — | [0.930](../../../jobs/8799/2026-10-02__23-55-49/kernel-network-hardening-bash-centos5-8799) |
| repair-application-permissions | — | — | — | — | — | — | — | — | [0.980](../../../jobs/8799/2026-10-02__23-55-49/repair-application-permissions-bash-centos5-8799) |
| scheduled-maintenance | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8799/2026-10-02__23-55-49/scheduled-maintenance-bash-centos5-8799) |
| ssh-key-only | — | — | — | — | — | — | — | — | [0.850](../../../jobs/8799/2026-10-02__23-55-49/ssh-key-only-bash-centos5-8799) |
| sticky-drop-directory | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8799/2026-10-02__23-55-49/sticky-drop-directory-bash-centos5-8799) |
| unprivileged-service | — | — | — | — | — | — | — | — | [0.980](../../../jobs/8799/2026-10-02__23-55-49/unprivileged-service-bash-centos5-8799) |
| mandatory-access-control-port | — | — | — | — | — | — | — | — | [0.900](../../../jobs/8799/2026-10-02__23-55-49/mandatory-access-control-port-bash-centos5-8799) |
| kernel-module-blacklist | — | — | — | — | — | — | — | — | [0.950](../../../jobs/8799/2026-10-02__23-55-49/kernel-module-blacklist-bash-centos5-8799) |
| boot-kernel-parameter | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8799/2026-10-02__23-55-49/boot-kernel-parameter-bash-centos5-8799) |
| mount-option-hardening | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-02__23-55-49/mount-option-hardening-bash-centos5-8799) |
| service-sandboxing | — | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — | [0.520](../../../jobs/8799/2026-10-02__23-55-49/password-complexity-policy-bash-centos5-8799) |
| sudo-command-logging | — | — | — | — | — | — | — | — | [0.920](../../../jobs/8799/2026-10-02__23-55-49/sudo-command-logging-bash-centos5-8799) |
| cron-access-control | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-02__23-55-49/cron-access-control-bash-centos5-8799) |
| ssh-host-certificate | — | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — | [0.900](../../../jobs/8799/2026-10-02__23-55-49/disk-quota-bash-centos5-8799) |
| encrypted-volume | — | — | — | — | — | — | — | — | [0.910](../../../jobs/8799/2026-10-02__23-55-49/encrypted-volume-bash-centos5-8799) |
| lvm-extend | — | — | — | — | — | — | — | — | [0.900](../../../jobs/8799/2026-10-02__23-55-49/lvm-extend-bash-centos5-8799) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8799/2026-10-02__23-55-49/filesystem-snapshot-rollback-bash-centos5-8799) |
| zram-swap | — | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — | [0.900](../../../jobs/8799/2026-10-02__23-55-49/package-version-hold-bash-centos5-8799) |
| local-package-repository | — | — | — | — | — | — | — | — | [0.880](../../../jobs/8799/2026-10-02__23-55-49/local-package-repository-bash-centos5-8799) |
| oom-protection | — | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-02__23-55-49/certificate-rotation-bash-centos5-8799) |
| file-integrity-baseline | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-02__23-55-49/file-integrity-baseline-bash-centos5-8799) |
| chroot-web-service | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8799/2026-10-02__23-55-49/chroot-web-service-bash-centos5-8799) |
| persistent-swap | — | — | — | — | — | — | — | — | [0.920](../../../jobs/8799/2026-10-02__23-55-49/persistent-swap-bash-centos5-8799) |
| service-confinement | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-02__23-55-49/service-confinement-bash-centos5-8799) |
| service-resource-limits | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-02__23-55-49/service-resource-limits-bash-centos5-8799) |
| ssh-host-key-pinning | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-02__23-55-49/ssh-host-key-pinning-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 0.921 |
