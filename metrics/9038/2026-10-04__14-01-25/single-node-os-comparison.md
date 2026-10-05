# single-node-os-comparison: command execution summary

Scope: `9038/2026-10-04__14-01-25`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [11/0](../../../jobs/9038/2026-10-04__14-01-25/account-resource-limits-bash-rhel10-9038) | — | — |
| application-log-rotation | — | — | — | — | — | [10/0](../../../jobs/9038/2026-10-04__14-01-25/application-log-rotation-bash-rhel10-9038) | — | — |
| custom-ca-trust | — | — | — | — | — | [0/0](../../../jobs/9038/2026-10-04__14-01-25/custom-ca-trust-bash-rhel10-9038) | — | — |
| host-firewall-baseline | — | — | — | — | — | [10/0](../../../jobs/9038/2026-10-04__14-01-25/host-firewall-baseline-bash-rhel10-9038) | — | — |
| kernel-network-hardening | — | — | — | — | — | [12/0](../../../jobs/9038/2026-10-04__14-01-25/kernel-network-hardening-bash-rhel10-9038) | — | — |
| repair-application-permissions | — | — | — | — | — | [9/0](../../../jobs/9038/2026-10-04__14-01-25/repair-application-permissions-bash-rhel10-9038) | — | — |
| scheduled-maintenance | — | — | — | — | — | [13/0](../../../jobs/9038/2026-10-04__14-01-25/scheduled-maintenance-bash-rhel10-9038) | — | — |
| ssh-key-only | — | — | — | — | — | [11/0](../../../jobs/9038/2026-10-04__14-01-25/ssh-key-only-bash-rhel10-9038) | — | — |
| sticky-drop-directory | — | — | — | — | — | [12/0](../../../jobs/9038/2026-10-04__14-01-25/sticky-drop-directory-bash-rhel10-9038) | — | — |
| unprivileged-service | — | — | — | — | — | [10/0](../../../jobs/9038/2026-10-04__14-01-25/unprivileged-service-bash-rhel10-9038) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [13/1](../../../jobs/9038/2026-10-04__14-01-25/mandatory-access-control-port-bash-rhel10-9038) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [8/0](../../../jobs/9038/2026-10-04__14-01-25/kernel-module-blacklist-bash-rhel10-9038) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [7/0](../../../jobs/9038/2026-10-04__14-01-25/boot-kernel-parameter-bash-rhel10-9038) | — | — |
| mount-option-hardening | — | — | — | — | — | [12/1](../../../jobs/9038/2026-10-04__14-01-25/mount-option-hardening-bash-rhel10-9038) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [8/0](../../../jobs/9038/2026-10-04__14-01-25/password-complexity-policy-bash-rhel10-9038) | — | — |
| sudo-command-logging | — | — | — | — | — | [13/1](../../../jobs/9038/2026-10-04__14-01-25/sudo-command-logging-bash-rhel10-9038) | — | — |
| cron-access-control | — | — | — | — | — | [9/0](../../../jobs/9038/2026-10-04__14-01-25/cron-access-control-bash-rhel10-9038) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [11/1](../../../jobs/9038/2026-10-04__14-01-25/disk-quota-bash-rhel10-9038) | — | — |
| encrypted-volume | — | — | — | — | — | [15/0](../../../jobs/9038/2026-10-04__14-01-25/encrypted-volume-bash-rhel10-9038) | — | — |
| lvm-extend | — | — | — | — | — | [11/0](../../../jobs/9038/2026-10-04__14-01-25/lvm-extend-bash-rhel10-9038) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | [22/2](../../../jobs/9038/2026-10-04__14-01-25/filesystem-snapshot-rollback-bash-rhel10-9038) | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [14/0](../../../jobs/9038/2026-10-04__14-01-25/package-version-hold-bash-rhel10-9038) | — | — |
| local-package-repository | — | — | — | — | — | [0/0](../../../jobs/9038/2026-10-04__14-01-25/local-package-repository-bash-rhel10-9038) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [17/1](../../../jobs/9038/2026-10-04__14-01-25/certificate-rotation-bash-rhel10-9038) | — | — |
| file-integrity-baseline | — | — | — | — | — | [21/4](../../../jobs/9038/2026-10-04__14-01-25/file-integrity-baseline-bash-rhel10-9038) | — | — |
| archive-member-safety | — | — | — | — | — | [9/1](../../../jobs/9038/2026-10-04__14-01-25/archive-member-safety-bash-rhel10-9038) | — | — |
| atomic-release-publication | — | — | — | — | — | [10/0](../../../jobs/9038/2026-10-04__14-01-25/atomic-release-publication-bash-rhel10-9038) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [8/0](../../../jobs/9038/2026-10-04__14-01-25/batch-exclusive-lock-bash-rhel10-9038) | — | — |
| cgi-report-execution | — | — | — | — | — | [16/0](../../../jobs/9038/2026-10-04__14-01-25/cgi-report-execution-bash-rhel10-9038) | — | — |
| child-process-reaping | — | — | — | — | — | [10/2](../../../jobs/9038/2026-10-04__14-01-25/child-process-reaping-bash-rhel10-9038) | — | — |
| chroot-web-service | — | — | — | — | — | [25/5](../../../jobs/9038/2026-10-04__14-01-25/chroot-web-service-bash-rhel10-9038) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [11/0](../../../jobs/9038/2026-10-04__14-01-25/cross-file-accounting-reconciliation-bash-rhel10-9038) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [17/0](../../../jobs/9038/2026-10-04__14-01-25/deleted-open-file-recovery-bash-rhel10-9038) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [17/0](../../../jobs/9038/2026-10-04__14-01-25/fifo-worker-reconnection-bash-rhel10-9038) | — | — |
| file-descriptor-leak | — | — | — | — | — | [12/0](../../../jobs/9038/2026-10-04__14-01-25/file-descriptor-leak-bash-rhel10-9038) | — | — |
| filename-encoding-migration | — | — | — | — | — | [9/1](../../../jobs/9038/2026-10-04__14-01-25/filename-encoding-migration-bash-rhel10-9038) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [13/0](../../../jobs/9038/2026-10-04__14-01-25/fixed-width-import-recovery-bash-rhel10-9038) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [11/1](../../../jobs/9038/2026-10-04__14-01-25/hardlink-aware-deduplication-bash-rhel10-9038) | — | — |
| incremental-archive-chain | — | — | — | — | — | [10/0](../../../jobs/9038/2026-10-04__14-01-25/incremental-archive-chain-bash-rhel10-9038) | — | — |
| inherited-directory-acls | — | — | — | — | — | [11/0](../../../jobs/9038/2026-10-04__14-01-25/inherited-directory-acls-bash-rhel10-9038) | — | — |
| inode-cache-retention | — | — | — | — | — | [0/0](../../../jobs/9038/2026-10-04__14-01-25/inode-cache-retention-bash-rhel10-9038) | — | — |
| large-counter-overflow | — | — | — | — | — | [13/0](../../../jobs/9038/2026-10-04__14-01-25/large-counter-overflow-bash-rhel10-9038) | — | — |
| mail-filter-routing | — | — | — | — | — | [10/0](../../../jobs/9038/2026-10-04__14-01-25/mail-filter-routing-bash-rhel10-9038) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [10/1](../../../jobs/9038/2026-10-04__14-01-25/mail-spool-deduplication-bash-rhel10-9038) | — | — |
| minimal-environment-job | — | — | — | — | — | [10/1](../../../jobs/9038/2026-10-04__14-01-25/minimal-environment-job-bash-rhel10-9038) | — | — |
| name-based-web-tenants | — | — | — | — | — | [23/0](../../../jobs/9038/2026-10-04__14-01-25/name-based-web-tenants-bash-rhel10-9038) | — | — |
| numeric-record-ordering | — | — | — | — | — | [10/0](../../../jobs/9038/2026-10-04__14-01-25/numeric-record-ordering-bash-rhel10-9038) | — | — |
| permanent-url-migration | — | — | — | — | — | [17/0](../../../jobs/9038/2026-10-04__14-01-25/permanent-url-migration-bash-rhel10-9038) | — | — |
| persistent-swap | — | — | — | — | — | [10/1](../../../jobs/9038/2026-10-04__14-01-25/persistent-swap-bash-rhel10-9038) | — | — |
| posix-shell-installer | — | — | — | — | — | [13/0](../../../jobs/9038/2026-10-04__14-01-25/posix-shell-installer-bash-rhel10-9038) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [13/0](../../../jobs/9038/2026-10-04__14-01-25/postgresql-sequence-repair-bash-rhel10-9038) | — | — |
| print-spool-recovery | — | — | — | — | — | [19/0](../../../jobs/9038/2026-10-04__14-01-25/print-spool-recovery-bash-rhel10-9038) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [11/0](../../../jobs/9038/2026-10-04__14-01-25/privacy-safe-support-export-bash-rhel10-9038) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [7/1](../../../jobs/9038/2026-10-04__14-01-25/relative-symlink-relocation-bash-rhel10-9038) | — | — |
| selective-tape-restore | — | — | — | — | — | [9/0](../../../jobs/9038/2026-10-04__14-01-25/selective-tape-restore-bash-rhel10-9038) | — | — |
| service-confinement | — | — | — | — | — | [24/8](../../../jobs/9038/2026-10-04__14-01-25/service-confinement-bash-rhel10-9038) | — | — |
| service-resource-limits | — | — | — | — | — | [15/1](../../../jobs/9038/2026-10-04__14-01-25/service-resource-limits-bash-rhel10-9038) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [14/0](../../../jobs/9038/2026-10-04__14-01-25/signal-driven-config-reload-bash-rhel10-9038) | — | — |
| sparse-image-copy | — | — | — | — | — | [8/0](../../../jobs/9038/2026-10-04__14-01-25/sparse-image-copy-bash-rhel10-9038) | — | — |
| sqlite-lock-contention | — | — | — | — | — | [18/1](../../../jobs/9038/2026-10-04__14-01-25/sqlite-lock-contention-bash-rhel10-9038) | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [14/0](../../../jobs/9038/2026-10-04__14-01-25/ssh-host-key-pinning-bash-rhel10-9038) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [20/0](../../../jobs/9038/2026-10-04__14-01-25/stale-pidfile-startup-bash-rhel10-9038) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [12/1](../../../jobs/9038/2026-10-04__14-01-25/temporary-file-symlink-defense-bash-rhel10-9038) | — | — |
| text-export-normalization | — | — | — | — | — | [12/1](../../../jobs/9038/2026-10-04__14-01-25/text-export-normalization-bash-rhel10-9038) | — | — |
| timezone-log-merge | — | — | — | — | — | [14/0](../../../jobs/9038/2026-10-04__14-01-25/timezone-log-merge-bash-rhel10-9038) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [13/0](../../../jobs/9038/2026-10-04__14-01-25/transactional-schema-upgrade-bash-rhel10-9038) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [14/1](../../../jobs/9038/2026-10-04__14-01-25/unix-socket-access-boundary-bash-rhel10-9038) | — | — |
| web-authentication-boundary | — | — | — | — | — | [12/0](../../../jobs/9038/2026-10-04__14-01-25/web-authentication-boundary-bash-rhel10-9038) | — | — |
| webdav-document-locks | — | — | — | — | — | [15/0](../../../jobs/9038/2026-10-04__14-01-25/webdav-document-locks-bash-rhel10-9038) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [11/0](../../../jobs/9038/2026-10-04__14-01-25/working-directory-independent-launch-bash-rhel10-9038) | — | — |
| **Average** | — | — | — | — | — | 12.3/0.5 | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [3m 37s](../../../jobs/9038/2026-10-04__14-01-25/account-resource-limits-bash-rhel10-9038) | — | — |
| application-log-rotation | — | — | — | — | — | [3m 54s](../../../jobs/9038/2026-10-04__14-01-25/application-log-rotation-bash-rhel10-9038) | — | — |
| custom-ca-trust | — | — | — | — | — | [1m 20s](../../../jobs/9038/2026-10-04__14-01-25/custom-ca-trust-bash-rhel10-9038) | — | — |
| host-firewall-baseline | — | — | — | — | — | [4m 06s](../../../jobs/9038/2026-10-04__14-01-25/host-firewall-baseline-bash-rhel10-9038) | — | — |
| kernel-network-hardening | — | — | — | — | — | [3m 57s](../../../jobs/9038/2026-10-04__14-01-25/kernel-network-hardening-bash-rhel10-9038) | — | — |
| repair-application-permissions | — | — | — | — | — | [3m 27s](../../../jobs/9038/2026-10-04__14-01-25/repair-application-permissions-bash-rhel10-9038) | — | — |
| scheduled-maintenance | — | — | — | — | — | [28m 31s](../../../jobs/9038/2026-10-04__14-01-25/scheduled-maintenance-bash-rhel10-9038) | — | — |
| ssh-key-only | — | — | — | — | — | [4m 18s](../../../jobs/9038/2026-10-04__14-01-25/ssh-key-only-bash-rhel10-9038) | — | — |
| sticky-drop-directory | — | — | — | — | — | [4m 19s](../../../jobs/9038/2026-10-04__14-01-25/sticky-drop-directory-bash-rhel10-9038) | — | — |
| unprivileged-service | — | — | — | — | — | [3m 05s](../../../jobs/9038/2026-10-04__14-01-25/unprivileged-service-bash-rhel10-9038) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [19m 09s](../../../jobs/9038/2026-10-04__14-01-25/mandatory-access-control-port-bash-rhel10-9038) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [3m 19s](../../../jobs/9038/2026-10-04__14-01-25/kernel-module-blacklist-bash-rhel10-9038) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [3m 31s](../../../jobs/9038/2026-10-04__14-01-25/boot-kernel-parameter-bash-rhel10-9038) | — | — |
| mount-option-hardening | — | — | — | — | — | [3m 39s](../../../jobs/9038/2026-10-04__14-01-25/mount-option-hardening-bash-rhel10-9038) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [3m 26s](../../../jobs/9038/2026-10-04__14-01-25/password-complexity-policy-bash-rhel10-9038) | — | — |
| sudo-command-logging | — | — | — | — | — | [5m 07s](../../../jobs/9038/2026-10-04__14-01-25/sudo-command-logging-bash-rhel10-9038) | — | — |
| cron-access-control | — | — | — | — | — | [3m 38s](../../../jobs/9038/2026-10-04__14-01-25/cron-access-control-bash-rhel10-9038) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [3m 26s](../../../jobs/9038/2026-10-04__14-01-25/disk-quota-bash-rhel10-9038) | — | — |
| encrypted-volume | — | — | — | — | — | [5m 42s](../../../jobs/9038/2026-10-04__14-01-25/encrypted-volume-bash-rhel10-9038) | — | — |
| lvm-extend | — | — | — | — | — | [9m 54s](../../../jobs/9038/2026-10-04__14-01-25/lvm-extend-bash-rhel10-9038) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | [6m 53s](../../../jobs/9038/2026-10-04__14-01-25/filesystem-snapshot-rollback-bash-rhel10-9038) | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [3m 33s](../../../jobs/9038/2026-10-04__14-01-25/package-version-hold-bash-rhel10-9038) | — | — |
| local-package-repository | — | — | — | — | — | [41m 05s](../../../jobs/9038/2026-10-04__14-01-25/local-package-repository-bash-rhel10-9038) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [5m 54s](../../../jobs/9038/2026-10-04__14-01-25/certificate-rotation-bash-rhel10-9038) | — | — |
| file-integrity-baseline | — | — | — | — | — | [6m 13s](../../../jobs/9038/2026-10-04__14-01-25/file-integrity-baseline-bash-rhel10-9038) | — | — |
| archive-member-safety | — | — | — | — | — | [4m 29s](../../../jobs/9038/2026-10-04__14-01-25/archive-member-safety-bash-rhel10-9038) | — | — |
| atomic-release-publication | — | — | — | — | — | [4m 19s](../../../jobs/9038/2026-10-04__14-01-25/atomic-release-publication-bash-rhel10-9038) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [5m 14s](../../../jobs/9038/2026-10-04__14-01-25/batch-exclusive-lock-bash-rhel10-9038) | — | — |
| cgi-report-execution | — | — | — | — | — | [5m 48s](../../../jobs/9038/2026-10-04__14-01-25/cgi-report-execution-bash-rhel10-9038) | — | — |
| child-process-reaping | — | — | — | — | — | [5m 36s](../../../jobs/9038/2026-10-04__14-01-25/child-process-reaping-bash-rhel10-9038) | — | — |
| chroot-web-service | — | — | — | — | — | [9m 14s](../../../jobs/9038/2026-10-04__14-01-25/chroot-web-service-bash-rhel10-9038) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [4m 29s](../../../jobs/9038/2026-10-04__14-01-25/cross-file-accounting-reconciliation-bash-rhel10-9038) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [31m 40s](../../../jobs/9038/2026-10-04__14-01-25/deleted-open-file-recovery-bash-rhel10-9038) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [5m 17s](../../../jobs/9038/2026-10-04__14-01-25/fifo-worker-reconnection-bash-rhel10-9038) | — | — |
| file-descriptor-leak | — | — | — | — | — | [4m 18s](../../../jobs/9038/2026-10-04__14-01-25/file-descriptor-leak-bash-rhel10-9038) | — | — |
| filename-encoding-migration | — | — | — | — | — | [4m 27s](../../../jobs/9038/2026-10-04__14-01-25/filename-encoding-migration-bash-rhel10-9038) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [4m 33s](../../../jobs/9038/2026-10-04__14-01-25/fixed-width-import-recovery-bash-rhel10-9038) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [4m 20s](../../../jobs/9038/2026-10-04__14-01-25/hardlink-aware-deduplication-bash-rhel10-9038) | — | — |
| incremental-archive-chain | — | — | — | — | — | [4m 14s](../../../jobs/9038/2026-10-04__14-01-25/incremental-archive-chain-bash-rhel10-9038) | — | — |
| inherited-directory-acls | — | — | — | — | — | [4m 35s](../../../jobs/9038/2026-10-04__14-01-25/inherited-directory-acls-bash-rhel10-9038) | — | — |
| inode-cache-retention | — | — | — | — | — | [51s](../../../jobs/9038/2026-10-04__14-01-25/inode-cache-retention-bash-rhel10-9038) | — | — |
| large-counter-overflow | — | — | — | — | — | [30m 14s](../../../jobs/9038/2026-10-04__14-01-25/large-counter-overflow-bash-rhel10-9038) | — | — |
| mail-filter-routing | — | — | — | — | — | [4m 24s](../../../jobs/9038/2026-10-04__14-01-25/mail-filter-routing-bash-rhel10-9038) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [29m 19s](../../../jobs/9038/2026-10-04__14-01-25/mail-spool-deduplication-bash-rhel10-9038) | — | — |
| minimal-environment-job | — | — | — | — | — | [4m 04s](../../../jobs/9038/2026-10-04__14-01-25/minimal-environment-job-bash-rhel10-9038) | — | — |
| name-based-web-tenants | — | — | — | — | — | [6m 18s](../../../jobs/9038/2026-10-04__14-01-25/name-based-web-tenants-bash-rhel10-9038) | — | — |
| numeric-record-ordering | — | — | — | — | — | [3m 45s](../../../jobs/9038/2026-10-04__14-01-25/numeric-record-ordering-bash-rhel10-9038) | — | — |
| permanent-url-migration | — | — | — | — | — | [29m 52s](../../../jobs/9038/2026-10-04__14-01-25/permanent-url-migration-bash-rhel10-9038) | — | — |
| persistent-swap | — | — | — | — | — | [3m 40s](../../../jobs/9038/2026-10-04__14-01-25/persistent-swap-bash-rhel10-9038) | — | — |
| posix-shell-installer | — | — | — | — | — | [4m 33s](../../../jobs/9038/2026-10-04__14-01-25/posix-shell-installer-bash-rhel10-9038) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [4m 26s](../../../jobs/9038/2026-10-04__14-01-25/postgresql-sequence-repair-bash-rhel10-9038) | — | — |
| print-spool-recovery | — | — | — | — | — | [6m 43s](../../../jobs/9038/2026-10-04__14-01-25/print-spool-recovery-bash-rhel10-9038) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [5m 06s](../../../jobs/9038/2026-10-04__14-01-25/privacy-safe-support-export-bash-rhel10-9038) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [3m 58s](../../../jobs/9038/2026-10-04__14-01-25/relative-symlink-relocation-bash-rhel10-9038) | — | — |
| selective-tape-restore | — | — | — | — | — | [2m 43s](../../../jobs/9038/2026-10-04__14-01-25/selective-tape-restore-bash-rhel10-9038) | — | — |
| service-confinement | — | — | — | — | — | [9m 23s](../../../jobs/9038/2026-10-04__14-01-25/service-confinement-bash-rhel10-9038) | — | — |
| service-resource-limits | — | — | — | — | — | [4m 20s](../../../jobs/9038/2026-10-04__14-01-25/service-resource-limits-bash-rhel10-9038) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [4m 47s](../../../jobs/9038/2026-10-04__14-01-25/signal-driven-config-reload-bash-rhel10-9038) | — | — |
| sparse-image-copy | — | — | — | — | — | [3m 30s](../../../jobs/9038/2026-10-04__14-01-25/sparse-image-copy-bash-rhel10-9038) | — | — |
| sqlite-lock-contention | — | — | — | — | — | [6m 27s](../../../jobs/9038/2026-10-04__14-01-25/sqlite-lock-contention-bash-rhel10-9038) | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [4m 14s](../../../jobs/9038/2026-10-04__14-01-25/ssh-host-key-pinning-bash-rhel10-9038) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [8m 55s](../../../jobs/9038/2026-10-04__14-01-25/stale-pidfile-startup-bash-rhel10-9038) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [5m 29s](../../../jobs/9038/2026-10-04__14-01-25/temporary-file-symlink-defense-bash-rhel10-9038) | — | — |
| text-export-normalization | — | — | — | — | — | [4m 08s](../../../jobs/9038/2026-10-04__14-01-25/text-export-normalization-bash-rhel10-9038) | — | — |
| timezone-log-merge | — | — | — | — | — | [4m 50s](../../../jobs/9038/2026-10-04__14-01-25/timezone-log-merge-bash-rhel10-9038) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [3m 29s](../../../jobs/9038/2026-10-04__14-01-25/transactional-schema-upgrade-bash-rhel10-9038) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [4m 43s](../../../jobs/9038/2026-10-04__14-01-25/unix-socket-access-boundary-bash-rhel10-9038) | — | — |
| web-authentication-boundary | — | — | — | — | — | [4m 37s](../../../jobs/9038/2026-10-04__14-01-25/web-authentication-boundary-bash-rhel10-9038) | — | — |
| webdav-document-locks | — | — | — | — | — | [4m 24s](../../../jobs/9038/2026-10-04__14-01-25/webdav-document-locks-bash-rhel10-9038) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [3m 46s](../../../jobs/9038/2026-10-04__14-01-25/working-directory-independent-launch-bash-rhel10-9038) | — | — |
| **Average** | — | — | — | — | — | 7m 12s | — | — |

