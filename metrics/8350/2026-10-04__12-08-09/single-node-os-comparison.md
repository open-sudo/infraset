# single-node-os-comparison: command execution summary

Scope: `8350/2026-10-04__12-08-09`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | [8/1](../../../jobs/8350/2026-10-04__12-08-09/account-resource-limits-bash-rhel7-8350) | — | — | — | — |
| application-log-rotation | — | — | — | [12/1](../../../jobs/8350/2026-10-04__12-08-09/application-log-rotation-bash-rhel7-8350) | — | — | — | — |
| custom-ca-trust | — | — | — | [8/1](../../../jobs/8350/2026-10-04__12-08-09/custom-ca-trust-bash-rhel7-8350) | — | — | — | — |
| host-firewall-baseline | — | — | — | [13/3](../../../jobs/8350/2026-10-04__12-08-09/host-firewall-baseline-bash-rhel7-8350) | — | — | — | — |
| kernel-network-hardening | — | — | — | [7/1](../../../jobs/8350/2026-10-04__12-08-09/kernel-network-hardening-bash-rhel7-8350) | — | — | — | — |
| repair-application-permissions | — | — | — | [10/3](../../../jobs/8350/2026-10-04__12-08-09/repair-application-permissions-bash-rhel7-8350) | — | — | — | — |
| scheduled-maintenance | — | — | — | [10/0](../../../jobs/8350/2026-10-04__12-08-09/scheduled-maintenance-bash-rhel7-8350) | — | — | — | — |
| ssh-key-only | — | — | — | [15/0](../../../jobs/8350/2026-10-04__12-08-09/ssh-key-only-bash-rhel7-8350) | — | — | — | — |
| sticky-drop-directory | — | — | — | [10/0](../../../jobs/8350/2026-10-04__12-08-09/sticky-drop-directory-bash-rhel7-8350) | — | — | — | — |
| unprivileged-service | — | — | — | [9/17](../../../jobs/8350/2026-10-04__12-08-09/unprivileged-service-bash-rhel7-8350) | — | — | — | — |
| mandatory-access-control-port | — | — | — | [21/2](../../../jobs/8350/2026-10-04__12-08-09/mandatory-access-control-port-bash-rhel7-8350) | — | — | — | — |
| kernel-module-blacklist | — | — | — | [13/0](../../../jobs/8350/2026-10-04__12-08-09/kernel-module-blacklist-bash-rhel7-8350) | — | — | — | — |
| boot-kernel-parameter | — | — | — | [10/2](../../../jobs/8350/2026-10-04__12-08-09/boot-kernel-parameter-bash-rhel7-8350) | — | — | — | — |
| mount-option-hardening | — | — | — | [15/6](../../../jobs/8350/2026-10-04__12-08-09/mount-option-hardening-bash-rhel7-8350) | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | [7/1](../../../jobs/8350/2026-10-04__12-08-09/password-complexity-policy-bash-rhel7-8350) | — | — | — | — |
| sudo-command-logging | — | — | — | [8/1](../../../jobs/8350/2026-10-04__12-08-09/sudo-command-logging-bash-rhel7-8350) | — | — | — | — |
| cron-access-control | — | — | — | [7/6](../../../jobs/8350/2026-10-04__12-08-09/cron-access-control-bash-rhel7-8350) | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | [17/7](../../../jobs/8350/2026-10-04__12-08-09/disk-quota-bash-rhel7-8350) | — | — | — | — |
| encrypted-volume | — | — | — | [17/2](../../../jobs/8350/2026-10-04__12-08-09/encrypted-volume-bash-rhel7-8350) | — | — | — | — |
| lvm-extend | — | — | — | [19/5](../../../jobs/8350/2026-10-04__12-08-09/lvm-extend-bash-rhel7-8350) | — | — | — | — |
| filesystem-snapshot-rollback | — | — | — | [20/1](../../../jobs/8350/2026-10-04__12-08-09/filesystem-snapshot-rollback-bash-rhel7-8350) | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | [8/3](../../../jobs/8350/2026-10-04__12-08-09/package-version-hold-bash-rhel7-8350) | — | — | — | — |
| local-package-repository | — | — | — | [13/5](../../../jobs/8350/2026-10-04__12-08-09/local-package-repository-bash-rhel7-8350) | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | [14/4](../../../jobs/8350/2026-10-04__12-08-09/certificate-rotation-bash-rhel7-8350) | — | — | — | — |
| file-integrity-baseline | — | — | — | [25/3](../../../jobs/8350/2026-10-04__12-08-09/file-integrity-baseline-bash-rhel7-8350) | — | — | — | — |
| archive-member-safety | — | — | — | [8/4](../../../jobs/8350/2026-10-04__12-08-09/archive-member-safety-bash-rhel7-8350) | — | — | — | — |
| atomic-release-publication | — | — | — | [11/5](../../../jobs/8350/2026-10-04__12-08-09/atomic-release-publication-bash-rhel7-8350) | — | — | — | — |
| batch-exclusive-lock | — | — | — | [12/2](../../../jobs/8350/2026-10-04__12-08-09/batch-exclusive-lock-bash-rhel7-8350) | — | — | — | — |
| cgi-report-execution | — | — | — | [12/2](../../../jobs/8350/2026-10-04__12-08-09/cgi-report-execution-bash-rhel7-8350) | — | — | — | — |
| child-process-reaping | — | — | — | [10/4](../../../jobs/8350/2026-10-04__12-08-09/child-process-reaping-bash-rhel7-8350) | — | — | — | — |
| chroot-web-service | — | — | — | [16/6](../../../jobs/8350/2026-10-04__12-08-09/chroot-web-service-bash-rhel7-8350) | — | — | — | — |
| cross-file-accounting-reconciliation | — | — | — | [11/2](../../../jobs/8350/2026-10-04__12-08-09/cross-file-accounting-reconciliation-bash-rhel7-8350) | — | — | — | — |
| deleted-open-file-recovery | — | — | — | [14/5](../../../jobs/8350/2026-10-04__12-08-09/deleted-open-file-recovery-bash-rhel7-8350) | — | — | — | — |
| fifo-worker-reconnection | — | — | — | [22/2](../../../jobs/8350/2026-10-04__12-08-09/fifo-worker-reconnection-bash-rhel7-8350) | — | — | — | — |
| file-descriptor-leak | — | — | — | [9/1](../../../jobs/8350/2026-10-04__12-08-09/file-descriptor-leak-bash-rhel7-8350) | — | — | — | — |
| filename-encoding-migration | — | — | — | [8/6](../../../jobs/8350/2026-10-04__12-08-09/filename-encoding-migration-bash-rhel7-8350) | — | — | — | — |
| fixed-width-import-recovery | — | — | — | [10/1](../../../jobs/8350/2026-10-04__12-08-09/fixed-width-import-recovery-bash-rhel7-8350) | — | — | — | — |
| hardlink-aware-deduplication | — | — | — | [12/2](../../../jobs/8350/2026-10-04__12-08-09/hardlink-aware-deduplication-bash-rhel7-8350) | — | — | — | — |
| incremental-archive-chain | — | — | — | [8/2](../../../jobs/8350/2026-10-04__12-08-09/incremental-archive-chain-bash-rhel7-8350) | — | — | — | — |
| inherited-directory-acls | — | — | — | [10/0](../../../jobs/8350/2026-10-04__12-08-09/inherited-directory-acls-bash-rhel7-8350) | — | — | — | — |
| inode-cache-retention | — | — | — | [0/0](../../../jobs/8350/2026-10-04__12-08-09/inode-cache-retention-bash-rhel7-8350) | — | — | — | — |
| large-counter-overflow | — | — | — | [9/4](../../../jobs/8350/2026-10-04__12-08-09/large-counter-overflow-bash-rhel7-8350) | — | — | — | — |
| mail-filter-routing | — | — | — | [11/1](../../../jobs/8350/2026-10-04__12-08-09/mail-filter-routing-bash-rhel7-8350) | — | — | — | — |
| mail-spool-deduplication | — | — | — | [14/2](../../../jobs/8350/2026-10-04__12-08-09/mail-spool-deduplication-bash-rhel7-8350) | — | — | — | — |
| minimal-environment-job | — | — | — | [9/1](../../../jobs/8350/2026-10-04__12-08-09/minimal-environment-job-bash-rhel7-8350) | — | — | — | — |
| name-based-web-tenants | — | — | — | [9/2](../../../jobs/8350/2026-10-04__12-08-09/name-based-web-tenants-bash-rhel7-8350) | — | — | — | — |
| numeric-record-ordering | — | — | — | [10/5](../../../jobs/8350/2026-10-04__12-08-09/numeric-record-ordering-bash-rhel7-8350) | — | — | — | — |
| permanent-url-migration | — | — | — | [14/2](../../../jobs/8350/2026-10-04__12-08-09/permanent-url-migration-bash-rhel7-8350) | — | — | — | — |
| persistent-swap | — | — | — | [11/0](../../../jobs/8350/2026-10-04__12-08-09/persistent-swap-bash-rhel7-8350) | — | — | — | — |
| posix-shell-installer | — | — | — | [13/14](../../../jobs/8350/2026-10-04__12-08-09/posix-shell-installer-bash-rhel7-8350) | — | — | — | — |
| postgresql-sequence-repair | — | — | — | [18/3](../../../jobs/8350/2026-10-04__12-08-09/postgresql-sequence-repair-bash-rhel7-8350) | — | — | — | — |
| print-spool-recovery | — | — | — | [14/4](../../../jobs/8350/2026-10-04__12-08-09/print-spool-recovery-bash-rhel7-8350) | — | — | — | — |
| privacy-safe-support-export | — | — | — | [8/2](../../../jobs/8350/2026-10-04__12-08-09/privacy-safe-support-export-bash-rhel7-8350) | — | — | — | — |
| relative-symlink-relocation | — | — | — | [12/2](../../../jobs/8350/2026-10-04__12-08-09/relative-symlink-relocation-bash-rhel7-8350) | — | — | — | — |
| selective-tape-restore | — | — | — | [9/1](../../../jobs/8350/2026-10-04__12-08-09/selective-tape-restore-bash-rhel7-8350) | — | — | — | — |
| service-confinement | — | — | — | [16/1](../../../jobs/8350/2026-10-04__12-08-09/service-confinement-bash-rhel7-8350) | — | — | — | — |
| service-resource-limits | — | — | — | [11/3](../../../jobs/8350/2026-10-04__12-08-09/service-resource-limits-bash-rhel7-8350) | — | — | — | — |
| signal-driven-config-reload | — | — | — | [12/8](../../../jobs/8350/2026-10-04__12-08-09/signal-driven-config-reload-bash-rhel7-8350) | — | — | — | — |
| sparse-image-copy | — | — | — | [8/1](../../../jobs/8350/2026-10-04__12-08-09/sparse-image-copy-bash-rhel7-8350) | — | — | — | — |
| sqlite-lock-contention | — | — | — | [12/3](../../../jobs/8350/2026-10-04__12-08-09/sqlite-lock-contention-bash-rhel7-8350) | — | — | — | — |
| ssh-host-key-pinning | — | — | — | [11/2](../../../jobs/8350/2026-10-04__12-08-09/ssh-host-key-pinning-bash-rhel7-8350) | — | — | — | — |
| stale-pidfile-startup | — | — | — | [11/1](../../../jobs/8350/2026-10-04__12-08-09/stale-pidfile-startup-bash-rhel7-8350) | — | — | — | — |
| temporary-file-symlink-defense | — | — | — | [10/2](../../../jobs/8350/2026-10-04__12-08-09/temporary-file-symlink-defense-bash-rhel7-8350) | — | — | — | — |
| text-export-normalization | — | — | — | [12/4](../../../jobs/8350/2026-10-04__12-08-09/text-export-normalization-bash-rhel7-8350) | — | — | — | — |
| timezone-log-merge | — | — | — | [11/4](../../../jobs/8350/2026-10-04__12-08-09/timezone-log-merge-bash-rhel7-8350) | — | — | — | — |
| transactional-schema-upgrade | — | — | — | [16/15](../../../jobs/8350/2026-10-04__12-08-09/transactional-schema-upgrade-bash-rhel7-8350) | — | — | — | — |
| unix-socket-access-boundary | — | — | — | [6/3](../../../jobs/8350/2026-10-04__12-08-09/unix-socket-access-boundary-bash-rhel7-8350) | — | — | — | — |
| web-authentication-boundary | — | — | — | [17/2](../../../jobs/8350/2026-10-04__12-08-09/web-authentication-boundary-bash-rhel7-8350) | — | — | — | — |
| webdav-document-locks | — | — | — | [19/1](../../../jobs/8350/2026-10-04__12-08-09/webdav-document-locks-bash-rhel7-8350) | — | — | — | — |
| working-directory-independent-launch | — | — | — | [11/1](../../../jobs/8350/2026-10-04__12-08-09/working-directory-independent-launch-bash-rhel7-8350) | — | — | — | — |
| **Average** | — | — | — | 11.9/3.0 | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | [4m 44s](../../../jobs/8350/2026-10-04__12-08-09/account-resource-limits-bash-rhel7-8350) | — | — | — | — |
| application-log-rotation | — | — | — | [6m 53s](../../../jobs/8350/2026-10-04__12-08-09/application-log-rotation-bash-rhel7-8350) | — | — | — | — |
| custom-ca-trust | — | — | — | [4m 35s](../../../jobs/8350/2026-10-04__12-08-09/custom-ca-trust-bash-rhel7-8350) | — | — | — | — |
| host-firewall-baseline | — | — | — | [8m 26s](../../../jobs/8350/2026-10-04__12-08-09/host-firewall-baseline-bash-rhel7-8350) | — | — | — | — |
| kernel-network-hardening | — | — | — | [4m 40s](../../../jobs/8350/2026-10-04__12-08-09/kernel-network-hardening-bash-rhel7-8350) | — | — | — | — |
| repair-application-permissions | — | — | — | [5m 29s](../../../jobs/8350/2026-10-04__12-08-09/repair-application-permissions-bash-rhel7-8350) | — | — | — | — |
| scheduled-maintenance | — | — | — | [5m 20s](../../../jobs/8350/2026-10-04__12-08-09/scheduled-maintenance-bash-rhel7-8350) | — | — | — | — |
| ssh-key-only | — | — | — | [6m 08s](../../../jobs/8350/2026-10-04__12-08-09/ssh-key-only-bash-rhel7-8350) | — | — | — | — |
| sticky-drop-directory | — | — | — | [4m 34s](../../../jobs/8350/2026-10-04__12-08-09/sticky-drop-directory-bash-rhel7-8350) | — | — | — | — |
| unprivileged-service | — | — | — | [6m 17s](../../../jobs/8350/2026-10-04__12-08-09/unprivileged-service-bash-rhel7-8350) | — | — | — | — |
| mandatory-access-control-port | — | — | — | [8m 52s](../../../jobs/8350/2026-10-04__12-08-09/mandatory-access-control-port-bash-rhel7-8350) | — | — | — | — |
| kernel-module-blacklist | — | — | — | [5m 22s](../../../jobs/8350/2026-10-04__12-08-09/kernel-module-blacklist-bash-rhel7-8350) | — | — | — | — |
| boot-kernel-parameter | — | — | — | [4m 45s](../../../jobs/8350/2026-10-04__12-08-09/boot-kernel-parameter-bash-rhel7-8350) | — | — | — | — |
| mount-option-hardening | — | — | — | [6m 35s](../../../jobs/8350/2026-10-04__12-08-09/mount-option-hardening-bash-rhel7-8350) | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | [4m 48s](../../../jobs/8350/2026-10-04__12-08-09/password-complexity-policy-bash-rhel7-8350) | — | — | — | — |
| sudo-command-logging | — | — | — | [4m 45s](../../../jobs/8350/2026-10-04__12-08-09/sudo-command-logging-bash-rhel7-8350) | — | — | — | — |
| cron-access-control | — | — | — | [5m 14s](../../../jobs/8350/2026-10-04__12-08-09/cron-access-control-bash-rhel7-8350) | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | [33m 14s](../../../jobs/8350/2026-10-04__12-08-09/disk-quota-bash-rhel7-8350) | — | — | — | — |
| encrypted-volume | — | — | — | [9m 01s](../../../jobs/8350/2026-10-04__12-08-09/encrypted-volume-bash-rhel7-8350) | — | — | — | — |
| lvm-extend | — | — | — | [6m 15s](../../../jobs/8350/2026-10-04__12-08-09/lvm-extend-bash-rhel7-8350) | — | — | — | — |
| filesystem-snapshot-rollback | — | — | — | [7m 54s](../../../jobs/8350/2026-10-04__12-08-09/filesystem-snapshot-rollback-bash-rhel7-8350) | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | [5m 17s](../../../jobs/8350/2026-10-04__12-08-09/package-version-hold-bash-rhel7-8350) | — | — | — | — |
| local-package-repository | — | — | — | [7m 18s](../../../jobs/8350/2026-10-04__12-08-09/local-package-repository-bash-rhel7-8350) | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | [7m 44s](../../../jobs/8350/2026-10-04__12-08-09/certificate-rotation-bash-rhel7-8350) | — | — | — | — |
| file-integrity-baseline | — | — | — | [7m 24s](../../../jobs/8350/2026-10-04__12-08-09/file-integrity-baseline-bash-rhel7-8350) | — | — | — | — |
| archive-member-safety | — | — | — | [7m 12s](../../../jobs/8350/2026-10-04__12-08-09/archive-member-safety-bash-rhel7-8350) | — | — | — | — |
| atomic-release-publication | — | — | — | [7m 26s](../../../jobs/8350/2026-10-04__12-08-09/atomic-release-publication-bash-rhel7-8350) | — | — | — | — |
| batch-exclusive-lock | — | — | — | [6m 31s](../../../jobs/8350/2026-10-04__12-08-09/batch-exclusive-lock-bash-rhel7-8350) | — | — | — | — |
| cgi-report-execution | — | — | — | [6m 10s](../../../jobs/8350/2026-10-04__12-08-09/cgi-report-execution-bash-rhel7-8350) | — | — | — | — |
| child-process-reaping | — | — | — | [7m 34s](../../../jobs/8350/2026-10-04__12-08-09/child-process-reaping-bash-rhel7-8350) | — | — | — | — |
| chroot-web-service | — | — | — | [7m 29s](../../../jobs/8350/2026-10-04__12-08-09/chroot-web-service-bash-rhel7-8350) | — | — | — | — |
| cross-file-accounting-reconciliation | — | — | — | [6m 13s](../../../jobs/8350/2026-10-04__12-08-09/cross-file-accounting-reconciliation-bash-rhel7-8350) | — | — | — | — |
| deleted-open-file-recovery | — | — | — | [8m 28s](../../../jobs/8350/2026-10-04__12-08-09/deleted-open-file-recovery-bash-rhel7-8350) | — | — | — | — |
| fifo-worker-reconnection | — | — | — | [10m 29s](../../../jobs/8350/2026-10-04__12-08-09/fifo-worker-reconnection-bash-rhel7-8350) | — | — | — | — |
| file-descriptor-leak | — | — | — | [6m 22s](../../../jobs/8350/2026-10-04__12-08-09/file-descriptor-leak-bash-rhel7-8350) | — | — | — | — |
| filename-encoding-migration | — | — | — | [6m 33s](../../../jobs/8350/2026-10-04__12-08-09/filename-encoding-migration-bash-rhel7-8350) | — | — | — | — |
| fixed-width-import-recovery | — | — | — | [6m 59s](../../../jobs/8350/2026-10-04__12-08-09/fixed-width-import-recovery-bash-rhel7-8350) | — | — | — | — |
| hardlink-aware-deduplication | — | — | — | [6m 28s](../../../jobs/8350/2026-10-04__12-08-09/hardlink-aware-deduplication-bash-rhel7-8350) | — | — | — | — |
| incremental-archive-chain | — | — | — | [5m 44s](../../../jobs/8350/2026-10-04__12-08-09/incremental-archive-chain-bash-rhel7-8350) | — | — | — | — |
| inherited-directory-acls | — | — | — | [5m 46s](../../../jobs/8350/2026-10-04__12-08-09/inherited-directory-acls-bash-rhel7-8350) | — | — | — | — |
| inode-cache-retention | — | — | — | [2m 22s](../../../jobs/8350/2026-10-04__12-08-09/inode-cache-retention-bash-rhel7-8350) | — | — | — | — |
| large-counter-overflow | — | — | — | [6m 37s](../../../jobs/8350/2026-10-04__12-08-09/large-counter-overflow-bash-rhel7-8350) | — | — | — | — |
| mail-filter-routing | — | — | — | [6m 36s](../../../jobs/8350/2026-10-04__12-08-09/mail-filter-routing-bash-rhel7-8350) | — | — | — | — |
| mail-spool-deduplication | — | — | — | [7m 25s](../../../jobs/8350/2026-10-04__12-08-09/mail-spool-deduplication-bash-rhel7-8350) | — | — | — | — |
| minimal-environment-job | — | — | — | [5m 22s](../../../jobs/8350/2026-10-04__12-08-09/minimal-environment-job-bash-rhel7-8350) | — | — | — | — |
| name-based-web-tenants | — | — | — | [6m 10s](../../../jobs/8350/2026-10-04__12-08-09/name-based-web-tenants-bash-rhel7-8350) | — | — | — | — |
| numeric-record-ordering | — | — | — | [6m 19s](../../../jobs/8350/2026-10-04__12-08-09/numeric-record-ordering-bash-rhel7-8350) | — | — | — | — |
| permanent-url-migration | — | — | — | [7m 15s](../../../jobs/8350/2026-10-04__12-08-09/permanent-url-migration-bash-rhel7-8350) | — | — | — | — |
| persistent-swap | — | — | — | [4m 55s](../../../jobs/8350/2026-10-04__12-08-09/persistent-swap-bash-rhel7-8350) | — | — | — | — |
| posix-shell-installer | — | — | — | [7m 01s](../../../jobs/8350/2026-10-04__12-08-09/posix-shell-installer-bash-rhel7-8350) | — | — | — | — |
| postgresql-sequence-repair | — | — | — | [9m 48s](../../../jobs/8350/2026-10-04__12-08-09/postgresql-sequence-repair-bash-rhel7-8350) | — | — | — | — |
| print-spool-recovery | — | — | — | [7m 39s](../../../jobs/8350/2026-10-04__12-08-09/print-spool-recovery-bash-rhel7-8350) | — | — | — | — |
| privacy-safe-support-export | — | — | — | [6m 21s](../../../jobs/8350/2026-10-04__12-08-09/privacy-safe-support-export-bash-rhel7-8350) | — | — | — | — |
| relative-symlink-relocation | — | — | — | [5m 52s](../../../jobs/8350/2026-10-04__12-08-09/relative-symlink-relocation-bash-rhel7-8350) | — | — | — | — |
| selective-tape-restore | — | — | — | [5m 36s](../../../jobs/8350/2026-10-04__12-08-09/selective-tape-restore-bash-rhel7-8350) | — | — | — | — |
| service-confinement | — | — | — | [7m 40s](../../../jobs/8350/2026-10-04__12-08-09/service-confinement-bash-rhel7-8350) | — | — | — | — |
| service-resource-limits | — | — | — | [6m 02s](../../../jobs/8350/2026-10-04__12-08-09/service-resource-limits-bash-rhel7-8350) | — | — | — | — |
| signal-driven-config-reload | — | — | — | [8m 19s](../../../jobs/8350/2026-10-04__12-08-09/signal-driven-config-reload-bash-rhel7-8350) | — | — | — | — |
| sparse-image-copy | — | — | — | [5m 37s](../../../jobs/8350/2026-10-04__12-08-09/sparse-image-copy-bash-rhel7-8350) | — | — | — | — |
| sqlite-lock-contention | — | — | — | [7m 16s](../../../jobs/8350/2026-10-04__12-08-09/sqlite-lock-contention-bash-rhel7-8350) | — | — | — | — |
| ssh-host-key-pinning | — | — | — | [5m 35s](../../../jobs/8350/2026-10-04__12-08-09/ssh-host-key-pinning-bash-rhel7-8350) | — | — | — | — |
| stale-pidfile-startup | — | — | — | [6m 45s](../../../jobs/8350/2026-10-04__12-08-09/stale-pidfile-startup-bash-rhel7-8350) | — | — | — | — |
| temporary-file-symlink-defense | — | — | — | [7m 01s](../../../jobs/8350/2026-10-04__12-08-09/temporary-file-symlink-defense-bash-rhel7-8350) | — | — | — | — |
| text-export-normalization | — | — | — | [7m 06s](../../../jobs/8350/2026-10-04__12-08-09/text-export-normalization-bash-rhel7-8350) | — | — | — | — |
| timezone-log-merge | — | — | — | [6m 27s](../../../jobs/8350/2026-10-04__12-08-09/timezone-log-merge-bash-rhel7-8350) | — | — | — | — |
| transactional-schema-upgrade | — | — | — | [7m 42s](../../../jobs/8350/2026-10-04__12-08-09/transactional-schema-upgrade-bash-rhel7-8350) | — | — | — | — |
| unix-socket-access-boundary | — | — | — | [6m 21s](../../../jobs/8350/2026-10-04__12-08-09/unix-socket-access-boundary-bash-rhel7-8350) | — | — | — | — |
| web-authentication-boundary | — | — | — | [9m 40s](../../../jobs/8350/2026-10-04__12-08-09/web-authentication-boundary-bash-rhel7-8350) | — | — | — | — |
| webdav-document-locks | — | — | — | [12m 37s](../../../jobs/8350/2026-10-04__12-08-09/webdav-document-locks-bash-rhel7-8350) | — | — | — | — |
| working-directory-independent-launch | — | — | — | [5m 46s](../../../jobs/8350/2026-10-04__12-08-09/working-directory-independent-launch-bash-rhel7-8350) | — | — | — | — |
| **Average** | — | — | — | 7m 02s | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 958 ms across 100 clusters, about 0.22% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | [0.970](../../../jobs/8350/2026-10-04__12-08-09/account-resource-limits-bash-rhel7-8350) | — | — | — | — |
| application-log-rotation | — | — | — | [0.780](../../../jobs/8350/2026-10-04__12-08-09/application-log-rotation-bash-rhel7-8350) | — | — | — | — |
| custom-ca-trust | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/custom-ca-trust-bash-rhel7-8350) | — | — | — | — |
| host-firewall-baseline | — | — | — | [0.880](../../../jobs/8350/2026-10-04__12-08-09/host-firewall-baseline-bash-rhel7-8350) | — | — | — | — |
| kernel-network-hardening | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/kernel-network-hardening-bash-rhel7-8350) | — | — | — | — |
| repair-application-permissions | — | — | — | [0.940](../../../jobs/8350/2026-10-04__12-08-09/repair-application-permissions-bash-rhel7-8350) | — | — | — | — |
| scheduled-maintenance | — | — | — | [0.860](../../../jobs/8350/2026-10-04__12-08-09/scheduled-maintenance-bash-rhel7-8350) | — | — | — | — |
| ssh-key-only | — | — | — | [0.920](../../../jobs/8350/2026-10-04__12-08-09/ssh-key-only-bash-rhel7-8350) | — | — | — | — |
| sticky-drop-directory | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/sticky-drop-directory-bash-rhel7-8350) | — | — | — | — |
| unprivileged-service | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/unprivileged-service-bash-rhel7-8350) | — | — | — | — |
| mandatory-access-control-port | — | — | — | [0.920](../../../jobs/8350/2026-10-04__12-08-09/mandatory-access-control-port-bash-rhel7-8350) | — | — | — | — |
| kernel-module-blacklist | — | — | — | [0.960](../../../jobs/8350/2026-10-04__12-08-09/kernel-module-blacklist-bash-rhel7-8350) | — | — | — | — |
| boot-kernel-parameter | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/boot-kernel-parameter-bash-rhel7-8350) | — | — | — | — |
| mount-option-hardening | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/mount-option-hardening-bash-rhel7-8350) | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | [0.980](../../../jobs/8350/2026-10-04__12-08-09/password-complexity-policy-bash-rhel7-8350) | — | — | — | — |
| sudo-command-logging | — | — | — | [0.940](../../../jobs/8350/2026-10-04__12-08-09/sudo-command-logging-bash-rhel7-8350) | — | — | — | — |
| cron-access-control | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/cron-access-control-bash-rhel7-8350) | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | [0.820](../../../jobs/8350/2026-10-04__12-08-09/disk-quota-bash-rhel7-8350) | — | — | — | — |
| encrypted-volume | — | — | — | [0.860](../../../jobs/8350/2026-10-04__12-08-09/encrypted-volume-bash-rhel7-8350) | — | — | — | — |
| lvm-extend | — | — | — | [0.920](../../../jobs/8350/2026-10-04__12-08-09/lvm-extend-bash-rhel7-8350) | — | — | — | — |
| filesystem-snapshot-rollback | — | — | — | [0.940](../../../jobs/8350/2026-10-04__12-08-09/filesystem-snapshot-rollback-bash-rhel7-8350) | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/package-version-hold-bash-rhel7-8350) | — | — | — | — |
| local-package-repository | — | — | — | [0.720](../../../jobs/8350/2026-10-04__12-08-09/local-package-repository-bash-rhel7-8350) | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | [0.950](../../../jobs/8350/2026-10-04__12-08-09/certificate-rotation-bash-rhel7-8350) | — | — | — | — |
| file-integrity-baseline | — | — | — | [0.840](../../../jobs/8350/2026-10-04__12-08-09/file-integrity-baseline-bash-rhel7-8350) | — | — | — | — |
| archive-member-safety | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/archive-member-safety-bash-rhel7-8350) | — | — | — | — |
| atomic-release-publication | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/atomic-release-publication-bash-rhel7-8350) | — | — | — | — |
| batch-exclusive-lock | — | — | — | [0.860](../../../jobs/8350/2026-10-04__12-08-09/batch-exclusive-lock-bash-rhel7-8350) | — | — | — | — |
| cgi-report-execution | — | — | — | [0.970](../../../jobs/8350/2026-10-04__12-08-09/cgi-report-execution-bash-rhel7-8350) | — | — | — | — |
| child-process-reaping | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/child-process-reaping-bash-rhel7-8350) | — | — | — | — |
| chroot-web-service | — | — | — | [0.860](../../../jobs/8350/2026-10-04__12-08-09/chroot-web-service-bash-rhel7-8350) | — | — | — | — |
| cross-file-accounting-reconciliation | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/cross-file-accounting-reconciliation-bash-rhel7-8350) | — | — | — | — |
| deleted-open-file-recovery | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/deleted-open-file-recovery-bash-rhel7-8350) | — | — | — | — |
| fifo-worker-reconnection | — | — | — | [0.820](../../../jobs/8350/2026-10-04__12-08-09/fifo-worker-reconnection-bash-rhel7-8350) | — | — | — | — |
| file-descriptor-leak | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/file-descriptor-leak-bash-rhel7-8350) | — | — | — | — |
| filename-encoding-migration | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/filename-encoding-migration-bash-rhel7-8350) | — | — | — | — |
| fixed-width-import-recovery | — | — | — | [0.880](../../../jobs/8350/2026-10-04__12-08-09/fixed-width-import-recovery-bash-rhel7-8350) | — | — | — | — |
| hardlink-aware-deduplication | — | — | — | [0.950](../../../jobs/8350/2026-10-04__12-08-09/hardlink-aware-deduplication-bash-rhel7-8350) | — | — | — | — |
| incremental-archive-chain | — | — | — | [0.970](../../../jobs/8350/2026-10-04__12-08-09/incremental-archive-chain-bash-rhel7-8350) | — | — | — | — |
| inherited-directory-acls | — | — | — | [0.960](../../../jobs/8350/2026-10-04__12-08-09/inherited-directory-acls-bash-rhel7-8350) | — | — | — | — |
| inode-cache-retention | — | — | — | — | — | — | — | — |
| large-counter-overflow | — | — | — | [0.800](../../../jobs/8350/2026-10-04__12-08-09/large-counter-overflow-bash-rhel7-8350) | — | — | — | — |
| mail-filter-routing | — | — | — | [0.970](../../../jobs/8350/2026-10-04__12-08-09/mail-filter-routing-bash-rhel7-8350) | — | — | — | — |
| mail-spool-deduplication | — | — | — | [0.970](../../../jobs/8350/2026-10-04__12-08-09/mail-spool-deduplication-bash-rhel7-8350) | — | — | — | — |
| minimal-environment-job | — | — | — | [0.840](../../../jobs/8350/2026-10-04__12-08-09/minimal-environment-job-bash-rhel7-8350) | — | — | — | — |
| name-based-web-tenants | — | — | — | [0.870](../../../jobs/8350/2026-10-04__12-08-09/name-based-web-tenants-bash-rhel7-8350) | — | — | — | — |
| numeric-record-ordering | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/numeric-record-ordering-bash-rhel7-8350) | — | — | — | — |
| permanent-url-migration | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/permanent-url-migration-bash-rhel7-8350) | — | — | — | — |
| persistent-swap | — | — | — | [0.940](../../../jobs/8350/2026-10-04__12-08-09/persistent-swap-bash-rhel7-8350) | — | — | — | — |
| posix-shell-installer | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/posix-shell-installer-bash-rhel7-8350) | — | — | — | — |
| postgresql-sequence-repair | — | — | — | [0.780](../../../jobs/8350/2026-10-04__12-08-09/postgresql-sequence-repair-bash-rhel7-8350) | — | — | — | — |
| print-spool-recovery | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/print-spool-recovery-bash-rhel7-8350) | — | — | — | — |
| privacy-safe-support-export | — | — | — | [0.820](../../../jobs/8350/2026-10-04__12-08-09/privacy-safe-support-export-bash-rhel7-8350) | — | — | — | — |
| relative-symlink-relocation | — | — | — | [0.970](../../../jobs/8350/2026-10-04__12-08-09/relative-symlink-relocation-bash-rhel7-8350) | — | — | — | — |
| selective-tape-restore | — | — | — | [0.970](../../../jobs/8350/2026-10-04__12-08-09/selective-tape-restore-bash-rhel7-8350) | — | — | — | — |
| service-confinement | — | — | — | [0.980](../../../jobs/8350/2026-10-04__12-08-09/service-confinement-bash-rhel7-8350) | — | — | — | — |
| service-resource-limits | — | — | — | [0.980](../../../jobs/8350/2026-10-04__12-08-09/service-resource-limits-bash-rhel7-8350) | — | — | — | — |
| signal-driven-config-reload | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/signal-driven-config-reload-bash-rhel7-8350) | — | — | — | — |
| sparse-image-copy | — | — | — | [0.980](../../../jobs/8350/2026-10-04__12-08-09/sparse-image-copy-bash-rhel7-8350) | — | — | — | — |
| sqlite-lock-contention | — | — | — | [0.840](../../../jobs/8350/2026-10-04__12-08-09/sqlite-lock-contention-bash-rhel7-8350) | — | — | — | — |
| ssh-host-key-pinning | — | — | — | [0.960](../../../jobs/8350/2026-10-04__12-08-09/ssh-host-key-pinning-bash-rhel7-8350) | — | — | — | — |
| stale-pidfile-startup | — | — | — | [0.920](../../../jobs/8350/2026-10-04__12-08-09/stale-pidfile-startup-bash-rhel7-8350) | — | — | — | — |
| temporary-file-symlink-defense | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/temporary-file-symlink-defense-bash-rhel7-8350) | — | — | — | — |
| text-export-normalization | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/text-export-normalization-bash-rhel7-8350) | — | — | — | — |
| timezone-log-merge | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/timezone-log-merge-bash-rhel7-8350) | — | — | — | — |
| transactional-schema-upgrade | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/transactional-schema-upgrade-bash-rhel7-8350) | — | — | — | — |
| unix-socket-access-boundary | — | — | — | [0.860](../../../jobs/8350/2026-10-04__12-08-09/unix-socket-access-boundary-bash-rhel7-8350) | — | — | — | — |
| web-authentication-boundary | — | — | — | [0.920](../../../jobs/8350/2026-10-04__12-08-09/web-authentication-boundary-bash-rhel7-8350) | — | — | — | — |
| webdav-document-locks | — | — | — | [0.920](../../../jobs/8350/2026-10-04__12-08-09/webdav-document-locks-bash-rhel7-8350) | — | — | — | — |
| working-directory-independent-launch | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/working-directory-independent-launch-bash-rhel7-8350) | — | — | — | — |
| **Average** | — | — | — | 0.928 | — | — | — | — |
