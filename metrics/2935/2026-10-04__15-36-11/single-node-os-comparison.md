# single-node-os-comparison: command execution summary

Scope: `2935/2026-10-04__15-36-11`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [13/0](../../../jobs/2935/2026-10-04__15-36-11/account-resource-limits-bash-rhel10-2935) | — | — |
| application-log-rotation | — | — | — | — | — | [25/0](../../../jobs/2935/2026-10-04__15-36-11/application-log-rotation-bash-rhel10-2935) | — | — |
| custom-ca-trust | — | — | — | — | — | [14/1](../../../jobs/2935/2026-10-04__15-36-11/custom-ca-trust-bash-rhel10-2935) | — | — |
| host-firewall-baseline | — | — | — | — | — | [15/1](../../../jobs/2935/2026-10-04__15-36-11/host-firewall-baseline-bash-rhel10-2935) | — | — |
| kernel-network-hardening | — | — | — | — | — | [8/0](../../../jobs/2935/2026-10-04__15-36-11/kernel-network-hardening-bash-rhel10-2935) | — | — |
| repair-application-permissions | — | — | — | — | — | [9/0](../../../jobs/2935/2026-10-04__15-36-11/repair-application-permissions-bash-rhel10-2935) | — | — |
| scheduled-maintenance | — | — | — | — | — | [8/1](../../../jobs/2935/2026-10-04__15-36-11/scheduled-maintenance-bash-rhel10-2935) | — | — |
| ssh-key-only | — | — | — | — | — | [17/0](../../../jobs/2935/2026-10-04__15-36-11/ssh-key-only-bash-rhel10-2935) | — | — |
| sticky-drop-directory | — | — | — | — | — | [11/0](../../../jobs/2935/2026-10-04__15-36-11/sticky-drop-directory-bash-rhel10-2935) | — | — |
| unprivileged-service | — | — | — | — | — | [12/0](../../../jobs/2935/2026-10-04__15-36-11/unprivileged-service-bash-rhel10-2935) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [17/0](../../../jobs/2935/2026-10-04__15-36-11/mandatory-access-control-port-bash-rhel10-2935) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [11/0](../../../jobs/2935/2026-10-04__15-36-11/kernel-module-blacklist-bash-rhel10-2935) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [15/0](../../../jobs/2935/2026-10-04__15-36-11/boot-kernel-parameter-bash-rhel10-2935) | — | — |
| mount-option-hardening | — | — | — | — | — | [12/2](../../../jobs/2935/2026-10-04__15-36-11/mount-option-hardening-bash-rhel10-2935) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [26/2](../../../jobs/2935/2026-10-04__15-36-11/password-complexity-policy-bash-rhel10-2935) | — | — |
| sudo-command-logging | — | — | — | — | — | [12/1](../../../jobs/2935/2026-10-04__15-36-11/sudo-command-logging-bash-rhel10-2935) | — | — |
| cron-access-control | — | — | — | — | — | [12/0](../../../jobs/2935/2026-10-04__15-36-11/cron-access-control-bash-rhel10-2935) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [20/2](../../../jobs/2935/2026-10-04__15-36-11/disk-quota-bash-rhel10-2935) | — | — |
| encrypted-volume | — | — | — | — | — | [15/1](../../../jobs/2935/2026-10-04__15-36-11/encrypted-volume-bash-rhel10-2935) | — | — |
| lvm-extend | — | — | — | — | — | [11/0](../../../jobs/2935/2026-10-04__15-36-11/lvm-extend-bash-rhel10-2935) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | [18/1](../../../jobs/2935/2026-10-04__15-36-11/filesystem-snapshot-rollback-bash-rhel10-2935) | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [17/0](../../../jobs/2935/2026-10-04__15-36-11/package-version-hold-bash-rhel10-2935) | — | — |
| local-package-repository | — | — | — | — | — | [44/8](../../../jobs/2935/2026-10-04__15-36-11/local-package-repository-bash-rhel10-2935) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [20/1](../../../jobs/2935/2026-10-04__15-36-11/certificate-rotation-bash-rhel10-2935) | — | — |
| file-integrity-baseline | — | — | — | — | — | [19/1](../../../jobs/2935/2026-10-04__15-36-11/file-integrity-baseline-bash-rhel10-2935) | — | — |
| archive-member-safety | — | — | — | — | — | [9/1](../../../jobs/2935/2026-10-04__15-36-11/archive-member-safety-bash-rhel10-2935) | — | — |
| atomic-release-publication | — | — | — | — | — | [13/0](../../../jobs/2935/2026-10-04__15-36-11/atomic-release-publication-bash-rhel10-2935) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [18/0](../../../jobs/2935/2026-10-04__15-36-11/batch-exclusive-lock-bash-rhel10-2935) | — | — |
| cgi-report-execution | — | — | — | — | — | [14/1](../../../jobs/2935/2026-10-04__15-36-11/cgi-report-execution-bash-rhel10-2935) | — | — |
| child-process-reaping | — | — | — | — | — | [11/0](../../../jobs/2935/2026-10-04__15-36-11/child-process-reaping-bash-rhel10-2935) | — | — |
| chroot-web-service | — | — | — | — | — | [20/1](../../../jobs/2935/2026-10-04__15-36-11/chroot-web-service-bash-rhel10-2935) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [11/0](../../../jobs/2935/2026-10-04__15-36-11/cross-file-accounting-reconciliation-bash-rhel10-2935) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [20/0](../../../jobs/2935/2026-10-04__15-36-11/deleted-open-file-recovery-bash-rhel10-2935) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [12/0](../../../jobs/2935/2026-10-04__15-36-11/fifo-worker-reconnection-bash-rhel10-2935) | — | — |
| file-descriptor-leak | — | — | — | — | — | [12/0](../../../jobs/2935/2026-10-04__15-36-11/file-descriptor-leak-bash-rhel10-2935) | — | — |
| filename-encoding-migration | — | — | — | — | — | [11/0](../../../jobs/2935/2026-10-04__15-36-11/filename-encoding-migration-bash-rhel10-2935) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [10/0](../../../jobs/2935/2026-10-04__15-36-11/fixed-width-import-recovery-bash-rhel10-2935) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [13/0](../../../jobs/2935/2026-10-04__15-36-11/hardlink-aware-deduplication-bash-rhel10-2935) | — | — |
| incremental-archive-chain | — | — | — | — | — | [11/1](../../../jobs/2935/2026-10-04__15-36-11/incremental-archive-chain-bash-rhel10-2935) | — | — |
| inherited-directory-acls | — | — | — | — | — | [9/1](../../../jobs/2935/2026-10-04__15-36-11/inherited-directory-acls-bash-rhel10-2935) | — | — |
| inode-cache-retention | — | — | — | — | — | [0/0](../../../jobs/2935/2026-10-04__15-36-11/inode-cache-retention-bash-rhel10-2935) | — | — |
| large-counter-overflow | — | — | — | — | — | [14/0](../../../jobs/2935/2026-10-04__15-36-11/large-counter-overflow-bash-rhel10-2935) | — | — |
| mail-filter-routing | — | — | — | — | — | [12/0](../../../jobs/2935/2026-10-04__15-36-11/mail-filter-routing-bash-rhel10-2935) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [14/2](../../../jobs/2935/2026-10-04__15-36-11/mail-spool-deduplication-bash-rhel10-2935) | — | — |
| minimal-environment-job | — | — | — | — | — | [12/0](../../../jobs/2935/2026-10-04__15-36-11/minimal-environment-job-bash-rhel10-2935) | — | — |
| name-based-web-tenants | — | — | — | — | — | [16/0](../../../jobs/2935/2026-10-04__15-36-11/name-based-web-tenants-bash-rhel10-2935) | — | — |
| numeric-record-ordering | — | — | — | — | — | [11/0](../../../jobs/2935/2026-10-04__15-36-11/numeric-record-ordering-bash-rhel10-2935) | — | — |
| permanent-url-migration | — | — | — | — | — | [15/0](../../../jobs/2935/2026-10-04__15-36-11/permanent-url-migration-bash-rhel10-2935) | — | — |
| persistent-swap | — | — | — | — | — | [10/1](../../../jobs/2935/2026-10-04__15-36-11/persistent-swap-bash-rhel10-2935) | — | — |
| posix-shell-installer | — | — | — | — | — | [11/0](../../../jobs/2935/2026-10-04__15-36-11/posix-shell-installer-bash-rhel10-2935) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [18/2](../../../jobs/2935/2026-10-04__15-36-11/postgresql-sequence-repair-bash-rhel10-2935) | — | — |
| print-spool-recovery | — | — | — | — | — | [16/1](../../../jobs/2935/2026-10-04__15-36-11/print-spool-recovery-bash-rhel10-2935) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [13/0](../../../jobs/2935/2026-10-04__15-36-11/privacy-safe-support-export-bash-rhel10-2935) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [11/1](../../../jobs/2935/2026-10-04__15-36-11/relative-symlink-relocation-bash-rhel10-2935) | — | — |
| selective-tape-restore | — | — | — | — | — | [10/0](../../../jobs/2935/2026-10-04__15-36-11/selective-tape-restore-bash-rhel10-2935) | — | — |
| service-confinement | — | — | — | — | — | [33/7](../../../jobs/2935/2026-10-04__15-36-11/service-confinement-bash-rhel10-2935) | — | — |
| service-resource-limits | — | — | — | — | — | [11/1](../../../jobs/2935/2026-10-04__15-36-11/service-resource-limits-bash-rhel10-2935) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [12/1](../../../jobs/2935/2026-10-04__15-36-11/signal-driven-config-reload-bash-rhel10-2935) | — | — |
| sparse-image-copy | — | — | — | — | — | [15/0](../../../jobs/2935/2026-10-04__15-36-11/sparse-image-copy-bash-rhel10-2935) | — | — |
| sqlite-lock-contention | — | — | — | — | — | [19/0](../../../jobs/2935/2026-10-04__15-36-11/sqlite-lock-contention-bash-rhel10-2935) | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [15/0](../../../jobs/2935/2026-10-04__15-36-11/ssh-host-key-pinning-bash-rhel10-2935) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [16/0](../../../jobs/2935/2026-10-04__15-36-11/stale-pidfile-startup-bash-rhel10-2935) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [16/5](../../../jobs/2935/2026-10-04__15-36-11/temporary-file-symlink-defense-bash-rhel10-2935) | — | — |
| text-export-normalization | — | — | — | — | — | [7/2](../../../jobs/2935/2026-10-04__15-36-11/text-export-normalization-bash-rhel10-2935) | — | — |
| timezone-log-merge | — | — | — | — | — | [17/0](../../../jobs/2935/2026-10-04__15-36-11/timezone-log-merge-bash-rhel10-2935) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [12/1](../../../jobs/2935/2026-10-04__15-36-11/transactional-schema-upgrade-bash-rhel10-2935) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [10/0](../../../jobs/2935/2026-10-04__15-36-11/unix-socket-access-boundary-bash-rhel10-2935) | — | — |
| web-authentication-boundary | — | — | — | — | — | [20/0](../../../jobs/2935/2026-10-04__15-36-11/web-authentication-boundary-bash-rhel10-2935) | — | — |
| webdav-document-locks | — | — | — | — | — | [11/0](../../../jobs/2935/2026-10-04__15-36-11/webdav-document-locks-bash-rhel10-2935) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [10/0](../../../jobs/2935/2026-10-04__15-36-11/working-directory-independent-launch-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 14.3/0.7 | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [3m 57s](../../../jobs/2935/2026-10-04__15-36-11/account-resource-limits-bash-rhel10-2935) | — | — |
| application-log-rotation | — | — | — | — | — | [10m 30s](../../../jobs/2935/2026-10-04__15-36-11/application-log-rotation-bash-rhel10-2935) | — | — |
| custom-ca-trust | — | — | — | — | — | [4m 36s](../../../jobs/2935/2026-10-04__15-36-11/custom-ca-trust-bash-rhel10-2935) | — | — |
| host-firewall-baseline | — | — | — | — | — | [5m 03s](../../../jobs/2935/2026-10-04__15-36-11/host-firewall-baseline-bash-rhel10-2935) | — | — |
| kernel-network-hardening | — | — | — | — | — | [3m 06s](../../../jobs/2935/2026-10-04__15-36-11/kernel-network-hardening-bash-rhel10-2935) | — | — |
| repair-application-permissions | — | — | — | — | — | [3m 42s](../../../jobs/2935/2026-10-04__15-36-11/repair-application-permissions-bash-rhel10-2935) | — | — |
| scheduled-maintenance | — | — | — | — | — | [4m 31s](../../../jobs/2935/2026-10-04__15-36-11/scheduled-maintenance-bash-rhel10-2935) | — | — |
| ssh-key-only | — | — | — | — | — | [5m 36s](../../../jobs/2935/2026-10-04__15-36-11/ssh-key-only-bash-rhel10-2935) | — | — |
| sticky-drop-directory | — | — | — | — | — | [3m 27s](../../../jobs/2935/2026-10-04__15-36-11/sticky-drop-directory-bash-rhel10-2935) | — | — |
| unprivileged-service | — | — | — | — | — | [3m 40s](../../../jobs/2935/2026-10-04__15-36-11/unprivileged-service-bash-rhel10-2935) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [4m 26s](../../../jobs/2935/2026-10-04__15-36-11/mandatory-access-control-port-bash-rhel10-2935) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [3m 22s](../../../jobs/2935/2026-10-04__15-36-11/kernel-module-blacklist-bash-rhel10-2935) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [3m 49s](../../../jobs/2935/2026-10-04__15-36-11/boot-kernel-parameter-bash-rhel10-2935) | — | — |
| mount-option-hardening | — | — | — | — | — | [4m 40s](../../../jobs/2935/2026-10-04__15-36-11/mount-option-hardening-bash-rhel10-2935) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [7m 11s](../../../jobs/2935/2026-10-04__15-36-11/password-complexity-policy-bash-rhel10-2935) | — | — |
| sudo-command-logging | — | — | — | — | — | [5m 10s](../../../jobs/2935/2026-10-04__15-36-11/sudo-command-logging-bash-rhel10-2935) | — | — |
| cron-access-control | — | — | — | — | — | [5m 37s](../../../jobs/2935/2026-10-04__15-36-11/cron-access-control-bash-rhel10-2935) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [5m 35s](../../../jobs/2935/2026-10-04__15-36-11/disk-quota-bash-rhel10-2935) | — | — |
| encrypted-volume | — | — | — | — | — | [3m 55s](../../../jobs/2935/2026-10-04__15-36-11/encrypted-volume-bash-rhel10-2935) | — | — |
| lvm-extend | — | — | — | — | — | [10m 45s](../../../jobs/2935/2026-10-04__15-36-11/lvm-extend-bash-rhel10-2935) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | [10m 06s](../../../jobs/2935/2026-10-04__15-36-11/filesystem-snapshot-rollback-bash-rhel10-2935) | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [4m 27s](../../../jobs/2935/2026-10-04__15-36-11/package-version-hold-bash-rhel10-2935) | — | — |
| local-package-repository | — | — | — | — | — | [15m 47s](../../../jobs/2935/2026-10-04__15-36-11/local-package-repository-bash-rhel10-2935) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [9m 00s](../../../jobs/2935/2026-10-04__15-36-11/certificate-rotation-bash-rhel10-2935) | — | — |
| file-integrity-baseline | — | — | — | — | — | [5m 46s](../../../jobs/2935/2026-10-04__15-36-11/file-integrity-baseline-bash-rhel10-2935) | — | — |
| archive-member-safety | — | — | — | — | — | [5m 02s](../../../jobs/2935/2026-10-04__15-36-11/archive-member-safety-bash-rhel10-2935) | — | — |
| atomic-release-publication | — | — | — | — | — | [7m 10s](../../../jobs/2935/2026-10-04__15-36-11/atomic-release-publication-bash-rhel10-2935) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [5m 37s](../../../jobs/2935/2026-10-04__15-36-11/batch-exclusive-lock-bash-rhel10-2935) | — | — |
| cgi-report-execution | — | — | — | — | — | [4m 59s](../../../jobs/2935/2026-10-04__15-36-11/cgi-report-execution-bash-rhel10-2935) | — | — |
| child-process-reaping | — | — | — | — | — | [4m 01s](../../../jobs/2935/2026-10-04__15-36-11/child-process-reaping-bash-rhel10-2935) | — | — |
| chroot-web-service | — | — | — | — | — | [33m 30s](../../../jobs/2935/2026-10-04__15-36-11/chroot-web-service-bash-rhel10-2935) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [5m 06s](../../../jobs/2935/2026-10-04__15-36-11/cross-file-accounting-reconciliation-bash-rhel10-2935) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [6m 43s](../../../jobs/2935/2026-10-04__15-36-11/deleted-open-file-recovery-bash-rhel10-2935) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [5m 09s](../../../jobs/2935/2026-10-04__15-36-11/fifo-worker-reconnection-bash-rhel10-2935) | — | — |
| file-descriptor-leak | — | — | — | — | — | [3m 26s](../../../jobs/2935/2026-10-04__15-36-11/file-descriptor-leak-bash-rhel10-2935) | — | — |
| filename-encoding-migration | — | — | — | — | — | [4m 12s](../../../jobs/2935/2026-10-04__15-36-11/filename-encoding-migration-bash-rhel10-2935) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [3m 44s](../../../jobs/2935/2026-10-04__15-36-11/fixed-width-import-recovery-bash-rhel10-2935) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [3m 47s](../../../jobs/2935/2026-10-04__15-36-11/hardlink-aware-deduplication-bash-rhel10-2935) | — | — |
| incremental-archive-chain | — | — | — | — | — | [3m 47s](../../../jobs/2935/2026-10-04__15-36-11/incremental-archive-chain-bash-rhel10-2935) | — | — |
| inherited-directory-acls | — | — | — | — | — | [3m 17s](../../../jobs/2935/2026-10-04__15-36-11/inherited-directory-acls-bash-rhel10-2935) | — | — |
| inode-cache-retention | — | — | — | — | — | [50s](../../../jobs/2935/2026-10-04__15-36-11/inode-cache-retention-bash-rhel10-2935) | — | — |
| large-counter-overflow | — | — | — | — | — | [4m 12s](../../../jobs/2935/2026-10-04__15-36-11/large-counter-overflow-bash-rhel10-2935) | — | — |
| mail-filter-routing | — | — | — | — | — | [5m 06s](../../../jobs/2935/2026-10-04__15-36-11/mail-filter-routing-bash-rhel10-2935) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [5m 43s](../../../jobs/2935/2026-10-04__15-36-11/mail-spool-deduplication-bash-rhel10-2935) | — | — |
| minimal-environment-job | — | — | — | — | — | [3m 47s](../../../jobs/2935/2026-10-04__15-36-11/minimal-environment-job-bash-rhel10-2935) | — | — |
| name-based-web-tenants | — | — | — | — | — | [5m 39s](../../../jobs/2935/2026-10-04__15-36-11/name-based-web-tenants-bash-rhel10-2935) | — | — |
| numeric-record-ordering | — | — | — | — | — | [4m 01s](../../../jobs/2935/2026-10-04__15-36-11/numeric-record-ordering-bash-rhel10-2935) | — | — |
| permanent-url-migration | — | — | — | — | — | [4m 40s](../../../jobs/2935/2026-10-04__15-36-11/permanent-url-migration-bash-rhel10-2935) | — | — |
| persistent-swap | — | — | — | — | — | [3m 17s](../../../jobs/2935/2026-10-04__15-36-11/persistent-swap-bash-rhel10-2935) | — | — |
| posix-shell-installer | — | — | — | — | — | [4m 12s](../../../jobs/2935/2026-10-04__15-36-11/posix-shell-installer-bash-rhel10-2935) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [4m 11s](../../../jobs/2935/2026-10-04__15-36-11/postgresql-sequence-repair-bash-rhel10-2935) | — | — |
| print-spool-recovery | — | — | — | — | — | [5m 57s](../../../jobs/2935/2026-10-04__15-36-11/print-spool-recovery-bash-rhel10-2935) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [6m 07s](../../../jobs/2935/2026-10-04__15-36-11/privacy-safe-support-export-bash-rhel10-2935) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [3m 51s](../../../jobs/2935/2026-10-04__15-36-11/relative-symlink-relocation-bash-rhel10-2935) | — | — |
| selective-tape-restore | — | — | — | — | — | [3m 09s](../../../jobs/2935/2026-10-04__15-36-11/selective-tape-restore-bash-rhel10-2935) | — | — |
| service-confinement | — | — | — | — | — | [10m 17s](../../../jobs/2935/2026-10-04__15-36-11/service-confinement-bash-rhel10-2935) | — | — |
| service-resource-limits | — | — | — | — | — | [4m 18s](../../../jobs/2935/2026-10-04__15-36-11/service-resource-limits-bash-rhel10-2935) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [5m 04s](../../../jobs/2935/2026-10-04__15-36-11/signal-driven-config-reload-bash-rhel10-2935) | — | — |
| sparse-image-copy | — | — | — | — | — | [4m 24s](../../../jobs/2935/2026-10-04__15-36-11/sparse-image-copy-bash-rhel10-2935) | — | — |
| sqlite-lock-contention | — | — | — | — | — | [6m 48s](../../../jobs/2935/2026-10-04__15-36-11/sqlite-lock-contention-bash-rhel10-2935) | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [4m 30s](../../../jobs/2935/2026-10-04__15-36-11/ssh-host-key-pinning-bash-rhel10-2935) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [7m 57s](../../../jobs/2935/2026-10-04__15-36-11/stale-pidfile-startup-bash-rhel10-2935) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [5m 21s](../../../jobs/2935/2026-10-04__15-36-11/temporary-file-symlink-defense-bash-rhel10-2935) | — | — |
| text-export-normalization | — | — | — | — | — | [4m 12s](../../../jobs/2935/2026-10-04__15-36-11/text-export-normalization-bash-rhel10-2935) | — | — |
| timezone-log-merge | — | — | — | — | — | [4m 55s](../../../jobs/2935/2026-10-04__15-36-11/timezone-log-merge-bash-rhel10-2935) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [4m 37s](../../../jobs/2935/2026-10-04__15-36-11/transactional-schema-upgrade-bash-rhel10-2935) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [4m 27s](../../../jobs/2935/2026-10-04__15-36-11/unix-socket-access-boundary-bash-rhel10-2935) | — | — |
| web-authentication-boundary | — | — | — | — | — | [5m 56s](../../../jobs/2935/2026-10-04__15-36-11/web-authentication-boundary-bash-rhel10-2935) | — | — |
| webdav-document-locks | — | — | — | — | — | [4m 40s](../../../jobs/2935/2026-10-04__15-36-11/webdav-document-locks-bash-rhel10-2935) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [3m 06s](../../../jobs/2935/2026-10-04__15-36-11/working-directory-independent-launch-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 5m 36s | — | — |

Cluster provisioning is not a meaningful part of these times: median 788 ms across 100 clusters, about 0.25% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/account-resource-limits-bash-rhel10-2935) | — | — |
| application-log-rotation | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/application-log-rotation-bash-rhel10-2935) | — | — |
| custom-ca-trust | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/custom-ca-trust-bash-rhel10-2935) | — | — |
| host-firewall-baseline | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/host-firewall-baseline-bash-rhel10-2935) | — | — |
| kernel-network-hardening | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/kernel-network-hardening-bash-rhel10-2935) | — | — |
| repair-application-permissions | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/repair-application-permissions-bash-rhel10-2935) | — | — |
| scheduled-maintenance | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/scheduled-maintenance-bash-rhel10-2935) | — | — |
| ssh-key-only | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/ssh-key-only-bash-rhel10-2935) | — | — |
| sticky-drop-directory | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/sticky-drop-directory-bash-rhel10-2935) | — | — |
| unprivileged-service | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/unprivileged-service-bash-rhel10-2935) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/mandatory-access-control-port-bash-rhel10-2935) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/kernel-module-blacklist-bash-rhel10-2935) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/boot-kernel-parameter-bash-rhel10-2935) | — | — |
| mount-option-hardening | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/mount-option-hardening-bash-rhel10-2935) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__15-36-11/password-complexity-policy-bash-rhel10-2935) | — | — |
| sudo-command-logging | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/sudo-command-logging-bash-rhel10-2935) | — | — |
| cron-access-control | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/cron-access-control-bash-rhel10-2935) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [0.860](../../../jobs/2935/2026-10-04__15-36-11/disk-quota-bash-rhel10-2935) | — | — |
| encrypted-volume | — | — | — | — | — | [0.990](../../../jobs/2935/2026-10-04__15-36-11/encrypted-volume-bash-rhel10-2935) | — | — |
| lvm-extend | — | — | — | — | — | [0.700](../../../jobs/2935/2026-10-04__15-36-11/lvm-extend-bash-rhel10-2935) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | [0.480](../../../jobs/2935/2026-10-04__15-36-11/filesystem-snapshot-rollback-bash-rhel10-2935) | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/package-version-hold-bash-rhel10-2935) | — | — |
| local-package-repository | — | — | — | — | — | [0.840](../../../jobs/2935/2026-10-04__15-36-11/local-package-repository-bash-rhel10-2935) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/certificate-rotation-bash-rhel10-2935) | — | — |
| file-integrity-baseline | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/file-integrity-baseline-bash-rhel10-2935) | — | — |
| archive-member-safety | — | — | — | — | — | [0.960](../../../jobs/2935/2026-10-04__15-36-11/archive-member-safety-bash-rhel10-2935) | — | — |
| atomic-release-publication | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/atomic-release-publication-bash-rhel10-2935) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/batch-exclusive-lock-bash-rhel10-2935) | — | — |
| cgi-report-execution | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/cgi-report-execution-bash-rhel10-2935) | — | — |
| child-process-reaping | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/child-process-reaping-bash-rhel10-2935) | — | — |
| chroot-web-service | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__15-36-11/chroot-web-service-bash-rhel10-2935) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/cross-file-accounting-reconciliation-bash-rhel10-2935) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/deleted-open-file-recovery-bash-rhel10-2935) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/fifo-worker-reconnection-bash-rhel10-2935) | — | — |
| file-descriptor-leak | — | — | — | — | — | [0.960](../../../jobs/2935/2026-10-04__15-36-11/file-descriptor-leak-bash-rhel10-2935) | — | — |
| filename-encoding-migration | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/filename-encoding-migration-bash-rhel10-2935) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/fixed-width-import-recovery-bash-rhel10-2935) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/hardlink-aware-deduplication-bash-rhel10-2935) | — | — |
| incremental-archive-chain | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/incremental-archive-chain-bash-rhel10-2935) | — | — |
| inherited-directory-acls | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/inherited-directory-acls-bash-rhel10-2935) | — | — |
| inode-cache-retention | — | — | — | — | — | — | — | — |
| large-counter-overflow | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/large-counter-overflow-bash-rhel10-2935) | — | — |
| mail-filter-routing | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/mail-filter-routing-bash-rhel10-2935) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/mail-spool-deduplication-bash-rhel10-2935) | — | — |
| minimal-environment-job | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/minimal-environment-job-bash-rhel10-2935) | — | — |
| name-based-web-tenants | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/name-based-web-tenants-bash-rhel10-2935) | — | — |
| numeric-record-ordering | — | — | — | — | — | [0.960](../../../jobs/2935/2026-10-04__15-36-11/numeric-record-ordering-bash-rhel10-2935) | — | — |
| permanent-url-migration | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/permanent-url-migration-bash-rhel10-2935) | — | — |
| persistent-swap | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/persistent-swap-bash-rhel10-2935) | — | — |
| posix-shell-installer | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/posix-shell-installer-bash-rhel10-2935) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/postgresql-sequence-repair-bash-rhel10-2935) | — | — |
| print-spool-recovery | — | — | — | — | — | [0.900](../../../jobs/2935/2026-10-04__15-36-11/print-spool-recovery-bash-rhel10-2935) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [0.970](../../../jobs/2935/2026-10-04__15-36-11/privacy-safe-support-export-bash-rhel10-2935) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/relative-symlink-relocation-bash-rhel10-2935) | — | — |
| selective-tape-restore | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/selective-tape-restore-bash-rhel10-2935) | — | — |
| service-confinement | — | — | — | — | — | [0.940](../../../jobs/2935/2026-10-04__15-36-11/service-confinement-bash-rhel10-2935) | — | — |
| service-resource-limits | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__15-36-11/service-resource-limits-bash-rhel10-2935) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/signal-driven-config-reload-bash-rhel10-2935) | — | — |
| sparse-image-copy | — | — | — | — | — | [0.970](../../../jobs/2935/2026-10-04__15-36-11/sparse-image-copy-bash-rhel10-2935) | — | — |
| sqlite-lock-contention | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/sqlite-lock-contention-bash-rhel10-2935) | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/ssh-host-key-pinning-bash-rhel10-2935) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/stale-pidfile-startup-bash-rhel10-2935) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/temporary-file-symlink-defense-bash-rhel10-2935) | — | — |
| text-export-normalization | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/text-export-normalization-bash-rhel10-2935) | — | — |
| timezone-log-merge | — | — | — | — | — | [0.950](../../../jobs/2935/2026-10-04__15-36-11/timezone-log-merge-bash-rhel10-2935) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/transactional-schema-upgrade-bash-rhel10-2935) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/unix-socket-access-boundary-bash-rhel10-2935) | — | — |
| web-authentication-boundary | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__15-36-11/web-authentication-boundary-bash-rhel10-2935) | — | — |
| webdav-document-locks | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__15-36-11/webdav-document-locks-bash-rhel10-2935) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/working-directory-independent-launch-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 0.977 | — | — |
