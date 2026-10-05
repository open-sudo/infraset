# single-node-os-comparison: command execution summary

Scope: `6324/2026-10-03__19-28-10`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | [9/0](../../../jobs/6324/2026-10-03__19-28-10/account-resource-limits-bash-rhel9-6324) | — | — | — |
| application-log-rotation | — | — | — | — | [7/1](../../../jobs/6324/2026-10-03__19-28-10/application-log-rotation-bash-rhel9-6324) | — | — | — |
| custom-ca-trust | — | — | — | — | [8/0](../../../jobs/6324/2026-10-03__19-28-10/custom-ca-trust-bash-rhel9-6324) | — | — | — |
| host-firewall-baseline | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/host-firewall-baseline-bash-rhel9-6324) | — | — | — |
| kernel-network-hardening | — | — | — | — | [10/0](../../../jobs/6324/2026-10-03__19-28-10/kernel-network-hardening-bash-rhel9-6324) | — | — | — |
| repair-application-permissions | — | — | — | — | [10/0](../../../jobs/6324/2026-10-03__19-28-10/repair-application-permissions-bash-rhel9-6324) | — | — | — |
| scheduled-maintenance | — | — | — | — | [8/0](../../../jobs/6324/2026-10-03__19-28-10/scheduled-maintenance-bash-rhel9-6324) | — | — | — |
| ssh-key-only | — | — | — | — | [9/0](../../../jobs/6324/2026-10-03__19-28-10/ssh-key-only-bash-rhel9-6324) | — | — | — |
| sticky-drop-directory | — | — | — | — | [6/0](../../../jobs/6324/2026-10-03__19-28-10/sticky-drop-directory-bash-rhel9-6324) | — | — | — |
| unprivileged-service | — | — | — | — | [12/0](../../../jobs/6324/2026-10-03__19-28-10/unprivileged-service-bash-rhel9-6324) | — | — | — |
| mandatory-access-control-port | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/mandatory-access-control-port-bash-rhel9-6324) | — | — | — |
| kernel-module-blacklist | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/kernel-module-blacklist-bash-rhel9-6324) | — | — | — |
| boot-kernel-parameter | — | — | — | — | [5/0](../../../jobs/6324/2026-10-03__19-28-10/boot-kernel-parameter-bash-rhel9-6324) | — | — | — |
| mount-option-hardening | — | — | — | — | [9/0](../../../jobs/6324/2026-10-03__19-28-10/mount-option-hardening-bash-rhel9-6324) | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | [8/0](../../../jobs/6324/2026-10-03__19-28-10/password-complexity-policy-bash-rhel9-6324) | — | — | — |
| sudo-command-logging | — | — | — | — | [10/0](../../../jobs/6324/2026-10-03__19-28-10/sudo-command-logging-bash-rhel9-6324) | — | — | — |
| cron-access-control | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/cron-access-control-bash-rhel9-6324) | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | [10/1](../../../jobs/6324/2026-10-03__19-28-10/disk-quota-bash-rhel9-6324) | — | — | — |
| encrypted-volume | — | — | — | — | [16/0](../../../jobs/6324/2026-10-03__19-28-10/encrypted-volume-bash-rhel9-6324) | — | — | — |
| lvm-extend | — | — | — | — | [13/0](../../../jobs/6324/2026-10-03__19-28-10/lvm-extend-bash-rhel9-6324) | — | — | — |
| filesystem-snapshot-rollback | — | — | — | — | [18/1](../../../jobs/6324/2026-10-03__19-28-10/filesystem-snapshot-rollback-bash-rhel9-6324) | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | [12/0](../../../jobs/6324/2026-10-03__19-28-10/package-version-hold-bash-rhel9-6324) | — | — | — |
| local-package-repository | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/local-package-repository-bash-rhel9-6324) | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — |
| file-integrity-baseline | — | — | — | — | [25/2](../../../jobs/6324/2026-10-03__19-28-10/file-integrity-baseline-bash-rhel9-6324) | — | — | — |
| archive-member-safety | — | — | — | — | [10/0](../../../jobs/6324/2026-10-03__19-28-10/archive-member-safety-bash-rhel9-6324) | — | — | — |
| atomic-release-publication | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/atomic-release-publication-bash-rhel9-6324) | — | — | — |
| batch-exclusive-lock | — | — | — | — | [10/0](../../../jobs/6324/2026-10-03__19-28-10/batch-exclusive-lock-bash-rhel9-6324) | — | — | — |
| cgi-report-execution | — | — | — | — | [10/0](../../../jobs/6324/2026-10-03__19-28-10/cgi-report-execution-bash-rhel9-6324) | — | — | — |
| child-process-reaping | — | — | — | — | [9/0](../../../jobs/6324/2026-10-03__19-28-10/child-process-reaping-bash-rhel9-6324) | — | — | — |
| chroot-web-service | — | — | — | — | [20/0](../../../jobs/6324/2026-10-03__19-28-10/chroot-web-service-bash-rhel9-6324) | — | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | [9/0](../../../jobs/6324/2026-10-03__19-28-10/cross-file-accounting-reconciliation-bash-rhel9-6324) | — | — | — |
| deleted-open-file-recovery | — | — | — | — | [15/0](../../../jobs/6324/2026-10-03__19-28-10/deleted-open-file-recovery-bash-rhel9-6324) | — | — | — |
| fifo-worker-reconnection | — | — | — | — | [15/0](../../../jobs/6324/2026-10-03__19-28-10/fifo-worker-reconnection-bash-rhel9-6324) | — | — | — |
| file-descriptor-leak | — | — | — | — | [12/0](../../../jobs/6324/2026-10-03__19-28-10/file-descriptor-leak-bash-rhel9-6324) | — | — | — |
| filename-encoding-migration | — | — | — | — | [12/0](../../../jobs/6324/2026-10-03__19-28-10/filename-encoding-migration-bash-rhel9-6324) | — | — | — |
| fixed-width-import-recovery | — | — | — | — | [9/0](../../../jobs/6324/2026-10-03__19-28-10/fixed-width-import-recovery-bash-rhel9-6324) | — | — | — |
| hardlink-aware-deduplication | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/hardlink-aware-deduplication-bash-rhel9-6324) | — | — | — |
| incremental-archive-chain | — | — | — | — | [9/0](../../../jobs/6324/2026-10-03__19-28-10/incremental-archive-chain-bash-rhel9-6324) | — | — | — |
| inherited-directory-acls | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/inherited-directory-acls-bash-rhel9-6324) | — | — | — |
| inode-cache-retention | — | — | — | — | [0/0](../../../jobs/6324/2026-10-03__19-28-10/inode-cache-retention-bash-rhel9-6324) | — | — | — |
| large-counter-overflow | — | — | — | — | [12/1](../../../jobs/6324/2026-10-03__19-28-10/large-counter-overflow-bash-rhel9-6324) | — | — | — |
| mail-filter-routing | — | — | — | — | [9/0](../../../jobs/6324/2026-10-03__19-28-10/mail-filter-routing-bash-rhel9-6324) | — | — | — |
| mail-spool-deduplication | — | — | — | — | [10/0](../../../jobs/6324/2026-10-03__19-28-10/mail-spool-deduplication-bash-rhel9-6324) | — | — | — |
| minimal-environment-job | — | — | — | — | [7/1](../../../jobs/6324/2026-10-03__19-28-10/minimal-environment-job-bash-rhel9-6324) | — | — | — |
| name-based-web-tenants | — | — | — | — | [12/0](../../../jobs/6324/2026-10-03__19-28-10/name-based-web-tenants-bash-rhel9-6324) | — | — | — |
| numeric-record-ordering | — | — | — | — | [10/0](../../../jobs/6324/2026-10-03__19-28-10/numeric-record-ordering-bash-rhel9-6324) | — | — | — |
| permanent-url-migration | — | — | — | — | [12/1](../../../jobs/6324/2026-10-03__19-28-10/permanent-url-migration-bash-rhel9-6324) | — | — | — |
| persistent-swap | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/persistent-swap-bash-rhel9-6324) | — | — | — |
| posix-shell-installer | — | — | — | — | [10/0](../../../jobs/6324/2026-10-03__19-28-10/posix-shell-installer-bash-rhel9-6324) | — | — | — |
| postgresql-sequence-repair | — | — | — | — | [14/0](../../../jobs/6324/2026-10-03__19-28-10/postgresql-sequence-repair-bash-rhel9-6324) | — | — | — |
| print-spool-recovery | — | — | — | — | [14/0](../../../jobs/6324/2026-10-03__19-28-10/print-spool-recovery-bash-rhel9-6324) | — | — | — |
| privacy-safe-support-export | — | — | — | — | [13/0](../../../jobs/6324/2026-10-03__19-28-10/privacy-safe-support-export-bash-rhel9-6324) | — | — | — |
| relative-symlink-relocation | — | — | — | — | [12/0](../../../jobs/6324/2026-10-03__19-28-10/relative-symlink-relocation-bash-rhel9-6324) | — | — | — |
| selective-tape-restore | — | — | — | — | [9/0](../../../jobs/6324/2026-10-03__19-28-10/selective-tape-restore-bash-rhel9-6324) | — | — | — |
| service-confinement | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/service-confinement-bash-rhel9-6324) | — | — | — |
| service-resource-limits | — | — | — | — | [14/0](../../../jobs/6324/2026-10-03__19-28-10/service-resource-limits-bash-rhel9-6324) | — | — | — |
| signal-driven-config-reload | — | — | — | — | [13/0](../../../jobs/6324/2026-10-03__19-28-10/signal-driven-config-reload-bash-rhel9-6324) | — | — | — |
| sparse-image-copy | — | — | — | — | [7/0](../../../jobs/6324/2026-10-03__19-28-10/sparse-image-copy-bash-rhel9-6324) | — | — | — |
| sqlite-lock-contention | — | — | — | — | [10/0](../../../jobs/6324/2026-10-03__19-28-10/sqlite-lock-contention-bash-rhel9-6324) | — | — | — |
| ssh-host-key-pinning | — | — | — | — | [12/0](../../../jobs/6324/2026-10-03__19-28-10/ssh-host-key-pinning-bash-rhel9-6324) | — | — | — |
| stale-pidfile-startup | — | — | — | — | [28/0](../../../jobs/6324/2026-10-03__19-28-10/stale-pidfile-startup-bash-rhel9-6324) | — | — | — |
| temporary-file-symlink-defense | — | — | — | — | [10/1](../../../jobs/6324/2026-10-03__19-28-10/temporary-file-symlink-defense-bash-rhel9-6324) | — | — | — |
| text-export-normalization | — | — | — | — | [9/0](../../../jobs/6324/2026-10-03__19-28-10/text-export-normalization-bash-rhel9-6324) | — | — | — |
| timezone-log-merge | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/timezone-log-merge-bash-rhel9-6324) | — | — | — |
| transactional-schema-upgrade | — | — | — | — | [11/0](../../../jobs/6324/2026-10-03__19-28-10/transactional-schema-upgrade-bash-rhel9-6324) | — | — | — |
| unix-socket-access-boundary | — | — | — | — | [9/1](../../../jobs/6324/2026-10-03__19-28-10/unix-socket-access-boundary-bash-rhel9-6324) | — | — | — |
| web-authentication-boundary | — | — | — | — | [19/0](../../../jobs/6324/2026-10-03__19-28-10/web-authentication-boundary-bash-rhel9-6324) | — | — | — |
| webdav-document-locks | — | — | — | — | [17/0](../../../jobs/6324/2026-10-03__19-28-10/webdav-document-locks-bash-rhel9-6324) | — | — | — |
| working-directory-independent-launch | — | — | — | — | [9/0](../../../jobs/6324/2026-10-03__19-28-10/working-directory-independent-launch-bash-rhel9-6324) | — | — | — |
| **Average** | — | — | — | — | 11.3/0.1 | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | [2m 23s](../../../jobs/6324/2026-10-03__19-28-10/account-resource-limits-bash-rhel9-6324) | — | — | — |
| application-log-rotation | — | — | — | — | [2m 52s](../../../jobs/6324/2026-10-03__19-28-10/application-log-rotation-bash-rhel9-6324) | — | — | — |
| custom-ca-trust | — | — | — | — | [2m 51s](../../../jobs/6324/2026-10-03__19-28-10/custom-ca-trust-bash-rhel9-6324) | — | — | — |
| host-firewall-baseline | — | — | — | — | [3m 26s](../../../jobs/6324/2026-10-03__19-28-10/host-firewall-baseline-bash-rhel9-6324) | — | — | — |
| kernel-network-hardening | — | — | — | — | [3m 06s](../../../jobs/6324/2026-10-03__19-28-10/kernel-network-hardening-bash-rhel9-6324) | — | — | — |
| repair-application-permissions | — | — | — | — | [3m 13s](../../../jobs/6324/2026-10-03__19-28-10/repair-application-permissions-bash-rhel9-6324) | — | — | — |
| scheduled-maintenance | — | — | — | — | [2m 34s](../../../jobs/6324/2026-10-03__19-28-10/scheduled-maintenance-bash-rhel9-6324) | — | — | — |
| ssh-key-only | — | — | — | — | [3m 12s](../../../jobs/6324/2026-10-03__19-28-10/ssh-key-only-bash-rhel9-6324) | — | — | — |
| sticky-drop-directory | — | — | — | — | [2m 48s](../../../jobs/6324/2026-10-03__19-28-10/sticky-drop-directory-bash-rhel9-6324) | — | — | — |
| unprivileged-service | — | — | — | — | [2m 42s](../../../jobs/6324/2026-10-03__19-28-10/unprivileged-service-bash-rhel9-6324) | — | — | — |
| mandatory-access-control-port | — | — | — | — | [2m 51s](../../../jobs/6324/2026-10-03__19-28-10/mandatory-access-control-port-bash-rhel9-6324) | — | — | — |
| kernel-module-blacklist | — | — | — | — | [2m 36s](../../../jobs/6324/2026-10-03__19-28-10/kernel-module-blacklist-bash-rhel9-6324) | — | — | — |
| boot-kernel-parameter | — | — | — | — | [2m 39s](../../../jobs/6324/2026-10-03__19-28-10/boot-kernel-parameter-bash-rhel9-6324) | — | — | — |
| mount-option-hardening | — | — | — | — | [2m 56s](../../../jobs/6324/2026-10-03__19-28-10/mount-option-hardening-bash-rhel9-6324) | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | [2m 49s](../../../jobs/6324/2026-10-03__19-28-10/password-complexity-policy-bash-rhel9-6324) | — | — | — |
| sudo-command-logging | — | — | — | — | [3m 21s](../../../jobs/6324/2026-10-03__19-28-10/sudo-command-logging-bash-rhel9-6324) | — | — | — |
| cron-access-control | — | — | — | — | [3m 11s](../../../jobs/6324/2026-10-03__19-28-10/cron-access-control-bash-rhel9-6324) | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | [3m 05s](../../../jobs/6324/2026-10-03__19-28-10/disk-quota-bash-rhel9-6324) | — | — | — |
| encrypted-volume | — | — | — | — | [4m 25s](../../../jobs/6324/2026-10-03__19-28-10/encrypted-volume-bash-rhel9-6324) | — | — | — |
| lvm-extend | — | — | — | — | [4m 01s](../../../jobs/6324/2026-10-03__19-28-10/lvm-extend-bash-rhel9-6324) | — | — | — |
| filesystem-snapshot-rollback | — | — | — | — | [5m 01s](../../../jobs/6324/2026-10-03__19-28-10/filesystem-snapshot-rollback-bash-rhel9-6324) | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | [3m 45s](../../../jobs/6324/2026-10-03__19-28-10/package-version-hold-bash-rhel9-6324) | — | — | — |
| local-package-repository | — | — | — | — | [3m 15s](../../../jobs/6324/2026-10-03__19-28-10/local-package-repository-bash-rhel9-6324) | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — |
| file-integrity-baseline | — | — | — | — | [5m 47s](../../../jobs/6324/2026-10-03__19-28-10/file-integrity-baseline-bash-rhel9-6324) | — | — | — |
| archive-member-safety | — | — | — | — | [4m 05s](../../../jobs/6324/2026-10-03__19-28-10/archive-member-safety-bash-rhel9-6324) | — | — | — |
| atomic-release-publication | — | — | — | — | [3m 49s](../../../jobs/6324/2026-10-03__19-28-10/atomic-release-publication-bash-rhel9-6324) | — | — | — |
| batch-exclusive-lock | — | — | — | — | [3m 39s](../../../jobs/6324/2026-10-03__19-28-10/batch-exclusive-lock-bash-rhel9-6324) | — | — | — |
| cgi-report-execution | — | — | — | — | [3m 42s](../../../jobs/6324/2026-10-03__19-28-10/cgi-report-execution-bash-rhel9-6324) | — | — | — |
| child-process-reaping | — | — | — | — | [3m 33s](../../../jobs/6324/2026-10-03__19-28-10/child-process-reaping-bash-rhel9-6324) | — | — | — |
| chroot-web-service | — | — | — | — | [4m 28s](../../../jobs/6324/2026-10-03__19-28-10/chroot-web-service-bash-rhel9-6324) | — | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | [3m 24s](../../../jobs/6324/2026-10-03__19-28-10/cross-file-accounting-reconciliation-bash-rhel9-6324) | — | — | — |
| deleted-open-file-recovery | — | — | — | — | [4m 45s](../../../jobs/6324/2026-10-03__19-28-10/deleted-open-file-recovery-bash-rhel9-6324) | — | — | — |
| fifo-worker-reconnection | — | — | — | — | [3m 57s](../../../jobs/6324/2026-10-03__19-28-10/fifo-worker-reconnection-bash-rhel9-6324) | — | — | — |
| file-descriptor-leak | — | — | — | — | [3m 41s](../../../jobs/6324/2026-10-03__19-28-10/file-descriptor-leak-bash-rhel9-6324) | — | — | — |
| filename-encoding-migration | — | — | — | — | [3m 25s](../../../jobs/6324/2026-10-03__19-28-10/filename-encoding-migration-bash-rhel9-6324) | — | — | — |
| fixed-width-import-recovery | — | — | — | — | [2m 47s](../../../jobs/6324/2026-10-03__19-28-10/fixed-width-import-recovery-bash-rhel9-6324) | — | — | — |
| hardlink-aware-deduplication | — | — | — | — | [2m 57s](../../../jobs/6324/2026-10-03__19-28-10/hardlink-aware-deduplication-bash-rhel9-6324) | — | — | — |
| incremental-archive-chain | — | — | — | — | [2m 54s](../../../jobs/6324/2026-10-03__19-28-10/incremental-archive-chain-bash-rhel9-6324) | — | — | — |
| inherited-directory-acls | — | — | — | — | [3m 29s](../../../jobs/6324/2026-10-03__19-28-10/inherited-directory-acls-bash-rhel9-6324) | — | — | — |
| inode-cache-retention | — | — | — | — | [51s](../../../jobs/6324/2026-10-03__19-28-10/inode-cache-retention-bash-rhel9-6324) | — | — | — |
| large-counter-overflow | — | — | — | — | [3m 32s](../../../jobs/6324/2026-10-03__19-28-10/large-counter-overflow-bash-rhel9-6324) | — | — | — |
| mail-filter-routing | — | — | — | — | [3m 29s](../../../jobs/6324/2026-10-03__19-28-10/mail-filter-routing-bash-rhel9-6324) | — | — | — |
| mail-spool-deduplication | — | — | — | — | [3m 56s](../../../jobs/6324/2026-10-03__19-28-10/mail-spool-deduplication-bash-rhel9-6324) | — | — | — |
| minimal-environment-job | — | — | — | — | [2m 51s](../../../jobs/6324/2026-10-03__19-28-10/minimal-environment-job-bash-rhel9-6324) | — | — | — |
| name-based-web-tenants | — | — | — | — | [3m 51s](../../../jobs/6324/2026-10-03__19-28-10/name-based-web-tenants-bash-rhel9-6324) | — | — | — |
| numeric-record-ordering | — | — | — | — | [3m 39s](../../../jobs/6324/2026-10-03__19-28-10/numeric-record-ordering-bash-rhel9-6324) | — | — | — |
| permanent-url-migration | — | — | — | — | [3m 48s](../../../jobs/6324/2026-10-03__19-28-10/permanent-url-migration-bash-rhel9-6324) | — | — | — |
| persistent-swap | — | — | — | — | [3m 02s](../../../jobs/6324/2026-10-03__19-28-10/persistent-swap-bash-rhel9-6324) | — | — | — |
| posix-shell-installer | — | — | — | — | [3m 31s](../../../jobs/6324/2026-10-03__19-28-10/posix-shell-installer-bash-rhel9-6324) | — | — | — |
| postgresql-sequence-repair | — | — | — | — | [3m 48s](../../../jobs/6324/2026-10-03__19-28-10/postgresql-sequence-repair-bash-rhel9-6324) | — | — | — |
| print-spool-recovery | — | — | — | — | [3m 51s](../../../jobs/6324/2026-10-03__19-28-10/print-spool-recovery-bash-rhel9-6324) | — | — | — |
| privacy-safe-support-export | — | — | — | — | [5m 16s](../../../jobs/6324/2026-10-03__19-28-10/privacy-safe-support-export-bash-rhel9-6324) | — | — | — |
| relative-symlink-relocation | — | — | — | — | [2m 49s](../../../jobs/6324/2026-10-03__19-28-10/relative-symlink-relocation-bash-rhel9-6324) | — | — | — |
| selective-tape-restore | — | — | — | — | [2m 36s](../../../jobs/6324/2026-10-03__19-28-10/selective-tape-restore-bash-rhel9-6324) | — | — | — |
| service-confinement | — | — | — | — | [4m 23s](../../../jobs/6324/2026-10-03__19-28-10/service-confinement-bash-rhel9-6324) | — | — | — |
| service-resource-limits | — | — | — | — | [3m 32s](../../../jobs/6324/2026-10-03__19-28-10/service-resource-limits-bash-rhel9-6324) | — | — | — |
| signal-driven-config-reload | — | — | — | — | [4m 07s](../../../jobs/6324/2026-10-03__19-28-10/signal-driven-config-reload-bash-rhel9-6324) | — | — | — |
| sparse-image-copy | — | — | — | — | [3m 54s](../../../jobs/6324/2026-10-03__19-28-10/sparse-image-copy-bash-rhel9-6324) | — | — | — |
| sqlite-lock-contention | — | — | — | — | [3m 43s](../../../jobs/6324/2026-10-03__19-28-10/sqlite-lock-contention-bash-rhel9-6324) | — | — | — |
| ssh-host-key-pinning | — | — | — | — | [3m 35s](../../../jobs/6324/2026-10-03__19-28-10/ssh-host-key-pinning-bash-rhel9-6324) | — | — | — |
| stale-pidfile-startup | — | — | — | — | [8m 55s](../../../jobs/6324/2026-10-03__19-28-10/stale-pidfile-startup-bash-rhel9-6324) | — | — | — |
| temporary-file-symlink-defense | — | — | — | — | [3m 33s](../../../jobs/6324/2026-10-03__19-28-10/temporary-file-symlink-defense-bash-rhel9-6324) | — | — | — |
| text-export-normalization | — | — | — | — | [3m 13s](../../../jobs/6324/2026-10-03__19-28-10/text-export-normalization-bash-rhel9-6324) | — | — | — |
| timezone-log-merge | — | — | — | — | [30m 01s](../../../jobs/6324/2026-10-03__19-28-10/timezone-log-merge-bash-rhel9-6324) | — | — | — |
| transactional-schema-upgrade | — | — | — | — | [3m 36s](../../../jobs/6324/2026-10-03__19-28-10/transactional-schema-upgrade-bash-rhel9-6324) | — | — | — |
| unix-socket-access-boundary | — | — | — | — | [3m 23s](../../../jobs/6324/2026-10-03__19-28-10/unix-socket-access-boundary-bash-rhel9-6324) | — | — | — |
| web-authentication-boundary | — | — | — | — | [5m 07s](../../../jobs/6324/2026-10-03__19-28-10/web-authentication-boundary-bash-rhel9-6324) | — | — | — |
| webdav-document-locks | — | — | — | — | [3m 39s](../../../jobs/6324/2026-10-03__19-28-10/webdav-document-locks-bash-rhel9-6324) | — | — | — |
| working-directory-independent-launch | — | — | — | — | [2m 33s](../../../jobs/6324/2026-10-03__19-28-10/working-directory-independent-launch-bash-rhel9-6324) | — | — | — |
| **Average** | — | — | — | — | 3m 56s | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 790 ms across 99 clusters, about 0.34% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/account-resource-limits-bash-rhel9-6324) | — | — | — |
| application-log-rotation | — | — | — | — | [0.930](../../../jobs/6324/2026-10-03__19-28-10/application-log-rotation-bash-rhel9-6324) | — | — | — |
| custom-ca-trust | — | — | — | — | [0.980](../../../jobs/6324/2026-10-03__19-28-10/custom-ca-trust-bash-rhel9-6324) | — | — | — |
| host-firewall-baseline | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/host-firewall-baseline-bash-rhel9-6324) | — | — | — |
| kernel-network-hardening | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/kernel-network-hardening-bash-rhel9-6324) | — | — | — |
| repair-application-permissions | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/repair-application-permissions-bash-rhel9-6324) | — | — | — |
| scheduled-maintenance | — | — | — | — | [0.950](../../../jobs/6324/2026-10-03__19-28-10/scheduled-maintenance-bash-rhel9-6324) | — | — | — |
| ssh-key-only | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/ssh-key-only-bash-rhel9-6324) | — | — | — |
| sticky-drop-directory | — | — | — | — | [0.900](../../../jobs/6324/2026-10-03__19-28-10/sticky-drop-directory-bash-rhel9-6324) | — | — | — |
| unprivileged-service | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/unprivileged-service-bash-rhel9-6324) | — | — | — |
| mandatory-access-control-port | — | — | — | — | [0.940](../../../jobs/6324/2026-10-03__19-28-10/mandatory-access-control-port-bash-rhel9-6324) | — | — | — |
| kernel-module-blacklist | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/kernel-module-blacklist-bash-rhel9-6324) | — | — | — |
| boot-kernel-parameter | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/boot-kernel-parameter-bash-rhel9-6324) | — | — | — |
| mount-option-hardening | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/mount-option-hardening-bash-rhel9-6324) | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | [0.960](../../../jobs/6324/2026-10-03__19-28-10/password-complexity-policy-bash-rhel9-6324) | — | — | — |
| sudo-command-logging | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/sudo-command-logging-bash-rhel9-6324) | — | — | — |
| cron-access-control | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/cron-access-control-bash-rhel9-6324) | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/disk-quota-bash-rhel9-6324) | — | — | — |
| encrypted-volume | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/encrypted-volume-bash-rhel9-6324) | — | — | — |
| lvm-extend | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/lvm-extend-bash-rhel9-6324) | — | — | — |
| filesystem-snapshot-rollback | — | — | — | — | [0.940](../../../jobs/6324/2026-10-03__19-28-10/filesystem-snapshot-rollback-bash-rhel9-6324) | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/package-version-hold-bash-rhel9-6324) | — | — | — |
| local-package-repository | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/local-package-repository-bash-rhel9-6324) | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — |
| file-integrity-baseline | — | — | — | — | [0.950](../../../jobs/6324/2026-10-03__19-28-10/file-integrity-baseline-bash-rhel9-6324) | — | — | — |
| archive-member-safety | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/archive-member-safety-bash-rhel9-6324) | — | — | — |
| atomic-release-publication | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/atomic-release-publication-bash-rhel9-6324) | — | — | — |
| batch-exclusive-lock | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/batch-exclusive-lock-bash-rhel9-6324) | — | — | — |
| cgi-report-execution | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/cgi-report-execution-bash-rhel9-6324) | — | — | — |
| child-process-reaping | — | — | — | — | [0.900](../../../jobs/6324/2026-10-03__19-28-10/child-process-reaping-bash-rhel9-6324) | — | — | — |
| chroot-web-service | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/chroot-web-service-bash-rhel9-6324) | — | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | [0.880](../../../jobs/6324/2026-10-03__19-28-10/cross-file-accounting-reconciliation-bash-rhel9-6324) | — | — | — |
| deleted-open-file-recovery | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/deleted-open-file-recovery-bash-rhel9-6324) | — | — | — |
| fifo-worker-reconnection | — | — | — | — | [0.900](../../../jobs/6324/2026-10-03__19-28-10/fifo-worker-reconnection-bash-rhel9-6324) | — | — | — |
| file-descriptor-leak | — | — | — | — | [0.930](../../../jobs/6324/2026-10-03__19-28-10/file-descriptor-leak-bash-rhel9-6324) | — | — | — |
| filename-encoding-migration | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/filename-encoding-migration-bash-rhel9-6324) | — | — | — |
| fixed-width-import-recovery | — | — | — | — | [0.880](../../../jobs/6324/2026-10-03__19-28-10/fixed-width-import-recovery-bash-rhel9-6324) | — | — | — |
| hardlink-aware-deduplication | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/hardlink-aware-deduplication-bash-rhel9-6324) | — | — | — |
| incremental-archive-chain | — | — | — | — | [0.980](../../../jobs/6324/2026-10-03__19-28-10/incremental-archive-chain-bash-rhel9-6324) | — | — | — |
| inherited-directory-acls | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/inherited-directory-acls-bash-rhel9-6324) | — | — | — |
| inode-cache-retention | — | — | — | — | — | — | — | — |
| large-counter-overflow | — | — | — | — | [0.860](../../../jobs/6324/2026-10-03__19-28-10/large-counter-overflow-bash-rhel9-6324) | — | — | — |
| mail-filter-routing | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/mail-filter-routing-bash-rhel9-6324) | — | — | — |
| mail-spool-deduplication | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/mail-spool-deduplication-bash-rhel9-6324) | — | — | — |
| minimal-environment-job | — | — | — | — | [0.920](../../../jobs/6324/2026-10-03__19-28-10/minimal-environment-job-bash-rhel9-6324) | — | — | — |
| name-based-web-tenants | — | — | — | — | [0.940](../../../jobs/6324/2026-10-03__19-28-10/name-based-web-tenants-bash-rhel9-6324) | — | — | — |
| numeric-record-ordering | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/numeric-record-ordering-bash-rhel9-6324) | — | — | — |
| permanent-url-migration | — | — | — | — | [0.910](../../../jobs/6324/2026-10-03__19-28-10/permanent-url-migration-bash-rhel9-6324) | — | — | — |
| persistent-swap | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/persistent-swap-bash-rhel9-6324) | — | — | — |
| posix-shell-installer | — | — | — | — | [0.930](../../../jobs/6324/2026-10-03__19-28-10/posix-shell-installer-bash-rhel9-6324) | — | — | — |
| postgresql-sequence-repair | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/postgresql-sequence-repair-bash-rhel9-6324) | — | — | — |
| print-spool-recovery | — | — | — | — | [0.900](../../../jobs/6324/2026-10-03__19-28-10/print-spool-recovery-bash-rhel9-6324) | — | — | — |
| privacy-safe-support-export | — | — | — | — | [0.880](../../../jobs/6324/2026-10-03__19-28-10/privacy-safe-support-export-bash-rhel9-6324) | — | — | — |
| relative-symlink-relocation | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/relative-symlink-relocation-bash-rhel9-6324) | — | — | — |
| selective-tape-restore | — | — | — | — | [0.980](../../../jobs/6324/2026-10-03__19-28-10/selective-tape-restore-bash-rhel9-6324) | — | — | — |
| service-confinement | — | — | — | — | [0.950](../../../jobs/6324/2026-10-03__19-28-10/service-confinement-bash-rhel9-6324) | — | — | — |
| service-resource-limits | — | — | — | — | [0.980](../../../jobs/6324/2026-10-03__19-28-10/service-resource-limits-bash-rhel9-6324) | — | — | — |
| signal-driven-config-reload | — | — | — | — | [0.950](../../../jobs/6324/2026-10-03__19-28-10/signal-driven-config-reload-bash-rhel9-6324) | — | — | — |
| sparse-image-copy | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/sparse-image-copy-bash-rhel9-6324) | — | — | — |
| sqlite-lock-contention | — | — | — | — | [0.980](../../../jobs/6324/2026-10-03__19-28-10/sqlite-lock-contention-bash-rhel9-6324) | — | — | — |
| ssh-host-key-pinning | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/ssh-host-key-pinning-bash-rhel9-6324) | — | — | — |
| stale-pidfile-startup | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/stale-pidfile-startup-bash-rhel9-6324) | — | — | — |
| temporary-file-symlink-defense | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/temporary-file-symlink-defense-bash-rhel9-6324) | — | — | — |
| text-export-normalization | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/text-export-normalization-bash-rhel9-6324) | — | — | — |
| timezone-log-merge | — | — | — | — | [0.880](../../../jobs/6324/2026-10-03__19-28-10/timezone-log-merge-bash-rhel9-6324) | — | — | — |
| transactional-schema-upgrade | — | — | — | — | [0.960](../../../jobs/6324/2026-10-03__19-28-10/transactional-schema-upgrade-bash-rhel9-6324) | — | — | — |
| unix-socket-access-boundary | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/unix-socket-access-boundary-bash-rhel9-6324) | — | — | — |
| web-authentication-boundary | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/web-authentication-boundary-bash-rhel9-6324) | — | — | — |
| webdav-document-locks | — | — | — | — | [0.820](../../../jobs/6324/2026-10-03__19-28-10/webdav-document-locks-bash-rhel9-6324) | — | — | — |
| working-directory-independent-launch | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/working-directory-independent-launch-bash-rhel9-6324) | — | — | — |
| **Average** | — | — | — | — | 0.963 | — | — | — |
