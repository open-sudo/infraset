# single-node-os-comparison: command execution summary

Scope: `3922/2026-10-03__22-34-06`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [7/0](../../../jobs/3922/2026-10-03__22-34-06/account-resource-limits-bash-rhel10-3922) | — | — |
| application-log-rotation | — | — | — | — | — | [12/0](../../../jobs/3922/2026-10-03__22-34-06/application-log-rotation-bash-rhel10-3922) | — | — |
| custom-ca-trust | — | — | — | — | — | [11/1](../../../jobs/3922/2026-10-03__22-34-06/custom-ca-trust-bash-rhel10-3922) | — | — |
| host-firewall-baseline | — | — | — | — | — | [11/1](../../../jobs/3922/2026-10-03__22-34-06/host-firewall-baseline-bash-rhel10-3922) | — | — |
| kernel-network-hardening | — | — | — | — | — | [10/0](../../../jobs/3922/2026-10-03__22-34-06/kernel-network-hardening-bash-rhel10-3922) | — | — |
| repair-application-permissions | — | — | — | — | — | [11/1](../../../jobs/3922/2026-10-03__22-34-06/repair-application-permissions-bash-rhel10-3922) | — | — |
| scheduled-maintenance | — | — | — | — | — | [12/0](../../../jobs/3922/2026-10-03__22-34-06/scheduled-maintenance-bash-rhel10-3922) | — | — |
| ssh-key-only | — | — | — | — | — | [10/1](../../../jobs/3922/2026-10-03__22-34-06/ssh-key-only-bash-rhel10-3922) | — | — |
| sticky-drop-directory | — | — | — | — | — | [11/0](../../../jobs/3922/2026-10-03__22-34-06/sticky-drop-directory-bash-rhel10-3922) | — | — |
| unprivileged-service | — | — | — | — | — | [12/0](../../../jobs/3922/2026-10-03__22-34-06/unprivileged-service-bash-rhel10-3922) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [13/0](../../../jobs/3922/2026-10-03__22-34-06/mandatory-access-control-port-bash-rhel10-3922) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [11/0](../../../jobs/3922/2026-10-03__22-34-06/kernel-module-blacklist-bash-rhel10-3922) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [9/0](../../../jobs/3922/2026-10-03__22-34-06/boot-kernel-parameter-bash-rhel10-3922) | — | — |
| mount-option-hardening | — | — | — | — | — | [15/0](../../../jobs/3922/2026-10-03__22-34-06/mount-option-hardening-bash-rhel10-3922) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [11/1](../../../jobs/3922/2026-10-03__22-34-06/password-complexity-policy-bash-rhel10-3922) | — | — |
| sudo-command-logging | — | — | — | — | — | [12/0](../../../jobs/3922/2026-10-03__22-34-06/sudo-command-logging-bash-rhel10-3922) | — | — |
| cron-access-control | — | — | — | — | — | [7/0](../../../jobs/3922/2026-10-03__22-34-06/cron-access-control-bash-rhel10-3922) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [20/3](../../../jobs/3922/2026-10-03__22-34-06/disk-quota-bash-rhel10-3922) | — | — |
| encrypted-volume | — | — | — | — | — | [16/1](../../../jobs/3922/2026-10-03__22-34-06/encrypted-volume-bash-rhel10-3922) | — | — |
| lvm-extend | — | — | — | — | — | [12/0](../../../jobs/3922/2026-10-03__22-34-06/lvm-extend-bash-rhel10-3922) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | [16/1](../../../jobs/3922/2026-10-03__22-34-06/filesystem-snapshot-rollback-bash-rhel10-3922) | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [11/0](../../../jobs/3922/2026-10-03__22-34-06/package-version-hold-bash-rhel10-3922) | — | — |
| local-package-repository | — | — | — | — | — | [36/1](../../../jobs/3922/2026-10-03__22-34-06/local-package-repository-bash-rhel10-3922) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [13/2](../../../jobs/3922/2026-10-03__22-34-06/certificate-rotation-bash-rhel10-3922) | — | — |
| file-integrity-baseline | — | — | — | — | — | [21/2](../../../jobs/3922/2026-10-03__22-34-06/file-integrity-baseline-bash-rhel10-3922) | — | — |
| archive-member-safety | — | — | — | — | — | [9/0](../../../jobs/3922/2026-10-03__22-34-06/archive-member-safety-bash-rhel10-3922) | — | — |
| atomic-release-publication | — | — | — | — | — | [13/0](../../../jobs/3922/2026-10-03__22-34-06/atomic-release-publication-bash-rhel10-3922) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [14/1](../../../jobs/3922/2026-10-03__22-34-06/batch-exclusive-lock-bash-rhel10-3922) | — | — |
| cgi-report-execution | — | — | — | — | — | [15/0](../../../jobs/3922/2026-10-03__22-34-06/cgi-report-execution-bash-rhel10-3922) | — | — |
| child-process-reaping | — | — | — | — | — | [9/0](../../../jobs/3922/2026-10-03__22-34-06/child-process-reaping-bash-rhel10-3922) | — | — |
| chroot-web-service | — | — | — | — | — | [23/7](../../../jobs/3922/2026-10-03__22-34-06/chroot-web-service-bash-rhel10-3922) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [8/0](../../../jobs/3922/2026-10-03__22-34-06/cross-file-accounting-reconciliation-bash-rhel10-3922) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [12/1](../../../jobs/3922/2026-10-03__22-34-06/deleted-open-file-recovery-bash-rhel10-3922) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [18/0](../../../jobs/3922/2026-10-03__22-34-06/fifo-worker-reconnection-bash-rhel10-3922) | — | — |
| file-descriptor-leak | — | — | — | — | — | [10/0](../../../jobs/3922/2026-10-03__22-34-06/file-descriptor-leak-bash-rhel10-3922) | — | — |
| filename-encoding-migration | — | — | — | — | — | [10/0](../../../jobs/3922/2026-10-03__22-34-06/filename-encoding-migration-bash-rhel10-3922) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [10/0](../../../jobs/3922/2026-10-03__22-34-06/fixed-width-import-recovery-bash-rhel10-3922) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [13/1](../../../jobs/3922/2026-10-03__22-34-06/hardlink-aware-deduplication-bash-rhel10-3922) | — | — |
| incremental-archive-chain | — | — | — | — | — | [12/0](../../../jobs/3922/2026-10-03__22-34-06/incremental-archive-chain-bash-rhel10-3922) | — | — |
| inherited-directory-acls | — | — | — | — | — | [11/0](../../../jobs/3922/2026-10-03__22-34-06/inherited-directory-acls-bash-rhel10-3922) | — | — |
| inode-cache-retention | — | — | — | — | — | [0/0](../../../jobs/3922/2026-10-03__22-34-06/inode-cache-retention-bash-rhel10-3922) | — | — |
| large-counter-overflow | — | — | — | — | — | [9/1](../../../jobs/3922/2026-10-03__22-34-06/large-counter-overflow-bash-rhel10-3922) | — | — |
| mail-filter-routing | — | — | — | — | — | [12/0](../../../jobs/3922/2026-10-03__22-34-06/mail-filter-routing-bash-rhel10-3922) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [10/0](../../../jobs/3922/2026-10-03__22-34-06/mail-spool-deduplication-bash-rhel10-3922) | — | — |
| minimal-environment-job | — | — | — | — | — | [8/1](../../../jobs/3922/2026-10-03__22-34-06/minimal-environment-job-bash-rhel10-3922) | — | — |
| name-based-web-tenants | — | — | — | — | — | [15/0](../../../jobs/3922/2026-10-03__22-34-06/name-based-web-tenants-bash-rhel10-3922) | — | — |
| numeric-record-ordering | — | — | — | — | — | [9/0](../../../jobs/3922/2026-10-03__22-34-06/numeric-record-ordering-bash-rhel10-3922) | — | — |
| permanent-url-migration | — | — | — | — | — | [12/0](../../../jobs/3922/2026-10-03__22-34-06/permanent-url-migration-bash-rhel10-3922) | — | — |
| persistent-swap | — | — | — | — | — | [10/0](../../../jobs/3922/2026-10-03__22-34-06/persistent-swap-bash-rhel10-3922) | — | — |
| posix-shell-installer | — | — | — | — | — | [8/1](../../../jobs/3922/2026-10-03__22-34-06/posix-shell-installer-bash-rhel10-3922) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [11/0](../../../jobs/3922/2026-10-03__22-34-06/postgresql-sequence-repair-bash-rhel10-3922) | — | — |
| print-spool-recovery | — | — | — | — | — | [12/1](../../../jobs/3922/2026-10-03__22-34-06/print-spool-recovery-bash-rhel10-3922) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [11/1](../../../jobs/3922/2026-10-03__22-34-06/privacy-safe-support-export-bash-rhel10-3922) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [12/0](../../../jobs/3922/2026-10-03__22-34-06/relative-symlink-relocation-bash-rhel10-3922) | — | — |
| selective-tape-restore | — | — | — | — | — | [10/0](../../../jobs/3922/2026-10-03__22-34-06/selective-tape-restore-bash-rhel10-3922) | — | — |
| service-confinement | — | — | — | — | — | [14/2](../../../jobs/3922/2026-10-03__22-34-06/service-confinement-bash-rhel10-3922) | — | — |
| service-resource-limits | — | — | — | — | — | [13/0](../../../jobs/3922/2026-10-03__22-34-06/service-resource-limits-bash-rhel10-3922) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [19/0](../../../jobs/3922/2026-10-03__22-34-06/signal-driven-config-reload-bash-rhel10-3922) | — | — |
| sparse-image-copy | — | — | — | — | — | [12/0](../../../jobs/3922/2026-10-03__22-34-06/sparse-image-copy-bash-rhel10-3922) | — | — |
| sqlite-lock-contention | — | — | — | — | — | [11/0](../../../jobs/3922/2026-10-03__22-34-06/sqlite-lock-contention-bash-rhel10-3922) | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [9/1](../../../jobs/3922/2026-10-03__22-34-06/ssh-host-key-pinning-bash-rhel10-3922) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [17/0](../../../jobs/3922/2026-10-03__22-34-06/stale-pidfile-startup-bash-rhel10-3922) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [11/0](../../../jobs/3922/2026-10-03__22-34-06/temporary-file-symlink-defense-bash-rhel10-3922) | — | — |
| text-export-normalization | — | — | — | — | — | [11/0](../../../jobs/3922/2026-10-03__22-34-06/text-export-normalization-bash-rhel10-3922) | — | — |
| timezone-log-merge | — | — | — | — | — | [8/0](../../../jobs/3922/2026-10-03__22-34-06/timezone-log-merge-bash-rhel10-3922) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [13/0](../../../jobs/3922/2026-10-03__22-34-06/transactional-schema-upgrade-bash-rhel10-3922) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [10/1](../../../jobs/3922/2026-10-03__22-34-06/unix-socket-access-boundary-bash-rhel10-3922) | — | — |
| web-authentication-boundary | — | — | — | — | — | [12/4](../../../jobs/3922/2026-10-03__22-34-06/web-authentication-boundary-bash-rhel10-3922) | — | — |
| webdav-document-locks | — | — | — | — | — | [14/1](../../../jobs/3922/2026-10-03__22-34-06/webdav-document-locks-bash-rhel10-3922) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [10/1](../../../jobs/3922/2026-10-03__22-34-06/working-directory-independent-launch-bash-rhel10-3922) | — | — |
| **Average** | — | — | — | — | — | 12.1/0.6 | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [2m 29s](../../../jobs/3922/2026-10-03__22-34-06/account-resource-limits-bash-rhel10-3922) | — | — |
| application-log-rotation | — | — | — | — | — | [3m 03s](../../../jobs/3922/2026-10-03__22-34-06/application-log-rotation-bash-rhel10-3922) | — | — |
| custom-ca-trust | — | — | — | — | — | [3m 20s](../../../jobs/3922/2026-10-03__22-34-06/custom-ca-trust-bash-rhel10-3922) | — | — |
| host-firewall-baseline | — | — | — | — | — | [3m 30s](../../../jobs/3922/2026-10-03__22-34-06/host-firewall-baseline-bash-rhel10-3922) | — | — |
| kernel-network-hardening | — | — | — | — | — | [3m 02s](../../../jobs/3922/2026-10-03__22-34-06/kernel-network-hardening-bash-rhel10-3922) | — | — |
| repair-application-permissions | — | — | — | — | — | [2m 57s](../../../jobs/3922/2026-10-03__22-34-06/repair-application-permissions-bash-rhel10-3922) | — | — |
| scheduled-maintenance | — | — | — | — | — | [3m 22s](../../../jobs/3922/2026-10-03__22-34-06/scheduled-maintenance-bash-rhel10-3922) | — | — |
| ssh-key-only | — | — | — | — | — | [3m 30s](../../../jobs/3922/2026-10-03__22-34-06/ssh-key-only-bash-rhel10-3922) | — | — |
| sticky-drop-directory | — | — | — | — | — | [2m 42s](../../../jobs/3922/2026-10-03__22-34-06/sticky-drop-directory-bash-rhel10-3922) | — | — |
| unprivileged-service | — | — | — | — | — | [3m 03s](../../../jobs/3922/2026-10-03__22-34-06/unprivileged-service-bash-rhel10-3922) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [28m 27s](../../../jobs/3922/2026-10-03__22-34-06/mandatory-access-control-port-bash-rhel10-3922) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [3m 05s](../../../jobs/3922/2026-10-03__22-34-06/kernel-module-blacklist-bash-rhel10-3922) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [3m 17s](../../../jobs/3922/2026-10-03__22-34-06/boot-kernel-parameter-bash-rhel10-3922) | — | — |
| mount-option-hardening | — | — | — | — | — | [3m 32s](../../../jobs/3922/2026-10-03__22-34-06/mount-option-hardening-bash-rhel10-3922) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [3m 22s](../../../jobs/3922/2026-10-03__22-34-06/password-complexity-policy-bash-rhel10-3922) | — | — |
| sudo-command-logging | — | — | — | — | — | [3m 11s](../../../jobs/3922/2026-10-03__22-34-06/sudo-command-logging-bash-rhel10-3922) | — | — |
| cron-access-control | — | — | — | — | — | [2m 57s](../../../jobs/3922/2026-10-03__22-34-06/cron-access-control-bash-rhel10-3922) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [5m 36s](../../../jobs/3922/2026-10-03__22-34-06/disk-quota-bash-rhel10-3922) | — | — |
| encrypted-volume | — | — | — | — | — | [3m 52s](../../../jobs/3922/2026-10-03__22-34-06/encrypted-volume-bash-rhel10-3922) | — | — |
| lvm-extend | — | — | — | — | — | [3m 12s](../../../jobs/3922/2026-10-03__22-34-06/lvm-extend-bash-rhel10-3922) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | [3m 49s](../../../jobs/3922/2026-10-03__22-34-06/filesystem-snapshot-rollback-bash-rhel10-3922) | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [3m 12s](../../../jobs/3922/2026-10-03__22-34-06/package-version-hold-bash-rhel10-3922) | — | — |
| local-package-repository | — | — | — | — | — | [6m 40s](../../../jobs/3922/2026-10-03__22-34-06/local-package-repository-bash-rhel10-3922) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [4m 42s](../../../jobs/3922/2026-10-03__22-34-06/certificate-rotation-bash-rhel10-3922) | — | — |
| file-integrity-baseline | — | — | — | — | — | [4m 35s](../../../jobs/3922/2026-10-03__22-34-06/file-integrity-baseline-bash-rhel10-3922) | — | — |
| archive-member-safety | — | — | — | — | — | [3m 59s](../../../jobs/3922/2026-10-03__22-34-06/archive-member-safety-bash-rhel10-3922) | — | — |
| atomic-release-publication | — | — | — | — | — | [3m 18s](../../../jobs/3922/2026-10-03__22-34-06/atomic-release-publication-bash-rhel10-3922) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [3m 58s](../../../jobs/3922/2026-10-03__22-34-06/batch-exclusive-lock-bash-rhel10-3922) | — | — |
| cgi-report-execution | — | — | — | — | — | [4m 41s](../../../jobs/3922/2026-10-03__22-34-06/cgi-report-execution-bash-rhel10-3922) | — | — |
| child-process-reaping | — | — | — | — | — | [2m 46s](../../../jobs/3922/2026-10-03__22-34-06/child-process-reaping-bash-rhel10-3922) | — | — |
| chroot-web-service | — | — | — | — | — | [5m 46s](../../../jobs/3922/2026-10-03__22-34-06/chroot-web-service-bash-rhel10-3922) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [3m 30s](../../../jobs/3922/2026-10-03__22-34-06/cross-file-accounting-reconciliation-bash-rhel10-3922) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [4m 27s](../../../jobs/3922/2026-10-03__22-34-06/deleted-open-file-recovery-bash-rhel10-3922) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [4m 39s](../../../jobs/3922/2026-10-03__22-34-06/fifo-worker-reconnection-bash-rhel10-3922) | — | — |
| file-descriptor-leak | — | — | — | — | — | [3m 26s](../../../jobs/3922/2026-10-03__22-34-06/file-descriptor-leak-bash-rhel10-3922) | — | — |
| filename-encoding-migration | — | — | — | — | — | [3m 07s](../../../jobs/3922/2026-10-03__22-34-06/filename-encoding-migration-bash-rhel10-3922) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [3m 38s](../../../jobs/3922/2026-10-03__22-34-06/fixed-width-import-recovery-bash-rhel10-3922) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [3m 32s](../../../jobs/3922/2026-10-03__22-34-06/hardlink-aware-deduplication-bash-rhel10-3922) | — | — |
| incremental-archive-chain | — | — | — | — | — | [3m 23s](../../../jobs/3922/2026-10-03__22-34-06/incremental-archive-chain-bash-rhel10-3922) | — | — |
| inherited-directory-acls | — | — | — | — | — | [3m 49s](../../../jobs/3922/2026-10-03__22-34-06/inherited-directory-acls-bash-rhel10-3922) | — | — |
| inode-cache-retention | — | — | — | — | — | [49s](../../../jobs/3922/2026-10-03__22-34-06/inode-cache-retention-bash-rhel10-3922) | — | — |
| large-counter-overflow | — | — | — | — | — | [3m 48s](../../../jobs/3922/2026-10-03__22-34-06/large-counter-overflow-bash-rhel10-3922) | — | — |
| mail-filter-routing | — | — | — | — | — | [3m 35s](../../../jobs/3922/2026-10-03__22-34-06/mail-filter-routing-bash-rhel10-3922) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [4m 54s](../../../jobs/3922/2026-10-03__22-34-06/mail-spool-deduplication-bash-rhel10-3922) | — | — |
| minimal-environment-job | — | — | — | — | — | [2m 42s](../../../jobs/3922/2026-10-03__22-34-06/minimal-environment-job-bash-rhel10-3922) | — | — |
| name-based-web-tenants | — | — | — | — | — | [3m 17s](../../../jobs/3922/2026-10-03__22-34-06/name-based-web-tenants-bash-rhel10-3922) | — | — |
| numeric-record-ordering | — | — | — | — | — | [3m 40s](../../../jobs/3922/2026-10-03__22-34-06/numeric-record-ordering-bash-rhel10-3922) | — | — |
| permanent-url-migration | — | — | — | — | — | [3m 57s](../../../jobs/3922/2026-10-03__22-34-06/permanent-url-migration-bash-rhel10-3922) | — | — |
| persistent-swap | — | — | — | — | — | [2m 59s](../../../jobs/3922/2026-10-03__22-34-06/persistent-swap-bash-rhel10-3922) | — | — |
| posix-shell-installer | — | — | — | — | — | [3m 23s](../../../jobs/3922/2026-10-03__22-34-06/posix-shell-installer-bash-rhel10-3922) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [3m 24s](../../../jobs/3922/2026-10-03__22-34-06/postgresql-sequence-repair-bash-rhel10-3922) | — | — |
| print-spool-recovery | — | — | — | — | — | [4m 49s](../../../jobs/3922/2026-10-03__22-34-06/print-spool-recovery-bash-rhel10-3922) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [4m 11s](../../../jobs/3922/2026-10-03__22-34-06/privacy-safe-support-export-bash-rhel10-3922) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [2m 42s](../../../jobs/3922/2026-10-03__22-34-06/relative-symlink-relocation-bash-rhel10-3922) | — | — |
| selective-tape-restore | — | — | — | — | — | [2m 53s](../../../jobs/3922/2026-10-03__22-34-06/selective-tape-restore-bash-rhel10-3922) | — | — |
| service-confinement | — | — | — | — | — | [30m 32s](../../../jobs/3922/2026-10-03__22-34-06/service-confinement-bash-rhel10-3922) | — | — |
| service-resource-limits | — | — | — | — | — | [3m 08s](../../../jobs/3922/2026-10-03__22-34-06/service-resource-limits-bash-rhel10-3922) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [5m 11s](../../../jobs/3922/2026-10-03__22-34-06/signal-driven-config-reload-bash-rhel10-3922) | — | — |
| sparse-image-copy | — | — | — | — | — | [2m 48s](../../../jobs/3922/2026-10-03__22-34-06/sparse-image-copy-bash-rhel10-3922) | — | — |
| sqlite-lock-contention | — | — | — | — | — | [4m 08s](../../../jobs/3922/2026-10-03__22-34-06/sqlite-lock-contention-bash-rhel10-3922) | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [2m 28s](../../../jobs/3922/2026-10-03__22-34-06/ssh-host-key-pinning-bash-rhel10-3922) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [7m 01s](../../../jobs/3922/2026-10-03__22-34-06/stale-pidfile-startup-bash-rhel10-3922) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [3m 48s](../../../jobs/3922/2026-10-03__22-34-06/temporary-file-symlink-defense-bash-rhel10-3922) | — | — |
| text-export-normalization | — | — | — | — | — | [3m 31s](../../../jobs/3922/2026-10-03__22-34-06/text-export-normalization-bash-rhel10-3922) | — | — |
| timezone-log-merge | — | — | — | — | — | [3m 08s](../../../jobs/3922/2026-10-03__22-34-06/timezone-log-merge-bash-rhel10-3922) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [3m 31s](../../../jobs/3922/2026-10-03__22-34-06/transactional-schema-upgrade-bash-rhel10-3922) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [4m 44s](../../../jobs/3922/2026-10-03__22-34-06/unix-socket-access-boundary-bash-rhel10-3922) | — | — |
| web-authentication-boundary | — | — | — | — | — | [4m 09s](../../../jobs/3922/2026-10-03__22-34-06/web-authentication-boundary-bash-rhel10-3922) | — | — |
| webdav-document-locks | — | — | — | — | — | [4m 33s](../../../jobs/3922/2026-10-03__22-34-06/webdav-document-locks-bash-rhel10-3922) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [20m 24s](../../../jobs/3922/2026-10-03__22-34-06/working-directory-independent-launch-bash-rhel10-3922) | — | — |
| **Average** | — | — | — | — | — | 4m 40s | — | — |

