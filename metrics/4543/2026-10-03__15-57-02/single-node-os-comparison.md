# single-node-os-comparison: command execution summary

Scope: `4543/2026-10-03__15-57-02`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | [10/0](../../../jobs/4543/2026-10-03__15-57-02/account-resource-limits-bash-centos-stream10-4543) | — | — | — | — | — |
| application-log-rotation | — | — | [9/0](../../../jobs/4543/2026-10-03__15-57-02/application-log-rotation-bash-centos-stream10-4543) | — | — | — | — | — |
| custom-ca-trust | — | — | [11/0](../../../jobs/4543/2026-10-03__15-57-02/custom-ca-trust-bash-centos-stream10-4543) | — | — | — | — | — |
| host-firewall-baseline | — | — | [11/1](../../../jobs/4543/2026-10-03__15-57-02/host-firewall-baseline-bash-centos-stream10-4543) | — | — | — | — | — |
| kernel-network-hardening | — | — | [12/1](../../../jobs/4543/2026-10-03__15-57-02/kernel-network-hardening-bash-centos-stream10-4543) | — | — | — | — | — |
| repair-application-permissions | — | — | [10/1](../../../jobs/4543/2026-10-03__15-57-02/repair-application-permissions-bash-centos-stream10-4543) | — | — | — | — | — |
| scheduled-maintenance | — | — | [14/0](../../../jobs/4543/2026-10-03__15-57-02/scheduled-maintenance-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-key-only | — | — | [10/0](../../../jobs/4543/2026-10-03__15-57-02/ssh-key-only-bash-centos-stream10-4543) | — | — | — | — | — |
| sticky-drop-directory | — | — | [9/1](../../../jobs/4543/2026-10-03__15-57-02/sticky-drop-directory-bash-centos-stream10-4543) | — | — | — | — | — |
| unprivileged-service | — | — | [12/0](../../../jobs/4543/2026-10-03__15-57-02/unprivileged-service-bash-centos-stream10-4543) | — | — | — | — | — |
| mandatory-access-control-port | — | — | [15/2](../../../jobs/4543/2026-10-03__15-57-02/mandatory-access-control-port-bash-centos-stream10-4543) | — | — | — | — | — |
| kernel-module-blacklist | — | — | [9/0](../../../jobs/4543/2026-10-03__15-57-02/kernel-module-blacklist-bash-centos-stream10-4543) | — | — | — | — | — |
| boot-kernel-parameter | — | — | [7/0](../../../jobs/4543/2026-10-03__15-57-02/boot-kernel-parameter-bash-centos-stream10-4543) | — | — | — | — | — |
| mount-option-hardening | — | — | [12/0](../../../jobs/4543/2026-10-03__15-57-02/mount-option-hardening-bash-centos-stream10-4543) | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | [11/0](../../../jobs/4543/2026-10-03__15-57-02/password-complexity-policy-bash-centos-stream10-4543) | — | — | — | — | — |
| sudo-command-logging | — | — | [9/0](../../../jobs/4543/2026-10-03__15-57-02/sudo-command-logging-bash-centos-stream10-4543) | — | — | — | — | — |
| cron-access-control | — | — | [15/0](../../../jobs/4543/2026-10-03__15-57-02/cron-access-control-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | [14/1](../../../jobs/4543/2026-10-03__15-57-02/disk-quota-bash-centos-stream10-4543) | — | — | — | — | — |
| encrypted-volume | — | — | [11/0](../../../jobs/4543/2026-10-03__15-57-02/encrypted-volume-bash-centos-stream10-4543) | — | — | — | — | — |
| lvm-extend | — | — | [13/0](../../../jobs/4543/2026-10-03__15-57-02/lvm-extend-bash-centos-stream10-4543) | — | — | — | — | — |
| filesystem-snapshot-rollback | — | — | [25/0](../../../jobs/4543/2026-10-03__15-57-02/filesystem-snapshot-rollback-bash-centos-stream10-4543) | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | [9/0](../../../jobs/4543/2026-10-03__15-57-02/package-version-hold-bash-centos-stream10-4543) | — | — | — | — | — |
| local-package-repository | — | — | [12/1](../../../jobs/4543/2026-10-03__15-57-02/local-package-repository-bash-centos-stream10-4543) | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | [18/1](../../../jobs/4543/2026-10-03__15-57-02/certificate-rotation-bash-centos-stream10-4543) | — | — | — | — | — |
| file-integrity-baseline | — | — | [22/1](../../../jobs/4543/2026-10-03__15-57-02/file-integrity-baseline-bash-centos-stream10-4543) | — | — | — | — | — |
| archive-member-safety | — | — | [13/1](../../../jobs/4543/2026-10-03__15-57-02/archive-member-safety-bash-centos-stream10-4543) | — | — | — | — | — |
| atomic-release-publication | — | — | [12/0](../../../jobs/4543/2026-10-03__15-57-02/atomic-release-publication-bash-centos-stream10-4543) | — | — | — | — | — |
| batch-exclusive-lock | — | — | [10/1](../../../jobs/4543/2026-10-03__15-57-02/batch-exclusive-lock-bash-centos-stream10-4543) | — | — | — | — | — |
| cgi-report-execution | — | — | [13/0](../../../jobs/4543/2026-10-03__15-57-02/cgi-report-execution-bash-centos-stream10-4543) | — | — | — | — | — |
| child-process-reaping | — | — | [9/2](../../../jobs/4543/2026-10-03__15-57-02/child-process-reaping-bash-centos-stream10-4543) | — | — | — | — | — |
| chroot-web-service | — | — | [13/0](../../../jobs/4543/2026-10-03__15-57-02/chroot-web-service-bash-centos-stream10-4543) | — | — | — | — | — |
| cross-file-accounting-reconciliation | — | — | [10/0](../../../jobs/4543/2026-10-03__15-57-02/cross-file-accounting-reconciliation-bash-centos-stream10-4543) | — | — | — | — | — |
| deleted-open-file-recovery | — | — | [21/0](../../../jobs/4543/2026-10-03__15-57-02/deleted-open-file-recovery-bash-centos-stream10-4543) | — | — | — | — | — |
| fifo-worker-reconnection | — | — | [14/0](../../../jobs/4543/2026-10-03__15-57-02/fifo-worker-reconnection-bash-centos-stream10-4543) | — | — | — | — | — |
| file-descriptor-leak | — | — | [10/0](../../../jobs/4543/2026-10-03__15-57-02/file-descriptor-leak-bash-centos-stream10-4543) | — | — | — | — | — |
| filename-encoding-migration | — | — | [8/0](../../../jobs/4543/2026-10-03__15-57-02/filename-encoding-migration-bash-centos-stream10-4543) | — | — | — | — | — |
| fixed-width-import-recovery | — | — | [10/0](../../../jobs/4543/2026-10-03__15-57-02/fixed-width-import-recovery-bash-centos-stream10-4543) | — | — | — | — | — |
| hardlink-aware-deduplication | — | — | [14/0](../../../jobs/4543/2026-10-03__15-57-02/hardlink-aware-deduplication-bash-centos-stream10-4543) | — | — | — | — | — |
| incremental-archive-chain | — | — | [11/0](../../../jobs/4543/2026-10-03__15-57-02/incremental-archive-chain-bash-centos-stream10-4543) | — | — | — | — | — |
| inherited-directory-acls | — | — | [10/0](../../../jobs/4543/2026-10-03__15-57-02/inherited-directory-acls-bash-centos-stream10-4543) | — | — | — | — | — |
| inode-cache-retention | — | — | [0/0](../../../jobs/4543/2026-10-03__15-57-02/inode-cache-retention-bash-centos-stream10-4543) | — | — | — | — | — |
| large-counter-overflow | — | — | [13/0](../../../jobs/4543/2026-10-03__15-57-02/large-counter-overflow-bash-centos-stream10-4543) | — | — | — | — | — |
| mail-filter-routing | — | — | [8/0](../../../jobs/4543/2026-10-03__15-57-02/mail-filter-routing-bash-centos-stream10-4543) | — | — | — | — | — |
| mail-spool-deduplication | — | — | [13/0](../../../jobs/4543/2026-10-03__15-57-02/mail-spool-deduplication-bash-centos-stream10-4543) | — | — | — | — | — |
| minimal-environment-job | — | — | [8/1](../../../jobs/4543/2026-10-03__15-57-02/minimal-environment-job-bash-centos-stream10-4543) | — | — | — | — | — |
| name-based-web-tenants | — | — | [13/1](../../../jobs/4543/2026-10-03__15-57-02/name-based-web-tenants-bash-centos-stream10-4543) | — | — | — | — | — |
| numeric-record-ordering | — | — | [10/1](../../../jobs/4543/2026-10-03__15-57-02/numeric-record-ordering-bash-centos-stream10-4543) | — | — | — | — | — |
| permanent-url-migration | — | — | [14/0](../../../jobs/4543/2026-10-03__15-57-02/permanent-url-migration-bash-centos-stream10-4543) | — | — | — | — | — |
| persistent-swap | — | — | [10/0](../../../jobs/4543/2026-10-03__15-57-02/persistent-swap-bash-centos-stream10-4543) | — | — | — | — | — |
| posix-shell-installer | — | — | [9/0](../../../jobs/4543/2026-10-03__15-57-02/posix-shell-installer-bash-centos-stream10-4543) | — | — | — | — | — |
| postgresql-sequence-repair | — | — | [10/0](../../../jobs/4543/2026-10-03__15-57-02/postgresql-sequence-repair-bash-centos-stream10-4543) | — | — | — | — | — |
| print-spool-recovery | — | — | [16/2](../../../jobs/4543/2026-10-03__15-57-02/print-spool-recovery-bash-centos-stream10-4543) | — | — | — | — | — |
| privacy-safe-support-export | — | — | [11/0](../../../jobs/4543/2026-10-03__15-57-02/privacy-safe-support-export-bash-centos-stream10-4543) | — | — | — | — | — |
| relative-symlink-relocation | — | — | [12/1](../../../jobs/4543/2026-10-03__15-57-02/relative-symlink-relocation-bash-centos-stream10-4543) | — | — | — | — | — |
| selective-tape-restore | — | — | [8/0](../../../jobs/4543/2026-10-03__15-57-02/selective-tape-restore-bash-centos-stream10-4543) | — | — | — | — | — |
| service-confinement | — | — | [37/3](../../../jobs/4543/2026-10-03__15-57-02/service-confinement-bash-centos-stream10-4543) | — | — | — | — | — |
| service-resource-limits | — | — | [14/0](../../../jobs/4543/2026-10-03__15-57-02/service-resource-limits-bash-centos-stream10-4543) | — | — | — | — | — |
| signal-driven-config-reload | — | — | [14/0](../../../jobs/4543/2026-10-03__15-57-02/signal-driven-config-reload-bash-centos-stream10-4543) | — | — | — | — | — |
| sparse-image-copy | — | — | [12/1](../../../jobs/4543/2026-10-03__15-57-02/sparse-image-copy-bash-centos-stream10-4543) | — | — | — | — | — |
| sqlite-lock-contention | — | — | [11/1](../../../jobs/4543/2026-10-03__15-57-02/sqlite-lock-contention-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-host-key-pinning | — | — | [8/0](../../../jobs/4543/2026-10-03__15-57-02/ssh-host-key-pinning-bash-centos-stream10-4543) | — | — | — | — | — |
| stale-pidfile-startup | — | — | [17/0](../../../jobs/4543/2026-10-03__15-57-02/stale-pidfile-startup-bash-centos-stream10-4543) | — | — | — | — | — |
| temporary-file-symlink-defense | — | — | [9/0](../../../jobs/4543/2026-10-03__15-57-02/temporary-file-symlink-defense-bash-centos-stream10-4543) | — | — | — | — | — |
| text-export-normalization | — | — | [10/1](../../../jobs/4543/2026-10-03__15-57-02/text-export-normalization-bash-centos-stream10-4543) | — | — | — | — | — |
| timezone-log-merge | — | — | [12/0](../../../jobs/4543/2026-10-03__15-57-02/timezone-log-merge-bash-centos-stream10-4543) | — | — | — | — | — |
| transactional-schema-upgrade | — | — | [10/0](../../../jobs/4543/2026-10-03__15-57-02/transactional-schema-upgrade-bash-centos-stream10-4543) | — | — | — | — | — |
| unix-socket-access-boundary | — | — | [13/0](../../../jobs/4543/2026-10-03__15-57-02/unix-socket-access-boundary-bash-centos-stream10-4543) | — | — | — | — | — |
| web-authentication-boundary | — | — | [13/0](../../../jobs/4543/2026-10-03__15-57-02/web-authentication-boundary-bash-centos-stream10-4543) | — | — | — | — | — |
| webdav-document-locks | — | — | [13/0](../../../jobs/4543/2026-10-03__15-57-02/webdav-document-locks-bash-centos-stream10-4543) | — | — | — | — | — |
| working-directory-independent-launch | — | — | [12/0](../../../jobs/4543/2026-10-03__15-57-02/working-directory-independent-launch-bash-centos-stream10-4543) | — | — | — | — | — |
| **Average** | — | — | 12.1/0.4 | — | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | [1m 47s](../../../jobs/4543/2026-10-03__15-57-02/account-resource-limits-bash-centos-stream10-4543) | — | — | — | — | — |
| application-log-rotation | — | — | [2m 13s](../../../jobs/4543/2026-10-03__15-57-02/application-log-rotation-bash-centos-stream10-4543) | — | — | — | — | — |
| custom-ca-trust | — | — | [2m 07s](../../../jobs/4543/2026-10-03__15-57-02/custom-ca-trust-bash-centos-stream10-4543) | — | — | — | — | — |
| host-firewall-baseline | — | — | [2m 56s](../../../jobs/4543/2026-10-03__15-57-02/host-firewall-baseline-bash-centos-stream10-4543) | — | — | — | — | — |
| kernel-network-hardening | — | — | [2m 05s](../../../jobs/4543/2026-10-03__15-57-02/kernel-network-hardening-bash-centos-stream10-4543) | — | — | — | — | — |
| repair-application-permissions | — | — | [2m 28s](../../../jobs/4543/2026-10-03__15-57-02/repair-application-permissions-bash-centos-stream10-4543) | — | — | — | — | — |
| scheduled-maintenance | — | — | [4m 50s](../../../jobs/4543/2026-10-03__15-57-02/scheduled-maintenance-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-key-only | — | — | [2m 09s](../../../jobs/4543/2026-10-03__15-57-02/ssh-key-only-bash-centos-stream10-4543) | — | — | — | — | — |
| sticky-drop-directory | — | — | [2m 44s](../../../jobs/4543/2026-10-03__15-57-02/sticky-drop-directory-bash-centos-stream10-4543) | — | — | — | — | — |
| unprivileged-service | — | — | [4m 29s](../../../jobs/4543/2026-10-03__15-57-02/unprivileged-service-bash-centos-stream10-4543) | — | — | — | — | — |
| mandatory-access-control-port | — | — | [2m 37s](../../../jobs/4543/2026-10-03__15-57-02/mandatory-access-control-port-bash-centos-stream10-4543) | — | — | — | — | — |
| kernel-module-blacklist | — | — | [2m 34s](../../../jobs/4543/2026-10-03__15-57-02/kernel-module-blacklist-bash-centos-stream10-4543) | — | — | — | — | — |
| boot-kernel-parameter | — | — | [1m 36s](../../../jobs/4543/2026-10-03__15-57-02/boot-kernel-parameter-bash-centos-stream10-4543) | — | — | — | — | — |
| mount-option-hardening | — | — | [2m 31s](../../../jobs/4543/2026-10-03__15-57-02/mount-option-hardening-bash-centos-stream10-4543) | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | [2m 45s](../../../jobs/4543/2026-10-03__15-57-02/password-complexity-policy-bash-centos-stream10-4543) | — | — | — | — | — |
| sudo-command-logging | — | — | [2m 20s](../../../jobs/4543/2026-10-03__15-57-02/sudo-command-logging-bash-centos-stream10-4543) | — | — | — | — | — |
| cron-access-control | — | — | [3m 34s](../../../jobs/4543/2026-10-03__15-57-02/cron-access-control-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | [2m 52s](../../../jobs/4543/2026-10-03__15-57-02/disk-quota-bash-centos-stream10-4543) | — | — | — | — | — |
| encrypted-volume | — | — | [15m 31s](../../../jobs/4543/2026-10-03__15-57-02/encrypted-volume-bash-centos-stream10-4543) | — | — | — | — | — |
| lvm-extend | — | — | [2m 36s](../../../jobs/4543/2026-10-03__15-57-02/lvm-extend-bash-centos-stream10-4543) | — | — | — | — | — |
| filesystem-snapshot-rollback | — | — | [4m 08s](../../../jobs/4543/2026-10-03__15-57-02/filesystem-snapshot-rollback-bash-centos-stream10-4543) | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | [2m 14s](../../../jobs/4543/2026-10-03__15-57-02/package-version-hold-bash-centos-stream10-4543) | — | — | — | — | — |
| local-package-repository | — | — | [3m 08s](../../../jobs/4543/2026-10-03__15-57-02/local-package-repository-bash-centos-stream10-4543) | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | [4m 06s](../../../jobs/4543/2026-10-03__15-57-02/certificate-rotation-bash-centos-stream10-4543) | — | — | — | — | — |
| file-integrity-baseline | — | — | [3m 41s](../../../jobs/4543/2026-10-03__15-57-02/file-integrity-baseline-bash-centos-stream10-4543) | — | — | — | — | — |
| archive-member-safety | — | — | [3m 26s](../../../jobs/4543/2026-10-03__15-57-02/archive-member-safety-bash-centos-stream10-4543) | — | — | — | — | — |
| atomic-release-publication | — | — | [3m 35s](../../../jobs/4543/2026-10-03__15-57-02/atomic-release-publication-bash-centos-stream10-4543) | — | — | — | — | — |
| batch-exclusive-lock | — | — | [3m 08s](../../../jobs/4543/2026-10-03__15-57-02/batch-exclusive-lock-bash-centos-stream10-4543) | — | — | — | — | — |
| cgi-report-execution | — | — | [3m 13s](../../../jobs/4543/2026-10-03__15-57-02/cgi-report-execution-bash-centos-stream10-4543) | — | — | — | — | — |
| child-process-reaping | — | — | [3m 03s](../../../jobs/4543/2026-10-03__15-57-02/child-process-reaping-bash-centos-stream10-4543) | — | — | — | — | — |
| chroot-web-service | — | — | [3m 21s](../../../jobs/4543/2026-10-03__15-57-02/chroot-web-service-bash-centos-stream10-4543) | — | — | — | — | — |
| cross-file-accounting-reconciliation | — | — | [1m 54s](../../../jobs/4543/2026-10-03__15-57-02/cross-file-accounting-reconciliation-bash-centos-stream10-4543) | — | — | — | — | — |
| deleted-open-file-recovery | — | — | [3m 30s](../../../jobs/4543/2026-10-03__15-57-02/deleted-open-file-recovery-bash-centos-stream10-4543) | — | — | — | — | — |
| fifo-worker-reconnection | — | — | [29m 24s](../../../jobs/4543/2026-10-03__15-57-02/fifo-worker-reconnection-bash-centos-stream10-4543) | — | — | — | — | — |
| file-descriptor-leak | — | — | [2m 31s](../../../jobs/4543/2026-10-03__15-57-02/file-descriptor-leak-bash-centos-stream10-4543) | — | — | — | — | — |
| filename-encoding-migration | — | — | [2m 09s](../../../jobs/4543/2026-10-03__15-57-02/filename-encoding-migration-bash-centos-stream10-4543) | — | — | — | — | — |
| fixed-width-import-recovery | — | — | [2m 50s](../../../jobs/4543/2026-10-03__15-57-02/fixed-width-import-recovery-bash-centos-stream10-4543) | — | — | — | — | — |
| hardlink-aware-deduplication | — | — | [2m 43s](../../../jobs/4543/2026-10-03__15-57-02/hardlink-aware-deduplication-bash-centos-stream10-4543) | — | — | — | — | — |
| incremental-archive-chain | — | — | [2m 22s](../../../jobs/4543/2026-10-03__15-57-02/incremental-archive-chain-bash-centos-stream10-4543) | — | — | — | — | — |
| inherited-directory-acls | — | — | [2m 45s](../../../jobs/4543/2026-10-03__15-57-02/inherited-directory-acls-bash-centos-stream10-4543) | — | — | — | — | — |
| inode-cache-retention | — | — | [6s](../../../jobs/4543/2026-10-03__15-57-02/inode-cache-retention-bash-centos-stream10-4543) | — | — | — | — | — |
| large-counter-overflow | — | — | [2m 59s](../../../jobs/4543/2026-10-03__15-57-02/large-counter-overflow-bash-centos-stream10-4543) | — | — | — | — | — |
| mail-filter-routing | — | — | [28m 31s](../../../jobs/4543/2026-10-03__15-57-02/mail-filter-routing-bash-centos-stream10-4543) | — | — | — | — | — |
| mail-spool-deduplication | — | — | [3m 05s](../../../jobs/4543/2026-10-03__15-57-02/mail-spool-deduplication-bash-centos-stream10-4543) | — | — | — | — | — |
| minimal-environment-job | — | — | [2m 16s](../../../jobs/4543/2026-10-03__15-57-02/minimal-environment-job-bash-centos-stream10-4543) | — | — | — | — | — |
| name-based-web-tenants | — | — | [3m 18s](../../../jobs/4543/2026-10-03__15-57-02/name-based-web-tenants-bash-centos-stream10-4543) | — | — | — | — | — |
| numeric-record-ordering | — | — | [2m 40s](../../../jobs/4543/2026-10-03__15-57-02/numeric-record-ordering-bash-centos-stream10-4543) | — | — | — | — | — |
| permanent-url-migration | — | — | [2m 45s](../../../jobs/4543/2026-10-03__15-57-02/permanent-url-migration-bash-centos-stream10-4543) | — | — | — | — | — |
| persistent-swap | — | — | [2m 40s](../../../jobs/4543/2026-10-03__15-57-02/persistent-swap-bash-centos-stream10-4543) | — | — | — | — | — |
| posix-shell-installer | — | — | [2m 13s](../../../jobs/4543/2026-10-03__15-57-02/posix-shell-installer-bash-centos-stream10-4543) | — | — | — | — | — |
| postgresql-sequence-repair | — | — | [2m 29s](../../../jobs/4543/2026-10-03__15-57-02/postgresql-sequence-repair-bash-centos-stream10-4543) | — | — | — | — | — |
| print-spool-recovery | — | — | [4m 34s](../../../jobs/4543/2026-10-03__15-57-02/print-spool-recovery-bash-centos-stream10-4543) | — | — | — | — | — |
| privacy-safe-support-export | — | — | [4m 03s](../../../jobs/4543/2026-10-03__15-57-02/privacy-safe-support-export-bash-centos-stream10-4543) | — | — | — | — | — |
| relative-symlink-relocation | — | — | [2m 36s](../../../jobs/4543/2026-10-03__15-57-02/relative-symlink-relocation-bash-centos-stream10-4543) | — | — | — | — | — |
| selective-tape-restore | — | — | [1m 43s](../../../jobs/4543/2026-10-03__15-57-02/selective-tape-restore-bash-centos-stream10-4543) | — | — | — | — | — |
| service-confinement | — | — | [7m 41s](../../../jobs/4543/2026-10-03__15-57-02/service-confinement-bash-centos-stream10-4543) | — | — | — | — | — |
| service-resource-limits | — | — | [2m 15s](../../../jobs/4543/2026-10-03__15-57-02/service-resource-limits-bash-centos-stream10-4543) | — | — | — | — | — |
| signal-driven-config-reload | — | — | [3m 38s](../../../jobs/4543/2026-10-03__15-57-02/signal-driven-config-reload-bash-centos-stream10-4543) | — | — | — | — | — |
| sparse-image-copy | — | — | [2m 46s](../../../jobs/4543/2026-10-03__15-57-02/sparse-image-copy-bash-centos-stream10-4543) | — | — | — | — | — |
| sqlite-lock-contention | — | — | [3m 46s](../../../jobs/4543/2026-10-03__15-57-02/sqlite-lock-contention-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-host-key-pinning | — | — | [1m 52s](../../../jobs/4543/2026-10-03__15-57-02/ssh-host-key-pinning-bash-centos-stream10-4543) | — | — | — | — | — |
| stale-pidfile-startup | — | — | [4m 06s](../../../jobs/4543/2026-10-03__15-57-02/stale-pidfile-startup-bash-centos-stream10-4543) | — | — | — | — | — |
| temporary-file-symlink-defense | — | — | [3m 08s](../../../jobs/4543/2026-10-03__15-57-02/temporary-file-symlink-defense-bash-centos-stream10-4543) | — | — | — | — | — |
| text-export-normalization | — | — | [2m 54s](../../../jobs/4543/2026-10-03__15-57-02/text-export-normalization-bash-centos-stream10-4543) | — | — | — | — | — |
| timezone-log-merge | — | — | [3m 29s](../../../jobs/4543/2026-10-03__15-57-02/timezone-log-merge-bash-centos-stream10-4543) | — | — | — | — | — |
| transactional-schema-upgrade | — | — | [2m 46s](../../../jobs/4543/2026-10-03__15-57-02/transactional-schema-upgrade-bash-centos-stream10-4543) | — | — | — | — | — |
| unix-socket-access-boundary | — | — | [3m 08s](../../../jobs/4543/2026-10-03__15-57-02/unix-socket-access-boundary-bash-centos-stream10-4543) | — | — | — | — | — |
| web-authentication-boundary | — | — | [3m 23s](../../../jobs/4543/2026-10-03__15-57-02/web-authentication-boundary-bash-centos-stream10-4543) | — | — | — | — | — |
| webdav-document-locks | — | — | [3m 46s](../../../jobs/4543/2026-10-03__15-57-02/webdav-document-locks-bash-centos-stream10-4543) | — | — | — | — | — |
| working-directory-independent-launch | — | — | [2m 34s](../../../jobs/4543/2026-10-03__15-57-02/working-directory-independent-launch-bash-centos-stream10-4543) | — | — | — | — | — |
| **Average** | — | — | 3m 52s | — | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 1138 ms across 100 clusters, about 0.59% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/account-resource-limits-bash-centos-stream10-4543) | — | — | — | — | — |
| application-log-rotation | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/application-log-rotation-bash-centos-stream10-4543) | — | — | — | — | — |
| custom-ca-trust | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/custom-ca-trust-bash-centos-stream10-4543) | — | — | — | — | — |
| host-firewall-baseline | — | — | [0.960](../../../jobs/4543/2026-10-03__15-57-02/host-firewall-baseline-bash-centos-stream10-4543) | — | — | — | — | — |
| kernel-network-hardening | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/kernel-network-hardening-bash-centos-stream10-4543) | — | — | — | — | — |
| repair-application-permissions | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/repair-application-permissions-bash-centos-stream10-4543) | — | — | — | — | — |
| scheduled-maintenance | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/scheduled-maintenance-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-key-only | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/ssh-key-only-bash-centos-stream10-4543) | — | — | — | — | — |
| sticky-drop-directory | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/sticky-drop-directory-bash-centos-stream10-4543) | — | — | — | — | — |
| unprivileged-service | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/unprivileged-service-bash-centos-stream10-4543) | — | — | — | — | — |
| mandatory-access-control-port | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/mandatory-access-control-port-bash-centos-stream10-4543) | — | — | — | — | — |
| kernel-module-blacklist | — | — | [0.960](../../../jobs/4543/2026-10-03__15-57-02/kernel-module-blacklist-bash-centos-stream10-4543) | — | — | — | — | — |
| boot-kernel-parameter | — | — | [0.960](../../../jobs/4543/2026-10-03__15-57-02/boot-kernel-parameter-bash-centos-stream10-4543) | — | — | — | — | — |
| mount-option-hardening | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/mount-option-hardening-bash-centos-stream10-4543) | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/password-complexity-policy-bash-centos-stream10-4543) | — | — | — | — | — |
| sudo-command-logging | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/sudo-command-logging-bash-centos-stream10-4543) | — | — | — | — | — |
| cron-access-control | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/cron-access-control-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/disk-quota-bash-centos-stream10-4543) | — | — | — | — | — |
| encrypted-volume | — | — | [0.750](../../../jobs/4543/2026-10-03__15-57-02/encrypted-volume-bash-centos-stream10-4543) | — | — | — | — | — |
| lvm-extend | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/lvm-extend-bash-centos-stream10-4543) | — | — | — | — | — |
| filesystem-snapshot-rollback | — | — | [0.910](../../../jobs/4543/2026-10-03__15-57-02/filesystem-snapshot-rollback-bash-centos-stream10-4543) | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/package-version-hold-bash-centos-stream10-4543) | — | — | — | — | — |
| local-package-repository | — | — | [0.880](../../../jobs/4543/2026-10-03__15-57-02/local-package-repository-bash-centos-stream10-4543) | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | [0.880](../../../jobs/4543/2026-10-03__15-57-02/certificate-rotation-bash-centos-stream10-4543) | — | — | — | — | — |
| file-integrity-baseline | — | — | [0.940](../../../jobs/4543/2026-10-03__15-57-02/file-integrity-baseline-bash-centos-stream10-4543) | — | — | — | — | — |
| archive-member-safety | — | — | [0.990](../../../jobs/4543/2026-10-03__15-57-02/archive-member-safety-bash-centos-stream10-4543) | — | — | — | — | — |
| atomic-release-publication | — | — | [0.960](../../../jobs/4543/2026-10-03__15-57-02/atomic-release-publication-bash-centos-stream10-4543) | — | — | — | — | — |
| batch-exclusive-lock | — | — | [0.820](../../../jobs/4543/2026-10-03__15-57-02/batch-exclusive-lock-bash-centos-stream10-4543) | — | — | — | — | — |
| cgi-report-execution | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/cgi-report-execution-bash-centos-stream10-4543) | — | — | — | — | — |
| child-process-reaping | — | — | [0.820](../../../jobs/4543/2026-10-03__15-57-02/child-process-reaping-bash-centos-stream10-4543) | — | — | — | — | — |
| chroot-web-service | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/chroot-web-service-bash-centos-stream10-4543) | — | — | — | — | — |
| cross-file-accounting-reconciliation | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/cross-file-accounting-reconciliation-bash-centos-stream10-4543) | — | — | — | — | — |
| deleted-open-file-recovery | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/deleted-open-file-recovery-bash-centos-stream10-4543) | — | — | — | — | — |
| fifo-worker-reconnection | — | — | [0.900](../../../jobs/4543/2026-10-03__15-57-02/fifo-worker-reconnection-bash-centos-stream10-4543) | — | — | — | — | — |
| file-descriptor-leak | — | — | [0.900](../../../jobs/4543/2026-10-03__15-57-02/file-descriptor-leak-bash-centos-stream10-4543) | — | — | — | — | — |
| filename-encoding-migration | — | — | [0.980](../../../jobs/4543/2026-10-03__15-57-02/filename-encoding-migration-bash-centos-stream10-4543) | — | — | — | — | — |
| fixed-width-import-recovery | — | — | [0.900](../../../jobs/4543/2026-10-03__15-57-02/fixed-width-import-recovery-bash-centos-stream10-4543) | — | — | — | — | — |
| hardlink-aware-deduplication | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/hardlink-aware-deduplication-bash-centos-stream10-4543) | — | — | — | — | — |
| incremental-archive-chain | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/incremental-archive-chain-bash-centos-stream10-4543) | — | — | — | — | — |
| inherited-directory-acls | — | — | [0.950](../../../jobs/4543/2026-10-03__15-57-02/inherited-directory-acls-bash-centos-stream10-4543) | — | — | — | — | — |
| inode-cache-retention | — | — | — | — | — | — | — | — |
| large-counter-overflow | — | — | [0.840](../../../jobs/4543/2026-10-03__15-57-02/large-counter-overflow-bash-centos-stream10-4543) | — | — | — | — | — |
| mail-filter-routing | — | — | [0.940](../../../jobs/4543/2026-10-03__15-57-02/mail-filter-routing-bash-centos-stream10-4543) | — | — | — | — | — |
| mail-spool-deduplication | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/mail-spool-deduplication-bash-centos-stream10-4543) | — | — | — | — | — |
| minimal-environment-job | — | — | [0.900](../../../jobs/4543/2026-10-03__15-57-02/minimal-environment-job-bash-centos-stream10-4543) | — | — | — | — | — |
| name-based-web-tenants | — | — | [0.860](../../../jobs/4543/2026-10-03__15-57-02/name-based-web-tenants-bash-centos-stream10-4543) | — | — | — | — | — |
| numeric-record-ordering | — | — | [0.980](../../../jobs/4543/2026-10-03__15-57-02/numeric-record-ordering-bash-centos-stream10-4543) | — | — | — | — | — |
| permanent-url-migration | — | — | [0.940](../../../jobs/4543/2026-10-03__15-57-02/permanent-url-migration-bash-centos-stream10-4543) | — | — | — | — | — |
| persistent-swap | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/persistent-swap-bash-centos-stream10-4543) | — | — | — | — | — |
| posix-shell-installer | — | — | [0.820](../../../jobs/4543/2026-10-03__15-57-02/posix-shell-installer-bash-centos-stream10-4543) | — | — | — | — | — |
| postgresql-sequence-repair | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/postgresql-sequence-repair-bash-centos-stream10-4543) | — | — | — | — | — |
| print-spool-recovery | — | — | [0.860](../../../jobs/4543/2026-10-03__15-57-02/print-spool-recovery-bash-centos-stream10-4543) | — | — | — | — | — |
| privacy-safe-support-export | — | — | [0.840](../../../jobs/4543/2026-10-03__15-57-02/privacy-safe-support-export-bash-centos-stream10-4543) | — | — | — | — | — |
| relative-symlink-relocation | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/relative-symlink-relocation-bash-centos-stream10-4543) | — | — | — | — | — |
| selective-tape-restore | — | — | [0.960](../../../jobs/4543/2026-10-03__15-57-02/selective-tape-restore-bash-centos-stream10-4543) | — | — | — | — | — |
| service-confinement | — | — | [0.720](../../../jobs/4543/2026-10-03__15-57-02/service-confinement-bash-centos-stream10-4543) | — | — | — | — | — |
| service-resource-limits | — | — | [0.960](../../../jobs/4543/2026-10-03__15-57-02/service-resource-limits-bash-centos-stream10-4543) | — | — | — | — | — |
| signal-driven-config-reload | — | — | [0.840](../../../jobs/4543/2026-10-03__15-57-02/signal-driven-config-reload-bash-centos-stream10-4543) | — | — | — | — | — |
| sparse-image-copy | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/sparse-image-copy-bash-centos-stream10-4543) | — | — | — | — | — |
| sqlite-lock-contention | — | — | [0.820](../../../jobs/4543/2026-10-03__15-57-02/sqlite-lock-contention-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-host-key-pinning | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/ssh-host-key-pinning-bash-centos-stream10-4543) | — | — | — | — | — |
| stale-pidfile-startup | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/stale-pidfile-startup-bash-centos-stream10-4543) | — | — | — | — | — |
| temporary-file-symlink-defense | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/temporary-file-symlink-defense-bash-centos-stream10-4543) | — | — | — | — | — |
| text-export-normalization | — | — | [0.880](../../../jobs/4543/2026-10-03__15-57-02/text-export-normalization-bash-centos-stream10-4543) | — | — | — | — | — |
| timezone-log-merge | — | — | [0.920](../../../jobs/4543/2026-10-03__15-57-02/timezone-log-merge-bash-centos-stream10-4543) | — | — | — | — | — |
| transactional-schema-upgrade | — | — | [0.940](../../../jobs/4543/2026-10-03__15-57-02/transactional-schema-upgrade-bash-centos-stream10-4543) | — | — | — | — | — |
| unix-socket-access-boundary | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/unix-socket-access-boundary-bash-centos-stream10-4543) | — | — | — | — | — |
| web-authentication-boundary | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/web-authentication-boundary-bash-centos-stream10-4543) | — | — | — | — | — |
| webdav-document-locks | — | — | [0.960](../../../jobs/4543/2026-10-03__15-57-02/webdav-document-locks-bash-centos-stream10-4543) | — | — | — | — | — |
| working-directory-independent-launch | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/working-directory-independent-launch-bash-centos-stream10-4543) | — | — | — | — | — |
| **Average** | — | — | 0.944 | — | — | — | — | — |
