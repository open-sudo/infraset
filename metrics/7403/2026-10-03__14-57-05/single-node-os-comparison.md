# single-node-os-comparison: command execution summary

Scope: `7403/2026-10-03__14-57-05`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | [8/0](../../../jobs/7403/2026-10-03__14-57-05/account-resource-limits-bash-ubuntu24-7403) |
| application-log-rotation | — | — | — | — | — | — | — | [8/0](../../../jobs/7403/2026-10-03__14-57-05/application-log-rotation-bash-ubuntu24-7403) |
| custom-ca-trust | — | — | — | — | — | — | — | [8/0](../../../jobs/7403/2026-10-03__14-57-05/custom-ca-trust-bash-ubuntu24-7403) |
| host-firewall-baseline | — | — | — | — | — | — | — | [16/3](../../../jobs/7403/2026-10-03__14-57-05/host-firewall-baseline-bash-ubuntu24-7403) |
| kernel-network-hardening | — | — | — | — | — | — | — | [7/0](../../../jobs/7403/2026-10-03__14-57-05/kernel-network-hardening-bash-ubuntu24-7403) |
| repair-application-permissions | — | — | — | — | — | — | — | [7/0](../../../jobs/7403/2026-10-03__14-57-05/repair-application-permissions-bash-ubuntu24-7403) |
| scheduled-maintenance | — | — | — | — | — | — | — | [7/1](../../../jobs/7403/2026-10-03__14-57-05/scheduled-maintenance-bash-ubuntu24-7403) |
| ssh-key-only | — | — | — | — | — | — | — | [13/0](../../../jobs/7403/2026-10-03__14-57-05/ssh-key-only-bash-ubuntu24-7403) |
| sticky-drop-directory | — | — | — | — | — | — | — | [9/0](../../../jobs/7403/2026-10-03__14-57-05/sticky-drop-directory-bash-ubuntu24-7403) |
| unprivileged-service | — | — | — | — | — | — | — | [9/0](../../../jobs/7403/2026-10-03__14-57-05/unprivileged-service-bash-ubuntu24-7403) |
| mandatory-access-control-port | — | — | — | — | — | — | — | [16/0](../../../jobs/7403/2026-10-03__14-57-05/mandatory-access-control-port-bash-ubuntu24-7403) |
| kernel-module-blacklist | — | — | — | — | — | — | — | [10/0](../../../jobs/7403/2026-10-03__14-57-05/kernel-module-blacklist-bash-ubuntu24-7403) |
| boot-kernel-parameter | — | — | — | — | — | — | — | [9/0](../../../jobs/7403/2026-10-03__14-57-05/boot-kernel-parameter-bash-ubuntu24-7403) |
| mount-option-hardening | — | — | — | — | — | — | — | [14/0](../../../jobs/7403/2026-10-03__14-57-05/mount-option-hardening-bash-ubuntu24-7403) |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | [12/0](../../../jobs/7403/2026-10-03__14-57-05/password-complexity-policy-bash-ubuntu24-7403) |
| sudo-command-logging | — | — | — | — | — | — | — | [9/0](../../../jobs/7403/2026-10-03__14-57-05/sudo-command-logging-bash-ubuntu24-7403) |
| cron-access-control | — | — | — | — | — | — | — | [7/0](../../../jobs/7403/2026-10-03__14-57-05/cron-access-control-bash-ubuntu24-7403) |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | [20/4](../../../jobs/7403/2026-10-03__14-57-05/disk-quota-bash-ubuntu24-7403) |
| encrypted-volume | — | — | — | — | — | — | — | [11/1](../../../jobs/7403/2026-10-03__14-57-05/encrypted-volume-bash-ubuntu24-7403) |
| lvm-extend | — | — | — | — | — | — | — | [29/2](../../../jobs/7403/2026-10-03__14-57-05/lvm-extend-bash-ubuntu24-7403) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | [13/1](../../../jobs/7403/2026-10-03__14-57-05/filesystem-snapshot-rollback-bash-ubuntu24-7403) |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | [11/0](../../../jobs/7403/2026-10-03__14-57-05/package-version-hold-bash-ubuntu24-7403) |
| local-package-repository | — | — | — | — | — | — | — | [12/1](../../../jobs/7403/2026-10-03__14-57-05/local-package-repository-bash-ubuntu24-7403) |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | [17/0](../../../jobs/7403/2026-10-03__14-57-05/certificate-rotation-bash-ubuntu24-7403) |
| file-integrity-baseline | — | — | — | — | — | — | — | [29/0](../../../jobs/7403/2026-10-03__14-57-05/file-integrity-baseline-bash-ubuntu24-7403) |
| archive-member-safety | — | — | — | — | — | — | — | [9/1](../../../jobs/7403/2026-10-03__14-57-05/archive-member-safety-bash-ubuntu24-7403) |
| atomic-release-publication | — | — | — | — | — | — | — | [11/2](../../../jobs/7403/2026-10-03__14-57-05/atomic-release-publication-bash-ubuntu24-7403) |
| batch-exclusive-lock | — | — | — | — | — | — | — | [9/0](../../../jobs/7403/2026-10-03__14-57-05/batch-exclusive-lock-bash-ubuntu24-7403) |
| cgi-report-execution | — | — | — | — | — | — | — | [14/0](../../../jobs/7403/2026-10-03__14-57-05/cgi-report-execution-bash-ubuntu24-7403) |
| child-process-reaping | — | — | — | — | — | — | — | [10/0](../../../jobs/7403/2026-10-03__14-57-05/child-process-reaping-bash-ubuntu24-7403) |
| chroot-web-service | — | — | — | — | — | — | — | [10/1](../../../jobs/7403/2026-10-03__14-57-05/chroot-web-service-bash-ubuntu24-7403) |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | — | [10/0](../../../jobs/7403/2026-10-03__14-57-05/cross-file-accounting-reconciliation-bash-ubuntu24-7403) |
| deleted-open-file-recovery | — | — | — | — | — | — | — | [10/2](../../../jobs/7403/2026-10-03__14-57-05/deleted-open-file-recovery-bash-ubuntu24-7403) |
| fifo-worker-reconnection | — | — | — | — | — | — | — | [15/1](../../../jobs/7403/2026-10-03__14-57-05/fifo-worker-reconnection-bash-ubuntu24-7403) |
| file-descriptor-leak | — | — | — | — | — | — | — | [12/0](../../../jobs/7403/2026-10-03__14-57-05/file-descriptor-leak-bash-ubuntu24-7403) |
| filename-encoding-migration | — | — | — | — | — | — | — | [7/0](../../../jobs/7403/2026-10-03__14-57-05/filename-encoding-migration-bash-ubuntu24-7403) |
| fixed-width-import-recovery | — | — | — | — | — | — | — | [11/0](../../../jobs/7403/2026-10-03__14-57-05/fixed-width-import-recovery-bash-ubuntu24-7403) |
| hardlink-aware-deduplication | — | — | — | — | — | — | — | [12/0](../../../jobs/7403/2026-10-03__14-57-05/hardlink-aware-deduplication-bash-ubuntu24-7403) |
| incremental-archive-chain | — | — | — | — | — | — | — | [7/0](../../../jobs/7403/2026-10-03__14-57-05/incremental-archive-chain-bash-ubuntu24-7403) |
| inherited-directory-acls | — | — | — | — | — | — | — | [12/1](../../../jobs/7403/2026-10-03__14-57-05/inherited-directory-acls-bash-ubuntu24-7403) |
| inode-cache-retention | — | — | — | — | — | — | — | [0/0](../../../jobs/7403/2026-10-03__14-57-05/inode-cache-retention-bash-ubuntu24-7403) |
| large-counter-overflow | — | — | — | — | — | — | — | [10/0](../../../jobs/7403/2026-10-03__14-57-05/large-counter-overflow-bash-ubuntu24-7403) |
| mail-filter-routing | — | — | — | — | — | — | — | [10/0](../../../jobs/7403/2026-10-03__14-57-05/mail-filter-routing-bash-ubuntu24-7403) |
| mail-spool-deduplication | — | — | — | — | — | — | — | [11/0](../../../jobs/7403/2026-10-03__14-57-05/mail-spool-deduplication-bash-ubuntu24-7403) |
| minimal-environment-job | — | — | — | — | — | — | — | [7/0](../../../jobs/7403/2026-10-03__14-57-05/minimal-environment-job-bash-ubuntu24-7403) |
| name-based-web-tenants | — | — | — | — | — | — | — | [11/0](../../../jobs/7403/2026-10-03__14-57-05/name-based-web-tenants-bash-ubuntu24-7403) |
| numeric-record-ordering | — | — | — | — | — | — | — | [13/0](../../../jobs/7403/2026-10-03__14-57-05/numeric-record-ordering-bash-ubuntu24-7403) |
| permanent-url-migration | — | — | — | — | — | — | — | [12/0](../../../jobs/7403/2026-10-03__14-57-05/permanent-url-migration-bash-ubuntu24-7403) |
| persistent-swap | — | — | — | — | — | — | — | [11/0](../../../jobs/7403/2026-10-03__14-57-05/persistent-swap-bash-ubuntu24-7403) |
| posix-shell-installer | — | — | — | — | — | — | — | [11/0](../../../jobs/7403/2026-10-03__14-57-05/posix-shell-installer-bash-ubuntu24-7403) |
| postgresql-sequence-repair | — | — | — | — | — | — | — | [19/0](../../../jobs/7403/2026-10-03__14-57-05/postgresql-sequence-repair-bash-ubuntu24-7403) |
| print-spool-recovery | — | — | — | — | — | — | — | [21/1](../../../jobs/7403/2026-10-03__14-57-05/print-spool-recovery-bash-ubuntu24-7403) |
| privacy-safe-support-export | — | — | — | — | — | — | — | [10/2](../../../jobs/7403/2026-10-03__14-57-05/privacy-safe-support-export-bash-ubuntu24-7403) |
| relative-symlink-relocation | — | — | — | — | — | — | — | [11/1](../../../jobs/7403/2026-10-03__14-57-05/relative-symlink-relocation-bash-ubuntu24-7403) |
| selective-tape-restore | — | — | — | — | — | — | — | [9/0](../../../jobs/7403/2026-10-03__14-57-05/selective-tape-restore-bash-ubuntu24-7403) |
| service-confinement | — | — | — | — | — | — | — | [17/5](../../../jobs/7403/2026-10-03__14-57-05/service-confinement-bash-ubuntu24-7403) |
| service-resource-limits | — | — | — | — | — | — | — | [12/1](../../../jobs/7403/2026-10-03__14-57-05/service-resource-limits-bash-ubuntu24-7403) |
| signal-driven-config-reload | — | — | — | — | — | — | — | [17/0](../../../jobs/7403/2026-10-03__14-57-05/signal-driven-config-reload-bash-ubuntu24-7403) |
| sparse-image-copy | — | — | — | — | — | — | — | [11/1](../../../jobs/7403/2026-10-03__14-57-05/sparse-image-copy-bash-ubuntu24-7403) |
| sqlite-lock-contention | — | — | — | — | — | — | — | [21/2](../../../jobs/7403/2026-10-03__14-57-05/sqlite-lock-contention-bash-ubuntu24-7403) |
| ssh-host-key-pinning | — | — | — | — | — | — | — | [14/1](../../../jobs/7403/2026-10-03__14-57-05/ssh-host-key-pinning-bash-ubuntu24-7403) |
| stale-pidfile-startup | — | — | — | — | — | — | — | [17/0](../../../jobs/7403/2026-10-03__14-57-05/stale-pidfile-startup-bash-ubuntu24-7403) |
| temporary-file-symlink-defense | — | — | — | — | — | — | — | [8/1](../../../jobs/7403/2026-10-03__14-57-05/temporary-file-symlink-defense-bash-ubuntu24-7403) |
| text-export-normalization | — | — | — | — | — | — | — | [7/1](../../../jobs/7403/2026-10-03__14-57-05/text-export-normalization-bash-ubuntu24-7403) |
| timezone-log-merge | — | — | — | — | — | — | — | [8/0](../../../jobs/7403/2026-10-03__14-57-05/timezone-log-merge-bash-ubuntu24-7403) |
| transactional-schema-upgrade | — | — | — | — | — | — | — | [9/0](../../../jobs/7403/2026-10-03__14-57-05/transactional-schema-upgrade-bash-ubuntu24-7403) |
| unix-socket-access-boundary | — | — | — | — | — | — | — | [13/1](../../../jobs/7403/2026-10-03__14-57-05/unix-socket-access-boundary-bash-ubuntu24-7403) |
| web-authentication-boundary | — | — | — | — | — | — | — | [10/0](../../../jobs/7403/2026-10-03__14-57-05/web-authentication-boundary-bash-ubuntu24-7403) |
| webdav-document-locks | — | — | — | — | — | — | — | [11/0](../../../jobs/7403/2026-10-03__14-57-05/webdav-document-locks-bash-ubuntu24-7403) |
| working-directory-independent-launch | — | — | — | — | — | — | — | [11/0](../../../jobs/7403/2026-10-03__14-57-05/working-directory-independent-launch-bash-ubuntu24-7403) |
| **Average** | — | — | — | — | — | — | — | 11.7/0.5 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | [1m 56s](../../../jobs/7403/2026-10-03__14-57-05/account-resource-limits-bash-ubuntu24-7403) |
| application-log-rotation | — | — | — | — | — | — | — | [27m 44s](../../../jobs/7403/2026-10-03__14-57-05/application-log-rotation-bash-ubuntu24-7403) |
| custom-ca-trust | — | — | — | — | — | — | — | [2m 00s](../../../jobs/7403/2026-10-03__14-57-05/custom-ca-trust-bash-ubuntu24-7403) |
| host-firewall-baseline | — | — | — | — | — | — | — | [4m 10s](../../../jobs/7403/2026-10-03__14-57-05/host-firewall-baseline-bash-ubuntu24-7403) |
| kernel-network-hardening | — | — | — | — | — | — | — | [1m 52s](../../../jobs/7403/2026-10-03__14-57-05/kernel-network-hardening-bash-ubuntu24-7403) |
| repair-application-permissions | — | — | — | — | — | — | — | [1m 57s](../../../jobs/7403/2026-10-03__14-57-05/repair-application-permissions-bash-ubuntu24-7403) |
| scheduled-maintenance | — | — | — | — | — | — | — | [2m 02s](../../../jobs/7403/2026-10-03__14-57-05/scheduled-maintenance-bash-ubuntu24-7403) |
| ssh-key-only | — | — | — | — | — | — | — | [2m 48s](../../../jobs/7403/2026-10-03__14-57-05/ssh-key-only-bash-ubuntu24-7403) |
| sticky-drop-directory | — | — | — | — | — | — | — | [2m 09s](../../../jobs/7403/2026-10-03__14-57-05/sticky-drop-directory-bash-ubuntu24-7403) |
| unprivileged-service | — | — | — | — | — | — | — | [1m 54s](../../../jobs/7403/2026-10-03__14-57-05/unprivileged-service-bash-ubuntu24-7403) |
| mandatory-access-control-port | — | — | — | — | — | — | — | [2m 32s](../../../jobs/7403/2026-10-03__14-57-05/mandatory-access-control-port-bash-ubuntu24-7403) |
| kernel-module-blacklist | — | — | — | — | — | — | — | [27m 32s](../../../jobs/7403/2026-10-03__14-57-05/kernel-module-blacklist-bash-ubuntu24-7403) |
| boot-kernel-parameter | — | — | — | — | — | — | — | [1m 44s](../../../jobs/7403/2026-10-03__14-57-05/boot-kernel-parameter-bash-ubuntu24-7403) |
| mount-option-hardening | — | — | — | — | — | — | — | [2m 31s](../../../jobs/7403/2026-10-03__14-57-05/mount-option-hardening-bash-ubuntu24-7403) |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | [2m 35s](../../../jobs/7403/2026-10-03__14-57-05/password-complexity-policy-bash-ubuntu24-7403) |
| sudo-command-logging | — | — | — | — | — | — | — | [1m 57s](../../../jobs/7403/2026-10-03__14-57-05/sudo-command-logging-bash-ubuntu24-7403) |
| cron-access-control | — | — | — | — | — | — | — | [2m 17s](../../../jobs/7403/2026-10-03__14-57-05/cron-access-control-bash-ubuntu24-7403) |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | [4m 20s](../../../jobs/7403/2026-10-03__14-57-05/disk-quota-bash-ubuntu24-7403) |
| encrypted-volume | — | — | — | — | — | — | — | [2m 34s](../../../jobs/7403/2026-10-03__14-57-05/encrypted-volume-bash-ubuntu24-7403) |
| lvm-extend | — | — | — | — | — | — | — | [4m 26s](../../../jobs/7403/2026-10-03__14-57-05/lvm-extend-bash-ubuntu24-7403) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | [2m 44s](../../../jobs/7403/2026-10-03__14-57-05/filesystem-snapshot-rollback-bash-ubuntu24-7403) |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | [2m 08s](../../../jobs/7403/2026-10-03__14-57-05/package-version-hold-bash-ubuntu24-7403) |
| local-package-repository | — | — | — | — | — | — | — | [2m 57s](../../../jobs/7403/2026-10-03__14-57-05/local-package-repository-bash-ubuntu24-7403) |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | [3m 27s](../../../jobs/7403/2026-10-03__14-57-05/certificate-rotation-bash-ubuntu24-7403) |
| file-integrity-baseline | — | — | — | — | — | — | — | [3m 59s](../../../jobs/7403/2026-10-03__14-57-05/file-integrity-baseline-bash-ubuntu24-7403) |
| archive-member-safety | — | — | — | — | — | — | — | [2m 57s](../../../jobs/7403/2026-10-03__14-57-05/archive-member-safety-bash-ubuntu24-7403) |
| atomic-release-publication | — | — | — | — | — | — | — | [3m 55s](../../../jobs/7403/2026-10-03__14-57-05/atomic-release-publication-bash-ubuntu24-7403) |
| batch-exclusive-lock | — | — | — | — | — | — | — | [2m 34s](../../../jobs/7403/2026-10-03__14-57-05/batch-exclusive-lock-bash-ubuntu24-7403) |
| cgi-report-execution | — | — | — | — | — | — | — | [2m 34s](../../../jobs/7403/2026-10-03__14-57-05/cgi-report-execution-bash-ubuntu24-7403) |
| child-process-reaping | — | — | — | — | — | — | — | [2m 35s](../../../jobs/7403/2026-10-03__14-57-05/child-process-reaping-bash-ubuntu24-7403) |
| chroot-web-service | — | — | — | — | — | — | — | [3m 00s](../../../jobs/7403/2026-10-03__14-57-05/chroot-web-service-bash-ubuntu24-7403) |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | — | [2m 21s](../../../jobs/7403/2026-10-03__14-57-05/cross-file-accounting-reconciliation-bash-ubuntu24-7403) |
| deleted-open-file-recovery | — | — | — | — | — | — | — | [3m 13s](../../../jobs/7403/2026-10-03__14-57-05/deleted-open-file-recovery-bash-ubuntu24-7403) |
| fifo-worker-reconnection | — | — | — | — | — | — | — | [5m 52s](../../../jobs/7403/2026-10-03__14-57-05/fifo-worker-reconnection-bash-ubuntu24-7403) |
| file-descriptor-leak | — | — | — | — | — | — | — | [2m 47s](../../../jobs/7403/2026-10-03__14-57-05/file-descriptor-leak-bash-ubuntu24-7403) |
| filename-encoding-migration | — | — | — | — | — | — | — | [2m 27s](../../../jobs/7403/2026-10-03__14-57-05/filename-encoding-migration-bash-ubuntu24-7403) |
| fixed-width-import-recovery | — | — | — | — | — | — | — | [2m 52s](../../../jobs/7403/2026-10-03__14-57-05/fixed-width-import-recovery-bash-ubuntu24-7403) |
| hardlink-aware-deduplication | — | — | — | — | — | — | — | [1m 59s](../../../jobs/7403/2026-10-03__14-57-05/hardlink-aware-deduplication-bash-ubuntu24-7403) |
| incremental-archive-chain | — | — | — | — | — | — | — | [28m 13s](../../../jobs/7403/2026-10-03__14-57-05/incremental-archive-chain-bash-ubuntu24-7403) |
| inherited-directory-acls | — | — | — | — | — | — | — | [3m 03s](../../../jobs/7403/2026-10-03__14-57-05/inherited-directory-acls-bash-ubuntu24-7403) |
| inode-cache-retention | — | — | — | — | — | — | — | [4s](../../../jobs/7403/2026-10-03__14-57-05/inode-cache-retention-bash-ubuntu24-7403) |
| large-counter-overflow | — | — | — | — | — | — | — | [3m 17s](../../../jobs/7403/2026-10-03__14-57-05/large-counter-overflow-bash-ubuntu24-7403) |
| mail-filter-routing | — | — | — | — | — | — | — | [2m 31s](../../../jobs/7403/2026-10-03__14-57-05/mail-filter-routing-bash-ubuntu24-7403) |
| mail-spool-deduplication | — | — | — | — | — | — | — | [3m 21s](../../../jobs/7403/2026-10-03__14-57-05/mail-spool-deduplication-bash-ubuntu24-7403) |
| minimal-environment-job | — | — | — | — | — | — | — | [2m 35s](../../../jobs/7403/2026-10-03__14-57-05/minimal-environment-job-bash-ubuntu24-7403) |
| name-based-web-tenants | — | — | — | — | — | — | — | [3m 02s](../../../jobs/7403/2026-10-03__14-57-05/name-based-web-tenants-bash-ubuntu24-7403) |
| numeric-record-ordering | — | — | — | — | — | — | — | [2m 32s](../../../jobs/7403/2026-10-03__14-57-05/numeric-record-ordering-bash-ubuntu24-7403) |
| permanent-url-migration | — | — | — | — | — | — | — | [1m 52s](../../../jobs/7403/2026-10-03__14-57-05/permanent-url-migration-bash-ubuntu24-7403) |
| persistent-swap | — | — | — | — | — | — | — | [1m 55s](../../../jobs/7403/2026-10-03__14-57-05/persistent-swap-bash-ubuntu24-7403) |
| posix-shell-installer | — | — | — | — | — | — | — | [2m 27s](../../../jobs/7403/2026-10-03__14-57-05/posix-shell-installer-bash-ubuntu24-7403) |
| postgresql-sequence-repair | — | — | — | — | — | — | — | [2m 32s](../../../jobs/7403/2026-10-03__14-57-05/postgresql-sequence-repair-bash-ubuntu24-7403) |
| print-spool-recovery | — | — | — | — | — | — | — | [4m 18s](../../../jobs/7403/2026-10-03__14-57-05/print-spool-recovery-bash-ubuntu24-7403) |
| privacy-safe-support-export | — | — | — | — | — | — | — | [4m 03s](../../../jobs/7403/2026-10-03__14-57-05/privacy-safe-support-export-bash-ubuntu24-7403) |
| relative-symlink-relocation | — | — | — | — | — | — | — | [2m 22s](../../../jobs/7403/2026-10-03__14-57-05/relative-symlink-relocation-bash-ubuntu24-7403) |
| selective-tape-restore | — | — | — | — | — | — | — | [1m 48s](../../../jobs/7403/2026-10-03__14-57-05/selective-tape-restore-bash-ubuntu24-7403) |
| service-confinement | — | — | — | — | — | — | — | [3m 56s](../../../jobs/7403/2026-10-03__14-57-05/service-confinement-bash-ubuntu24-7403) |
| service-resource-limits | — | — | — | — | — | — | — | [2m 35s](../../../jobs/7403/2026-10-03__14-57-05/service-resource-limits-bash-ubuntu24-7403) |
| signal-driven-config-reload | — | — | — | — | — | — | — | [3m 16s](../../../jobs/7403/2026-10-03__14-57-05/signal-driven-config-reload-bash-ubuntu24-7403) |
| sparse-image-copy | — | — | — | — | — | — | — | [2m 34s](../../../jobs/7403/2026-10-03__14-57-05/sparse-image-copy-bash-ubuntu24-7403) |
| sqlite-lock-contention | — | — | — | — | — | — | — | [5m 11s](../../../jobs/7403/2026-10-03__14-57-05/sqlite-lock-contention-bash-ubuntu24-7403) |
| ssh-host-key-pinning | — | — | — | — | — | — | — | [2m 51s](../../../jobs/7403/2026-10-03__14-57-05/ssh-host-key-pinning-bash-ubuntu24-7403) |
| stale-pidfile-startup | — | — | — | — | — | — | — | [6m 30s](../../../jobs/7403/2026-10-03__14-57-05/stale-pidfile-startup-bash-ubuntu24-7403) |
| temporary-file-symlink-defense | — | — | — | — | — | — | — | [2m 51s](../../../jobs/7403/2026-10-03__14-57-05/temporary-file-symlink-defense-bash-ubuntu24-7403) |
| text-export-normalization | — | — | — | — | — | — | — | [2m 14s](../../../jobs/7403/2026-10-03__14-57-05/text-export-normalization-bash-ubuntu24-7403) |
| timezone-log-merge | — | — | — | — | — | — | — | [2m 28s](../../../jobs/7403/2026-10-03__14-57-05/timezone-log-merge-bash-ubuntu24-7403) |
| transactional-schema-upgrade | — | — | — | — | — | — | — | [2m 40s](../../../jobs/7403/2026-10-03__14-57-05/transactional-schema-upgrade-bash-ubuntu24-7403) |
| unix-socket-access-boundary | — | — | — | — | — | — | — | [3m 00s](../../../jobs/7403/2026-10-03__14-57-05/unix-socket-access-boundary-bash-ubuntu24-7403) |
| web-authentication-boundary | — | — | — | — | — | — | — | [3m 08s](../../../jobs/7403/2026-10-03__14-57-05/web-authentication-boundary-bash-ubuntu24-7403) |
| webdav-document-locks | — | — | — | — | — | — | — | [3m 11s](../../../jobs/7403/2026-10-03__14-57-05/webdav-document-locks-bash-ubuntu24-7403) |
| working-directory-independent-launch | — | — | — | — | — | — | — | [2m 06s](../../../jobs/7403/2026-10-03__14-57-05/working-directory-independent-launch-bash-ubuntu24-7403) |
| **Average** | — | — | — | — | — | — | — | 3m 55s |

