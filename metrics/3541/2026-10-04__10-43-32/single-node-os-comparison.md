# single-node-os-comparison: command execution summary

Scope: `3541/2026-10-04__10-43-32`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | [9/2](../../../jobs/3541/2026-10-04__10-43-32/account-resource-limits-bash-ubuntu16-3541) | — |
| application-log-rotation | — | — | — | — | — | — | [11/11](../../../jobs/3541/2026-10-04__10-43-32/application-log-rotation-bash-ubuntu16-3541) | — |
| custom-ca-trust | — | — | — | — | — | — | [7/1](../../../jobs/3541/2026-10-04__10-43-32/custom-ca-trust-bash-ubuntu16-3541) | — |
| host-firewall-baseline | — | — | — | — | — | — | [18/5](../../../jobs/3541/2026-10-04__10-43-32/host-firewall-baseline-bash-ubuntu16-3541) | — |
| kernel-network-hardening | — | — | — | — | — | — | [8/1](../../../jobs/3541/2026-10-04__10-43-32/kernel-network-hardening-bash-ubuntu16-3541) | — |
| repair-application-permissions | — | — | — | — | — | — | [7/11](../../../jobs/3541/2026-10-04__10-43-32/repair-application-permissions-bash-ubuntu16-3541) | — |
| scheduled-maintenance | — | — | — | — | — | — | [9/4](../../../jobs/3541/2026-10-04__10-43-32/scheduled-maintenance-bash-ubuntu16-3541) | — |
| ssh-key-only | — | — | — | — | — | — | [7/2](../../../jobs/3541/2026-10-04__10-43-32/ssh-key-only-bash-ubuntu16-3541) | — |
| sticky-drop-directory | — | — | — | — | — | — | [8/1](../../../jobs/3541/2026-10-04__10-43-32/sticky-drop-directory-bash-ubuntu16-3541) | — |
| unprivileged-service | — | — | — | — | — | — | [9/2](../../../jobs/3541/2026-10-04__10-43-32/unprivileged-service-bash-ubuntu16-3541) | — |
| mandatory-access-control-port | — | — | — | — | — | — | [14/3](../../../jobs/3541/2026-10-04__10-43-32/mandatory-access-control-port-bash-ubuntu16-3541) | — |
| kernel-module-blacklist | — | — | — | — | — | — | [7/1](../../../jobs/3541/2026-10-04__10-43-32/kernel-module-blacklist-bash-ubuntu16-3541) | — |
| boot-kernel-parameter | — | — | — | — | — | — | [14/1](../../../jobs/3541/2026-10-04__10-43-32/boot-kernel-parameter-bash-ubuntu16-3541) | — |
| mount-option-hardening | — | — | — | — | — | — | [9/5](../../../jobs/3541/2026-10-04__10-43-32/mount-option-hardening-bash-ubuntu16-3541) | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | [16/2](../../../jobs/3541/2026-10-04__10-43-32/password-complexity-policy-bash-ubuntu16-3541) | — |
| sudo-command-logging | — | — | — | — | — | — | [9/2](../../../jobs/3541/2026-10-04__10-43-32/sudo-command-logging-bash-ubuntu16-3541) | — |
| cron-access-control | — | — | — | — | — | — | [11/2](../../../jobs/3541/2026-10-04__10-43-32/cron-access-control-bash-ubuntu16-3541) | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | [27/6](../../../jobs/3541/2026-10-04__10-43-32/disk-quota-bash-ubuntu16-3541) | — |
| encrypted-volume | — | — | — | — | — | — | [15/9](../../../jobs/3541/2026-10-04__10-43-32/encrypted-volume-bash-ubuntu16-3541) | — |
| lvm-extend | — | — | — | — | — | — | [11/1](../../../jobs/3541/2026-10-04__10-43-32/lvm-extend-bash-ubuntu16-3541) | — |
| filesystem-snapshot-rollback | — | — | — | — | — | — | [14/3](../../../jobs/3541/2026-10-04__10-43-32/filesystem-snapshot-rollback-bash-ubuntu16-3541) | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | [8/4](../../../jobs/3541/2026-10-04__10-43-32/package-version-hold-bash-ubuntu16-3541) | — |
| local-package-repository | — | — | — | — | — | — | [13/2](../../../jobs/3541/2026-10-04__10-43-32/local-package-repository-bash-ubuntu16-3541) | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | [20/2](../../../jobs/3541/2026-10-04__10-43-32/certificate-rotation-bash-ubuntu16-3541) | — |
| file-integrity-baseline | — | — | — | — | — | — | [10/3](../../../jobs/3541/2026-10-04__10-43-32/file-integrity-baseline-bash-ubuntu16-3541) | — |
| archive-member-safety | — | — | — | — | — | — | [12/4](../../../jobs/3541/2026-10-04__10-43-32/archive-member-safety-bash-ubuntu16-3541) | — |
| atomic-release-publication | — | — | — | — | — | — | [10/3](../../../jobs/3541/2026-10-04__10-43-32/atomic-release-publication-bash-ubuntu16-3541) | — |
| batch-exclusive-lock | — | — | — | — | — | — | [12/1](../../../jobs/3541/2026-10-04__10-43-32/batch-exclusive-lock-bash-ubuntu16-3541) | — |
| cgi-report-execution | — | — | — | — | — | — | [9/3](../../../jobs/3541/2026-10-04__10-43-32/cgi-report-execution-bash-ubuntu16-3541) | — |
| child-process-reaping | — | — | — | — | — | — | [11/2](../../../jobs/3541/2026-10-04__10-43-32/child-process-reaping-bash-ubuntu16-3541) | — |
| chroot-web-service | — | — | — | — | — | — | [9/8](../../../jobs/3541/2026-10-04__10-43-32/chroot-web-service-bash-ubuntu16-3541) | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | [10/4](../../../jobs/3541/2026-10-04__10-43-32/cross-file-accounting-reconciliation-bash-ubuntu16-3541) | — |
| deleted-open-file-recovery | — | — | — | — | — | — | [12/1](../../../jobs/3541/2026-10-04__10-43-32/deleted-open-file-recovery-bash-ubuntu16-3541) | — |
| fifo-worker-reconnection | — | — | — | — | — | — | [18/2](../../../jobs/3541/2026-10-04__10-43-32/fifo-worker-reconnection-bash-ubuntu16-3541) | — |
| file-descriptor-leak | — | — | — | — | — | — | [10/2](../../../jobs/3541/2026-10-04__10-43-32/file-descriptor-leak-bash-ubuntu16-3541) | — |
| filename-encoding-migration | — | — | — | — | — | — | [7/10](../../../jobs/3541/2026-10-04__10-43-32/filename-encoding-migration-bash-ubuntu16-3541) | — |
| fixed-width-import-recovery | — | — | — | — | — | — | [10/1](../../../jobs/3541/2026-10-04__10-43-32/fixed-width-import-recovery-bash-ubuntu16-3541) | — |
| hardlink-aware-deduplication | — | — | — | — | — | — | [11/1](../../../jobs/3541/2026-10-04__10-43-32/hardlink-aware-deduplication-bash-ubuntu16-3541) | — |
| incremental-archive-chain | — | — | — | — | — | — | [12/2](../../../jobs/3541/2026-10-04__10-43-32/incremental-archive-chain-bash-ubuntu16-3541) | — |
| inherited-directory-acls | — | — | — | — | — | — | [8/3](../../../jobs/3541/2026-10-04__10-43-32/inherited-directory-acls-bash-ubuntu16-3541) | — |
| inode-cache-retention | — | — | — | — | — | — | [0/0](../../../jobs/3541/2026-10-04__10-43-32/inode-cache-retention-bash-ubuntu16-3541) | — |
| large-counter-overflow | — | — | — | — | — | — | [10/12](../../../jobs/3541/2026-10-04__10-43-32/large-counter-overflow-bash-ubuntu16-3541) | — |
| mail-filter-routing | — | — | — | — | — | — | [10/2](../../../jobs/3541/2026-10-04__10-43-32/mail-filter-routing-bash-ubuntu16-3541) | — |
| mail-spool-deduplication | — | — | — | — | — | — | [0/0](../../../jobs/3541/2026-10-04__10-43-32/mail-spool-deduplication-bash-ubuntu16-3541) | — |
| minimal-environment-job | — | — | — | — | — | — | [9/0](../../../jobs/3541/2026-10-04__10-43-32/minimal-environment-job-bash-ubuntu16-3541) | — |
| name-based-web-tenants | — | — | — | — | — | — | [10/2](../../../jobs/3541/2026-10-04__10-43-32/name-based-web-tenants-bash-ubuntu16-3541) | — |
| numeric-record-ordering | — | — | — | — | — | — | [11/1](../../../jobs/3541/2026-10-04__10-43-32/numeric-record-ordering-bash-ubuntu16-3541) | — |
| permanent-url-migration | — | — | — | — | — | — | [11/1](../../../jobs/3541/2026-10-04__10-43-32/permanent-url-migration-bash-ubuntu16-3541) | — |
| persistent-swap | — | — | — | — | — | — | [10/3](../../../jobs/3541/2026-10-04__10-43-32/persistent-swap-bash-ubuntu16-3541) | — |
| posix-shell-installer | — | — | — | — | — | — | [12/7](../../../jobs/3541/2026-10-04__10-43-32/posix-shell-installer-bash-ubuntu16-3541) | — |
| postgresql-sequence-repair | — | — | — | — | — | — | [20/1](../../../jobs/3541/2026-10-04__10-43-32/postgresql-sequence-repair-bash-ubuntu16-3541) | — |
| print-spool-recovery | — | — | — | — | — | — | [11/4](../../../jobs/3541/2026-10-04__10-43-32/print-spool-recovery-bash-ubuntu16-3541) | — |
| privacy-safe-support-export | — | — | — | — | — | — | [12/4](../../../jobs/3541/2026-10-04__10-43-32/privacy-safe-support-export-bash-ubuntu16-3541) | — |
| relative-symlink-relocation | — | — | — | — | — | — | [11/4](../../../jobs/3541/2026-10-04__10-43-32/relative-symlink-relocation-bash-ubuntu16-3541) | — |
| selective-tape-restore | — | — | — | — | — | — | [7/6](../../../jobs/3541/2026-10-04__10-43-32/selective-tape-restore-bash-ubuntu16-3541) | — |
| service-confinement | — | — | — | — | — | — | [10/5](../../../jobs/3541/2026-10-04__10-43-32/service-confinement-bash-ubuntu16-3541) | — |
| service-resource-limits | — | — | — | — | — | — | [13/43](../../../jobs/3541/2026-10-04__10-43-32/service-resource-limits-bash-ubuntu16-3541) | — |
| signal-driven-config-reload | — | — | — | — | — | — | [12/4](../../../jobs/3541/2026-10-04__10-43-32/signal-driven-config-reload-bash-ubuntu16-3541) | — |
| sparse-image-copy | — | — | — | — | — | — | [13/3](../../../jobs/3541/2026-10-04__10-43-32/sparse-image-copy-bash-ubuntu16-3541) | — |
| sqlite-lock-contention | — | — | — | — | — | — | [12/4](../../../jobs/3541/2026-10-04__10-43-32/sqlite-lock-contention-bash-ubuntu16-3541) | — |
| ssh-host-key-pinning | — | — | — | — | — | — | [14/12](../../../jobs/3541/2026-10-04__10-43-32/ssh-host-key-pinning-bash-ubuntu16-3541) | — |
| stale-pidfile-startup | — | — | — | — | — | — | [12/2](../../../jobs/3541/2026-10-04__10-43-32/stale-pidfile-startup-bash-ubuntu16-3541) | — |
| temporary-file-symlink-defense | — | — | — | — | — | — | [12/19](../../../jobs/3541/2026-10-04__10-43-32/temporary-file-symlink-defense-bash-ubuntu16-3541) | — |
| text-export-normalization | — | — | — | — | — | — | [8/3](../../../jobs/3541/2026-10-04__10-43-32/text-export-normalization-bash-ubuntu16-3541) | — |
| timezone-log-merge | — | — | — | — | — | — | [13/3](../../../jobs/3541/2026-10-04__10-43-32/timezone-log-merge-bash-ubuntu16-3541) | — |
| transactional-schema-upgrade | — | — | — | — | — | — | [12/6](../../../jobs/3541/2026-10-04__10-43-32/transactional-schema-upgrade-bash-ubuntu16-3541) | — |
| unix-socket-access-boundary | — | — | — | — | — | — | [10/5](../../../jobs/3541/2026-10-04__10-43-32/unix-socket-access-boundary-bash-ubuntu16-3541) | — |
| web-authentication-boundary | — | — | — | — | — | — | [9/10](../../../jobs/3541/2026-10-04__10-43-32/web-authentication-boundary-bash-ubuntu16-3541) | — |
| webdav-document-locks | — | — | — | — | — | — | [15/4](../../../jobs/3541/2026-10-04__10-43-32/webdav-document-locks-bash-ubuntu16-3541) | — |
| working-directory-independent-launch | — | — | — | — | — | — | [10/2](../../../jobs/3541/2026-10-04__10-43-32/working-directory-independent-launch-bash-ubuntu16-3541) | — |
| **Average** | — | — | — | — | — | — | 11.0/4.4 | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | [2m 28s](../../../jobs/3541/2026-10-04__10-43-32/account-resource-limits-bash-ubuntu16-3541) | — |
| application-log-rotation | — | — | — | — | — | — | [4m 06s](../../../jobs/3541/2026-10-04__10-43-32/application-log-rotation-bash-ubuntu16-3541) | — |
| custom-ca-trust | — | — | — | — | — | — | [2m 23s](../../../jobs/3541/2026-10-04__10-43-32/custom-ca-trust-bash-ubuntu16-3541) | — |
| host-firewall-baseline | — | — | — | — | — | — | [4m 55s](../../../jobs/3541/2026-10-04__10-43-32/host-firewall-baseline-bash-ubuntu16-3541) | — |
| kernel-network-hardening | — | — | — | — | — | — | [2m 26s](../../../jobs/3541/2026-10-04__10-43-32/kernel-network-hardening-bash-ubuntu16-3541) | — |
| repair-application-permissions | — | — | — | — | — | — | [4m 13s](../../../jobs/3541/2026-10-04__10-43-32/repair-application-permissions-bash-ubuntu16-3541) | — |
| scheduled-maintenance | — | — | — | — | — | — | [3m 04s](../../../jobs/3541/2026-10-04__10-43-32/scheduled-maintenance-bash-ubuntu16-3541) | — |
| ssh-key-only | — | — | — | — | — | — | [2m 13s](../../../jobs/3541/2026-10-04__10-43-32/ssh-key-only-bash-ubuntu16-3541) | — |
| sticky-drop-directory | — | — | — | — | — | — | [2m 33s](../../../jobs/3541/2026-10-04__10-43-32/sticky-drop-directory-bash-ubuntu16-3541) | — |
| unprivileged-service | — | — | — | — | — | — | [4m 36s](../../../jobs/3541/2026-10-04__10-43-32/unprivileged-service-bash-ubuntu16-3541) | — |
| mandatory-access-control-port | — | — | — | — | — | — | [4m 09s](../../../jobs/3541/2026-10-04__10-43-32/mandatory-access-control-port-bash-ubuntu16-3541) | — |
| kernel-module-blacklist | — | — | — | — | — | — | [1m 56s](../../../jobs/3541/2026-10-04__10-43-32/kernel-module-blacklist-bash-ubuntu16-3541) | — |
| boot-kernel-parameter | — | — | — | — | — | — | [2m 39s](../../../jobs/3541/2026-10-04__10-43-32/boot-kernel-parameter-bash-ubuntu16-3541) | — |
| mount-option-hardening | — | — | — | — | — | — | [4m 20s](../../../jobs/3541/2026-10-04__10-43-32/mount-option-hardening-bash-ubuntu16-3541) | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | [4m 18s](../../../jobs/3541/2026-10-04__10-43-32/password-complexity-policy-bash-ubuntu16-3541) | — |
| sudo-command-logging | — | — | — | — | — | — | [2m 43s](../../../jobs/3541/2026-10-04__10-43-32/sudo-command-logging-bash-ubuntu16-3541) | — |
| cron-access-control | — | — | — | — | — | — | [2m 32s](../../../jobs/3541/2026-10-04__10-43-32/cron-access-control-bash-ubuntu16-3541) | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | [5m 35s](../../../jobs/3541/2026-10-04__10-43-32/disk-quota-bash-ubuntu16-3541) | — |
| encrypted-volume | — | — | — | — | — | — | [4m 39s](../../../jobs/3541/2026-10-04__10-43-32/encrypted-volume-bash-ubuntu16-3541) | — |
| lvm-extend | — | — | — | — | — | — | [3m 06s](../../../jobs/3541/2026-10-04__10-43-32/lvm-extend-bash-ubuntu16-3541) | — |
| filesystem-snapshot-rollback | — | — | — | — | — | — | [3m 59s](../../../jobs/3541/2026-10-04__10-43-32/filesystem-snapshot-rollback-bash-ubuntu16-3541) | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | [3m 23s](../../../jobs/3541/2026-10-04__10-43-32/package-version-hold-bash-ubuntu16-3541) | — |
| local-package-repository | — | — | — | — | — | — | [4m 00s](../../../jobs/3541/2026-10-04__10-43-32/local-package-repository-bash-ubuntu16-3541) | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | [5m 20s](../../../jobs/3541/2026-10-04__10-43-32/certificate-rotation-bash-ubuntu16-3541) | — |
| file-integrity-baseline | — | — | — | — | — | — | [4m 18s](../../../jobs/3541/2026-10-04__10-43-32/file-integrity-baseline-bash-ubuntu16-3541) | — |
| archive-member-safety | — | — | — | — | — | — | [6m 35s](../../../jobs/3541/2026-10-04__10-43-32/archive-member-safety-bash-ubuntu16-3541) | — |
| atomic-release-publication | — | — | — | — | — | — | [3m 47s](../../../jobs/3541/2026-10-04__10-43-32/atomic-release-publication-bash-ubuntu16-3541) | — |
| batch-exclusive-lock | — | — | — | — | — | — | [3m 48s](../../../jobs/3541/2026-10-04__10-43-32/batch-exclusive-lock-bash-ubuntu16-3541) | — |
| cgi-report-execution | — | — | — | — | — | — | [3m 09s](../../../jobs/3541/2026-10-04__10-43-32/cgi-report-execution-bash-ubuntu16-3541) | — |
| child-process-reaping | — | — | — | — | — | — | [4m 08s](../../../jobs/3541/2026-10-04__10-43-32/child-process-reaping-bash-ubuntu16-3541) | — |
| chroot-web-service | — | — | — | — | — | — | [4m 29s](../../../jobs/3541/2026-10-04__10-43-32/chroot-web-service-bash-ubuntu16-3541) | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | [3m 22s](../../../jobs/3541/2026-10-04__10-43-32/cross-file-accounting-reconciliation-bash-ubuntu16-3541) | — |
| deleted-open-file-recovery | — | — | — | — | — | — | [3m 57s](../../../jobs/3541/2026-10-04__10-43-32/deleted-open-file-recovery-bash-ubuntu16-3541) | — |
| fifo-worker-reconnection | — | — | — | — | — | — | [5m 06s](../../../jobs/3541/2026-10-04__10-43-32/fifo-worker-reconnection-bash-ubuntu16-3541) | — |
| file-descriptor-leak | — | — | — | — | — | — | [2m 52s](../../../jobs/3541/2026-10-04__10-43-32/file-descriptor-leak-bash-ubuntu16-3541) | — |
| filename-encoding-migration | — | — | — | — | — | — | [4m 38s](../../../jobs/3541/2026-10-04__10-43-32/filename-encoding-migration-bash-ubuntu16-3541) | — |
| fixed-width-import-recovery | — | — | — | — | — | — | [3m 18s](../../../jobs/3541/2026-10-04__10-43-32/fixed-width-import-recovery-bash-ubuntu16-3541) | — |
| hardlink-aware-deduplication | — | — | — | — | — | — | [3m 24s](../../../jobs/3541/2026-10-04__10-43-32/hardlink-aware-deduplication-bash-ubuntu16-3541) | — |
| incremental-archive-chain | — | — | — | — | — | — | [3m 07s](../../../jobs/3541/2026-10-04__10-43-32/incremental-archive-chain-bash-ubuntu16-3541) | — |
| inherited-directory-acls | — | — | — | — | — | — | [2m 56s](../../../jobs/3541/2026-10-04__10-43-32/inherited-directory-acls-bash-ubuntu16-3541) | — |
| inode-cache-retention | — | — | — | — | — | — | [14s](../../../jobs/3541/2026-10-04__10-43-32/inode-cache-retention-bash-ubuntu16-3541) | — |
| large-counter-overflow | — | — | — | — | — | — | [4m 03s](../../../jobs/3541/2026-10-04__10-43-32/large-counter-overflow-bash-ubuntu16-3541) | — |
| mail-filter-routing | — | — | — | — | — | — | [3m 19s](../../../jobs/3541/2026-10-04__10-43-32/mail-filter-routing-bash-ubuntu16-3541) | — |
| mail-spool-deduplication | — | — | — | — | — | — | [6m 12s](../../../jobs/3541/2026-10-04__10-43-32/mail-spool-deduplication-bash-ubuntu16-3541) | — |
| minimal-environment-job | — | — | — | — | — | — | [2m 13s](../../../jobs/3541/2026-10-04__10-43-32/minimal-environment-job-bash-ubuntu16-3541) | — |
| name-based-web-tenants | — | — | — | — | — | — | [2m 30s](../../../jobs/3541/2026-10-04__10-43-32/name-based-web-tenants-bash-ubuntu16-3541) | — |
| numeric-record-ordering | — | — | — | — | — | — | [3m 24s](../../../jobs/3541/2026-10-04__10-43-32/numeric-record-ordering-bash-ubuntu16-3541) | — |
| permanent-url-migration | — | — | — | — | — | — | [2m 38s](../../../jobs/3541/2026-10-04__10-43-32/permanent-url-migration-bash-ubuntu16-3541) | — |
| persistent-swap | — | — | — | — | — | — | [2m 41s](../../../jobs/3541/2026-10-04__10-43-32/persistent-swap-bash-ubuntu16-3541) | — |
| posix-shell-installer | — | — | — | — | — | — | [4m 11s](../../../jobs/3541/2026-10-04__10-43-32/posix-shell-installer-bash-ubuntu16-3541) | — |
| postgresql-sequence-repair | — | — | — | — | — | — | [4m 28s](../../../jobs/3541/2026-10-04__10-43-32/postgresql-sequence-repair-bash-ubuntu16-3541) | — |
| print-spool-recovery | — | — | — | — | — | — | [5m 30s](../../../jobs/3541/2026-10-04__10-43-32/print-spool-recovery-bash-ubuntu16-3541) | — |
| privacy-safe-support-export | — | — | — | — | — | — | [5m 38s](../../../jobs/3541/2026-10-04__10-43-32/privacy-safe-support-export-bash-ubuntu16-3541) | — |
| relative-symlink-relocation | — | — | — | — | — | — | [3m 15s](../../../jobs/3541/2026-10-04__10-43-32/relative-symlink-relocation-bash-ubuntu16-3541) | — |
| selective-tape-restore | — | — | — | — | — | — | [3m 20s](../../../jobs/3541/2026-10-04__10-43-32/selective-tape-restore-bash-ubuntu16-3541) | — |
| service-confinement | — | — | — | — | — | — | [4m 35s](../../../jobs/3541/2026-10-04__10-43-32/service-confinement-bash-ubuntu16-3541) | — |
| service-resource-limits | — | — | — | — | — | — | [5m 05s](../../../jobs/3541/2026-10-04__10-43-32/service-resource-limits-bash-ubuntu16-3541) | — |
| signal-driven-config-reload | — | — | — | — | — | — | [4m 18s](../../../jobs/3541/2026-10-04__10-43-32/signal-driven-config-reload-bash-ubuntu16-3541) | — |
| sparse-image-copy | — | — | — | — | — | — | [3m 30s](../../../jobs/3541/2026-10-04__10-43-32/sparse-image-copy-bash-ubuntu16-3541) | — |
| sqlite-lock-contention | — | — | — | — | — | — | [30m 06s](../../../jobs/3541/2026-10-04__10-43-32/sqlite-lock-contention-bash-ubuntu16-3541) | — |
| ssh-host-key-pinning | — | — | — | — | — | — | [4m 38s](../../../jobs/3541/2026-10-04__10-43-32/ssh-host-key-pinning-bash-ubuntu16-3541) | — |
| stale-pidfile-startup | — | — | — | — | — | — | [4m 38s](../../../jobs/3541/2026-10-04__10-43-32/stale-pidfile-startup-bash-ubuntu16-3541) | — |
| temporary-file-symlink-defense | — | — | — | — | — | — | [5m 03s](../../../jobs/3541/2026-10-04__10-43-32/temporary-file-symlink-defense-bash-ubuntu16-3541) | — |
| text-export-normalization | — | — | — | — | — | — | [3m 47s](../../../jobs/3541/2026-10-04__10-43-32/text-export-normalization-bash-ubuntu16-3541) | — |
| timezone-log-merge | — | — | — | — | — | — | [3m 45s](../../../jobs/3541/2026-10-04__10-43-32/timezone-log-merge-bash-ubuntu16-3541) | — |
| transactional-schema-upgrade | — | — | — | — | — | — | [4m 22s](../../../jobs/3541/2026-10-04__10-43-32/transactional-schema-upgrade-bash-ubuntu16-3541) | — |
| unix-socket-access-boundary | — | — | — | — | — | — | [3m 58s](../../../jobs/3541/2026-10-04__10-43-32/unix-socket-access-boundary-bash-ubuntu16-3541) | — |
| web-authentication-boundary | — | — | — | — | — | — | [4m 54s](../../../jobs/3541/2026-10-04__10-43-32/web-authentication-boundary-bash-ubuntu16-3541) | — |
| webdav-document-locks | — | — | — | — | — | — | [4m 29s](../../../jobs/3541/2026-10-04__10-43-32/webdav-document-locks-bash-ubuntu16-3541) | — |
| working-directory-independent-launch | — | — | — | — | — | — | [3m 02s](../../../jobs/3541/2026-10-04__10-43-32/working-directory-independent-launch-bash-ubuntu16-3541) | — |
| **Average** | — | — | — | — | — | — | 4m 11s | — |