Cluster provisioning is not a meaningful part of these times: median 1026 ms across 100 clusters, about 0.28% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/account-resource-limits-bash-rhel10-9038) | — | — |
| application-log-rotation | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/application-log-rotation-bash-rhel10-9038) | — | — |
| custom-ca-trust | — | — | — | — | — | — | — | — |
| host-firewall-baseline | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/host-firewall-baseline-bash-rhel10-9038) | — | — |
| kernel-network-hardening | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/kernel-network-hardening-bash-rhel10-9038) | — | — |
| repair-application-permissions | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/repair-application-permissions-bash-rhel10-9038) | — | — |
| scheduled-maintenance | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/scheduled-maintenance-bash-rhel10-9038) | — | — |
| ssh-key-only | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/ssh-key-only-bash-rhel10-9038) | — | — |
| sticky-drop-directory | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/sticky-drop-directory-bash-rhel10-9038) | — | — |
| unprivileged-service | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/unprivileged-service-bash-rhel10-9038) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/mandatory-access-control-port-bash-rhel10-9038) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/kernel-module-blacklist-bash-rhel10-9038) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/boot-kernel-parameter-bash-rhel10-9038) | — | — |
| mount-option-hardening | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/mount-option-hardening-bash-rhel10-9038) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/password-complexity-policy-bash-rhel10-9038) | — | — |
| sudo-command-logging | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/sudo-command-logging-bash-rhel10-9038) | — | — |
| cron-access-control | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/cron-access-control-bash-rhel10-9038) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [0.980](../../../jobs/9038/2026-10-04__14-01-25/disk-quota-bash-rhel10-9038) | — | — |
| encrypted-volume | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/encrypted-volume-bash-rhel10-9038) | — | — |
| lvm-extend | — | — | — | — | — | [0.800](../../../jobs/9038/2026-10-04__14-01-25/lvm-extend-bash-rhel10-9038) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/filesystem-snapshot-rollback-bash-rhel10-9038) | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/package-version-hold-bash-rhel10-9038) | — | — |
| local-package-repository | — | — | — | — | — | [0.900](../../../jobs/9038/2026-10-04__14-01-25/local-package-repository-bash-rhel10-9038) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [0.980](../../../jobs/9038/2026-10-04__14-01-25/certificate-rotation-bash-rhel10-9038) | — | — |
| file-integrity-baseline | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/file-integrity-baseline-bash-rhel10-9038) | — | — |
| archive-member-safety | — | — | — | — | — | [0.900](../../../jobs/9038/2026-10-04__14-01-25/archive-member-safety-bash-rhel10-9038) | — | — |
| atomic-release-publication | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/atomic-release-publication-bash-rhel10-9038) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/batch-exclusive-lock-bash-rhel10-9038) | — | — |
| cgi-report-execution | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/cgi-report-execution-bash-rhel10-9038) | — | — |
| child-process-reaping | — | — | — | — | — | [0.960](../../../jobs/9038/2026-10-04__14-01-25/child-process-reaping-bash-rhel10-9038) | — | — |
| chroot-web-service | — | — | — | — | — | [0.780](../../../jobs/9038/2026-10-04__14-01-25/chroot-web-service-bash-rhel10-9038) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [0.960](../../../jobs/9038/2026-10-04__14-01-25/cross-file-accounting-reconciliation-bash-rhel10-9038) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/deleted-open-file-recovery-bash-rhel10-9038) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [0.910](../../../jobs/9038/2026-10-04__14-01-25/fifo-worker-reconnection-bash-rhel10-9038) | — | — |
| file-descriptor-leak | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/file-descriptor-leak-bash-rhel10-9038) | — | — |
| filename-encoding-migration | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/filename-encoding-migration-bash-rhel10-9038) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/fixed-width-import-recovery-bash-rhel10-9038) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/hardlink-aware-deduplication-bash-rhel10-9038) | — | — |
| incremental-archive-chain | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/incremental-archive-chain-bash-rhel10-9038) | — | — |
| inherited-directory-acls | — | — | — | — | — | [0.970](../../../jobs/9038/2026-10-04__14-01-25/inherited-directory-acls-bash-rhel10-9038) | — | — |
| inode-cache-retention | — | — | — | — | — | — | — | — |
| large-counter-overflow | — | — | — | — | — | [0.940](../../../jobs/9038/2026-10-04__14-01-25/large-counter-overflow-bash-rhel10-9038) | — | — |
| mail-filter-routing | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/mail-filter-routing-bash-rhel10-9038) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [0.990](../../../jobs/9038/2026-10-04__14-01-25/mail-spool-deduplication-bash-rhel10-9038) | — | — |
| minimal-environment-job | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/minimal-environment-job-bash-rhel10-9038) | — | — |
| name-based-web-tenants | — | — | — | — | — | [0.970](../../../jobs/9038/2026-10-04__14-01-25/name-based-web-tenants-bash-rhel10-9038) | — | — |
| numeric-record-ordering | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/numeric-record-ordering-bash-rhel10-9038) | — | — |
| permanent-url-migration | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/permanent-url-migration-bash-rhel10-9038) | — | — |
| persistent-swap | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/persistent-swap-bash-rhel10-9038) | — | — |
| posix-shell-installer | — | — | — | — | — | [0.980](../../../jobs/9038/2026-10-04__14-01-25/posix-shell-installer-bash-rhel10-9038) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/postgresql-sequence-repair-bash-rhel10-9038) | — | — |
| print-spool-recovery | — | — | — | — | — | [0.840](../../../jobs/9038/2026-10-04__14-01-25/print-spool-recovery-bash-rhel10-9038) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/privacy-safe-support-export-bash-rhel10-9038) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/relative-symlink-relocation-bash-rhel10-9038) | — | — |
| selective-tape-restore | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/selective-tape-restore-bash-rhel10-9038) | — | — |
| service-confinement | — | — | — | — | — | [0.820](../../../jobs/9038/2026-10-04__14-01-25/service-confinement-bash-rhel10-9038) | — | — |
| service-resource-limits | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/service-resource-limits-bash-rhel10-9038) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/signal-driven-config-reload-bash-rhel10-9038) | — | — |
| sparse-image-copy | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/sparse-image-copy-bash-rhel10-9038) | — | — |
| sqlite-lock-contention | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/sqlite-lock-contention-bash-rhel10-9038) | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/ssh-host-key-pinning-bash-rhel10-9038) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [0.980](../../../jobs/9038/2026-10-04__14-01-25/stale-pidfile-startup-bash-rhel10-9038) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/temporary-file-symlink-defense-bash-rhel10-9038) | — | — |
| text-export-normalization | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/text-export-normalization-bash-rhel10-9038) | — | — |
| timezone-log-merge | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/timezone-log-merge-bash-rhel10-9038) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/transactional-schema-upgrade-bash-rhel10-9038) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [0.970](../../../jobs/9038/2026-10-04__14-01-25/unix-socket-access-boundary-bash-rhel10-9038) | — | — |
| web-authentication-boundary | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/web-authentication-boundary-bash-rhel10-9038) | — | — |
| webdav-document-locks | — | — | — | — | — | [0.900](../../../jobs/9038/2026-10-04__14-01-25/webdav-document-locks-bash-rhel10-9038) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [0.960](../../../jobs/9038/2026-10-04__14-01-25/working-directory-independent-launch-bash-rhel10-9038) | — | — |
| **Average** | — | — | — | — | — | 0.978 | — | — |