Cluster provisioning is not a meaningful part of these times: median 738 ms across 100 clusters, about 0.44% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/account-resource-limits-bash-ubuntu24-7403) |
| application-log-rotation | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/application-log-rotation-bash-ubuntu24-7403) |
| custom-ca-trust | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/custom-ca-trust-bash-ubuntu24-7403) |
| host-firewall-baseline | — | — | — | — | — | — | — | [0.940](../../../jobs/7403/2026-10-03__14-57-05/host-firewall-baseline-bash-ubuntu24-7403) |
| kernel-network-hardening | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/kernel-network-hardening-bash-ubuntu24-7403) |
| repair-application-permissions | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/repair-application-permissions-bash-ubuntu24-7403) |
| scheduled-maintenance | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/scheduled-maintenance-bash-ubuntu24-7403) |
| ssh-key-only | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/ssh-key-only-bash-ubuntu24-7403) |
| sticky-drop-directory | — | — | — | — | — | — | — | [0.970](../../../jobs/7403/2026-10-03__14-57-05/sticky-drop-directory-bash-ubuntu24-7403) |
| unprivileged-service | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/unprivileged-service-bash-ubuntu24-7403) |
| mandatory-access-control-port | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/mandatory-access-control-port-bash-ubuntu24-7403) |
| kernel-module-blacklist | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/kernel-module-blacklist-bash-ubuntu24-7403) |
| boot-kernel-parameter | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/boot-kernel-parameter-bash-ubuntu24-7403) |
| mount-option-hardening | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/mount-option-hardening-bash-ubuntu24-7403) |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/password-complexity-policy-bash-ubuntu24-7403) |
| sudo-command-logging | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/sudo-command-logging-bash-ubuntu24-7403) |
| cron-access-control | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/cron-access-control-bash-ubuntu24-7403) |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | [0.800](../../../jobs/7403/2026-10-03__14-57-05/disk-quota-bash-ubuntu24-7403) |
| encrypted-volume | — | — | — | — | — | — | — | [0.980](../../../jobs/7403/2026-10-03__14-57-05/encrypted-volume-bash-ubuntu24-7403) |
| lvm-extend | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/lvm-extend-bash-ubuntu24-7403) |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/filesystem-snapshot-rollback-bash-ubuntu24-7403) |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/package-version-hold-bash-ubuntu24-7403) |
| local-package-repository | — | — | — | — | — | — | — | [0.780](../../../jobs/7403/2026-10-03__14-57-05/local-package-repository-bash-ubuntu24-7403) |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/certificate-rotation-bash-ubuntu24-7403) |
| file-integrity-baseline | — | — | — | — | — | — | — | [0.700](../../../jobs/7403/2026-10-03__14-57-05/file-integrity-baseline-bash-ubuntu24-7403) |
| archive-member-safety | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/archive-member-safety-bash-ubuntu24-7403) |
| atomic-release-publication | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/atomic-release-publication-bash-ubuntu24-7403) |
| batch-exclusive-lock | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/batch-exclusive-lock-bash-ubuntu24-7403) |
| cgi-report-execution | — | — | — | — | — | — | — | [0.970](../../../jobs/7403/2026-10-03__14-57-05/cgi-report-execution-bash-ubuntu24-7403) |
| child-process-reaping | — | — | — | — | — | — | — | [0.980](../../../jobs/7403/2026-10-03__14-57-05/child-process-reaping-bash-ubuntu24-7403) |
| chroot-web-service | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/chroot-web-service-bash-ubuntu24-7403) |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/cross-file-accounting-reconciliation-bash-ubuntu24-7403) |
| deleted-open-file-recovery | — | — | — | — | — | — | — | [0.930](../../../jobs/7403/2026-10-03__14-57-05/deleted-open-file-recovery-bash-ubuntu24-7403) |
| fifo-worker-reconnection | — | — | — | — | — | — | — | [0.900](../../../jobs/7403/2026-10-03__14-57-05/fifo-worker-reconnection-bash-ubuntu24-7403) |
| file-descriptor-leak | — | — | — | — | — | — | — | [0.980](../../../jobs/7403/2026-10-03__14-57-05/file-descriptor-leak-bash-ubuntu24-7403) |
| filename-encoding-migration | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/filename-encoding-migration-bash-ubuntu24-7403) |
| fixed-width-import-recovery | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/fixed-width-import-recovery-bash-ubuntu24-7403) |
| hardlink-aware-deduplication | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/hardlink-aware-deduplication-bash-ubuntu24-7403) |
| incremental-archive-chain | — | — | — | — | — | — | — | [0.920](../../../jobs/7403/2026-10-03__14-57-05/incremental-archive-chain-bash-ubuntu24-7403) |
| inherited-directory-acls | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/inherited-directory-acls-bash-ubuntu24-7403) |
| inode-cache-retention | — | — | — | — | — | — | — | — |
| large-counter-overflow | — | — | — | — | — | — | — | [0.970](../../../jobs/7403/2026-10-03__14-57-05/large-counter-overflow-bash-ubuntu24-7403) |
| mail-filter-routing | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/mail-filter-routing-bash-ubuntu24-7403) |
| mail-spool-deduplication | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/mail-spool-deduplication-bash-ubuntu24-7403) |
| minimal-environment-job | — | — | — | — | — | — | — | [0.970](../../../jobs/7403/2026-10-03__14-57-05/minimal-environment-job-bash-ubuntu24-7403) |
| name-based-web-tenants | — | — | — | — | — | — | — | [0.960](../../../jobs/7403/2026-10-03__14-57-05/name-based-web-tenants-bash-ubuntu24-7403) |
| numeric-record-ordering | — | — | — | — | — | — | — | [0.970](../../../jobs/7403/2026-10-03__14-57-05/numeric-record-ordering-bash-ubuntu24-7403) |
| permanent-url-migration | — | — | — | — | — | — | — | [0.960](../../../jobs/7403/2026-10-03__14-57-05/permanent-url-migration-bash-ubuntu24-7403) |
| persistent-swap | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/persistent-swap-bash-ubuntu24-7403) |
| posix-shell-installer | — | — | — | — | — | — | — | [0.920](../../../jobs/7403/2026-10-03__14-57-05/posix-shell-installer-bash-ubuntu24-7403) |
| postgresql-sequence-repair | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/postgresql-sequence-repair-bash-ubuntu24-7403) |
| print-spool-recovery | — | — | — | — | — | — | — | [0.900](../../../jobs/7403/2026-10-03__14-57-05/print-spool-recovery-bash-ubuntu24-7403) |
| privacy-safe-support-export | — | — | — | — | — | — | — | [0.920](../../../jobs/7403/2026-10-03__14-57-05/privacy-safe-support-export-bash-ubuntu24-7403) |
| relative-symlink-relocation | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/relative-symlink-relocation-bash-ubuntu24-7403) |
| selective-tape-restore | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/selective-tape-restore-bash-ubuntu24-7403) |
| service-confinement | — | — | — | — | — | — | — | [0.820](../../../jobs/7403/2026-10-03__14-57-05/service-confinement-bash-ubuntu24-7403) |
| service-resource-limits | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/service-resource-limits-bash-ubuntu24-7403) |
| signal-driven-config-reload | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/signal-driven-config-reload-bash-ubuntu24-7403) |
| sparse-image-copy | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/sparse-image-copy-bash-ubuntu24-7403) |
| sqlite-lock-contention | — | — | — | — | — | — | — | [0.900](../../../jobs/7403/2026-10-03__14-57-05/sqlite-lock-contention-bash-ubuntu24-7403) |
| ssh-host-key-pinning | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/ssh-host-key-pinning-bash-ubuntu24-7403) |
| stale-pidfile-startup | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/stale-pidfile-startup-bash-ubuntu24-7403) |
| temporary-file-symlink-defense | — | — | — | — | — | — | — | [0.980](../../../jobs/7403/2026-10-03__14-57-05/temporary-file-symlink-defense-bash-ubuntu24-7403) |
| text-export-normalization | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/text-export-normalization-bash-ubuntu24-7403) |
| timezone-log-merge | — | — | — | — | — | — | — | [0.960](../../../jobs/7403/2026-10-03__14-57-05/timezone-log-merge-bash-ubuntu24-7403) |
| transactional-schema-upgrade | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/transactional-schema-upgrade-bash-ubuntu24-7403) |
| unix-socket-access-boundary | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/unix-socket-access-boundary-bash-ubuntu24-7403) |
| web-authentication-boundary | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/web-authentication-boundary-bash-ubuntu24-7403) |
| webdav-document-locks | — | — | — | — | — | — | — | [0.930](../../../jobs/7403/2026-10-03__14-57-05/webdav-document-locks-bash-ubuntu24-7403) |
| working-directory-independent-launch | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/working-directory-independent-launch-bash-ubuntu24-7403) |
| **Average** | — | — | — | — | — | — | — | 0.971 |
