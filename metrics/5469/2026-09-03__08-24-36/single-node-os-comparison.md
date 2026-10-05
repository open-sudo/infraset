# single-node-os-comparison: command execution summary

Scope: `5469/2026-09-03__08-24-36`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [6/1](../../../jobs/5469/2026-09-03__08-24-36/account-resource-limits-bash-rhel10-5469/analysis.md) | — | — |
| application-log-rotation | — | — | — | — | — | [12/0](../../../jobs/5469/2026-09-03__08-24-36/application-log-rotation-bash-rhel10-5469/analysis.md) | — | — |
| custom-ca-trust | — | — | — | — | — | [10/0](../../../jobs/5469/2026-09-03__08-24-36/custom-ca-trust-bash-rhel10-5469/analysis.md) | — | — |
| host-firewall-baseline | — | — | — | — | — | [14/1](../../../jobs/5469/2026-09-03__08-24-36/host-firewall-baseline-bash-rhel10-5469/analysis.md) | — | — |
| kernel-network-hardening | — | — | — | — | — | [10/0](../../../jobs/5469/2026-09-03__08-24-36/kernel-network-hardening-bash-rhel10-5469/analysis.md) | — | — |
| repair-application-permissions | — | — | — | — | — | [13/2](../../../jobs/5469/2026-09-03__08-24-36/repair-application-permissions-bash-rhel10-5469/analysis.md) | — | — |
| scheduled-maintenance | — | — | — | — | — | [12/1](../../../jobs/5469/2026-09-03__08-24-36/scheduled-maintenance-bash-rhel10-5469/analysis.md) | — | — |
| ssh-key-only | — | — | — | — | — | [19/0](../../../jobs/5469/2026-09-03__08-24-36/ssh-key-only-bash-rhel10-5469/analysis.md) | — | — |
| sticky-drop-directory | — | — | — | — | — | [14/0](../../../jobs/5469/2026-09-03__08-24-36/sticky-drop-directory-bash-rhel10-5469/analysis.md) | — | — |
| unprivileged-service | — | — | — | — | — | [8/1](../../../jobs/5469/2026-09-03__08-24-36/unprivileged-service-bash-rhel10-5469/analysis.md) | — | — |
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
| **Average** | — | — | — | — | — | 11.8/0.6 | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [2m 01s](../../../jobs/5469/2026-09-03__08-24-36/account-resource-limits-bash-rhel10-5469/analysis.md) | — | — |
| application-log-rotation | — | — | — | — | — | [2m 30s](../../../jobs/5469/2026-09-03__08-24-36/application-log-rotation-bash-rhel10-5469/analysis.md) | — | — |
| custom-ca-trust | — | — | — | — | — | [2m 22s](../../../jobs/5469/2026-09-03__08-24-36/custom-ca-trust-bash-rhel10-5469/analysis.md) | — | — |
| host-firewall-baseline | — | — | — | — | — | [3m 17s](../../../jobs/5469/2026-09-03__08-24-36/host-firewall-baseline-bash-rhel10-5469/analysis.md) | — | — |
| kernel-network-hardening | — | — | — | — | — | [2m 36s](../../../jobs/5469/2026-09-03__08-24-36/kernel-network-hardening-bash-rhel10-5469/analysis.md) | — | — |
| repair-application-permissions | — | — | — | — | — | [2m 24s](../../../jobs/5469/2026-09-03__08-24-36/repair-application-permissions-bash-rhel10-5469/analysis.md) | — | — |
| scheduled-maintenance | — | — | — | — | — | [2m 38s](../../../jobs/5469/2026-09-03__08-24-36/scheduled-maintenance-bash-rhel10-5469/analysis.md) | — | — |
| ssh-key-only | — | — | — | — | — | [2m 52s](../../../jobs/5469/2026-09-03__08-24-36/ssh-key-only-bash-rhel10-5469/analysis.md) | — | — |
| sticky-drop-directory | — | — | — | — | — | [2m 43s](../../../jobs/5469/2026-09-03__08-24-36/sticky-drop-directory-bash-rhel10-5469/analysis.md) | — | — |
| unprivileged-service | — | — | — | — | — | [2m 01s](../../../jobs/5469/2026-09-03__08-24-36/unprivileged-service-bash-rhel10-5469/analysis.md) | — | — |
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
| **Average** | — | — | — | — | — | 2m 33s | — | — |

Cluster provisioning is not a meaningful part of these times: median 852 ms across 10 clusters, about 0.57% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [0.900](../../../jobs/5469/2026-09-03__08-24-36/account-resource-limits-bash-rhel10-5469/analysis.md) | — | — |
| application-log-rotation | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__08-24-36/application-log-rotation-bash-rhel10-5469/analysis.md) | — | — |
| custom-ca-trust | — | — | — | — | — | [0.900](../../../jobs/5469/2026-09-03__08-24-36/custom-ca-trust-bash-rhel10-5469/analysis.md) | — | — |
| host-firewall-baseline | — | — | — | — | — | [0.700](../../../jobs/5469/2026-09-03__08-24-36/host-firewall-baseline-bash-rhel10-5469/analysis.md) | — | — |
| kernel-network-hardening | — | — | — | — | — | [0.900](../../../jobs/5469/2026-09-03__08-24-36/kernel-network-hardening-bash-rhel10-5469/analysis.md) | — | — |
| repair-application-permissions | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__08-24-36/repair-application-permissions-bash-rhel10-5469/analysis.md) | — | — |
| scheduled-maintenance | — | — | — | — | — | [0.900](../../../jobs/5469/2026-09-03__08-24-36/scheduled-maintenance-bash-rhel10-5469/analysis.md) | — | — |
| ssh-key-only | — | — | — | — | — | [0.950](../../../jobs/5469/2026-09-03__08-24-36/ssh-key-only-bash-rhel10-5469/analysis.md) | — | — |
| sticky-drop-directory | — | — | — | — | — | [0.700](../../../jobs/5469/2026-09-03__08-24-36/sticky-drop-directory-bash-rhel10-5469/analysis.md) | — | — |
| unprivileged-service | — | — | — | — | — | [0.900](../../../jobs/5469/2026-09-03__08-24-36/unprivileged-service-bash-rhel10-5469/analysis.md) | — | — |
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
| **Average** | — | — | — | — | — | 0.875 | — | — |
