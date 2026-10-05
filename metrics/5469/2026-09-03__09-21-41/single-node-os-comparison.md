# single-node-os-comparison: command execution summary

Scope: `5469/2026-09-03__09-21-41`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | [9/1](../../../jobs/5469/2026-09-03__09-21-41/account-resource-limits-bash-rhel7-5469/analysis.md) | — | — | — | — |
| application-log-rotation | — | — | — | [12/3](../../../jobs/5469/2026-09-03__09-21-41/application-log-rotation-bash-rhel7-5469/analysis.md) | — | — | — | — |
| custom-ca-trust | — | — | — | [12/2](../../../jobs/5469/2026-09-03__09-21-41/custom-ca-trust-bash-rhel7-5469/analysis.md) | — | — | — | — |
| host-firewall-baseline | — | — | — | [18/4](../../../jobs/5469/2026-09-03__09-21-41/host-firewall-baseline-bash-rhel7-5469/analysis.md) | — | — | — | — |
| kernel-network-hardening | — | — | — | [9/4](../../../jobs/5469/2026-09-03__09-21-41/kernel-network-hardening-bash-rhel7-5469/analysis.md) | — | — | — | — |
| repair-application-permissions | — | — | — | [12/4](../../../jobs/5469/2026-09-03__09-21-41/repair-application-permissions-bash-rhel7-5469/analysis.md) | — | — | — | — |
| scheduled-maintenance | — | — | — | [8/1](../../../jobs/5469/2026-09-03__09-21-41/scheduled-maintenance-bash-rhel7-5469/analysis.md) | — | — | — | — |
| ssh-key-only | — | — | — | [17/5](../../../jobs/5469/2026-09-03__09-21-41/ssh-key-only-bash-rhel7-5469/analysis.md) | — | — | — | — |
| sticky-drop-directory | — | — | — | [11/0](../../../jobs/5469/2026-09-03__09-21-41/sticky-drop-directory-bash-rhel7-5469/analysis.md) | — | — | — | — |
| unprivileged-service | — | — | — | [11/3](../../../jobs/5469/2026-09-03__09-21-41/unprivileged-service-bash-rhel7-5469/analysis.md) | — | — | — | — |
| mandatory-access-control-port | — | — | — | — | — | — | — | — |
| kernel-module-blacklist | — | — | — | — | — | — | — | — |
| boot-kernel-parameter | — | — | — | — | — | — | — | — |
| mount-option-hardening | — | — | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — |
| sudo-command-logging | — | — | — | — | — | — | — | — |
| cron-access-control | — | — | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — |
| encrypted-volume | — | — | — | — | — | — | — | — |
| lvm-extend | — | — | — | — | — | — | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — |
| local-package-repository | — | — | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — |
| file-integrity-baseline | — | — | — | — | — | — | — | — |
| **Average** | — | — | — | 11.9/2.7 | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | [3m 24s](../../../jobs/5469/2026-09-03__09-21-41/account-resource-limits-bash-rhel7-5469/analysis.md) | — | — | — | — |
| application-log-rotation | — | — | — | [4m 42s](../../../jobs/5469/2026-09-03__09-21-41/application-log-rotation-bash-rhel7-5469/analysis.md) | — | — | — | — |
| custom-ca-trust | — | — | — | [4m 04s](../../../jobs/5469/2026-09-03__09-21-41/custom-ca-trust-bash-rhel7-5469/analysis.md) | — | — | — | — |
| host-firewall-baseline | — | — | — | [7m 46s](../../../jobs/5469/2026-09-03__09-21-41/host-firewall-baseline-bash-rhel7-5469/analysis.md) | — | — | — | — |
| kernel-network-hardening | — | — | — | [4m 32s](../../../jobs/5469/2026-09-03__09-21-41/kernel-network-hardening-bash-rhel7-5469/analysis.md) | — | — | — | — |
| repair-application-permissions | — | — | — | [4m 50s](../../../jobs/5469/2026-09-03__09-21-41/repair-application-permissions-bash-rhel7-5469/analysis.md) | — | — | — | — |
| scheduled-maintenance | — | — | — | [4m 10s](../../../jobs/5469/2026-09-03__09-21-41/scheduled-maintenance-bash-rhel7-5469/analysis.md) | — | — | — | — |
| ssh-key-only | — | — | — | [4m 48s](../../../jobs/5469/2026-09-03__09-21-41/ssh-key-only-bash-rhel7-5469/analysis.md) | — | — | — | — |
| sticky-drop-directory | — | — | — | [3m 41s](../../../jobs/5469/2026-09-03__09-21-41/sticky-drop-directory-bash-rhel7-5469/analysis.md) | — | — | — | — |
| unprivileged-service | — | — | — | [4m 45s](../../../jobs/5469/2026-09-03__09-21-41/unprivileged-service-bash-rhel7-5469/analysis.md) | — | — | — | — |
| mandatory-access-control-port | — | — | — | — | — | — | — | — |
| kernel-module-blacklist | — | — | — | — | — | — | — | — |
| boot-kernel-parameter | — | — | — | — | — | — | — | — |
| mount-option-hardening | — | — | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — |
| sudo-command-logging | — | — | — | — | — | — | — | — |
| cron-access-control | — | — | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — |
| encrypted-volume | — | — | — | — | — | — | — | — |
| lvm-extend | — | — | — | — | — | — | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — |
| local-package-repository | — | — | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — |
| file-integrity-baseline | — | — | — | — | — | — | — | — |
| **Average** | — | — | — | 4m 40s | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 666 ms across 10 clusters, about 0.26% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | [0.950](../../../jobs/5469/2026-09-03__09-21-41/account-resource-limits-bash-rhel7-5469/analysis.md) | — | — | — | — |
| application-log-rotation | — | — | — | [0.700](../../../jobs/5469/2026-09-03__09-21-41/application-log-rotation-bash-rhel7-5469/analysis.md) | — | — | — | — |
| custom-ca-trust | — | — | — | [0.950](../../../jobs/5469/2026-09-03__09-21-41/custom-ca-trust-bash-rhel7-5469/analysis.md) | — | — | — | — |
| host-firewall-baseline | — | — | — | [0.650](../../../jobs/5469/2026-09-03__09-21-41/host-firewall-baseline-bash-rhel7-5469/analysis.md) | — | — | — | — |
| kernel-network-hardening | — | — | — | [1.000](../../../jobs/5469/2026-09-03__09-21-41/kernel-network-hardening-bash-rhel7-5469/analysis.md) | — | — | — | — |
| repair-application-permissions | — | — | — | [0.950](../../../jobs/5469/2026-09-03__09-21-41/repair-application-permissions-bash-rhel7-5469/analysis.md) | — | — | — | — |
| scheduled-maintenance | — | — | — | [0.930](../../../jobs/5469/2026-09-03__09-21-41/scheduled-maintenance-bash-rhel7-5469/analysis.md) | — | — | — | — |
| ssh-key-only | — | — | — | [0.900](../../../jobs/5469/2026-09-03__09-21-41/ssh-key-only-bash-rhel7-5469/analysis.md) | — | — | — | — |
| sticky-drop-directory | — | — | — | [0.850](../../../jobs/5469/2026-09-03__09-21-41/sticky-drop-directory-bash-rhel7-5469/analysis.md) | — | — | — | — |
| unprivileged-service | — | — | — | [0.900](../../../jobs/5469/2026-09-03__09-21-41/unprivileged-service-bash-rhel7-5469/analysis.md) | — | — | — | — |
| mandatory-access-control-port | — | — | — | — | — | — | — | — |
| kernel-module-blacklist | — | — | — | — | — | — | — | — |
| boot-kernel-parameter | — | — | — | — | — | — | — | — |
| mount-option-hardening | — | — | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — |
| sudo-command-logging | — | — | — | — | — | — | — | — |
| cron-access-control | — | — | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — |
| encrypted-volume | — | — | — | — | — | — | — | — |
| lvm-extend | — | — | — | — | — | — | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — |
| local-package-repository | — | — | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — |
| file-integrity-baseline | — | — | — | — | — | — | — | — |
| **Average** | — | — | — | 0.878 | — | — | — | — |
