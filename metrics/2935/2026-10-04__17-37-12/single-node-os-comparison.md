# single-node-os-comparison: command execution summary

Scope: `2935/2026-10-04__17-37-12`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [11/0](../../../jobs/2935/2026-10-04__17-37-12/account-resource-limits-bash-rhel10-2935) | — | — |
| application-log-rotation | — | — | — | — | — | [16/0](../../../jobs/2935/2026-10-04__17-37-12/application-log-rotation-bash-rhel10-2935) | — | — |
| custom-ca-trust | — | — | — | — | — | [15/0](../../../jobs/2935/2026-10-04__17-37-12/custom-ca-trust-bash-rhel10-2935) | — | — |
| host-firewall-baseline | — | — | — | — | — | [15/2](../../../jobs/2935/2026-10-04__17-37-12/host-firewall-baseline-bash-rhel10-2935) | — | — |
| kernel-network-hardening | — | — | — | — | — | [13/0](../../../jobs/2935/2026-10-04__17-37-12/kernel-network-hardening-bash-rhel10-2935) | — | — |
| repair-application-permissions | — | — | — | — | — | [24/0](../../../jobs/2935/2026-10-04__17-37-12/repair-application-permissions-bash-rhel10-2935) | — | — |
| scheduled-maintenance | — | — | — | — | — | [18/0](../../../jobs/2935/2026-10-04__17-37-12/scheduled-maintenance-bash-rhel10-2935) | — | — |
| ssh-key-only | — | — | — | — | — | [17/0](../../../jobs/2935/2026-10-04__17-37-12/ssh-key-only-bash-rhel10-2935) | — | — |
| sticky-drop-directory | — | — | — | — | — | [13/0](../../../jobs/2935/2026-10-04__17-37-12/sticky-drop-directory-bash-rhel10-2935) | — | — |
| unprivileged-service | — | — | — | — | — | [14/0](../../../jobs/2935/2026-10-04__17-37-12/unprivileged-service-bash-rhel10-2935) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [17/0](../../../jobs/2935/2026-10-04__17-37-12/mandatory-access-control-port-bash-rhel10-2935) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [10/0](../../../jobs/2935/2026-10-04__17-37-12/kernel-module-blacklist-bash-rhel10-2935) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [12/0](../../../jobs/2935/2026-10-04__17-37-12/boot-kernel-parameter-bash-rhel10-2935) | — | — |
| mount-option-hardening | — | — | — | — | — | [21/2](../../../jobs/2935/2026-10-04__17-37-12/mount-option-hardening-bash-rhel10-2935) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [19/2](../../../jobs/2935/2026-10-04__17-37-12/password-complexity-policy-bash-rhel10-2935) | — | — |
| sudo-command-logging | — | — | — | — | — | [10/0](../../../jobs/2935/2026-10-04__17-37-12/sudo-command-logging-bash-rhel10-2935) | — | — |
| cron-access-control | — | — | — | — | — | [14/1](../../../jobs/2935/2026-10-04__17-37-12/cron-access-control-bash-rhel10-2935) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [20/2](../../../jobs/2935/2026-10-04__17-37-12/disk-quota-bash-rhel10-2935) | — | — |
| encrypted-volume | — | — | — | — | — | [29/1](../../../jobs/2935/2026-10-04__17-37-12/encrypted-volume-bash-rhel10-2935) | — | — |
| lvm-extend | — | — | — | — | — | [12/0](../../../jobs/2935/2026-10-04__17-37-12/lvm-extend-bash-rhel10-2935) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | [0/0](../../../jobs/2935/2026-10-04__17-37-12/filesystem-snapshot-rollback-bash-rhel10-2935) | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [12/2](../../../jobs/2935/2026-10-04__17-37-12/package-version-hold-bash-rhel10-2935) | — | — |
| local-package-repository | — | — | — | — | — | [21/1](../../../jobs/2935/2026-10-04__17-37-12/local-package-repository-bash-rhel10-2935) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [30/3](../../../jobs/2935/2026-10-04__17-37-12/certificate-rotation-bash-rhel10-2935) | — | — |
| file-integrity-baseline | — | — | — | — | — | [20/3](../../../jobs/2935/2026-10-04__17-37-12/file-integrity-baseline-bash-rhel10-2935) | — | — |
| archive-member-safety | — | — | — | — | — | [27/0](../../../jobs/2935/2026-10-04__17-37-12/archive-member-safety-bash-rhel10-2935) | — | — |
| atomic-release-publication | — | — | — | — | — | [18/0](../../../jobs/2935/2026-10-04__17-37-12/atomic-release-publication-bash-rhel10-2935) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [17/1](../../../jobs/2935/2026-10-04__17-37-12/batch-exclusive-lock-bash-rhel10-2935) | — | — |
| cgi-report-execution | — | — | — | — | — | [26/0](../../../jobs/2935/2026-10-04__17-37-12/cgi-report-execution-bash-rhel10-2935) | — | — |
| child-process-reaping | — | — | — | — | — | [16/0](../../../jobs/2935/2026-10-04__17-37-12/child-process-reaping-bash-rhel10-2935) | — | — |
| chroot-web-service | — | — | — | — | — | [22/3](../../../jobs/2935/2026-10-04__17-37-12/chroot-web-service-bash-rhel10-2935) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [13/0](../../../jobs/2935/2026-10-04__17-37-12/cross-file-accounting-reconciliation-bash-rhel10-2935) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [19/0](../../../jobs/2935/2026-10-04__17-37-12/deleted-open-file-recovery-bash-rhel10-2935) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [14/1](../../../jobs/2935/2026-10-04__17-37-12/fifo-worker-reconnection-bash-rhel10-2935) | — | — |
| file-descriptor-leak | — | — | — | — | — | [14/0](../../../jobs/2935/2026-10-04__17-37-12/file-descriptor-leak-bash-rhel10-2935) | — | — |
| filename-encoding-migration | — | — | — | — | — | [11/0](../../../jobs/2935/2026-10-04__17-37-12/filename-encoding-migration-bash-rhel10-2935) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [15/1](../../../jobs/2935/2026-10-04__17-37-12/fixed-width-import-recovery-bash-rhel10-2935) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [10/0](../../../jobs/2935/2026-10-04__17-37-12/hardlink-aware-deduplication-bash-rhel10-2935) | — | — |
| incremental-archive-chain | — | — | — | — | — | [13/1](../../../jobs/2935/2026-10-04__17-37-12/incremental-archive-chain-bash-rhel10-2935) | — | — |
| inherited-directory-acls | — | — | — | — | — | [21/1](../../../jobs/2935/2026-10-04__17-37-12/inherited-directory-acls-bash-rhel10-2935) | — | — |
| inode-cache-retention | — | — | — | — | — | [0/0](../../../jobs/2935/2026-10-04__17-37-12/inode-cache-retention-bash-rhel10-2935) | — | — |
| large-counter-overflow | — | — | — | — | — | [11/1](../../../jobs/2935/2026-10-04__17-37-12/large-counter-overflow-bash-rhel10-2935) | — | — |
| mail-filter-routing | — | — | — | — | — | [16/0](../../../jobs/2935/2026-10-04__17-37-12/mail-filter-routing-bash-rhel10-2935) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [17/1](../../../jobs/2935/2026-10-04__17-37-12/mail-spool-deduplication-bash-rhel10-2935) | — | — |
| minimal-environment-job | — | — | — | — | — | [12/0](../../../jobs/2935/2026-10-04__17-37-12/minimal-environment-job-bash-rhel10-2935) | — | — |
| name-based-web-tenants | — | — | — | — | — | [14/0](../../../jobs/2935/2026-10-04__17-37-12/name-based-web-tenants-bash-rhel10-2935) | — | — |
| numeric-record-ordering | — | — | — | — | — | [14/0](../../../jobs/2935/2026-10-04__17-37-12/numeric-record-ordering-bash-rhel10-2935) | — | — |
| permanent-url-migration | — | — | — | — | — | [25/1](../../../jobs/2935/2026-10-04__17-37-12/permanent-url-migration-bash-rhel10-2935) | — | — |
| persistent-swap | — | — | — | — | — | [14/2](../../../jobs/2935/2026-10-04__17-37-12/persistent-swap-bash-rhel10-2935) | — | — |
| posix-shell-installer | — | — | — | — | — | [14/0](../../../jobs/2935/2026-10-04__17-37-12/posix-shell-installer-bash-rhel10-2935) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [19/0](../../../jobs/2935/2026-10-04__17-37-12/postgresql-sequence-repair-bash-rhel10-2935) | — | — |
| print-spool-recovery | — | — | — | — | — | [23/4](../../../jobs/2935/2026-10-04__17-37-12/print-spool-recovery-bash-rhel10-2935) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [20/2](../../../jobs/2935/2026-10-04__17-37-12/privacy-safe-support-export-bash-rhel10-2935) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [16/1](../../../jobs/2935/2026-10-04__17-37-12/relative-symlink-relocation-bash-rhel10-2935) | — | — |
| selective-tape-restore | — | — | — | — | — | [13/0](../../../jobs/2935/2026-10-04__17-37-12/selective-tape-restore-bash-rhel10-2935) | — | — |
| service-confinement | — | — | — | — | — | [29/2](../../../jobs/2935/2026-10-04__17-37-12/service-confinement-bash-rhel10-2935) | — | — |
| service-resource-limits | — | — | — | — | — | [14/0](../../../jobs/2935/2026-10-04__17-37-12/service-resource-limits-bash-rhel10-2935) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [15/0](../../../jobs/2935/2026-10-04__17-37-12/signal-driven-config-reload-bash-rhel10-2935) | — | — |
| sparse-image-copy | — | — | — | — | — | [10/1](../../../jobs/2935/2026-10-04__17-37-12/sparse-image-copy-bash-rhel10-2935) | — | — |
| sqlite-lock-contention | — | — | — | — | — | [21/2](../../../jobs/2935/2026-10-04__17-37-12/sqlite-lock-contention-bash-rhel10-2935) | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [18/0](../../../jobs/2935/2026-10-04__17-37-12/ssh-host-key-pinning-bash-rhel10-2935) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [12/0](../../../jobs/2935/2026-10-04__17-37-12/stale-pidfile-startup-bash-rhel10-2935) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [14/1](../../../jobs/2935/2026-10-04__17-37-12/temporary-file-symlink-defense-bash-rhel10-2935) | — | — |
| text-export-normalization | — | — | — | — | — | [12/3](../../../jobs/2935/2026-10-04__17-37-12/text-export-normalization-bash-rhel10-2935) | — | — |
| timezone-log-merge | — | — | — | — | — | [18/2](../../../jobs/2935/2026-10-04__17-37-12/timezone-log-merge-bash-rhel10-2935) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [18/2](../../../jobs/2935/2026-10-04__17-37-12/transactional-schema-upgrade-bash-rhel10-2935) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [11/1](../../../jobs/2935/2026-10-04__17-37-12/unix-socket-access-boundary-bash-rhel10-2935) | — | — |
| web-authentication-boundary | — | — | — | — | — | [16/0](../../../jobs/2935/2026-10-04__17-37-12/web-authentication-boundary-bash-rhel10-2935) | — | — |
| webdav-document-locks | — | — | — | — | — | [22/1](../../../jobs/2935/2026-10-04__17-37-12/webdav-document-locks-bash-rhel10-2935) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [18/0](../../../jobs/2935/2026-10-04__17-37-12/working-directory-independent-launch-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 16.2/0.8 | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [3m 41s](../../../jobs/2935/2026-10-04__17-37-12/account-resource-limits-bash-rhel10-2935) | — | — |
| application-log-rotation | — | — | — | — | — | [5m 48s](../../../jobs/2935/2026-10-04__17-37-12/application-log-rotation-bash-rhel10-2935) | — | — |
| custom-ca-trust | — | — | — | — | — | [4m 58s](../../../jobs/2935/2026-10-04__17-37-12/custom-ca-trust-bash-rhel10-2935) | — | — |
| host-firewall-baseline | — | — | — | — | — | [6m 07s](../../../jobs/2935/2026-10-04__17-37-12/host-firewall-baseline-bash-rhel10-2935) | — | — |
| kernel-network-hardening | — | — | — | — | — | [3m 54s](../../../jobs/2935/2026-10-04__17-37-12/kernel-network-hardening-bash-rhel10-2935) | — | — |
| repair-application-permissions | — | — | — | — | — | [5m 03s](../../../jobs/2935/2026-10-04__17-37-12/repair-application-permissions-bash-rhel10-2935) | — | — |
| scheduled-maintenance | — | — | — | — | — | [3m 58s](../../../jobs/2935/2026-10-04__17-37-12/scheduled-maintenance-bash-rhel10-2935) | — | — |
| ssh-key-only | — | — | — | — | — | [4m 33s](../../../jobs/2935/2026-10-04__17-37-12/ssh-key-only-bash-rhel10-2935) | — | — |
| sticky-drop-directory | — | — | — | — | — | [3m 33s](../../../jobs/2935/2026-10-04__17-37-12/sticky-drop-directory-bash-rhel10-2935) | — | — |
| unprivileged-service | — | — | — | — | — | [5m 01s](../../../jobs/2935/2026-10-04__17-37-12/unprivileged-service-bash-rhel10-2935) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [4m 47s](../../../jobs/2935/2026-10-04__17-37-12/mandatory-access-control-port-bash-rhel10-2935) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [4m 06s](../../../jobs/2935/2026-10-04__17-37-12/kernel-module-blacklist-bash-rhel10-2935) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [3m 52s](../../../jobs/2935/2026-10-04__17-37-12/boot-kernel-parameter-bash-rhel10-2935) | — | — |
| mount-option-hardening | — | — | — | — | — | [7m 26s](../../../jobs/2935/2026-10-04__17-37-12/mount-option-hardening-bash-rhel10-2935) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [7m 09s](../../../jobs/2935/2026-10-04__17-37-12/password-complexity-policy-bash-rhel10-2935) | — | — |
| sudo-command-logging | — | — | — | — | — | [4m 46s](../../../jobs/2935/2026-10-04__17-37-12/sudo-command-logging-bash-rhel10-2935) | — | — |
| cron-access-control | — | — | — | — | — | [6m 39s](../../../jobs/2935/2026-10-04__17-37-12/cron-access-control-bash-rhel10-2935) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [7m 08s](../../../jobs/2935/2026-10-04__17-37-12/disk-quota-bash-rhel10-2935) | — | — |
| encrypted-volume | — | — | — | — | — | [6m 15s](../../../jobs/2935/2026-10-04__17-37-12/encrypted-volume-bash-rhel10-2935) | — | — |
| lvm-extend | — | — | — | — | — | [17m 19s](../../../jobs/2935/2026-10-04__17-37-12/lvm-extend-bash-rhel10-2935) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | [1m 19s](../../../jobs/2935/2026-10-04__17-37-12/filesystem-snapshot-rollback-bash-rhel10-2935) | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [4m 12s](../../../jobs/2935/2026-10-04__17-37-12/package-version-hold-bash-rhel10-2935) | — | — |
| local-package-repository | — | — | — | — | — | [7m 54s](../../../jobs/2935/2026-10-04__17-37-12/local-package-repository-bash-rhel10-2935) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [7m 59s](../../../jobs/2935/2026-10-04__17-37-12/certificate-rotation-bash-rhel10-2935) | — | — |
| file-integrity-baseline | — | — | — | — | — | [6m 15s](../../../jobs/2935/2026-10-04__17-37-12/file-integrity-baseline-bash-rhel10-2935) | — | — |
| archive-member-safety | — | — | — | — | — | [8m 33s](../../../jobs/2935/2026-10-04__17-37-12/archive-member-safety-bash-rhel10-2935) | — | — |
| atomic-release-publication | — | — | — | — | — | [6m 18s](../../../jobs/2935/2026-10-04__17-37-12/atomic-release-publication-bash-rhel10-2935) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [5m 10s](../../../jobs/2935/2026-10-04__17-37-12/batch-exclusive-lock-bash-rhel10-2935) | — | — |
| cgi-report-execution | — | — | — | — | — | [7m 58s](../../../jobs/2935/2026-10-04__17-37-12/cgi-report-execution-bash-rhel10-2935) | — | — |
| child-process-reaping | — | — | — | — | — | [5m 41s](../../../jobs/2935/2026-10-04__17-37-12/child-process-reaping-bash-rhel10-2935) | — | — |
| chroot-web-service | — | — | — | — | — | [7m 30s](../../../jobs/2935/2026-10-04__17-37-12/chroot-web-service-bash-rhel10-2935) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [4m 49s](../../../jobs/2935/2026-10-04__17-37-12/cross-file-accounting-reconciliation-bash-rhel10-2935) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [6m 17s](../../../jobs/2935/2026-10-04__17-37-12/deleted-open-file-recovery-bash-rhel10-2935) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [7m 03s](../../../jobs/2935/2026-10-04__17-37-12/fifo-worker-reconnection-bash-rhel10-2935) | — | — |
| file-descriptor-leak | — | — | — | — | — | [4m 53s](../../../jobs/2935/2026-10-04__17-37-12/file-descriptor-leak-bash-rhel10-2935) | — | — |
| filename-encoding-migration | — | — | — | — | — | [4m 58s](../../../jobs/2935/2026-10-04__17-37-12/filename-encoding-migration-bash-rhel10-2935) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [4m 54s](../../../jobs/2935/2026-10-04__17-37-12/fixed-width-import-recovery-bash-rhel10-2935) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [4m 28s](../../../jobs/2935/2026-10-04__17-37-12/hardlink-aware-deduplication-bash-rhel10-2935) | — | — |
| incremental-archive-chain | — | — | — | — | — | [3m 09s](../../../jobs/2935/2026-10-04__17-37-12/incremental-archive-chain-bash-rhel10-2935) | — | — |
| inherited-directory-acls | — | — | — | — | — | [7m 00s](../../../jobs/2935/2026-10-04__17-37-12/inherited-directory-acls-bash-rhel10-2935) | — | — |
| inode-cache-retention | — | — | — | — | — | [48s](../../../jobs/2935/2026-10-04__17-37-12/inode-cache-retention-bash-rhel10-2935) | — | — |
| large-counter-overflow | — | — | — | — | — | [4m 58s](../../../jobs/2935/2026-10-04__17-37-12/large-counter-overflow-bash-rhel10-2935) | — | — |
| mail-filter-routing | — | — | — | — | — | [5m 56s](../../../jobs/2935/2026-10-04__17-37-12/mail-filter-routing-bash-rhel10-2935) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [7m 33s](../../../jobs/2935/2026-10-04__17-37-12/mail-spool-deduplication-bash-rhel10-2935) | — | — |
| minimal-environment-job | — | — | — | — | — | [4m 11s](../../../jobs/2935/2026-10-04__17-37-12/minimal-environment-job-bash-rhel10-2935) | — | — |
| name-based-web-tenants | — | — | — | — | — | [5m 36s](../../../jobs/2935/2026-10-04__17-37-12/name-based-web-tenants-bash-rhel10-2935) | — | — |
| numeric-record-ordering | — | — | — | — | — | [4m 38s](../../../jobs/2935/2026-10-04__17-37-12/numeric-record-ordering-bash-rhel10-2935) | — | — |
| permanent-url-migration | — | — | — | — | — | [6m 20s](../../../jobs/2935/2026-10-04__17-37-12/permanent-url-migration-bash-rhel10-2935) | — | — |
| persistent-swap | — | — | — | — | — | [4m 25s](../../../jobs/2935/2026-10-04__17-37-12/persistent-swap-bash-rhel10-2935) | — | — |
| posix-shell-installer | — | — | — | — | — | [5m 13s](../../../jobs/2935/2026-10-04__17-37-12/posix-shell-installer-bash-rhel10-2935) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [4m 33s](../../../jobs/2935/2026-10-04__17-37-12/postgresql-sequence-repair-bash-rhel10-2935) | — | — |
| print-spool-recovery | — | — | — | — | — | [7m 46s](../../../jobs/2935/2026-10-04__17-37-12/print-spool-recovery-bash-rhel10-2935) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [9m 04s](../../../jobs/2935/2026-10-04__17-37-12/privacy-safe-support-export-bash-rhel10-2935) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [4m 34s](../../../jobs/2935/2026-10-04__17-37-12/relative-symlink-relocation-bash-rhel10-2935) | — | — |
| selective-tape-restore | — | — | — | — | — | [3m 03s](../../../jobs/2935/2026-10-04__17-37-12/selective-tape-restore-bash-rhel10-2935) | — | — |
| service-confinement | — | — | — | — | — | [12m 15s](../../../jobs/2935/2026-10-04__17-37-12/service-confinement-bash-rhel10-2935) | — | — |
| service-resource-limits | — | — | — | — | — | [4m 57s](../../../jobs/2935/2026-10-04__17-37-12/service-resource-limits-bash-rhel10-2935) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [6m 21s](../../../jobs/2935/2026-10-04__17-37-12/signal-driven-config-reload-bash-rhel10-2935) | — | — |
| sparse-image-copy | — | — | — | — | — | [4m 09s](../../../jobs/2935/2026-10-04__17-37-12/sparse-image-copy-bash-rhel10-2935) | — | — |
| sqlite-lock-contention | — | — | — | — | — | [19m 06s](../../../jobs/2935/2026-10-04__17-37-12/sqlite-lock-contention-bash-rhel10-2935) | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [6m 13s](../../../jobs/2935/2026-10-04__17-37-12/ssh-host-key-pinning-bash-rhel10-2935) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [6m 35s](../../../jobs/2935/2026-10-04__17-37-12/stale-pidfile-startup-bash-rhel10-2935) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [4m 43s](../../../jobs/2935/2026-10-04__17-37-12/temporary-file-symlink-defense-bash-rhel10-2935) | — | — |
| text-export-normalization | — | — | — | — | — | [4m 41s](../../../jobs/2935/2026-10-04__17-37-12/text-export-normalization-bash-rhel10-2935) | — | — |
| timezone-log-merge | — | — | — | — | — | [6m 00s](../../../jobs/2935/2026-10-04__17-37-12/timezone-log-merge-bash-rhel10-2935) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [4m 57s](../../../jobs/2935/2026-10-04__17-37-12/transactional-schema-upgrade-bash-rhel10-2935) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [5m 38s](../../../jobs/2935/2026-10-04__17-37-12/unix-socket-access-boundary-bash-rhel10-2935) | — | — |
| web-authentication-boundary | — | — | — | — | — | [7m 16s](../../../jobs/2935/2026-10-04__17-37-12/web-authentication-boundary-bash-rhel10-2935) | — | — |
| webdav-document-locks | — | — | — | — | — | [7m 53s](../../../jobs/2935/2026-10-04__17-37-12/webdav-document-locks-bash-rhel10-2935) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [5m 11s](../../../jobs/2935/2026-10-04__17-37-12/working-directory-independent-launch-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 5m 57s | — | — |

Cluster provisioning is not a meaningful part of these times: median 805 ms across 100 clusters, about 0.22% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/account-resource-limits-bash-rhel10-2935) | — | — |
| application-log-rotation | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/application-log-rotation-bash-rhel10-2935) | — | — |
| custom-ca-trust | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/custom-ca-trust-bash-rhel10-2935) | — | — |
| host-firewall-baseline | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/host-firewall-baseline-bash-rhel10-2935) | — | — |
| kernel-network-hardening | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/kernel-network-hardening-bash-rhel10-2935) | — | — |
| repair-application-permissions | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/repair-application-permissions-bash-rhel10-2935) | — | — |
| scheduled-maintenance | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/scheduled-maintenance-bash-rhel10-2935) | — | — |
| ssh-key-only | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/ssh-key-only-bash-rhel10-2935) | — | — |
| sticky-drop-directory | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/sticky-drop-directory-bash-rhel10-2935) | — | — |
| unprivileged-service | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/unprivileged-service-bash-rhel10-2935) | — | — |
| mandatory-access-control-port | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/mandatory-access-control-port-bash-rhel10-2935) | — | — |
| kernel-module-blacklist | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/kernel-module-blacklist-bash-rhel10-2935) | — | — |
| boot-kernel-parameter | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/boot-kernel-parameter-bash-rhel10-2935) | — | — |
| mount-option-hardening | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/mount-option-hardening-bash-rhel10-2935) | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/password-complexity-policy-bash-rhel10-2935) | — | — |
| sudo-command-logging | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/sudo-command-logging-bash-rhel10-2935) | — | — |
| cron-access-control | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/cron-access-control-bash-rhel10-2935) | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | [0.930](../../../jobs/2935/2026-10-04__17-37-12/disk-quota-bash-rhel10-2935) | — | — |
| encrypted-volume | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/encrypted-volume-bash-rhel10-2935) | — | — |
| lvm-extend | — | — | — | — | — | [0.940](../../../jobs/2935/2026-10-04__17-37-12/lvm-extend-bash-rhel10-2935) | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/package-version-hold-bash-rhel10-2935) | — | — |
| local-package-repository | — | — | — | — | — | [0.970](../../../jobs/2935/2026-10-04__17-37-12/local-package-repository-bash-rhel10-2935) | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/certificate-rotation-bash-rhel10-2935) | — | — |
| file-integrity-baseline | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/file-integrity-baseline-bash-rhel10-2935) | — | — |
| archive-member-safety | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/archive-member-safety-bash-rhel10-2935) | — | — |
| atomic-release-publication | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/atomic-release-publication-bash-rhel10-2935) | — | — |
| batch-exclusive-lock | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__17-37-12/batch-exclusive-lock-bash-rhel10-2935) | — | — |
| cgi-report-execution | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__17-37-12/cgi-report-execution-bash-rhel10-2935) | — | — |
| child-process-reaping | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/child-process-reaping-bash-rhel10-2935) | — | — |
| chroot-web-service | — | — | — | — | — | [0.940](../../../jobs/2935/2026-10-04__17-37-12/chroot-web-service-bash-rhel10-2935) | — | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | [0.960](../../../jobs/2935/2026-10-04__17-37-12/cross-file-accounting-reconciliation-bash-rhel10-2935) | — | — |
| deleted-open-file-recovery | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/deleted-open-file-recovery-bash-rhel10-2935) | — | — |
| fifo-worker-reconnection | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/fifo-worker-reconnection-bash-rhel10-2935) | — | — |
| file-descriptor-leak | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/file-descriptor-leak-bash-rhel10-2935) | — | — |
| filename-encoding-migration | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/filename-encoding-migration-bash-rhel10-2935) | — | — |
| fixed-width-import-recovery | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/fixed-width-import-recovery-bash-rhel10-2935) | — | — |
| hardlink-aware-deduplication | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/hardlink-aware-deduplication-bash-rhel10-2935) | — | — |
| incremental-archive-chain | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/incremental-archive-chain-bash-rhel10-2935) | — | — |
| inherited-directory-acls | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/inherited-directory-acls-bash-rhel10-2935) | — | — |
| inode-cache-retention | — | — | — | — | — | — | — | — |
| large-counter-overflow | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/large-counter-overflow-bash-rhel10-2935) | — | — |
| mail-filter-routing | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/mail-filter-routing-bash-rhel10-2935) | — | — |
| mail-spool-deduplication | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/mail-spool-deduplication-bash-rhel10-2935) | — | — |
| minimal-environment-job | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/minimal-environment-job-bash-rhel10-2935) | — | — |
| name-based-web-tenants | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/name-based-web-tenants-bash-rhel10-2935) | — | — |
| numeric-record-ordering | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/numeric-record-ordering-bash-rhel10-2935) | — | — |
| permanent-url-migration | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/permanent-url-migration-bash-rhel10-2935) | — | — |
| persistent-swap | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/persistent-swap-bash-rhel10-2935) | — | — |
| posix-shell-installer | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/posix-shell-installer-bash-rhel10-2935) | — | — |
| postgresql-sequence-repair | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/postgresql-sequence-repair-bash-rhel10-2935) | — | — |
| print-spool-recovery | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/print-spool-recovery-bash-rhel10-2935) | — | — |
| privacy-safe-support-export | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/privacy-safe-support-export-bash-rhel10-2935) | — | — |
| relative-symlink-relocation | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/relative-symlink-relocation-bash-rhel10-2935) | — | — |
| selective-tape-restore | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/selective-tape-restore-bash-rhel10-2935) | — | — |
| service-confinement | — | — | — | — | — | [0.970](../../../jobs/2935/2026-10-04__17-37-12/service-confinement-bash-rhel10-2935) | — | — |
| service-resource-limits | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/service-resource-limits-bash-rhel10-2935) | — | — |
| signal-driven-config-reload | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/signal-driven-config-reload-bash-rhel10-2935) | — | — |
| sparse-image-copy | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/sparse-image-copy-bash-rhel10-2935) | — | — |
| sqlite-lock-contention | — | — | — | — | — | — | — | — |
| ssh-host-key-pinning | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/ssh-host-key-pinning-bash-rhel10-2935) | — | — |
| stale-pidfile-startup | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/stale-pidfile-startup-bash-rhel10-2935) | — | — |
| temporary-file-symlink-defense | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/temporary-file-symlink-defense-bash-rhel10-2935) | — | — |
| text-export-normalization | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/text-export-normalization-bash-rhel10-2935) | — | — |
| timezone-log-merge | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/timezone-log-merge-bash-rhel10-2935) | — | — |
| transactional-schema-upgrade | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/transactional-schema-upgrade-bash-rhel10-2935) | — | — |
| unix-socket-access-boundary | — | — | — | — | — | [0.940](../../../jobs/2935/2026-10-04__17-37-12/unix-socket-access-boundary-bash-rhel10-2935) | — | — |
| web-authentication-boundary | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/web-authentication-boundary-bash-rhel10-2935) | — | — |
| webdav-document-locks | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/webdav-document-locks-bash-rhel10-2935) | — | — |
| working-directory-independent-launch | — | — | — | — | — | [0.820](../../../jobs/2935/2026-10-04__17-37-12/working-directory-independent-launch-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 0.991 | — | — |