Cluster provisioning is not a meaningful part of these times: median 732 ms across 100 clusters, about 0.27% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/account-resource-limits-bash-ubuntu16-3541) | — |
| application-log-rotation | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/application-log-rotation-bash-ubuntu16-3541) | — |
| custom-ca-trust | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/custom-ca-trust-bash-ubuntu16-3541) | — |
| host-firewall-baseline | — | — | — | — | — | — | [0.960](../../../jobs/3541/2026-10-04__10-43-32/host-firewall-baseline-bash-ubuntu16-3541) | — |
| kernel-network-hardening | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/kernel-network-hardening-bash-ubuntu16-3541) | — |
| repair-application-permissions | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/repair-application-permissions-bash-ubuntu16-3541) | — |
| scheduled-maintenance | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/scheduled-maintenance-bash-ubuntu16-3541) | — |
| ssh-key-only | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/ssh-key-only-bash-ubuntu16-3541) | — |
| sticky-drop-directory | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/sticky-drop-directory-bash-ubuntu16-3541) | — |
| unprivileged-service | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/unprivileged-service-bash-ubuntu16-3541) | — |
| mandatory-access-control-port | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/mandatory-access-control-port-bash-ubuntu16-3541) | — |
| kernel-module-blacklist | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/kernel-module-blacklist-bash-ubuntu16-3541) | — |
| boot-kernel-parameter | — | — | — | — | — | — | [0.950](../../../jobs/3541/2026-10-04__10-43-32/boot-kernel-parameter-bash-ubuntu16-3541) | — |
| mount-option-hardening | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/mount-option-hardening-bash-ubuntu16-3541) | — |
| service-sandboxing | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/password-complexity-policy-bash-ubuntu16-3541) | — |
| sudo-command-logging | — | — | — | — | — | — | [0.940](../../../jobs/3541/2026-10-04__10-43-32/sudo-command-logging-bash-ubuntu16-3541) | — |
| cron-access-control | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/cron-access-control-bash-ubuntu16-3541) | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/disk-quota-bash-ubuntu16-3541) | — |
| encrypted-volume | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/encrypted-volume-bash-ubuntu16-3541) | — |
| lvm-extend | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/lvm-extend-bash-ubuntu16-3541) | — |
| filesystem-snapshot-rollback | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/filesystem-snapshot-rollback-bash-ubuntu16-3541) | — |
| zram-swap | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/package-version-hold-bash-ubuntu16-3541) | — |
| local-package-repository | — | — | — | — | — | — | [0.960](../../../jobs/3541/2026-10-04__10-43-32/local-package-repository-bash-ubuntu16-3541) | — |
| oom-protection | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/certificate-rotation-bash-ubuntu16-3541) | — |
| file-integrity-baseline | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/file-integrity-baseline-bash-ubuntu16-3541) | — |
| archive-member-safety | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/archive-member-safety-bash-ubuntu16-3541) | — |
| atomic-release-publication | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/atomic-release-publication-bash-ubuntu16-3541) | — |
| batch-exclusive-lock | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/batch-exclusive-lock-bash-ubuntu16-3541) | — |
| cgi-report-execution | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/cgi-report-execution-bash-ubuntu16-3541) | — |
| child-process-reaping | — | — | — | — | — | — | [0.960](../../../jobs/3541/2026-10-04__10-43-32/child-process-reaping-bash-ubuntu16-3541) | — |
| chroot-web-service | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/chroot-web-service-bash-ubuntu16-3541) | — |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/cross-file-accounting-reconciliation-bash-ubuntu16-3541) | — |
| deleted-open-file-recovery | — | — | — | — | — | — | [0.940](../../../jobs/3541/2026-10-04__10-43-32/deleted-open-file-recovery-bash-ubuntu16-3541) | — |
| fifo-worker-reconnection | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/fifo-worker-reconnection-bash-ubuntu16-3541) | — |
| file-descriptor-leak | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/file-descriptor-leak-bash-ubuntu16-3541) | — |
| filename-encoding-migration | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/filename-encoding-migration-bash-ubuntu16-3541) | — |
| fixed-width-import-recovery | — | — | — | — | — | — | [0.910](../../../jobs/3541/2026-10-04__10-43-32/fixed-width-import-recovery-bash-ubuntu16-3541) | — |
| hardlink-aware-deduplication | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/hardlink-aware-deduplication-bash-ubuntu16-3541) | — |
| incremental-archive-chain | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/incremental-archive-chain-bash-ubuntu16-3541) | — |
| inherited-directory-acls | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/inherited-directory-acls-bash-ubuntu16-3541) | — |
| inode-cache-retention | — | — | — | — | — | — | — | — |
| large-counter-overflow | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/large-counter-overflow-bash-ubuntu16-3541) | — |
| mail-filter-routing | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/mail-filter-routing-bash-ubuntu16-3541) | — |
| mail-spool-deduplication | — | — | — | — | — | — | — | — |
| minimal-environment-job | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/minimal-environment-job-bash-ubuntu16-3541) | — |
| name-based-web-tenants | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/name-based-web-tenants-bash-ubuntu16-3541) | — |
| numeric-record-ordering | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/numeric-record-ordering-bash-ubuntu16-3541) | — |
| permanent-url-migration | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/permanent-url-migration-bash-ubuntu16-3541) | — |
| persistent-swap | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/persistent-swap-bash-ubuntu16-3541) | — |
| posix-shell-installer | — | — | — | — | — | — | [0.950](../../../jobs/3541/2026-10-04__10-43-32/posix-shell-installer-bash-ubuntu16-3541) | — |
| postgresql-sequence-repair | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/postgresql-sequence-repair-bash-ubuntu16-3541) | — |
| print-spool-recovery | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/print-spool-recovery-bash-ubuntu16-3541) | — |
| privacy-safe-support-export | — | — | — | — | — | — | [0.900](../../../jobs/3541/2026-10-04__10-43-32/privacy-safe-support-export-bash-ubuntu16-3541) | — |
| relative-symlink-relocation | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/relative-symlink-relocation-bash-ubuntu16-3541) | — |
| selective-tape-restore | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/selective-tape-restore-bash-ubuntu16-3541) | — |
| service-confinement | — | — | — | — | — | — | [0.920](../../../jobs/3541/2026-10-04__10-43-32/service-confinement-bash-ubuntu16-3541) | — |
| service-resource-limits | — | — | — | — | — | — | [0.990](../../../jobs/3541/2026-10-04__10-43-32/service-resource-limits-bash-ubuntu16-3541) | — |
| signal-driven-config-reload | — | — | — | — | — | — | [0.960](../../../jobs/3541/2026-10-04__10-43-32/signal-driven-config-reload-bash-ubuntu16-3541) | — |
| sparse-image-copy | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/sparse-image-copy-bash-ubuntu16-3541) | — |
| sqlite-lock-contention | — | — | — | — | — | — | [0.820](../../../jobs/3541/2026-10-04__10-43-32/sqlite-lock-contention-bash-ubuntu16-3541) | — |
| ssh-host-key-pinning | — | — | — | — | — | — | [0.960](../../../jobs/3541/2026-10-04__10-43-32/ssh-host-key-pinning-bash-ubuntu16-3541) | — |
| stale-pidfile-startup | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/stale-pidfile-startup-bash-ubuntu16-3541) | — |
| temporary-file-symlink-defense | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/temporary-file-symlink-defense-bash-ubuntu16-3541) | — |
| text-export-normalization | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/text-export-normalization-bash-ubuntu16-3541) | — |
| timezone-log-merge | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/timezone-log-merge-bash-ubuntu16-3541) | — |
| transactional-schema-upgrade | — | — | — | — | — | — | [0.950](../../../jobs/3541/2026-10-04__10-43-32/transactional-schema-upgrade-bash-ubuntu16-3541) | — |
| unix-socket-access-boundary | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/unix-socket-access-boundary-bash-ubuntu16-3541) | — |
| web-authentication-boundary | — | — | — | — | — | — | [0.990](../../../jobs/3541/2026-10-04__10-43-32/web-authentication-boundary-bash-ubuntu16-3541) | — |
| webdav-document-locks | — | — | — | — | — | — | [0.900](../../../jobs/3541/2026-10-04__10-43-32/webdav-document-locks-bash-ubuntu16-3541) | — |
| working-directory-independent-launch | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/working-directory-independent-launch-bash-ubuntu16-3541) | — |
| **Average** | — | — | — | — | — | — | 0.979 | — |
