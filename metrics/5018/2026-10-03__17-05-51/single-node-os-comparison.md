# single-node-os-comparison: command execution summary

Scope: `5018/2026-10-03__17-05-51`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | [18/0](../../../jobs/5018/2026-10-03__17-05-51/account-resource-limits-bash-alpine-5018) | — | — | — | — | — | — | — |
| application-log-rotation | [11/0](../../../jobs/5018/2026-10-03__17-05-51/application-log-rotation-bash-alpine-5018) | — | — | — | — | — | — | — |
| custom-ca-trust | [9/1](../../../jobs/5018/2026-10-03__17-05-51/custom-ca-trust-bash-alpine-5018) | — | — | — | — | — | — | — |
| host-firewall-baseline | [23/1](../../../jobs/5018/2026-10-03__17-05-51/host-firewall-baseline-bash-alpine-5018) | — | — | — | — | — | — | — |
| kernel-network-hardening | [6/2](../../../jobs/5018/2026-10-03__17-05-51/kernel-network-hardening-bash-alpine-5018) | — | — | — | — | — | — | — |
| repair-application-permissions | [10/1](../../../jobs/5018/2026-10-03__17-05-51/repair-application-permissions-bash-alpine-5018) | — | — | — | — | — | — | — |
| scheduled-maintenance | [9/0](../../../jobs/5018/2026-10-03__17-05-51/scheduled-maintenance-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-key-only | [9/1](../../../jobs/5018/2026-10-03__17-05-51/ssh-key-only-bash-alpine-5018) | — | — | — | — | — | — | — |
| sticky-drop-directory | [8/0](../../../jobs/5018/2026-10-03__17-05-51/sticky-drop-directory-bash-alpine-5018) | — | — | — | — | — | — | — |
| unprivileged-service | [21/2](../../../jobs/5018/2026-10-03__17-05-51/unprivileged-service-bash-alpine-5018) | — | — | — | — | — | — | — |
| mandatory-access-control-port | [20/4](../../../jobs/5018/2026-10-03__17-05-51/mandatory-access-control-port-bash-alpine-5018) | — | — | — | — | — | — | — |
| kernel-module-blacklist | [12/1](../../../jobs/5018/2026-10-03__17-05-51/kernel-module-blacklist-bash-alpine-5018) | — | — | — | — | — | — | — |
| boot-kernel-parameter | [8/0](../../../jobs/5018/2026-10-03__17-05-51/boot-kernel-parameter-bash-alpine-5018) | — | — | — | — | — | — | — |
| mount-option-hardening | [12/1](../../../jobs/5018/2026-10-03__17-05-51/mount-option-hardening-bash-alpine-5018) | — | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | [13/1](../../../jobs/5018/2026-10-03__17-05-51/password-complexity-policy-bash-alpine-5018) | — | — | — | — | — | — | — |
| sudo-command-logging | [9/0](../../../jobs/5018/2026-10-03__17-05-51/sudo-command-logging-bash-alpine-5018) | — | — | — | — | — | — | — |
| cron-access-control | [22/0](../../../jobs/5018/2026-10-03__17-05-51/cron-access-control-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | [20/3](../../../jobs/5018/2026-10-03__17-05-51/disk-quota-bash-alpine-5018) | — | — | — | — | — | — | — |
| encrypted-volume | [14/2](../../../jobs/5018/2026-10-03__17-05-51/encrypted-volume-bash-alpine-5018) | — | — | — | — | — | — | — |
| lvm-extend | [11/1](../../../jobs/5018/2026-10-03__17-05-51/lvm-extend-bash-alpine-5018) | — | — | — | — | — | — | — |
| filesystem-snapshot-rollback | [23/2](../../../jobs/5018/2026-10-03__17-05-51/filesystem-snapshot-rollback-bash-alpine-5018) | — | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | [10/1](../../../jobs/5018/2026-10-03__17-05-51/package-version-hold-bash-alpine-5018) | — | — | — | — | — | — | — |
| local-package-repository | [16/5](../../../jobs/5018/2026-10-03__17-05-51/local-package-repository-bash-alpine-5018) | — | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | [12/2](../../../jobs/5018/2026-10-03__17-05-51/certificate-rotation-bash-alpine-5018) | — | — | — | — | — | — | — |
| file-integrity-baseline | [10/1](../../../jobs/5018/2026-10-03__17-05-51/file-integrity-baseline-bash-alpine-5018) | — | — | — | — | — | — | — |
| archive-member-safety | [9/1](../../../jobs/5018/2026-10-03__17-05-51/archive-member-safety-bash-alpine-5018) | — | — | — | — | — | — | — |
| atomic-release-publication | [8/0](../../../jobs/5018/2026-10-03__17-05-51/atomic-release-publication-bash-alpine-5018) | — | — | — | — | — | — | — |
| batch-exclusive-lock | [9/1](../../../jobs/5018/2026-10-03__17-05-51/batch-exclusive-lock-bash-alpine-5018) | — | — | — | — | — | — | — |
| cgi-report-execution | [18/2](../../../jobs/5018/2026-10-03__17-05-51/cgi-report-execution-bash-alpine-5018) | — | — | — | — | — | — | — |
| child-process-reaping | [9/1](../../../jobs/5018/2026-10-03__17-05-51/child-process-reaping-bash-alpine-5018) | — | — | — | — | — | — | — |
| chroot-web-service | [18/2](../../../jobs/5018/2026-10-03__17-05-51/chroot-web-service-bash-alpine-5018) | — | — | — | — | — | — | — |
| cross-file-accounting-reconciliation | [9/1](../../../jobs/5018/2026-10-03__17-05-51/cross-file-accounting-reconciliation-bash-alpine-5018) | — | — | — | — | — | — | — |
| deleted-open-file-recovery | [18/3](../../../jobs/5018/2026-10-03__17-05-51/deleted-open-file-recovery-bash-alpine-5018) | — | — | — | — | — | — | — |
| fifo-worker-reconnection | [13/4](../../../jobs/5018/2026-10-03__17-05-51/fifo-worker-reconnection-bash-alpine-5018) | — | — | — | — | — | — | — |
| file-descriptor-leak | [12/1](../../../jobs/5018/2026-10-03__17-05-51/file-descriptor-leak-bash-alpine-5018) | — | — | — | — | — | — | — |
| filename-encoding-migration | [7/1](../../../jobs/5018/2026-10-03__17-05-51/filename-encoding-migration-bash-alpine-5018) | — | — | — | — | — | — | — |
| fixed-width-import-recovery | [12/2](../../../jobs/5018/2026-10-03__17-05-51/fixed-width-import-recovery-bash-alpine-5018) | — | — | — | — | — | — | — |
| hardlink-aware-deduplication | [9/0](../../../jobs/5018/2026-10-03__17-05-51/hardlink-aware-deduplication-bash-alpine-5018) | — | — | — | — | — | — | — |
| incremental-archive-chain | [9/0](../../../jobs/5018/2026-10-03__17-05-51/incremental-archive-chain-bash-alpine-5018) | — | — | — | — | — | — | — |
| inherited-directory-acls | [10/0](../../../jobs/5018/2026-10-03__17-05-51/inherited-directory-acls-bash-alpine-5018) | — | — | — | — | — | — | — |
| inode-cache-retention | [0/0](../../../jobs/5018/2026-10-03__17-05-51/inode-cache-retention-bash-alpine-5018) | — | — | — | — | — | — | — |
| large-counter-overflow | [10/2](../../../jobs/5018/2026-10-03__17-05-51/large-counter-overflow-bash-alpine-5018) | — | — | — | — | — | — | — |
| mail-filter-routing | [7/2](../../../jobs/5018/2026-10-03__17-05-51/mail-filter-routing-bash-alpine-5018) | — | — | — | — | — | — | — |
| mail-spool-deduplication | [11/0](../../../jobs/5018/2026-10-03__17-05-51/mail-spool-deduplication-bash-alpine-5018) | — | — | — | — | — | — | — |
| minimal-environment-job | [7/0](../../../jobs/5018/2026-10-03__17-05-51/minimal-environment-job-bash-alpine-5018) | — | — | — | — | — | — | — |
| name-based-web-tenants | [12/0](../../../jobs/5018/2026-10-03__17-05-51/name-based-web-tenants-bash-alpine-5018) | — | — | — | — | — | — | — |
| numeric-record-ordering | [9/0](../../../jobs/5018/2026-10-03__17-05-51/numeric-record-ordering-bash-alpine-5018) | — | — | — | — | — | — | — |
| permanent-url-migration | [9/1](../../../jobs/5018/2026-10-03__17-05-51/permanent-url-migration-bash-alpine-5018) | — | — | — | — | — | — | — |
| persistent-swap | [8/1](../../../jobs/5018/2026-10-03__17-05-51/persistent-swap-bash-alpine-5018) | — | — | — | — | — | — | — |
| posix-shell-installer | [8/0](../../../jobs/5018/2026-10-03__17-05-51/posix-shell-installer-bash-alpine-5018) | — | — | — | — | — | — | — |
| postgresql-sequence-repair | [10/0](../../../jobs/5018/2026-10-03__17-05-51/postgresql-sequence-repair-bash-alpine-5018) | — | — | — | — | — | — | — |
| print-spool-recovery | [16/3](../../../jobs/5018/2026-10-03__17-05-51/print-spool-recovery-bash-alpine-5018) | — | — | — | — | — | — | — |
| privacy-safe-support-export | [9/0](../../../jobs/5018/2026-10-03__17-05-51/privacy-safe-support-export-bash-alpine-5018) | — | — | — | — | — | — | — |
| relative-symlink-relocation | [10/0](../../../jobs/5018/2026-10-03__17-05-51/relative-symlink-relocation-bash-alpine-5018) | — | — | — | — | — | — | — |
| selective-tape-restore | [9/1](../../../jobs/5018/2026-10-03__17-05-51/selective-tape-restore-bash-alpine-5018) | — | — | — | — | — | — | — |
| service-confinement | [16/4](../../../jobs/5018/2026-10-03__17-05-51/service-confinement-bash-alpine-5018) | — | — | — | — | — | — | — |
| service-resource-limits | [14/5](../../../jobs/5018/2026-10-03__17-05-51/service-resource-limits-bash-alpine-5018) | — | — | — | — | — | — | — |
| signal-driven-config-reload | [17/2](../../../jobs/5018/2026-10-03__17-05-51/signal-driven-config-reload-bash-alpine-5018) | — | — | — | — | — | — | — |
| sparse-image-copy | [13/1](../../../jobs/5018/2026-10-03__17-05-51/sparse-image-copy-bash-alpine-5018) | — | — | — | — | — | — | — |
| sqlite-lock-contention | [17/3](../../../jobs/5018/2026-10-03__17-05-51/sqlite-lock-contention-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-host-key-pinning | [12/2](../../../jobs/5018/2026-10-03__17-05-51/ssh-host-key-pinning-bash-alpine-5018) | — | — | — | — | — | — | — |
| stale-pidfile-startup | [12/0](../../../jobs/5018/2026-10-03__17-05-51/stale-pidfile-startup-bash-alpine-5018) | — | — | — | — | — | — | — |
| temporary-file-symlink-defense | [8/1](../../../jobs/5018/2026-10-03__17-05-51/temporary-file-symlink-defense-bash-alpine-5018) | — | — | — | — | — | — | — |
| text-export-normalization | [8/2](../../../jobs/5018/2026-10-03__17-05-51/text-export-normalization-bash-alpine-5018) | — | — | — | — | — | — | — |
| timezone-log-merge | [14/1](../../../jobs/5018/2026-10-03__17-05-51/timezone-log-merge-bash-alpine-5018) | — | — | — | — | — | — | — |
| transactional-schema-upgrade | [12/2](../../../jobs/5018/2026-10-03__17-05-51/transactional-schema-upgrade-bash-alpine-5018) | — | — | — | — | — | — | — |
| unix-socket-access-boundary | [9/1](../../../jobs/5018/2026-10-03__17-05-51/unix-socket-access-boundary-bash-alpine-5018) | — | — | — | — | — | — | — |
| web-authentication-boundary | [8/3](../../../jobs/5018/2026-10-03__17-05-51/web-authentication-boundary-bash-alpine-5018) | — | — | — | — | — | — | — |
| webdav-document-locks | [19/2](../../../jobs/5018/2026-10-03__17-05-51/webdav-document-locks-bash-alpine-5018) | — | — | — | — | — | — | — |
| working-directory-independent-launch | [12/1](../../../jobs/5018/2026-10-03__17-05-51/working-directory-independent-launch-bash-alpine-5018) | — | — | — | — | — | — | — |
| **Average** | 11.9/1.3 | — | — | — | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | [3m 16s](../../../jobs/5018/2026-10-03__17-05-51/account-resource-limits-bash-alpine-5018) | — | — | — | — | — | — | — |
| application-log-rotation | [3m 02s](../../../jobs/5018/2026-10-03__17-05-51/application-log-rotation-bash-alpine-5018) | — | — | — | — | — | — | — |
| custom-ca-trust | [2m 24s](../../../jobs/5018/2026-10-03__17-05-51/custom-ca-trust-bash-alpine-5018) | — | — | — | — | — | — | — |
| host-firewall-baseline | [4m 57s](../../../jobs/5018/2026-10-03__17-05-51/host-firewall-baseline-bash-alpine-5018) | — | — | — | — | — | — | — |
| kernel-network-hardening | [2m 38s](../../../jobs/5018/2026-10-03__17-05-51/kernel-network-hardening-bash-alpine-5018) | — | — | — | — | — | — | — |
| repair-application-permissions | [3m 13s](../../../jobs/5018/2026-10-03__17-05-51/repair-application-permissions-bash-alpine-5018) | — | — | — | — | — | — | — |
| scheduled-maintenance | [2m 15s](../../../jobs/5018/2026-10-03__17-05-51/scheduled-maintenance-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-key-only | [2m 47s](../../../jobs/5018/2026-10-03__17-05-51/ssh-key-only-bash-alpine-5018) | — | — | — | — | — | — | — |
| sticky-drop-directory | [2m 23s](../../../jobs/5018/2026-10-03__17-05-51/sticky-drop-directory-bash-alpine-5018) | — | — | — | — | — | — | — |
| unprivileged-service | [5m 44s](../../../jobs/5018/2026-10-03__17-05-51/unprivileged-service-bash-alpine-5018) | — | — | — | — | — | — | — |
| mandatory-access-control-port | [5m 41s](../../../jobs/5018/2026-10-03__17-05-51/mandatory-access-control-port-bash-alpine-5018) | — | — | — | — | — | — | — |
| kernel-module-blacklist | [2m 55s](../../../jobs/5018/2026-10-03__17-05-51/kernel-module-blacklist-bash-alpine-5018) | — | — | — | — | — | — | — |
| boot-kernel-parameter | [2m 22s](../../../jobs/5018/2026-10-03__17-05-51/boot-kernel-parameter-bash-alpine-5018) | — | — | — | — | — | — | — |
| mount-option-hardening | [3m 54s](../../../jobs/5018/2026-10-03__17-05-51/mount-option-hardening-bash-alpine-5018) | — | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | [4m 16s](../../../jobs/5018/2026-10-03__17-05-51/password-complexity-policy-bash-alpine-5018) | — | — | — | — | — | — | — |
| sudo-command-logging | [2m 47s](../../../jobs/5018/2026-10-03__17-05-51/sudo-command-logging-bash-alpine-5018) | — | — | — | — | — | — | — |
| cron-access-control | [5m 13s](../../../jobs/5018/2026-10-03__17-05-51/cron-access-control-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | [3m 51s](../../../jobs/5018/2026-10-03__17-05-51/disk-quota-bash-alpine-5018) | — | — | — | — | — | — | — |
| encrypted-volume | [4m 48s](../../../jobs/5018/2026-10-03__17-05-51/encrypted-volume-bash-alpine-5018) | — | — | — | — | — | — | — |
| lvm-extend | [3m 04s](../../../jobs/5018/2026-10-03__17-05-51/lvm-extend-bash-alpine-5018) | — | — | — | — | — | — | — |
| filesystem-snapshot-rollback | [4m 55s](../../../jobs/5018/2026-10-03__17-05-51/filesystem-snapshot-rollback-bash-alpine-5018) | — | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | [2m 53s](../../../jobs/5018/2026-10-03__17-05-51/package-version-hold-bash-alpine-5018) | — | — | — | — | — | — | — |
| local-package-repository | [4m 35s](../../../jobs/5018/2026-10-03__17-05-51/local-package-repository-bash-alpine-5018) | — | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | [4m 15s](../../../jobs/5018/2026-10-03__17-05-51/certificate-rotation-bash-alpine-5018) | — | — | — | — | — | — | — |
| file-integrity-baseline | [3m 30s](../../../jobs/5018/2026-10-03__17-05-51/file-integrity-baseline-bash-alpine-5018) | — | — | — | — | — | — | — |
| archive-member-safety | [3m 17s](../../../jobs/5018/2026-10-03__17-05-51/archive-member-safety-bash-alpine-5018) | — | — | — | — | — | — | — |
| atomic-release-publication | [3m 20s](../../../jobs/5018/2026-10-03__17-05-51/atomic-release-publication-bash-alpine-5018) | — | — | — | — | — | — | — |
| batch-exclusive-lock | [3m 10s](../../../jobs/5018/2026-10-03__17-05-51/batch-exclusive-lock-bash-alpine-5018) | — | — | — | — | — | — | — |
| cgi-report-execution | [3m 32s](../../../jobs/5018/2026-10-03__17-05-51/cgi-report-execution-bash-alpine-5018) | — | — | — | — | — | — | — |
| child-process-reaping | [3m 16s](../../../jobs/5018/2026-10-03__17-05-51/child-process-reaping-bash-alpine-5018) | — | — | — | — | — | — | — |
| chroot-web-service | [2m 48s](../../../jobs/5018/2026-10-03__17-05-51/chroot-web-service-bash-alpine-5018) | — | — | — | — | — | — | — |
| cross-file-accounting-reconciliation | [3m 17s](../../../jobs/5018/2026-10-03__17-05-51/cross-file-accounting-reconciliation-bash-alpine-5018) | — | — | — | — | — | — | — |
| deleted-open-file-recovery | [5m 29s](../../../jobs/5018/2026-10-03__17-05-51/deleted-open-file-recovery-bash-alpine-5018) | — | — | — | — | — | — | — |
| fifo-worker-reconnection | [3m 50s](../../../jobs/5018/2026-10-03__17-05-51/fifo-worker-reconnection-bash-alpine-5018) | — | — | — | — | — | — | — |
| file-descriptor-leak | [2m 45s](../../../jobs/5018/2026-10-03__17-05-51/file-descriptor-leak-bash-alpine-5018) | — | — | — | — | — | — | — |
| filename-encoding-migration | [2m 49s](../../../jobs/5018/2026-10-03__17-05-51/filename-encoding-migration-bash-alpine-5018) | — | — | — | — | — | — | — |
| fixed-width-import-recovery | [3m 55s](../../../jobs/5018/2026-10-03__17-05-51/fixed-width-import-recovery-bash-alpine-5018) | — | — | — | — | — | — | — |
| hardlink-aware-deduplication | [2m 22s](../../../jobs/5018/2026-10-03__17-05-51/hardlink-aware-deduplication-bash-alpine-5018) | — | — | — | — | — | — | — |
| incremental-archive-chain | [2m 18s](../../../jobs/5018/2026-10-03__17-05-51/incremental-archive-chain-bash-alpine-5018) | — | — | — | — | — | — | — |
| inherited-directory-acls | [3m 22s](../../../jobs/5018/2026-10-03__17-05-51/inherited-directory-acls-bash-alpine-5018) | — | — | — | — | — | — | — |
| inode-cache-retention | [4s](../../../jobs/5018/2026-10-03__17-05-51/inode-cache-retention-bash-alpine-5018) | — | — | — | — | — | — | — |
| large-counter-overflow | [3m 26s](../../../jobs/5018/2026-10-03__17-05-51/large-counter-overflow-bash-alpine-5018) | — | — | — | — | — | — | — |
| mail-filter-routing | [3m 06s](../../../jobs/5018/2026-10-03__17-05-51/mail-filter-routing-bash-alpine-5018) | — | — | — | — | — | — | — |
| mail-spool-deduplication | [3m 52s](../../../jobs/5018/2026-10-03__17-05-51/mail-spool-deduplication-bash-alpine-5018) | — | — | — | — | — | — | — |
| minimal-environment-job | [2m 22s](../../../jobs/5018/2026-10-03__17-05-51/minimal-environment-job-bash-alpine-5018) | — | — | — | — | — | — | — |
| name-based-web-tenants | [3m 00s](../../../jobs/5018/2026-10-03__17-05-51/name-based-web-tenants-bash-alpine-5018) | — | — | — | — | — | — | — |
| numeric-record-ordering | [3m 32s](../../../jobs/5018/2026-10-03__17-05-51/numeric-record-ordering-bash-alpine-5018) | — | — | — | — | — | — | — |
| permanent-url-migration | [2m 43s](../../../jobs/5018/2026-10-03__17-05-51/permanent-url-migration-bash-alpine-5018) | — | — | — | — | — | — | — |
| persistent-swap | [3m 45s](../../../jobs/5018/2026-10-03__17-05-51/persistent-swap-bash-alpine-5018) | — | — | — | — | — | — | — |
| posix-shell-installer | [3m 15s](../../../jobs/5018/2026-10-03__17-05-51/posix-shell-installer-bash-alpine-5018) | — | — | — | — | — | — | — |
| postgresql-sequence-repair | [2m 24s](../../../jobs/5018/2026-10-03__17-05-51/postgresql-sequence-repair-bash-alpine-5018) | — | — | — | — | — | — | — |
| print-spool-recovery | [4m 15s](../../../jobs/5018/2026-10-03__17-05-51/print-spool-recovery-bash-alpine-5018) | — | — | — | — | — | — | — |
| privacy-safe-support-export | [4m 01s](../../../jobs/5018/2026-10-03__17-05-51/privacy-safe-support-export-bash-alpine-5018) | — | — | — | — | — | — | — |
| relative-symlink-relocation | [2m 30s](../../../jobs/5018/2026-10-03__17-05-51/relative-symlink-relocation-bash-alpine-5018) | — | — | — | — | — | — | — |
| selective-tape-restore | [2m 39s](../../../jobs/5018/2026-10-03__17-05-51/selective-tape-restore-bash-alpine-5018) | — | — | — | — | — | — | — |
| service-confinement | [5m 12s](../../../jobs/5018/2026-10-03__17-05-51/service-confinement-bash-alpine-5018) | — | — | — | — | — | — | — |
| service-resource-limits | [4m 33s](../../../jobs/5018/2026-10-03__17-05-51/service-resource-limits-bash-alpine-5018) | — | — | — | — | — | — | — |
| signal-driven-config-reload | [4m 42s](../../../jobs/5018/2026-10-03__17-05-51/signal-driven-config-reload-bash-alpine-5018) | — | — | — | — | — | — | — |
| sparse-image-copy | [3m 22s](../../../jobs/5018/2026-10-03__17-05-51/sparse-image-copy-bash-alpine-5018) | — | — | — | — | — | — | — |
| sqlite-lock-contention | [5m 10s](../../../jobs/5018/2026-10-03__17-05-51/sqlite-lock-contention-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-host-key-pinning | [3m 35s](../../../jobs/5018/2026-10-03__17-05-51/ssh-host-key-pinning-bash-alpine-5018) | — | — | — | — | — | — | — |
| stale-pidfile-startup | [3m 51s](../../../jobs/5018/2026-10-03__17-05-51/stale-pidfile-startup-bash-alpine-5018) | — | — | — | — | — | — | — |
| temporary-file-symlink-defense | [9m 50s](../../../jobs/5018/2026-10-03__17-05-51/temporary-file-symlink-defense-bash-alpine-5018) | — | — | — | — | — | — | — |
| text-export-normalization | [3m 35s](../../../jobs/5018/2026-10-03__17-05-51/text-export-normalization-bash-alpine-5018) | — | — | — | — | — | — | — |
| timezone-log-merge | [3m 34s](../../../jobs/5018/2026-10-03__17-05-51/timezone-log-merge-bash-alpine-5018) | — | — | — | — | — | — | — |
| transactional-schema-upgrade | [3m 48s](../../../jobs/5018/2026-10-03__17-05-51/transactional-schema-upgrade-bash-alpine-5018) | — | — | — | — | — | — | — |
| unix-socket-access-boundary | [3m 39s](../../../jobs/5018/2026-10-03__17-05-51/unix-socket-access-boundary-bash-alpine-5018) | — | — | — | — | — | — | — |
| web-authentication-boundary | [3m 20s](../../../jobs/5018/2026-10-03__17-05-51/web-authentication-boundary-bash-alpine-5018) | — | — | — | — | — | — | — |
| webdav-document-locks | [4m 21s](../../../jobs/5018/2026-10-03__17-05-51/webdav-document-locks-bash-alpine-5018) | — | — | — | — | — | — | — |
| working-directory-independent-launch | [2m 38s](../../../jobs/5018/2026-10-03__17-05-51/working-directory-independent-launch-bash-alpine-5018) | — | — | — | — | — | — | — |
| **Average** | 3m 35s | — | — | — | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 712 ms across 100 clusters, about 0.31% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | [0.970](../../../jobs/5018/2026-10-03__17-05-51/account-resource-limits-bash-alpine-5018) | — | — | — | — | — | — | — |
| application-log-rotation | [0.900](../../../jobs/5018/2026-10-03__17-05-51/application-log-rotation-bash-alpine-5018) | — | — | — | — | — | — | — |
| custom-ca-trust | [0.970](../../../jobs/5018/2026-10-03__17-05-51/custom-ca-trust-bash-alpine-5018) | — | — | — | — | — | — | — |
| host-firewall-baseline | [0.820](../../../jobs/5018/2026-10-03__17-05-51/host-firewall-baseline-bash-alpine-5018) | — | — | — | — | — | — | — |
| kernel-network-hardening | [1.000](../../../jobs/5018/2026-10-03__17-05-51/kernel-network-hardening-bash-alpine-5018) | — | — | — | — | — | — | — |
| repair-application-permissions | [0.960](../../../jobs/5018/2026-10-03__17-05-51/repair-application-permissions-bash-alpine-5018) | — | — | — | — | — | — | — |
| scheduled-maintenance | [0.960](../../../jobs/5018/2026-10-03__17-05-51/scheduled-maintenance-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-key-only | [0.950](../../../jobs/5018/2026-10-03__17-05-51/ssh-key-only-bash-alpine-5018) | — | — | — | — | — | — | — |
| sticky-drop-directory | [0.900](../../../jobs/5018/2026-10-03__17-05-51/sticky-drop-directory-bash-alpine-5018) | — | — | — | — | — | — | — |
| unprivileged-service | [0.930](../../../jobs/5018/2026-10-03__17-05-51/unprivileged-service-bash-alpine-5018) | — | — | — | — | — | — | — |
| mandatory-access-control-port | [0.880](../../../jobs/5018/2026-10-03__17-05-51/mandatory-access-control-port-bash-alpine-5018) | — | — | — | — | — | — | — |
| kernel-module-blacklist | [0.880](../../../jobs/5018/2026-10-03__17-05-51/kernel-module-blacklist-bash-alpine-5018) | — | — | — | — | — | — | — |
| boot-kernel-parameter | [0.900](../../../jobs/5018/2026-10-03__17-05-51/boot-kernel-parameter-bash-alpine-5018) | — | — | — | — | — | — | — |
| mount-option-hardening | [0.820](../../../jobs/5018/2026-10-03__17-05-51/mount-option-hardening-bash-alpine-5018) | — | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | [0.960](../../../jobs/5018/2026-10-03__17-05-51/password-complexity-policy-bash-alpine-5018) | — | — | — | — | — | — | — |
| sudo-command-logging | [1.000](../../../jobs/5018/2026-10-03__17-05-51/sudo-command-logging-bash-alpine-5018) | — | — | — | — | — | — | — |
| cron-access-control | [0.940](../../../jobs/5018/2026-10-03__17-05-51/cron-access-control-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | [0.940](../../../jobs/5018/2026-10-03__17-05-51/disk-quota-bash-alpine-5018) | — | — | — | — | — | — | — |
| encrypted-volume | [0.870](../../../jobs/5018/2026-10-03__17-05-51/encrypted-volume-bash-alpine-5018) | — | — | — | — | — | — | — |
| lvm-extend | [0.960](../../../jobs/5018/2026-10-03__17-05-51/lvm-extend-bash-alpine-5018) | — | — | — | — | — | — | — |
| filesystem-snapshot-rollback | [0.900](../../../jobs/5018/2026-10-03__17-05-51/filesystem-snapshot-rollback-bash-alpine-5018) | — | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | [0.910](../../../jobs/5018/2026-10-03__17-05-51/package-version-hold-bash-alpine-5018) | — | — | — | — | — | — | — |
| local-package-repository | [0.840](../../../jobs/5018/2026-10-03__17-05-51/local-package-repository-bash-alpine-5018) | — | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | [0.930](../../../jobs/5018/2026-10-03__17-05-51/certificate-rotation-bash-alpine-5018) | — | — | — | — | — | — | — |
| file-integrity-baseline | [0.960](../../../jobs/5018/2026-10-03__17-05-51/file-integrity-baseline-bash-alpine-5018) | — | — | — | — | — | — | — |
| archive-member-safety | [0.960](../../../jobs/5018/2026-10-03__17-05-51/archive-member-safety-bash-alpine-5018) | — | — | — | — | — | — | — |
| atomic-release-publication | [0.940](../../../jobs/5018/2026-10-03__17-05-51/atomic-release-publication-bash-alpine-5018) | — | — | — | — | — | — | — |
| batch-exclusive-lock | [0.930](../../../jobs/5018/2026-10-03__17-05-51/batch-exclusive-lock-bash-alpine-5018) | — | — | — | — | — | — | — |
| cgi-report-execution | [0.940](../../../jobs/5018/2026-10-03__17-05-51/cgi-report-execution-bash-alpine-5018) | — | — | — | — | — | — | — |
| child-process-reaping | [0.860](../../../jobs/5018/2026-10-03__17-05-51/child-process-reaping-bash-alpine-5018) | — | — | — | — | — | — | — |
| chroot-web-service | [0.970](../../../jobs/5018/2026-10-03__17-05-51/chroot-web-service-bash-alpine-5018) | — | — | — | — | — | — | — |
| cross-file-accounting-reconciliation | [1.000](../../../jobs/5018/2026-10-03__17-05-51/cross-file-accounting-reconciliation-bash-alpine-5018) | — | — | — | — | — | — | — |
| deleted-open-file-recovery | [0.930](../../../jobs/5018/2026-10-03__17-05-51/deleted-open-file-recovery-bash-alpine-5018) | — | — | — | — | — | — | — |
| fifo-worker-reconnection | [0.880](../../../jobs/5018/2026-10-03__17-05-51/fifo-worker-reconnection-bash-alpine-5018) | — | — | — | — | — | — | — |
| file-descriptor-leak | [0.840](../../../jobs/5018/2026-10-03__17-05-51/file-descriptor-leak-bash-alpine-5018) | — | — | — | — | — | — | — |
| filename-encoding-migration | [0.960](../../../jobs/5018/2026-10-03__17-05-51/filename-encoding-migration-bash-alpine-5018) | — | — | — | — | — | — | — |
| fixed-width-import-recovery | [0.880](../../../jobs/5018/2026-10-03__17-05-51/fixed-width-import-recovery-bash-alpine-5018) | — | — | — | — | — | — | — |
| hardlink-aware-deduplication | [0.970](../../../jobs/5018/2026-10-03__17-05-51/hardlink-aware-deduplication-bash-alpine-5018) | — | — | — | — | — | — | — |
| incremental-archive-chain | [0.960](../../../jobs/5018/2026-10-03__17-05-51/incremental-archive-chain-bash-alpine-5018) | — | — | — | — | — | — | — |
| inherited-directory-acls | [0.820](../../../jobs/5018/2026-10-03__17-05-51/inherited-directory-acls-bash-alpine-5018) | — | — | — | — | — | — | — |
| inode-cache-retention | — | — | — | — | — | — | — | — |
| large-counter-overflow | [0.970](../../../jobs/5018/2026-10-03__17-05-51/large-counter-overflow-bash-alpine-5018) | — | — | — | — | — | — | — |
| mail-filter-routing | [0.970](../../../jobs/5018/2026-10-03__17-05-51/mail-filter-routing-bash-alpine-5018) | — | — | — | — | — | — | — |
| mail-spool-deduplication | [0.900](../../../jobs/5018/2026-10-03__17-05-51/mail-spool-deduplication-bash-alpine-5018) | — | — | — | — | — | — | — |
| minimal-environment-job | [0.900](../../../jobs/5018/2026-10-03__17-05-51/minimal-environment-job-bash-alpine-5018) | — | — | — | — | — | — | — |
| name-based-web-tenants | [0.920](../../../jobs/5018/2026-10-03__17-05-51/name-based-web-tenants-bash-alpine-5018) | — | — | — | — | — | — | — |
| numeric-record-ordering | [1.000](../../../jobs/5018/2026-10-03__17-05-51/numeric-record-ordering-bash-alpine-5018) | — | — | — | — | — | — | — |
| permanent-url-migration | [0.780](../../../jobs/5018/2026-10-03__17-05-51/permanent-url-migration-bash-alpine-5018) | — | — | — | — | — | — | — |
| persistent-swap | [0.970](../../../jobs/5018/2026-10-03__17-05-51/persistent-swap-bash-alpine-5018) | — | — | — | — | — | — | — |
| posix-shell-installer | [0.970](../../../jobs/5018/2026-10-03__17-05-51/posix-shell-installer-bash-alpine-5018) | — | — | — | — | — | — | — |
| postgresql-sequence-repair | [0.970](../../../jobs/5018/2026-10-03__17-05-51/postgresql-sequence-repair-bash-alpine-5018) | — | — | — | — | — | — | — |
| print-spool-recovery | [0.950](../../../jobs/5018/2026-10-03__17-05-51/print-spool-recovery-bash-alpine-5018) | — | — | — | — | — | — | — |
| privacy-safe-support-export | [0.970](../../../jobs/5018/2026-10-03__17-05-51/privacy-safe-support-export-bash-alpine-5018) | — | — | — | — | — | — | — |
| relative-symlink-relocation | [0.950](../../../jobs/5018/2026-10-03__17-05-51/relative-symlink-relocation-bash-alpine-5018) | — | — | — | — | — | — | — |
| selective-tape-restore | [0.960](../../../jobs/5018/2026-10-03__17-05-51/selective-tape-restore-bash-alpine-5018) | — | — | — | — | — | — | — |
| service-confinement | [0.960](../../../jobs/5018/2026-10-03__17-05-51/service-confinement-bash-alpine-5018) | — | — | — | — | — | — | — |
| service-resource-limits | [0.950](../../../jobs/5018/2026-10-03__17-05-51/service-resource-limits-bash-alpine-5018) | — | — | — | — | — | — | — |
| signal-driven-config-reload | [0.950](../../../jobs/5018/2026-10-03__17-05-51/signal-driven-config-reload-bash-alpine-5018) | — | — | — | — | — | — | — |
| sparse-image-copy | [0.920](../../../jobs/5018/2026-10-03__17-05-51/sparse-image-copy-bash-alpine-5018) | — | — | — | — | — | — | — |
| sqlite-lock-contention | [0.820](../../../jobs/5018/2026-10-03__17-05-51/sqlite-lock-contention-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-host-key-pinning | [0.970](../../../jobs/5018/2026-10-03__17-05-51/ssh-host-key-pinning-bash-alpine-5018) | — | — | — | — | — | — | — |
| stale-pidfile-startup | [0.970](../../../jobs/5018/2026-10-03__17-05-51/stale-pidfile-startup-bash-alpine-5018) | — | — | — | — | — | — | — |
| temporary-file-symlink-defense | [0.970](../../../jobs/5018/2026-10-03__17-05-51/temporary-file-symlink-defense-bash-alpine-5018) | — | — | — | — | — | — | — |
| text-export-normalization | [0.860](../../../jobs/5018/2026-10-03__17-05-51/text-export-normalization-bash-alpine-5018) | — | — | — | — | — | — | — |
| timezone-log-merge | [0.970](../../../jobs/5018/2026-10-03__17-05-51/timezone-log-merge-bash-alpine-5018) | — | — | — | — | — | — | — |
| transactional-schema-upgrade | [0.920](../../../jobs/5018/2026-10-03__17-05-51/transactional-schema-upgrade-bash-alpine-5018) | — | — | — | — | — | — | — |
| unix-socket-access-boundary | [0.860](../../../jobs/5018/2026-10-03__17-05-51/unix-socket-access-boundary-bash-alpine-5018) | — | — | — | — | — | — | — |
| web-authentication-boundary | [0.970](../../../jobs/5018/2026-10-03__17-05-51/web-authentication-boundary-bash-alpine-5018) | — | — | — | — | — | — | — |
| webdav-document-locks | [0.860](../../../jobs/5018/2026-10-03__17-05-51/webdav-document-locks-bash-alpine-5018) | — | — | — | — | — | — | — |
| working-directory-independent-launch | [0.970](../../../jobs/5018/2026-10-03__17-05-51/working-directory-independent-launch-bash-alpine-5018) | — | — | — | — | — | — | — |
| **Average** | 0.927 | — | — | — | — | — | — | — |