Cluster provisioning is not a meaningful part of these times: median 846 ms across 100 clusters, about 0.37% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/account-resource-limits-bash-rhel10-3922) | — | — |
| application-log-rotation | — | — | — | — | — | [0.930](../../../jobs/3922/2026-10-03__22-34-06/application-log-rotation-bash-rhel10-3922) | — | — |
| custom-ca-trust | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/custom-ca-trust-bash-rhel10-3922) | — | — |
| host-firewall-baseline | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/host-firewall-baseline-bash-rhel10-3922) | — | — |
| kernel-network-hardening | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/kernel-network-hardening-bash-rhel10-3922) | — | — |
| repair-application-permissions | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/repair-application-permissions-bash-rhel10-3922) | — | — |
| scheduled-maintenance | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/scheduled-maintenance-bash-rhel10-3922) | — | — |
| ssh-key-only | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/ssh-key-only-bash-rhel10-3922) | — | — |
| sticky-drop-directory | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/sticky-drop-directory-bash-rhel10-3922) | — | — |
| unprivileged-service | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/unprivileged-service-bash-rhel10-3922) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/mandatory-access-control-port-bash-rhel10-3922) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [0.940](../../../jobs/3922/2026-10-03__22-34-06/kernel-module-blacklist-bash-rhel10-3922) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/boot-kernel-parameter-bash-rhel10-3922) | — | — |
| mount-option-hardening | — | — | — | — | — | [0.970](../../../jobs/3922/2026-10-03__22-34-06/mount-option-hardening-bash-rhel10-3922) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/password-complexity-policy-bash-rhel10-3922) | — | — |
| sudo-command-logging | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/sudo-command-logging-bash-rhel10-3922) | — | — |
| cron-access-control | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/cron-access-control-bash-rhel10-3922) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [0.970](../../../jobs/3922/2026-10-03__22-34-06/disk-quota-bash-rhel10-3922) | — | — |
| encrypted-volume | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/encrypted-volume-bash-rhel10-3922) | — | — |
| lvm-extend | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/lvm-extend-bash-rhel10-3922) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | [0.970](../../../jobs/3922/2026-10-03__22-34-06/filesystem-snapshot-rollback-bash-rhel10-3922) | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [0.940](../../../jobs/3922/2026-10-03__22-34-06/package-version-hold-bash-rhel10-3922) | — | — |
| local-package-repository | — | — | — | — | — | [0.680](../../../jobs/3922/2026-10-03__22-34-06/local-package-repository-bash-rhel10-3922) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [0.970](../../../jobs/3922/2026-10-03__22-34-06/certificate-rotation-bash-rhel10-3922) | — | — |
| file-integrity-baseline | — | — | — | — | — | [0.950](../../../jobs/3922/2026-10-03__22-34-06/file-integrity-baseline-bash-rhel10-3922) | — | — |
| archive-member-safety | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/archive-member-safety-bash-rhel10-3922) | — | — |
| atomic-release-publication | — | — | — | — | — | [0.940](../../../jobs/3922/2026-10-03__22-34-06/atomic-release-publication-bash-rhel10-3922) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/batch-exclusive-lock-bash-rhel10-3922) | — | — |
| cgi-report-execution | — | — | — | — | — | [0.970](../../../jobs/3922/2026-10-03__22-34-06/cgi-report-execution-bash-rhel10-3922) | — | — |
| child-process-reaping | — | — | — | — | — | [0.920](../../../jobs/3922/2026-10-03__22-34-06/child-process-reaping-bash-rhel10-3922) | — | — |
| chroot-web-service | — | — | — | — | — | [0.820](../../../jobs/3922/2026-10-03__22-34-06/chroot-web-service-bash-rhel10-3922) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [0.880](../../../jobs/3922/2026-10-03__22-34-06/cross-file-accounting-reconciliation-bash-rhel10-3922) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [0.900](../../../jobs/3922/2026-10-03__22-34-06/deleted-open-file-recovery-bash-rhel10-3922) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [0.940](../../../jobs/3922/2026-10-03__22-34-06/fifo-worker-reconnection-bash-rhel10-3922) | — | — |
| file-descriptor-leak | — | — | — | — | — | [0.930](../../../jobs/3922/2026-10-03__22-34-06/file-descriptor-leak-bash-rhel10-3922) | — | — |
| filename-encoding-migration | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/filename-encoding-migration-bash-rhel10-3922) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [0.920](../../../jobs/3922/2026-10-03__22-34-06/fixed-width-import-recovery-bash-rhel10-3922) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/hardlink-aware-deduplication-bash-rhel10-3922) | — | — |
| incremental-archive-chain | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/incremental-archive-chain-bash-rhel10-3922) | — | — |
| inherited-directory-acls | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/inherited-directory-acls-bash-rhel10-3922) | — | — |
| inode-cache-retention | — | — | — | — | — | — | — | — |
| large-counter-overflow | — | — | — | — | — | [0.970](../../../jobs/3922/2026-10-03__22-34-06/large-counter-overflow-bash-rhel10-3922) | — | — |
| mail-filter-routing | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/mail-filter-routing-bash-rhel10-3922) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [0.980](../../../jobs/3922/2026-10-03__22-34-06/mail-spool-deduplication-bash-rhel10-3922) | — | — |
| minimal-environment-job | — | — | — | — | — | [0.900](../../../jobs/3922/2026-10-03__22-34-06/minimal-environment-job-bash-rhel10-3922) | — | — |
| name-based-web-tenants | — | — | — | — | — | [0.940](../../../jobs/3922/2026-10-03__22-34-06/name-based-web-tenants-bash-rhel10-3922) | — | — |
| numeric-record-ordering | — | — | — | — | — | [0.980](../../../jobs/3922/2026-10-03__22-34-06/numeric-record-ordering-bash-rhel10-3922) | — | — |
| permanent-url-migration | — | — | — | — | — | [0.910](../../../jobs/3922/2026-10-03__22-34-06/permanent-url-migration-bash-rhel10-3922) | — | — |
| persistent-swap | — | — | — | — | — | [0.960](../../../jobs/3922/2026-10-03__22-34-06/persistent-swap-bash-rhel10-3922) | — | — |
| posix-shell-installer | — | — | — | — | — | [0.820](../../../jobs/3922/2026-10-03__22-34-06/posix-shell-installer-bash-rhel10-3922) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/postgresql-sequence-repair-bash-rhel10-3922) | — | — |
| print-spool-recovery | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/print-spool-recovery-bash-rhel10-3922) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [0.800](../../../jobs/3922/2026-10-03__22-34-06/privacy-safe-support-export-bash-rhel10-3922) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/relative-symlink-relocation-bash-rhel10-3922) | — | — |
| selective-tape-restore | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/selective-tape-restore-bash-rhel10-3922) | — | — |
| service-confinement | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/service-confinement-bash-rhel10-3922) | — | — |
| service-resource-limits | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/service-resource-limits-bash-rhel10-3922) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [0.840](../../../jobs/3922/2026-10-03__22-34-06/signal-driven-config-reload-bash-rhel10-3922) | — | — |
| sparse-image-copy | — | — | — | — | — | [0.980](../../../jobs/3922/2026-10-03__22-34-06/sparse-image-copy-bash-rhel10-3922) | — | — |
| sqlite-lock-contention | — | — | — | — | — | [0.960](../../../jobs/3922/2026-10-03__22-34-06/sqlite-lock-contention-bash-rhel10-3922) | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/ssh-host-key-pinning-bash-rhel10-3922) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [0.970](../../../jobs/3922/2026-10-03__22-34-06/stale-pidfile-startup-bash-rhel10-3922) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/temporary-file-symlink-defense-bash-rhel10-3922) | — | — |
| text-export-normalization | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/text-export-normalization-bash-rhel10-3922) | — | — |
| timezone-log-merge | — | — | — | — | — | [0.900](../../../jobs/3922/2026-10-03__22-34-06/timezone-log-merge-bash-rhel10-3922) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [0.900](../../../jobs/3922/2026-10-03__22-34-06/transactional-schema-upgrade-bash-rhel10-3922) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [0.940](../../../jobs/3922/2026-10-03__22-34-06/unix-socket-access-boundary-bash-rhel10-3922) | — | — |
| web-authentication-boundary | — | — | — | — | — | [0.960](../../../jobs/3922/2026-10-03__22-34-06/web-authentication-boundary-bash-rhel10-3922) | — | — |
| webdav-document-locks | — | — | — | — | — | [0.940](../../../jobs/3922/2026-10-03__22-34-06/webdav-document-locks-bash-rhel10-3922) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [0.940](../../../jobs/3922/2026-10-03__22-34-06/working-directory-independent-launch-bash-rhel10-3922) | — | — |
| **Average** | — | — | — | — | — | 0.958 | — | — |
