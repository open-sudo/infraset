# single-node-os-comparison: command execution summary

Scope: `6324/2026-10-03__19-23-12`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — |
| application-log-rotation | — | — | — | — | — | — | — | — |
| custom-ca-trust | — | — | — | — | — | — | — | — |
| host-firewall-baseline | — | — | — | — | — | — | — | — |
| kernel-network-hardening | — | — | — | — | — | — | — | — |
| repair-application-permissions | — | — | — | — | — | — | — | — |
| scheduled-maintenance | — | — | — | — | — | — | — | — |
| ssh-key-only | — | — | — | — | — | — | — | — |
| sticky-drop-directory | — | — | — | — | — | — | — | — |
| unprivileged-service | — | — | — | — | — | — | — | — |
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
| certificate-rotation | — | — | — | — | [11/4](../../../jobs/6324/2026-10-03__19-23-12/certificate-rotation-bash-rhel9-6324) | — | — | — |
| file-integrity-baseline | — | — | — | — | — | — | — | — |
| **Average** | — | — | — | — | 11.0/4.0 | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — |
| application-log-rotation | — | — | — | — | — | — | — | — |
| custom-ca-trust | — | — | — | — | — | — | — | — |
| host-firewall-baseline | — | — | — | — | — | — | — | — |
| kernel-network-hardening | — | — | — | — | — | — | — | — |
| repair-application-permissions | — | — | — | — | — | — | — | — |
| scheduled-maintenance | — | — | — | — | — | — | — | — |
| ssh-key-only | — | — | — | — | — | — | — | — |
| sticky-drop-directory | — | — | — | — | — | — | — | — |
| unprivileged-service | — | — | — | — | — | — | — | — |
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
| certificate-rotation | — | — | — | — | [4m 08s](../../../jobs/6324/2026-10-03__19-23-12/certificate-rotation-bash-rhel9-6324) | — | — | — |
| file-integrity-baseline | — | — | — | — | — | — | — | — |
| **Average** | — | — | — | — | 4m 08s | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 661 ms across 1 clusters, about 0.27% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — |
| application-log-rotation | — | — | — | — | — | — | — | — |
| custom-ca-trust | — | — | — | — | — | — | — | — |
| host-firewall-baseline | — | — | — | — | — | — | — | — |
| kernel-network-hardening | — | — | — | — | — | — | — | — |
| repair-application-permissions | — | — | — | — | — | — | — | — |
| scheduled-maintenance | — | — | — | — | — | — | — | — |
| ssh-key-only | — | — | — | — | — | — | — | — |
| sticky-drop-directory | — | — | — | — | — | — | — | — |
| unprivileged-service | — | — | — | — | — | — | — | — |
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
| certificate-rotation | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-23-12/certificate-rotation-bash-rhel9-6324) | — | — | — |
| file-integrity-baseline | — | — | — | — | — | — | — | — |
| **Average** | — | — | — | — | 0.970 | — | — | — |
