# single-node-os-comparison: command execution summary

Scope: `9622/2026-10-04__09-20-16`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | [6/0](../../../jobs/9622/2026-10-04__09-20-16/account-resource-limits-bash-almalinux9-9622) | — | — | — | — | — | — |
| application-log-rotation | — | [11/0](../../../jobs/9622/2026-10-04__09-20-16/application-log-rotation-bash-almalinux9-9622) | — | — | — | — | — | — |
| custom-ca-trust | — | [10/0](../../../jobs/9622/2026-10-04__09-20-16/custom-ca-trust-bash-almalinux9-9622) | — | — | — | — | — | — |
| host-firewall-baseline | — | [15/0](../../../jobs/9622/2026-10-04__09-20-16/host-firewall-baseline-bash-almalinux9-9622) | — | — | — | — | — | — |
| kernel-network-hardening | — | [9/0](../../../jobs/9622/2026-10-04__09-20-16/kernel-network-hardening-bash-almalinux9-9622) | — | — | — | — | — | — |
| repair-application-permissions | — | [9/0](../../../jobs/9622/2026-10-04__09-20-16/repair-application-permissions-bash-almalinux9-9622) | — | — | — | — | — | — |
| scheduled-maintenance | — | [11/1](../../../jobs/9622/2026-10-04__09-20-16/scheduled-maintenance-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-key-only | — | [12/0](../../../jobs/9622/2026-10-04__09-20-16/ssh-key-only-bash-almalinux9-9622) | — | — | — | — | — | — |
| sticky-drop-directory | — | [8/0](../../../jobs/9622/2026-10-04__09-20-16/sticky-drop-directory-bash-almalinux9-9622) | — | — | — | — | — | — |
| unprivileged-service | — | [10/0](../../../jobs/9622/2026-10-04__09-20-16/unprivileged-service-bash-almalinux9-9622) | — | — | — | — | — | — |
| mandatory-access-control-port | — | [14/0](../../../jobs/9622/2026-10-04__09-20-16/mandatory-access-control-port-bash-almalinux9-9622) | — | — | — | — | — | — |
| kernel-module-blacklist | — | [11/0](../../../jobs/9622/2026-10-04__09-20-16/kernel-module-blacklist-bash-almalinux9-9622) | — | — | — | — | — | — |
| boot-kernel-parameter | — | [6/0](../../../jobs/9622/2026-10-04__09-20-16/boot-kernel-parameter-bash-almalinux9-9622) | — | — | — | — | — | — |
| mount-option-hardening | — | [13/0](../../../jobs/9622/2026-10-04__09-20-16/mount-option-hardening-bash-almalinux9-9622) | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | [8/0](../../../jobs/9622/2026-10-04__09-20-16/password-complexity-policy-bash-almalinux9-9622) | — | — | — | — | — | — |
| sudo-command-logging | — | [12/0](../../../jobs/9622/2026-10-04__09-20-16/sudo-command-logging-bash-almalinux9-9622) | — | — | — | — | — | — |
| cron-access-control | — | [9/0](../../../jobs/9622/2026-10-04__09-20-16/cron-access-control-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | [10/1](../../../jobs/9622/2026-10-04__09-20-16/disk-quota-bash-almalinux9-9622) | — | — | — | — | — | — |
| encrypted-volume | — | [16/0](../../../jobs/9622/2026-10-04__09-20-16/encrypted-volume-bash-almalinux9-9622) | — | — | — | — | — | — |
| lvm-extend | — | [11/1](../../../jobs/9622/2026-10-04__09-20-16/lvm-extend-bash-almalinux9-9622) | — | — | — | — | — | — |
| filesystem-snapshot-rollback | — | [12/0](../../../jobs/9622/2026-10-04__09-20-16/filesystem-snapshot-rollback-bash-almalinux9-9622) | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | [11/0](../../../jobs/9622/2026-10-04__09-20-16/package-version-hold-bash-almalinux9-9622) | — | — | — | — | — | — |
| local-package-repository | — | [12/1](../../../jobs/9622/2026-10-04__09-20-16/local-package-repository-bash-almalinux9-9622) | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | [19/1](../../../jobs/9622/2026-10-04__09-20-16/certificate-rotation-bash-almalinux9-9622) | — | — | — | — | — | — |
| file-integrity-baseline | — | [26/0](../../../jobs/9622/2026-10-04__09-20-16/file-integrity-baseline-bash-almalinux9-9622) | — | — | — | — | — | — |
| archive-member-safety | — | [14/1](../../../jobs/9622/2026-10-04__09-20-16/archive-member-safety-bash-almalinux9-9622) | — | — | — | — | — | — |
| atomic-release-publication | — | [9/0](../../../jobs/9622/2026-10-04__09-20-16/atomic-release-publication-bash-almalinux9-9622) | — | — | — | — | — | — |
| batch-exclusive-lock | — | [10/1](../../../jobs/9622/2026-10-04__09-20-16/batch-exclusive-lock-bash-almalinux9-9622) | — | — | — | — | — | — |
| cgi-report-execution | — | [14/0](../../../jobs/9622/2026-10-04__09-20-16/cgi-report-execution-bash-almalinux9-9622) | — | — | — | — | — | — |
| child-process-reaping | — | [11/1](../../../jobs/9622/2026-10-04__09-20-16/child-process-reaping-bash-almalinux9-9622) | — | — | — | — | — | — |
| chroot-web-service | — | [16/2](../../../jobs/9622/2026-10-04__09-20-16/chroot-web-service-bash-almalinux9-9622) | — | — | — | — | — | — |
| cross-file-accounting-reconciliation | — | [9/0](../../../jobs/9622/2026-10-04__09-20-16/cross-file-accounting-reconciliation-bash-almalinux9-9622) | — | — | — | — | — | — |
| deleted-open-file-recovery | — | [13/2](../../../jobs/9622/2026-10-04__09-20-16/deleted-open-file-recovery-bash-almalinux9-9622) | — | — | — | — | — | — |
| fifo-worker-reconnection | — | [11/1](../../../jobs/9622/2026-10-04__09-20-16/fifo-worker-reconnection-bash-almalinux9-9622) | — | — | — | — | — | — |
| file-descriptor-leak | — | [10/1](../../../jobs/9622/2026-10-04__09-20-16/file-descriptor-leak-bash-almalinux9-9622) | — | — | — | — | — | — |
| filename-encoding-migration | — | [9/0](../../../jobs/9622/2026-10-04__09-20-16/filename-encoding-migration-bash-almalinux9-9622) | — | — | — | — | — | — |
| fixed-width-import-recovery | — | [10/0](../../../jobs/9622/2026-10-04__09-20-16/fixed-width-import-recovery-bash-almalinux9-9622) | — | — | — | — | — | — |
| hardlink-aware-deduplication | — | [12/0](../../../jobs/9622/2026-10-04__09-20-16/hardlink-aware-deduplication-bash-almalinux9-9622) | — | — | — | — | — | — |
| incremental-archive-chain | — | [8/0](../../../jobs/9622/2026-10-04__09-20-16/incremental-archive-chain-bash-almalinux9-9622) | — | — | — | — | — | — |
| inherited-directory-acls | — | [8/0](../../../jobs/9622/2026-10-04__09-20-16/inherited-directory-acls-bash-almalinux9-9622) | — | — | — | — | — | — |
| inode-cache-retention | — | [0/0](../../../jobs/9622/2026-10-04__09-20-16/inode-cache-retention-bash-almalinux9-9622) | — | — | — | — | — | — |
| large-counter-overflow | — | [12/0](../../../jobs/9622/2026-10-04__09-20-16/large-counter-overflow-bash-almalinux9-9622) | — | — | — | — | — | — |
| mail-filter-routing | — | [9/0](../../../jobs/9622/2026-10-04__09-20-16/mail-filter-routing-bash-almalinux9-9622) | — | — | — | — | — | — |
| mail-spool-deduplication | — | [10/0](../../../jobs/9622/2026-10-04__09-20-16/mail-spool-deduplication-bash-almalinux9-9622) | — | — | — | — | — | — |
| minimal-environment-job | — | [12/0](../../../jobs/9622/2026-10-04__09-20-16/minimal-environment-job-bash-almalinux9-9622) | — | — | — | — | — | — |
| name-based-web-tenants | — | [13/1](../../../jobs/9622/2026-10-04__09-20-16/name-based-web-tenants-bash-almalinux9-9622) | — | — | — | — | — | — |
| numeric-record-ordering | — | [14/0](../../../jobs/9622/2026-10-04__09-20-16/numeric-record-ordering-bash-almalinux9-9622) | — | — | — | — | — | — |
| permanent-url-migration | — | [11/0](../../../jobs/9622/2026-10-04__09-20-16/permanent-url-migration-bash-almalinux9-9622) | — | — | — | — | — | — |
| persistent-swap | — | [9/1](../../../jobs/9622/2026-10-04__09-20-16/persistent-swap-bash-almalinux9-9622) | — | — | — | — | — | — |
| posix-shell-installer | — | [10/0](../../../jobs/9622/2026-10-04__09-20-16/posix-shell-installer-bash-almalinux9-9622) | — | — | — | — | — | — |
| postgresql-sequence-repair | — | [13/0](../../../jobs/9622/2026-10-04__09-20-16/postgresql-sequence-repair-bash-almalinux9-9622) | — | — | — | — | — | — |
| print-spool-recovery | — | [16/1](../../../jobs/9622/2026-10-04__09-20-16/print-spool-recovery-bash-almalinux9-9622) | — | — | — | — | — | — |
| privacy-safe-support-export | — | [11/0](../../../jobs/9622/2026-10-04__09-20-16/privacy-safe-support-export-bash-almalinux9-9622) | — | — | — | — | — | — |
| relative-symlink-relocation | — | [8/1](../../../jobs/9622/2026-10-04__09-20-16/relative-symlink-relocation-bash-almalinux9-9622) | — | — | — | — | — | — |
| selective-tape-restore | — | [10/0](../../../jobs/9622/2026-10-04__09-20-16/selective-tape-restore-bash-almalinux9-9622) | — | — | — | — | — | — |
| service-confinement | — | [11/2](../../../jobs/9622/2026-10-04__09-20-16/service-confinement-bash-almalinux9-9622) | — | — | — | — | — | — |
| service-resource-limits | — | [12/0](../../../jobs/9622/2026-10-04__09-20-16/service-resource-limits-bash-almalinux9-9622) | — | — | — | — | — | — |
| signal-driven-config-reload | — | [13/2](../../../jobs/9622/2026-10-04__09-20-16/signal-driven-config-reload-bash-almalinux9-9622) | — | — | — | — | — | — |
| sparse-image-copy | — | [12/0](../../../jobs/9622/2026-10-04__09-20-16/sparse-image-copy-bash-almalinux9-9622) | — | — | — | — | — | — |
| sqlite-lock-contention | — | [11/0](../../../jobs/9622/2026-10-04__09-20-16/sqlite-lock-contention-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-host-key-pinning | — | [11/0](../../../jobs/9622/2026-10-04__09-20-16/ssh-host-key-pinning-bash-almalinux9-9622) | — | — | — | — | — | — |
| stale-pidfile-startup | — | [17/0](../../../jobs/9622/2026-10-04__09-20-16/stale-pidfile-startup-bash-almalinux9-9622) | — | — | — | — | — | — |
| temporary-file-symlink-defense | — | [13/0](../../../jobs/9622/2026-10-04__09-20-16/temporary-file-symlink-defense-bash-almalinux9-9622) | — | — | — | — | — | — |
| text-export-normalization | — | [9/0](../../../jobs/9622/2026-10-04__09-20-16/text-export-normalization-bash-almalinux9-9622) | — | — | — | — | — | — |
| timezone-log-merge | — | [18/1](../../../jobs/9622/2026-10-04__09-20-16/timezone-log-merge-bash-almalinux9-9622) | — | — | — | — | — | — |
| transactional-schema-upgrade | — | [11/1](../../../jobs/9622/2026-10-04__09-20-16/transactional-schema-upgrade-bash-almalinux9-9622) | — | — | — | — | — | — |
| unix-socket-access-boundary | — | [11/1](../../../jobs/9622/2026-10-04__09-20-16/unix-socket-access-boundary-bash-almalinux9-9622) | — | — | — | — | — | — |
| web-authentication-boundary | — | [17/3](../../../jobs/9622/2026-10-04__09-20-16/web-authentication-boundary-bash-almalinux9-9622) | — | — | — | — | — | — |
| webdav-document-locks | — | [17/0](../../../jobs/9622/2026-10-04__09-20-16/webdav-document-locks-bash-almalinux9-9622) | — | — | — | — | — | — |
| working-directory-independent-launch | — | [12/1](../../../jobs/9622/2026-10-04__09-20-16/working-directory-independent-launch-bash-almalinux9-9622) | — | — | — | — | — | — |
| **Average** | — | 11.5/0.4 | — | — | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | [1m 44s](../../../jobs/9622/2026-10-04__09-20-16/account-resource-limits-bash-almalinux9-9622) | — | — | — | — | — | — |
| application-log-rotation | — | [2m 50s](../../../jobs/9622/2026-10-04__09-20-16/application-log-rotation-bash-almalinux9-9622) | — | — | — | — | — | — |
| custom-ca-trust | — | [2m 18s](../../../jobs/9622/2026-10-04__09-20-16/custom-ca-trust-bash-almalinux9-9622) | — | — | — | — | — | — |
| host-firewall-baseline | — | [3m 12s](../../../jobs/9622/2026-10-04__09-20-16/host-firewall-baseline-bash-almalinux9-9622) | — | — | — | — | — | — |
| kernel-network-hardening | — | [1m 54s](../../../jobs/9622/2026-10-04__09-20-16/kernel-network-hardening-bash-almalinux9-9622) | — | — | — | — | — | — |
| repair-application-permissions | — | [2m 20s](../../../jobs/9622/2026-10-04__09-20-16/repair-application-permissions-bash-almalinux9-9622) | — | — | — | — | — | — |
| scheduled-maintenance | — | [2m 15s](../../../jobs/9622/2026-10-04__09-20-16/scheduled-maintenance-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-key-only | — | [2m 54s](../../../jobs/9622/2026-10-04__09-20-16/ssh-key-only-bash-almalinux9-9622) | — | — | — | — | — | — |
| sticky-drop-directory | — | [2m 14s](../../../jobs/9622/2026-10-04__09-20-16/sticky-drop-directory-bash-almalinux9-9622) | — | — | — | — | — | — |
| unprivileged-service | — | [2m 09s](../../../jobs/9622/2026-10-04__09-20-16/unprivileged-service-bash-almalinux9-9622) | — | — | — | — | — | — |
| mandatory-access-control-port | — | [3m 10s](../../../jobs/9622/2026-10-04__09-20-16/mandatory-access-control-port-bash-almalinux9-9622) | — | — | — | — | — | — |
| kernel-module-blacklist | — | [2m 31s](../../../jobs/9622/2026-10-04__09-20-16/kernel-module-blacklist-bash-almalinux9-9622) | — | — | — | — | — | — |
| boot-kernel-parameter | — | [1m 44s](../../../jobs/9622/2026-10-04__09-20-16/boot-kernel-parameter-bash-almalinux9-9622) | — | — | — | — | — | — |
| mount-option-hardening | — | [4m 20s](../../../jobs/9622/2026-10-04__09-20-16/mount-option-hardening-bash-almalinux9-9622) | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | [2m 10s](../../../jobs/9622/2026-10-04__09-20-16/password-complexity-policy-bash-almalinux9-9622) | — | — | — | — | — | — |
| sudo-command-logging | — | [2m 34s](../../../jobs/9622/2026-10-04__09-20-16/sudo-command-logging-bash-almalinux9-9622) | — | — | — | — | — | — |
| cron-access-control | — | [2m 24s](../../../jobs/9622/2026-10-04__09-20-16/cron-access-control-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | [2m 38s](../../../jobs/9622/2026-10-04__09-20-16/disk-quota-bash-almalinux9-9622) | — | — | — | — | — | — |
| encrypted-volume | — | [3m 28s](../../../jobs/9622/2026-10-04__09-20-16/encrypted-volume-bash-almalinux9-9622) | — | — | — | — | — | — |
| lvm-extend | — | [3m 14s](../../../jobs/9622/2026-10-04__09-20-16/lvm-extend-bash-almalinux9-9622) | — | — | — | — | — | — |
| filesystem-snapshot-rollback | — | [3m 59s](../../../jobs/9622/2026-10-04__09-20-16/filesystem-snapshot-rollback-bash-almalinux9-9622) | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | [2m 51s](../../../jobs/9622/2026-10-04__09-20-16/package-version-hold-bash-almalinux9-9622) | — | — | — | — | — | — |
| local-package-repository | — | [3m 24s](../../../jobs/9622/2026-10-04__09-20-16/local-package-repository-bash-almalinux9-9622) | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | [5m 20s](../../../jobs/9622/2026-10-04__09-20-16/certificate-rotation-bash-almalinux9-9622) | — | — | — | — | — | — |
| file-integrity-baseline | — | [5m 22s](../../../jobs/9622/2026-10-04__09-20-16/file-integrity-baseline-bash-almalinux9-9622) | — | — | — | — | — | — |
| archive-member-safety | — | [3m 54s](../../../jobs/9622/2026-10-04__09-20-16/archive-member-safety-bash-almalinux9-9622) | — | — | — | — | — | — |
| atomic-release-publication | — | [3m 06s](../../../jobs/9622/2026-10-04__09-20-16/atomic-release-publication-bash-almalinux9-9622) | — | — | — | — | — | — |
| batch-exclusive-lock | — | [3m 19s](../../../jobs/9622/2026-10-04__09-20-16/batch-exclusive-lock-bash-almalinux9-9622) | — | — | — | — | — | — |
| cgi-report-execution | — | [3m 44s](../../../jobs/9622/2026-10-04__09-20-16/cgi-report-execution-bash-almalinux9-9622) | — | — | — | — | — | — |
| child-process-reaping | — | [4m 21s](../../../jobs/9622/2026-10-04__09-20-16/child-process-reaping-bash-almalinux9-9622) | — | — | — | — | — | — |
| chroot-web-service | — | [3m 31s](../../../jobs/9622/2026-10-04__09-20-16/chroot-web-service-bash-almalinux9-9622) | — | — | — | — | — | — |
| cross-file-accounting-reconciliation | — | [2m 59s](../../../jobs/9622/2026-10-04__09-20-16/cross-file-accounting-reconciliation-bash-almalinux9-9622) | — | — | — | — | — | — |
| deleted-open-file-recovery | — | [3m 59s](../../../jobs/9622/2026-10-04__09-20-16/deleted-open-file-recovery-bash-almalinux9-9622) | — | — | — | — | — | — |
| fifo-worker-reconnection | — | [3m 15s](../../../jobs/9622/2026-10-04__09-20-16/fifo-worker-reconnection-bash-almalinux9-9622) | — | — | — | — | — | — |
| file-descriptor-leak | — | [3m 13s](../../../jobs/9622/2026-10-04__09-20-16/file-descriptor-leak-bash-almalinux9-9622) | — | — | — | — | — | — |
| filename-encoding-migration | — | [2m 46s](../../../jobs/9622/2026-10-04__09-20-16/filename-encoding-migration-bash-almalinux9-9622) | — | — | — | — | — | — |
| fixed-width-import-recovery | — | [2m 47s](../../../jobs/9622/2026-10-04__09-20-16/fixed-width-import-recovery-bash-almalinux9-9622) | — | — | — | — | — | — |
| hardlink-aware-deduplication | — | [3m 06s](../../../jobs/9622/2026-10-04__09-20-16/hardlink-aware-deduplication-bash-almalinux9-9622) | — | — | — | — | — | — |
| incremental-archive-chain | — | [2m 08s](../../../jobs/9622/2026-10-04__09-20-16/incremental-archive-chain-bash-almalinux9-9622) | — | — | — | — | — | — |
| inherited-directory-acls | — | [2m 41s](../../../jobs/9622/2026-10-04__09-20-16/inherited-directory-acls-bash-almalinux9-9622) | — | — | — | — | — | — |
| inode-cache-retention | — | [5s](../../../jobs/9622/2026-10-04__09-20-16/inode-cache-retention-bash-almalinux9-9622) | — | — | — | — | — | — |
| large-counter-overflow | — | [3m 46s](../../../jobs/9622/2026-10-04__09-20-16/large-counter-overflow-bash-almalinux9-9622) | — | — | — | — | — | — |
| mail-filter-routing | — | [2m 36s](../../../jobs/9622/2026-10-04__09-20-16/mail-filter-routing-bash-almalinux9-9622) | — | — | — | — | — | — |
| mail-spool-deduplication | — | [3m 08s](../../../jobs/9622/2026-10-04__09-20-16/mail-spool-deduplication-bash-almalinux9-9622) | — | — | — | — | — | — |
| minimal-environment-job | — | [3m 03s](../../../jobs/9622/2026-10-04__09-20-16/minimal-environment-job-bash-almalinux9-9622) | — | — | — | — | — | — |
| name-based-web-tenants | — | [3m 31s](../../../jobs/9622/2026-10-04__09-20-16/name-based-web-tenants-bash-almalinux9-9622) | — | — | — | — | — | — |
| numeric-record-ordering | — | [3m 33s](../../../jobs/9622/2026-10-04__09-20-16/numeric-record-ordering-bash-almalinux9-9622) | — | — | — | — | — | — |
| permanent-url-migration | — | [2m 41s](../../../jobs/9622/2026-10-04__09-20-16/permanent-url-migration-bash-almalinux9-9622) | — | — | — | — | — | — |
| persistent-swap | — | [2m 04s](../../../jobs/9622/2026-10-04__09-20-16/persistent-swap-bash-almalinux9-9622) | — | — | — | — | — | — |
| posix-shell-installer | — | [2m 40s](../../../jobs/9622/2026-10-04__09-20-16/posix-shell-installer-bash-almalinux9-9622) | — | — | — | — | — | — |
| postgresql-sequence-repair | — | [3m 27s](../../../jobs/9622/2026-10-04__09-20-16/postgresql-sequence-repair-bash-almalinux9-9622) | — | — | — | — | — | — |
| print-spool-recovery | — | [6m 28s](../../../jobs/9622/2026-10-04__09-20-16/print-spool-recovery-bash-almalinux9-9622) | — | — | — | — | — | — |
| privacy-safe-support-export | — | [4m 40s](../../../jobs/9622/2026-10-04__09-20-16/privacy-safe-support-export-bash-almalinux9-9622) | — | — | — | — | — | — |
| relative-symlink-relocation | — | [3m 07s](../../../jobs/9622/2026-10-04__09-20-16/relative-symlink-relocation-bash-almalinux9-9622) | — | — | — | — | — | — |
| selective-tape-restore | — | [1m 30s](../../../jobs/9622/2026-10-04__09-20-16/selective-tape-restore-bash-almalinux9-9622) | — | — | — | — | — | — |
| service-confinement | — | [4m 19s](../../../jobs/9622/2026-10-04__09-20-16/service-confinement-bash-almalinux9-9622) | — | — | — | — | — | — |
| service-resource-limits | — | [2m 10s](../../../jobs/9622/2026-10-04__09-20-16/service-resource-limits-bash-almalinux9-9622) | — | — | — | — | — | — |
| signal-driven-config-reload | — | [29m 27s](../../../jobs/9622/2026-10-04__09-20-16/signal-driven-config-reload-bash-almalinux9-9622) | — | — | — | — | — | — |
| sparse-image-copy | — | [2m 22s](../../../jobs/9622/2026-10-04__09-20-16/sparse-image-copy-bash-almalinux9-9622) | — | — | — | — | — | — |
| sqlite-lock-contention | — | [4m 03s](../../../jobs/9622/2026-10-04__09-20-16/sqlite-lock-contention-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-host-key-pinning | — | [2m 40s](../../../jobs/9622/2026-10-04__09-20-16/ssh-host-key-pinning-bash-almalinux9-9622) | — | — | — | — | — | — |
| stale-pidfile-startup | — | [6m 36s](../../../jobs/9622/2026-10-04__09-20-16/stale-pidfile-startup-bash-almalinux9-9622) | — | — | — | — | — | — |
| temporary-file-symlink-defense | — | [4m 04s](../../../jobs/9622/2026-10-04__09-20-16/temporary-file-symlink-defense-bash-almalinux9-9622) | — | — | — | — | — | — |
| text-export-normalization | — | [2m 15s](../../../jobs/9622/2026-10-04__09-20-16/text-export-normalization-bash-almalinux9-9622) | — | — | — | — | — | — |
| timezone-log-merge | — | [4m 24s](../../../jobs/9622/2026-10-04__09-20-16/timezone-log-merge-bash-almalinux9-9622) | — | — | — | — | — | — |
| transactional-schema-upgrade | — | [3m 07s](../../../jobs/9622/2026-10-04__09-20-16/transactional-schema-upgrade-bash-almalinux9-9622) | — | — | — | — | — | — |
| unix-socket-access-boundary | — | [28m 34s](../../../jobs/9622/2026-10-04__09-20-16/unix-socket-access-boundary-bash-almalinux9-9622) | — | — | — | — | — | — |
| web-authentication-boundary | — | [4m 31s](../../../jobs/9622/2026-10-04__09-20-16/web-authentication-boundary-bash-almalinux9-9622) | — | — | — | — | — | — |
| webdav-document-locks | — | [4m 17s](../../../jobs/9622/2026-10-04__09-20-16/webdav-document-locks-bash-almalinux9-9622) | — | — | — | — | — | — |
| working-directory-independent-launch | — | [2m 58s](../../../jobs/9622/2026-10-04__09-20-16/working-directory-independent-launch-bash-almalinux9-9622) | — | — | — | — | — | — |
| **Average** | — | 3m 55s | — | — | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 1116 ms across 100 clusters, about 0.49% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/account-resource-limits-bash-almalinux9-9622) | — | — | — | — | — | — |
| application-log-rotation | — | [0.960](../../../jobs/9622/2026-10-04__09-20-16/application-log-rotation-bash-almalinux9-9622) | — | — | — | — | — | — |
| custom-ca-trust | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/custom-ca-trust-bash-almalinux9-9622) | — | — | — | — | — | — |
| host-firewall-baseline | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/host-firewall-baseline-bash-almalinux9-9622) | — | — | — | — | — | — |
| kernel-network-hardening | — | [0.970](../../../jobs/9622/2026-10-04__09-20-16/kernel-network-hardening-bash-almalinux9-9622) | — | — | — | — | — | — |
| repair-application-permissions | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/repair-application-permissions-bash-almalinux9-9622) | — | — | — | — | — | — |
| scheduled-maintenance | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/scheduled-maintenance-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-key-only | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/ssh-key-only-bash-almalinux9-9622) | — | — | — | — | — | — |
| sticky-drop-directory | — | [0.970](../../../jobs/9622/2026-10-04__09-20-16/sticky-drop-directory-bash-almalinux9-9622) | — | — | — | — | — | — |
| unprivileged-service | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/unprivileged-service-bash-almalinux9-9622) | — | — | — | — | — | — |
| mandatory-access-control-port | — | [0.970](../../../jobs/9622/2026-10-04__09-20-16/mandatory-access-control-port-bash-almalinux9-9622) | — | — | — | — | — | — |
| kernel-module-blacklist | — | [0.960](../../../jobs/9622/2026-10-04__09-20-16/kernel-module-blacklist-bash-almalinux9-9622) | — | — | — | — | — | — |
| boot-kernel-parameter | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/boot-kernel-parameter-bash-almalinux9-9622) | — | — | — | — | — | — |
| mount-option-hardening | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/mount-option-hardening-bash-almalinux9-9622) | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/password-complexity-policy-bash-almalinux9-9622) | — | — | — | — | — | — |
| sudo-command-logging | — | [0.940](../../../jobs/9622/2026-10-04__09-20-16/sudo-command-logging-bash-almalinux9-9622) | — | — | — | — | — | — |
| cron-access-control | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/cron-access-control-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/disk-quota-bash-almalinux9-9622) | — | — | — | — | — | — |
| encrypted-volume | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/encrypted-volume-bash-almalinux9-9622) | — | — | — | — | — | — |
| lvm-extend | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/lvm-extend-bash-almalinux9-9622) | — | — | — | — | — | — |
| filesystem-snapshot-rollback | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/filesystem-snapshot-rollback-bash-almalinux9-9622) | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/package-version-hold-bash-almalinux9-9622) | — | — | — | — | — | — |
| local-package-repository | — | [0.960](../../../jobs/9622/2026-10-04__09-20-16/local-package-repository-bash-almalinux9-9622) | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | [0.900](../../../jobs/9622/2026-10-04__09-20-16/certificate-rotation-bash-almalinux9-9622) | — | — | — | — | — | — |
| file-integrity-baseline | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/file-integrity-baseline-bash-almalinux9-9622) | — | — | — | — | — | — |
| archive-member-safety | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/archive-member-safety-bash-almalinux9-9622) | — | — | — | — | — | — |
| atomic-release-publication | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/atomic-release-publication-bash-almalinux9-9622) | — | — | — | — | — | — |
| batch-exclusive-lock | — | [0.780](../../../jobs/9622/2026-10-04__09-20-16/batch-exclusive-lock-bash-almalinux9-9622) | — | — | — | — | — | — |
| cgi-report-execution | — | [0.960](../../../jobs/9622/2026-10-04__09-20-16/cgi-report-execution-bash-almalinux9-9622) | — | — | — | — | — | — |
| child-process-reaping | — | [0.900](../../../jobs/9622/2026-10-04__09-20-16/child-process-reaping-bash-almalinux9-9622) | — | — | — | — | — | — |
| chroot-web-service | — | [0.900](../../../jobs/9622/2026-10-04__09-20-16/chroot-web-service-bash-almalinux9-9622) | — | — | — | — | — | — |
| cross-file-accounting-reconciliation | — | [0.840](../../../jobs/9622/2026-10-04__09-20-16/cross-file-accounting-reconciliation-bash-almalinux9-9622) | — | — | — | — | — | — |
| deleted-open-file-recovery | — | [0.840](../../../jobs/9622/2026-10-04__09-20-16/deleted-open-file-recovery-bash-almalinux9-9622) | — | — | — | — | — | — |
| fifo-worker-reconnection | — | [0.900](../../../jobs/9622/2026-10-04__09-20-16/fifo-worker-reconnection-bash-almalinux9-9622) | — | — | — | — | — | — |
| file-descriptor-leak | — | [0.900](../../../jobs/9622/2026-10-04__09-20-16/file-descriptor-leak-bash-almalinux9-9622) | — | — | — | — | — | — |
| filename-encoding-migration | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/filename-encoding-migration-bash-almalinux9-9622) | — | — | — | — | — | — |
| fixed-width-import-recovery | — | [0.880](../../../jobs/9622/2026-10-04__09-20-16/fixed-width-import-recovery-bash-almalinux9-9622) | — | — | — | — | — | — |
| hardlink-aware-deduplication | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/hardlink-aware-deduplication-bash-almalinux9-9622) | — | — | — | — | — | — |
| incremental-archive-chain | — | [0.970](../../../jobs/9622/2026-10-04__09-20-16/incremental-archive-chain-bash-almalinux9-9622) | — | — | — | — | — | — |
| inherited-directory-acls | — | [0.940](../../../jobs/9622/2026-10-04__09-20-16/inherited-directory-acls-bash-almalinux9-9622) | — | — | — | — | — | — |
| inode-cache-retention | — | — | — | — | — | — | — | — |
| large-counter-overflow | — | [0.830](../../../jobs/9622/2026-10-04__09-20-16/large-counter-overflow-bash-almalinux9-9622) | — | — | — | — | — | — |
| mail-filter-routing | — | [0.950](../../../jobs/9622/2026-10-04__09-20-16/mail-filter-routing-bash-almalinux9-9622) | — | — | — | — | — | — |
| mail-spool-deduplication | — | [0.980](../../../jobs/9622/2026-10-04__09-20-16/mail-spool-deduplication-bash-almalinux9-9622) | — | — | — | — | — | — |
| minimal-environment-job | — | [0.820](../../../jobs/9622/2026-10-04__09-20-16/minimal-environment-job-bash-almalinux9-9622) | — | — | — | — | — | — |
| name-based-web-tenants | — | [0.940](../../../jobs/9622/2026-10-04__09-20-16/name-based-web-tenants-bash-almalinux9-9622) | — | — | — | — | — | — |
| numeric-record-ordering | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/numeric-record-ordering-bash-almalinux9-9622) | — | — | — | — | — | — |
| permanent-url-migration | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/permanent-url-migration-bash-almalinux9-9622) | — | — | — | — | — | — |
| persistent-swap | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/persistent-swap-bash-almalinux9-9622) | — | — | — | — | — | — |
| posix-shell-installer | — | [0.880](../../../jobs/9622/2026-10-04__09-20-16/posix-shell-installer-bash-almalinux9-9622) | — | — | — | — | — | — |
| postgresql-sequence-repair | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/postgresql-sequence-repair-bash-almalinux9-9622) | — | — | — | — | — | — |
| print-spool-recovery | — | [0.940](../../../jobs/9622/2026-10-04__09-20-16/print-spool-recovery-bash-almalinux9-9622) | — | — | — | — | — | — |
| privacy-safe-support-export | — | [0.880](../../../jobs/9622/2026-10-04__09-20-16/privacy-safe-support-export-bash-almalinux9-9622) | — | — | — | — | — | — |
| relative-symlink-relocation | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/relative-symlink-relocation-bash-almalinux9-9622) | — | — | — | — | — | — |
| selective-tape-restore | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/selective-tape-restore-bash-almalinux9-9622) | — | — | — | — | — | — |
| service-confinement | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/service-confinement-bash-almalinux9-9622) | — | — | — | — | — | — |
| service-resource-limits | — | [0.960](../../../jobs/9622/2026-10-04__09-20-16/service-resource-limits-bash-almalinux9-9622) | — | — | — | — | — | — |
| signal-driven-config-reload | — | [0.920](../../../jobs/9622/2026-10-04__09-20-16/signal-driven-config-reload-bash-almalinux9-9622) | — | — | — | — | — | — |
| sparse-image-copy | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/sparse-image-copy-bash-almalinux9-9622) | — | — | — | — | — | — |
| sqlite-lock-contention | — | [0.870](../../../jobs/9622/2026-10-04__09-20-16/sqlite-lock-contention-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-host-key-pinning | — | [0.950](../../../jobs/9622/2026-10-04__09-20-16/ssh-host-key-pinning-bash-almalinux9-9622) | — | — | — | — | — | — |
| stale-pidfile-startup | — | [0.920](../../../jobs/9622/2026-10-04__09-20-16/stale-pidfile-startup-bash-almalinux9-9622) | — | — | — | — | — | — |
| temporary-file-symlink-defense | — | [0.960](../../../jobs/9622/2026-10-04__09-20-16/temporary-file-symlink-defense-bash-almalinux9-9622) | — | — | — | — | — | — |
| text-export-normalization | — | [0.960](../../../jobs/9622/2026-10-04__09-20-16/text-export-normalization-bash-almalinux9-9622) | — | — | — | — | — | — |
| timezone-log-merge | — | [0.880](../../../jobs/9622/2026-10-04__09-20-16/timezone-log-merge-bash-almalinux9-9622) | — | — | — | — | — | — |
| transactional-schema-upgrade | — | [0.950](../../../jobs/9622/2026-10-04__09-20-16/transactional-schema-upgrade-bash-almalinux9-9622) | — | — | — | — | — | — |
| unix-socket-access-boundary | — | [0.900](../../../jobs/9622/2026-10-04__09-20-16/unix-socket-access-boundary-bash-almalinux9-9622) | — | — | — | — | — | — |
| web-authentication-boundary | — | [0.920](../../../jobs/9622/2026-10-04__09-20-16/web-authentication-boundary-bash-almalinux9-9622) | — | — | — | — | — | — |
| webdav-document-locks | — | [0.880](../../../jobs/9622/2026-10-04__09-20-16/webdav-document-locks-bash-almalinux9-9622) | — | — | — | — | — | — |
| working-directory-independent-launch | — | [0.960](../../../jobs/9622/2026-10-04__09-20-16/working-directory-independent-launch-bash-almalinux9-9622) | — | — | — | — | — | — |
| **Average** | — | 0.952 | — | — | — | — | — | — |
