# single-node-os-comparison: command execution summary

Scope: `8220/2026-10-02__23-55-49`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — | [14/4](../../../jobs/8220/2026-10-02__23-55-49/account-resource-limits-bash-ubuntu7-8220) |
| application-log-rotation | — | — | — | — | — | — | — | — | [8/5](../../../jobs/8220/2026-10-02__23-55-49/application-log-rotation-bash-ubuntu7-8220) |
| custom-ca-trust | — | — | — | — | — | — | — | — | [14/3](../../../jobs/8220/2026-10-02__23-55-49/custom-ca-trust-bash-ubuntu7-8220) |
| host-firewall-baseline | — | — | — | — | — | — | — | — | [8/3](../../../jobs/8220/2026-10-02__23-55-49/host-firewall-baseline-bash-ubuntu7-8220) |
| kernel-network-hardening | — | — | — | — | — | — | — | — | [14/5](../../../jobs/8220/2026-10-02__23-55-49/kernel-network-hardening-bash-ubuntu7-8220) |
| repair-application-permissions | — | — | — | — | — | — | — | — | [8/4](../../../jobs/8220/2026-10-02__23-55-49/repair-application-permissions-bash-ubuntu7-8220) |
| scheduled-maintenance | — | — | — | — | — | — | — | — | [12/1](../../../jobs/8220/2026-10-02__23-55-49/scheduled-maintenance-bash-ubuntu7-8220) |
| ssh-key-only | — | — | — | — | — | — | — | — | [10/4](../../../jobs/8220/2026-10-02__23-55-49/ssh-key-only-bash-ubuntu7-8220) |
| sticky-drop-directory | — | — | — | — | — | — | — | — | [7/4](../../../jobs/8220/2026-10-02__23-55-49/sticky-drop-directory-bash-ubuntu7-8220) |
| unprivileged-service | — | — | — | — | — | — | — | — | [13/4](../../../jobs/8220/2026-10-02__23-55-49/unprivileged-service-bash-ubuntu7-8220) |
| mandatory-access-control-port | — | — | — | — | — | — | — | — | [12/4](../../../jobs/8220/2026-10-02__23-55-49/mandatory-access-control-port-bash-ubuntu7-8220) |
| kernel-module-blacklist | — | — | — | — | — | — | — | — | [9/3](../../../jobs/8220/2026-10-02__23-55-49/kernel-module-blacklist-bash-ubuntu7-8220) |
| boot-kernel-parameter | — | — | — | — | — | — | — | — | [9/3](../../../jobs/8220/2026-10-02__23-55-49/boot-kernel-parameter-bash-ubuntu7-8220) |
| mount-option-hardening | — | — | — | — | — | — | — | — | [18/3](../../../jobs/8220/2026-10-02__23-55-49/mount-option-hardening-bash-ubuntu7-8220) |
| service-sandboxing | — | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — | [18/6](../../../jobs/8220/2026-10-02__23-55-49/password-complexity-policy-bash-ubuntu7-8220) |
| sudo-command-logging | — | — | — | — | — | — | — | — | [10/3](../../../jobs/8220/2026-10-02__23-55-49/sudo-command-logging-bash-ubuntu7-8220) |
| cron-access-control | — | — | — | — | — | — | — | — | [11/2](../../../jobs/8220/2026-10-02__23-55-49/cron-access-control-bash-ubuntu7-8220) |
| ssh-host-certificate | — | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — | [20/7](../../../jobs/8220/2026-10-02__23-55-49/disk-quota-bash-ubuntu7-8220) |
| encrypted-volume | — | — | — | — | — | — | — | — | [23/2](../../../jobs/8220/2026-10-02__23-55-49/encrypted-volume-bash-ubuntu7-8220) |
| lvm-extend | — | — | — | — | — | — | — | — | [19/70](../../../jobs/8220/2026-10-02__23-55-49/lvm-extend-bash-ubuntu7-8220) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — | [14/3](../../../jobs/8220/2026-10-02__23-55-49/filesystem-snapshot-rollback-bash-ubuntu7-8220) |
| zram-swap | — | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — | [8/1](../../../jobs/8220/2026-10-02__23-55-49/package-version-hold-bash-ubuntu7-8220) |
| local-package-repository | — | — | — | — | — | — | — | — | [15/2](../../../jobs/8220/2026-10-02__23-55-49/local-package-repository-bash-ubuntu7-8220) |
| oom-protection | — | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — | [23/4](../../../jobs/8220/2026-10-02__23-55-49/certificate-rotation-bash-ubuntu7-8220) |
| file-integrity-baseline | — | — | — | — | — | — | — | — | [18/6](../../../jobs/8220/2026-10-02__23-55-49/file-integrity-baseline-bash-ubuntu7-8220) |
| chroot-web-service | — | — | — | — | — | — | — | — | [15/4](../../../jobs/8220/2026-10-02__23-55-49/chroot-web-service-bash-ubuntu7-8220) |
| persistent-swap | — | — | — | — | — | — | — | — | [11/1](../../../jobs/8220/2026-10-02__23-55-49/persistent-swap-bash-ubuntu7-8220) |
| service-confinement | — | — | — | — | — | — | — | — | [14/4](../../../jobs/8220/2026-10-02__23-55-49/service-confinement-bash-ubuntu7-8220) |
| service-resource-limits | — | — | — | — | — | — | — | — | [16/2](../../../jobs/8220/2026-10-02__23-55-49/service-resource-limits-bash-ubuntu7-8220) |
| ssh-host-key-pinning | — | — | — | — | — | — | — | — | [10/4](../../../jobs/8220/2026-10-02__23-55-49/ssh-host-key-pinning-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 13.4/5.7 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — | [3m 06s](../../../jobs/8220/2026-10-02__23-55-49/account-resource-limits-bash-ubuntu7-8220) |
| application-log-rotation | — | — | — | — | — | — | — | — | [2m 41s](../../../jobs/8220/2026-10-02__23-55-49/application-log-rotation-bash-ubuntu7-8220) |
| custom-ca-trust | — | — | — | — | — | — | — | — | [3m 37s](../../../jobs/8220/2026-10-02__23-55-49/custom-ca-trust-bash-ubuntu7-8220) |
| host-firewall-baseline | — | — | — | — | — | — | — | — | [2m 37s](../../../jobs/8220/2026-10-02__23-55-49/host-firewall-baseline-bash-ubuntu7-8220) |
| kernel-network-hardening | — | — | — | — | — | — | — | — | [3m 23s](../../../jobs/8220/2026-10-02__23-55-49/kernel-network-hardening-bash-ubuntu7-8220) |
| repair-application-permissions | — | — | — | — | — | — | — | — | [17m 33s](../../../jobs/8220/2026-10-02__23-55-49/repair-application-permissions-bash-ubuntu7-8220) |
| scheduled-maintenance | — | — | — | — | — | — | — | — | [2m 18s](../../../jobs/8220/2026-10-02__23-55-49/scheduled-maintenance-bash-ubuntu7-8220) |
| ssh-key-only | — | — | — | — | — | — | — | — | [2m 27s](../../../jobs/8220/2026-10-02__23-55-49/ssh-key-only-bash-ubuntu7-8220) |
| sticky-drop-directory | — | — | — | — | — | — | — | — | [1m 35s](../../../jobs/8220/2026-10-02__23-55-49/sticky-drop-directory-bash-ubuntu7-8220) |
| unprivileged-service | — | — | — | — | — | — | — | — | [3m 04s](../../../jobs/8220/2026-10-02__23-55-49/unprivileged-service-bash-ubuntu7-8220) |
| mandatory-access-control-port | — | — | — | — | — | — | — | — | [3m 23s](../../../jobs/8220/2026-10-02__23-55-49/mandatory-access-control-port-bash-ubuntu7-8220) |
| kernel-module-blacklist | — | — | — | — | — | — | — | — | [3m 35s](../../../jobs/8220/2026-10-02__23-55-49/kernel-module-blacklist-bash-ubuntu7-8220) |
| boot-kernel-parameter | — | — | — | — | — | — | — | — | [2m 13s](../../../jobs/8220/2026-10-02__23-55-49/boot-kernel-parameter-bash-ubuntu7-8220) |
| mount-option-hardening | — | — | — | — | — | — | — | — | [4m 07s](../../../jobs/8220/2026-10-02__23-55-49/mount-option-hardening-bash-ubuntu7-8220) |
| service-sandboxing | — | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — | [6m 07s](../../../jobs/8220/2026-10-02__23-55-49/password-complexity-policy-bash-ubuntu7-8220) |
| sudo-command-logging | — | — | — | — | — | — | — | — | [2m 56s](../../../jobs/8220/2026-10-02__23-55-49/sudo-command-logging-bash-ubuntu7-8220) |
| cron-access-control | — | — | — | — | — | — | — | — | [2m 58s](../../../jobs/8220/2026-10-02__23-55-49/cron-access-control-bash-ubuntu7-8220) |
| ssh-host-certificate | — | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — | [3m 28s](../../../jobs/8220/2026-10-02__23-55-49/disk-quota-bash-ubuntu7-8220) |
| encrypted-volume | — | — | — | — | — | — | — | — | [4m 57s](../../../jobs/8220/2026-10-02__23-55-49/encrypted-volume-bash-ubuntu7-8220) |
| lvm-extend | — | — | — | — | — | — | — | — | [37m 45s](../../../jobs/8220/2026-10-02__23-55-49/lvm-extend-bash-ubuntu7-8220) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — | [4m 09s](../../../jobs/8220/2026-10-02__23-55-49/filesystem-snapshot-rollback-bash-ubuntu7-8220) |
| zram-swap | — | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — | [1m 46s](../../../jobs/8220/2026-10-02__23-55-49/package-version-hold-bash-ubuntu7-8220) |
| local-package-repository | — | — | — | — | — | — | — | — | [3m 43s](../../../jobs/8220/2026-10-02__23-55-49/local-package-repository-bash-ubuntu7-8220) |
| oom-protection | — | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — | [5m 16s](../../../jobs/8220/2026-10-02__23-55-49/certificate-rotation-bash-ubuntu7-8220) |
| file-integrity-baseline | — | — | — | — | — | — | — | — | [29m 55s](../../../jobs/8220/2026-10-02__23-55-49/file-integrity-baseline-bash-ubuntu7-8220) |
| chroot-web-service | — | — | — | — | — | — | — | — | [3m 58s](../../../jobs/8220/2026-10-02__23-55-49/chroot-web-service-bash-ubuntu7-8220) |
| persistent-swap | — | — | — | — | — | — | — | — | [3m 16s](../../../jobs/8220/2026-10-02__23-55-49/persistent-swap-bash-ubuntu7-8220) |
| service-confinement | — | — | — | — | — | — | — | — | [4m 11s](../../../jobs/8220/2026-10-02__23-55-49/service-confinement-bash-ubuntu7-8220) |
| service-resource-limits | — | — | — | — | — | — | — | — | [3m 11s](../../../jobs/8220/2026-10-02__23-55-49/service-resource-limits-bash-ubuntu7-8220) |
| ssh-host-key-pinning | — | — | — | — | — | — | — | — | [2m 44s](../../../jobs/8220/2026-10-02__23-55-49/ssh-host-key-pinning-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 5m 52s |

Cluster provisioning is not a meaningful part of these times: median 572 ms across 40 clusters, about 0.26% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8220/2026-10-02__23-55-49/account-resource-limits-bash-ubuntu7-8220) |
| application-log-rotation | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/application-log-rotation-bash-ubuntu7-8220) |
| custom-ca-trust | — | — | — | — | — | — | — | — | [0.920](../../../jobs/8220/2026-10-02__23-55-49/custom-ca-trust-bash-ubuntu7-8220) |
| host-firewall-baseline | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/host-firewall-baseline-bash-ubuntu7-8220) |
| kernel-network-hardening | — | — | — | — | — | — | — | — | [0.980](../../../jobs/8220/2026-10-02__23-55-49/kernel-network-hardening-bash-ubuntu7-8220) |
| repair-application-permissions | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/repair-application-permissions-bash-ubuntu7-8220) |
| scheduled-maintenance | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/scheduled-maintenance-bash-ubuntu7-8220) |
| ssh-key-only | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/ssh-key-only-bash-ubuntu7-8220) |
| sticky-drop-directory | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/sticky-drop-directory-bash-ubuntu7-8220) |
| unprivileged-service | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/unprivileged-service-bash-ubuntu7-8220) |
| mandatory-access-control-port | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/mandatory-access-control-port-bash-ubuntu7-8220) |
| kernel-module-blacklist | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/kernel-module-blacklist-bash-ubuntu7-8220) |
| boot-kernel-parameter | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8220/2026-10-02__23-55-49/boot-kernel-parameter-bash-ubuntu7-8220) |
| mount-option-hardening | — | — | — | — | — | — | — | — | [0.860](../../../jobs/8220/2026-10-02__23-55-49/mount-option-hardening-bash-ubuntu7-8220) |
| service-sandboxing | — | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8220/2026-10-02__23-55-49/password-complexity-policy-bash-ubuntu7-8220) |
| sudo-command-logging | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8220/2026-10-02__23-55-49/sudo-command-logging-bash-ubuntu7-8220) |
| cron-access-control | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/cron-access-control-bash-ubuntu7-8220) |
| ssh-host-certificate | — | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — | [0.900](../../../jobs/8220/2026-10-02__23-55-49/disk-quota-bash-ubuntu7-8220) |
| encrypted-volume | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/encrypted-volume-bash-ubuntu7-8220) |
| lvm-extend | — | — | — | — | — | — | — | — | [0.720](../../../jobs/8220/2026-10-02__23-55-49/lvm-extend-bash-ubuntu7-8220) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/filesystem-snapshot-rollback-bash-ubuntu7-8220) |
| zram-swap | — | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/package-version-hold-bash-ubuntu7-8220) |
| local-package-repository | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/local-package-repository-bash-ubuntu7-8220) |
| oom-protection | — | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — | [0.680](../../../jobs/8220/2026-10-02__23-55-49/certificate-rotation-bash-ubuntu7-8220) |
| file-integrity-baseline | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8220/2026-10-02__23-55-49/file-integrity-baseline-bash-ubuntu7-8220) |
| chroot-web-service | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/chroot-web-service-bash-ubuntu7-8220) |
| persistent-swap | — | — | — | — | — | — | — | — | [0.880](../../../jobs/8220/2026-10-02__23-55-49/persistent-swap-bash-ubuntu7-8220) |
| service-confinement | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/service-confinement-bash-ubuntu7-8220) |
| service-resource-limits | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/service-resource-limits-bash-ubuntu7-8220) |
| ssh-host-key-pinning | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-02__23-55-49/ssh-host-key-pinning-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 0.956 |
