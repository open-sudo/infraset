# single-node-os-comparison: command execution summary

Scope: `8220/2026-10-03__01-23-07`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — | — |
| application-log-rotation | — | — | — | — | — | — | — | — | — |
| custom-ca-trust | — | — | — | — | — | — | — | — | — |
| host-firewall-baseline | — | — | — | — | — | — | — | — | — |
| kernel-network-hardening | — | — | — | — | — | — | — | — | — |
| repair-application-permissions | — | — | — | — | — | — | — | — | — |
| scheduled-maintenance | — | — | — | — | — | — | — | — | — |
| ssh-key-only | — | — | — | — | — | — | — | — | — |
| sticky-drop-directory | — | — | — | — | — | — | — | — | — |
| unprivileged-service | — | — | — | — | — | — | — | — | — |
| mandatory-access-control-port | — | — | — | — | — | — | — | — | — |
| kernel-module-blacklist | — | — | — | — | — | — | — | — | — |
| boot-kernel-parameter | — | — | — | — | — | — | — | — | — |
| mount-option-hardening | — | — | — | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — | — |
| sudo-command-logging | — | — | — | — | — | — | — | — | — |
| cron-access-control | — | — | — | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — | — |
| encrypted-volume | — | — | — | — | — | — | — | — | — |
| lvm-extend | — | — | — | — | — | — | — | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — | — |
| local-package-repository | — | — | — | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — | — |
| file-integrity-baseline | — | — | — | — | — | — | — | — | — |
| archive-member-safety | — | — | — | — | — | — | — | — | [12/4](../../../jobs/8220/2026-10-03__01-23-07/archive-member-safety-bash-ubuntu7-8220) |
| atomic-release-publication | — | — | — | — | — | — | — | — | [12/5](../../../jobs/8220/2026-10-03__01-23-07/atomic-release-publication-bash-ubuntu7-8220) |
| batch-exclusive-lock | — | — | — | — | — | — | — | — | [14/4](../../../jobs/8220/2026-10-03__01-23-07/batch-exclusive-lock-bash-ubuntu7-8220) |
| cgi-report-execution | — | — | — | — | — | — | — | — | [0/0](../../../jobs/8220/2026-10-03__01-23-07/cgi-report-execution-bash-ubuntu7-8220) |
| child-process-reaping | — | — | — | — | — | — | — | — | [10/1](../../../jobs/8220/2026-10-03__01-23-07/child-process-reaping-bash-ubuntu7-8220) |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | — | — | [11/5](../../../jobs/8220/2026-10-03__01-23-07/cross-file-accounting-reconciliation-bash-ubuntu7-8220) |
| deleted-open-file-recovery | — | — | — | — | — | — | — | — | [17/5](../../../jobs/8220/2026-10-03__01-23-07/deleted-open-file-recovery-bash-ubuntu7-8220) |
| fifo-worker-reconnection | — | — | — | — | — | — | — | — | [14/3](../../../jobs/8220/2026-10-03__01-23-07/fifo-worker-reconnection-bash-ubuntu7-8220) |
| file-descriptor-leak | — | — | — | — | — | — | — | — | [9/2](../../../jobs/8220/2026-10-03__01-23-07/file-descriptor-leak-bash-ubuntu7-8220) |
| filename-encoding-migration | — | — | — | — | — | — | — | — | [14/4](../../../jobs/8220/2026-10-03__01-23-07/filename-encoding-migration-bash-ubuntu7-8220) |
| fixed-width-import-recovery | — | — | — | — | — | — | — | — | [12/2](../../../jobs/8220/2026-10-03__01-23-07/fixed-width-import-recovery-bash-ubuntu7-8220) |
| hardlink-aware-deduplication | — | — | — | — | — | — | — | — | [12/4](../../../jobs/8220/2026-10-03__01-23-07/hardlink-aware-deduplication-bash-ubuntu7-8220) |
| incremental-archive-chain | — | — | — | — | — | — | — | — | [11/4](../../../jobs/8220/2026-10-03__01-23-07/incremental-archive-chain-bash-ubuntu7-8220) |
| inherited-directory-acls | — | — | — | — | — | — | — | — | [19/6](../../../jobs/8220/2026-10-03__01-23-07/inherited-directory-acls-bash-ubuntu7-8220) |
| inode-cache-retention | — | — | — | — | — | — | — | — | [11/4](../../../jobs/8220/2026-10-03__01-23-07/inode-cache-retention-bash-ubuntu7-8220) |
| large-counter-overflow | — | — | — | — | — | — | — | — | [9/3](../../../jobs/8220/2026-10-03__01-23-07/large-counter-overflow-bash-ubuntu7-8220) |
| mail-filter-routing | — | — | — | — | — | — | — | — | [9/6](../../../jobs/8220/2026-10-03__01-23-07/mail-filter-routing-bash-ubuntu7-8220) |
| mail-spool-deduplication | — | — | — | — | — | — | — | — | [16/5](../../../jobs/8220/2026-10-03__01-23-07/mail-spool-deduplication-bash-ubuntu7-8220) |
| minimal-environment-job | — | — | — | — | — | — | — | — | [8/3](../../../jobs/8220/2026-10-03__01-23-07/minimal-environment-job-bash-ubuntu7-8220) |
| name-based-web-tenants | — | — | — | — | — | — | — | — | [10/2](../../../jobs/8220/2026-10-03__01-23-07/name-based-web-tenants-bash-ubuntu7-8220) |
| numeric-record-ordering | — | — | — | — | — | — | — | — | [13/3](../../../jobs/8220/2026-10-03__01-23-07/numeric-record-ordering-bash-ubuntu7-8220) |
| permanent-url-migration | — | — | — | — | — | — | — | — | [14/4](../../../jobs/8220/2026-10-03__01-23-07/permanent-url-migration-bash-ubuntu7-8220) |
| posix-shell-installer | — | — | — | — | — | — | — | — | [11/3](../../../jobs/8220/2026-10-03__01-23-07/posix-shell-installer-bash-ubuntu7-8220) |
| postgresql-sequence-repair | — | — | — | — | — | — | — | — | [19/2](../../../jobs/8220/2026-10-03__01-23-07/postgresql-sequence-repair-bash-ubuntu7-8220) |
| print-spool-recovery | — | — | — | — | — | — | — | — | [21/3](../../../jobs/8220/2026-10-03__01-23-07/print-spool-recovery-bash-ubuntu7-8220) |
| privacy-safe-support-export | — | — | — | — | — | — | — | — | [14/6](../../../jobs/8220/2026-10-03__01-23-07/privacy-safe-support-export-bash-ubuntu7-8220) |
| relative-symlink-relocation | — | — | — | — | — | — | — | — | [9/2](../../../jobs/8220/2026-10-03__01-23-07/relative-symlink-relocation-bash-ubuntu7-8220) |
| selective-tape-restore | — | — | — | — | — | — | — | — | [8/4](../../../jobs/8220/2026-10-03__01-23-07/selective-tape-restore-bash-ubuntu7-8220) |
| signal-driven-config-reload | — | — | — | — | — | — | — | — | [26/5](../../../jobs/8220/2026-10-03__01-23-07/signal-driven-config-reload-bash-ubuntu7-8220) |
| sparse-image-copy | — | — | — | — | — | — | — | — | [10/4](../../../jobs/8220/2026-10-03__01-23-07/sparse-image-copy-bash-ubuntu7-8220) |
| sqlite-lock-contention | — | — | — | — | — | — | — | — | [25/5](../../../jobs/8220/2026-10-03__01-23-07/sqlite-lock-contention-bash-ubuntu7-8220) |
| stale-pidfile-startup | — | — | — | — | — | — | — | — | [17/0](../../../jobs/8220/2026-10-03__01-23-07/stale-pidfile-startup-bash-ubuntu7-8220) |
| temporary-file-symlink-defense | — | — | — | — | — | — | — | — | [12/5](../../../jobs/8220/2026-10-03__01-23-07/temporary-file-symlink-defense-bash-ubuntu7-8220) |
| text-export-normalization | — | — | — | — | — | — | — | — | [10/3](../../../jobs/8220/2026-10-03__01-23-07/text-export-normalization-bash-ubuntu7-8220) |
| timezone-log-merge | — | — | — | — | — | — | — | — | [13/2](../../../jobs/8220/2026-10-03__01-23-07/timezone-log-merge-bash-ubuntu7-8220) |
| transactional-schema-upgrade | — | — | — | — | — | — | — | — | [16/6](../../../jobs/8220/2026-10-03__01-23-07/transactional-schema-upgrade-bash-ubuntu7-8220) |
| unix-socket-access-boundary | — | — | — | — | — | — | — | — | [11/5](../../../jobs/8220/2026-10-03__01-23-07/unix-socket-access-boundary-bash-ubuntu7-8220) |
| web-authentication-boundary | — | — | — | — | — | — | — | — | [14/3](../../../jobs/8220/2026-10-03__01-23-07/web-authentication-boundary-bash-ubuntu7-8220) |
| webdav-document-locks | — | — | — | — | — | — | — | — | [15/4](../../../jobs/8220/2026-10-03__01-23-07/webdav-document-locks-bash-ubuntu7-8220) |
| working-directory-independent-launch | — | — | — | — | — | — | — | — | [9/2](../../../jobs/8220/2026-10-03__01-23-07/working-directory-independent-launch-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 12.9/3.6 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — | — |
| application-log-rotation | — | — | — | — | — | — | — | — | — |
| custom-ca-trust | — | — | — | — | — | — | — | — | — |
| host-firewall-baseline | — | — | — | — | — | — | — | — | — |
| kernel-network-hardening | — | — | — | — | — | — | — | — | — |
| repair-application-permissions | — | — | — | — | — | — | — | — | — |
| scheduled-maintenance | — | — | — | — | — | — | — | — | — |
| ssh-key-only | — | — | — | — | — | — | — | — | — |
| sticky-drop-directory | — | — | — | — | — | — | — | — | — |
| unprivileged-service | — | — | — | — | — | — | — | — | — |
| mandatory-access-control-port | — | — | — | — | — | — | — | — | — |
| kernel-module-blacklist | — | — | — | — | — | — | — | — | — |
| boot-kernel-parameter | — | — | — | — | — | — | — | — | — |
| mount-option-hardening | — | — | — | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — | — |
| sudo-command-logging | — | — | — | — | — | — | — | — | — |
| cron-access-control | — | — | — | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — | — |
| encrypted-volume | — | — | — | — | — | — | — | — | — |
| lvm-extend | — | — | — | — | — | — | — | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — | — |
| local-package-repository | — | — | — | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — | — |
| file-integrity-baseline | — | — | — | — | — | — | — | — | — |
| archive-member-safety | — | — | — | — | — | — | — | — | [3m 27s](../../../jobs/8220/2026-10-03__01-23-07/archive-member-safety-bash-ubuntu7-8220) |
| atomic-release-publication | — | — | — | — | — | — | — | — | [4m 06s](../../../jobs/8220/2026-10-03__01-23-07/atomic-release-publication-bash-ubuntu7-8220) |
| batch-exclusive-lock | — | — | — | — | — | — | — | — | [3m 24s](../../../jobs/8220/2026-10-03__01-23-07/batch-exclusive-lock-bash-ubuntu7-8220) |
| cgi-report-execution | — | — | — | — | — | — | — | — | [40m 39s](../../../jobs/8220/2026-10-03__01-23-07/cgi-report-execution-bash-ubuntu7-8220) |
| child-process-reaping | — | — | — | — | — | — | — | — | [3m 43s](../../../jobs/8220/2026-10-03__01-23-07/child-process-reaping-bash-ubuntu7-8220) |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | — | — | [3m 53s](../../../jobs/8220/2026-10-03__01-23-07/cross-file-accounting-reconciliation-bash-ubuntu7-8220) |
| deleted-open-file-recovery | — | — | — | — | — | — | — | — | [4m 10s](../../../jobs/8220/2026-10-03__01-23-07/deleted-open-file-recovery-bash-ubuntu7-8220) |
| fifo-worker-reconnection | — | — | — | — | — | — | — | — | [3m 53s](../../../jobs/8220/2026-10-03__01-23-07/fifo-worker-reconnection-bash-ubuntu7-8220) |
| file-descriptor-leak | — | — | — | — | — | — | — | — | [2m 45s](../../../jobs/8220/2026-10-03__01-23-07/file-descriptor-leak-bash-ubuntu7-8220) |
| filename-encoding-migration | — | — | — | — | — | — | — | — | [3m 52s](../../../jobs/8220/2026-10-03__01-23-07/filename-encoding-migration-bash-ubuntu7-8220) |
| fixed-width-import-recovery | — | — | — | — | — | — | — | — | [3m 12s](../../../jobs/8220/2026-10-03__01-23-07/fixed-width-import-recovery-bash-ubuntu7-8220) |
| hardlink-aware-deduplication | — | — | — | — | — | — | — | — | [3m 15s](../../../jobs/8220/2026-10-03__01-23-07/hardlink-aware-deduplication-bash-ubuntu7-8220) |
| incremental-archive-chain | — | — | — | — | — | — | — | — | [2m 33s](../../../jobs/8220/2026-10-03__01-23-07/incremental-archive-chain-bash-ubuntu7-8220) |
| inherited-directory-acls | — | — | — | — | — | — | — | — | [3m 44s](../../../jobs/8220/2026-10-03__01-23-07/inherited-directory-acls-bash-ubuntu7-8220) |
| inode-cache-retention | — | — | — | — | — | — | — | — | [3m 17s](../../../jobs/8220/2026-10-03__01-23-07/inode-cache-retention-bash-ubuntu7-8220) |
| large-counter-overflow | — | — | — | — | — | — | — | — | [2m 46s](../../../jobs/8220/2026-10-03__01-23-07/large-counter-overflow-bash-ubuntu7-8220) |
| mail-filter-routing | — | — | — | — | — | — | — | — | [3m 06s](../../../jobs/8220/2026-10-03__01-23-07/mail-filter-routing-bash-ubuntu7-8220) |
| mail-spool-deduplication | — | — | — | — | — | — | — | — | [4m 21s](../../../jobs/8220/2026-10-03__01-23-07/mail-spool-deduplication-bash-ubuntu7-8220) |
| minimal-environment-job | — | — | — | — | — | — | — | — | [2m 28s](../../../jobs/8220/2026-10-03__01-23-07/minimal-environment-job-bash-ubuntu7-8220) |
| name-based-web-tenants | — | — | — | — | — | — | — | — | [2m 49s](../../../jobs/8220/2026-10-03__01-23-07/name-based-web-tenants-bash-ubuntu7-8220) |
| numeric-record-ordering | — | — | — | — | — | — | — | — | [3m 44s](../../../jobs/8220/2026-10-03__01-23-07/numeric-record-ordering-bash-ubuntu7-8220) |
| permanent-url-migration | — | — | — | — | — | — | — | — | [3m 25s](../../../jobs/8220/2026-10-03__01-23-07/permanent-url-migration-bash-ubuntu7-8220) |
| posix-shell-installer | — | — | — | — | — | — | — | — | [2m 59s](../../../jobs/8220/2026-10-03__01-23-07/posix-shell-installer-bash-ubuntu7-8220) |
| postgresql-sequence-repair | — | — | — | — | — | — | — | — | [3m 25s](../../../jobs/8220/2026-10-03__01-23-07/postgresql-sequence-repair-bash-ubuntu7-8220) |
| print-spool-recovery | — | — | — | — | — | — | — | — | [3m 29s](../../../jobs/8220/2026-10-03__01-23-07/print-spool-recovery-bash-ubuntu7-8220) |
| privacy-safe-support-export | — | — | — | — | — | — | — | — | [3m 21s](../../../jobs/8220/2026-10-03__01-23-07/privacy-safe-support-export-bash-ubuntu7-8220) |
| relative-symlink-relocation | — | — | — | — | — | — | — | — | [2m 29s](../../../jobs/8220/2026-10-03__01-23-07/relative-symlink-relocation-bash-ubuntu7-8220) |
| selective-tape-restore | — | — | — | — | — | — | — | — | [2m 09s](../../../jobs/8220/2026-10-03__01-23-07/selective-tape-restore-bash-ubuntu7-8220) |
| signal-driven-config-reload | — | — | — | — | — | — | — | — | [7m 35s](../../../jobs/8220/2026-10-03__01-23-07/signal-driven-config-reload-bash-ubuntu7-8220) |
| sparse-image-copy | — | — | — | — | — | — | — | — | [2m 17s](../../../jobs/8220/2026-10-03__01-23-07/sparse-image-copy-bash-ubuntu7-8220) |
| sqlite-lock-contention | — | — | — | — | — | — | — | — | [5m 23s](../../../jobs/8220/2026-10-03__01-23-07/sqlite-lock-contention-bash-ubuntu7-8220) |
| stale-pidfile-startup | — | — | — | — | — | — | — | — | [6m 55s](../../../jobs/8220/2026-10-03__01-23-07/stale-pidfile-startup-bash-ubuntu7-8220) |
| temporary-file-symlink-defense | — | — | — | — | — | — | — | — | [4m 10s](../../../jobs/8220/2026-10-03__01-23-07/temporary-file-symlink-defense-bash-ubuntu7-8220) |
| text-export-normalization | — | — | — | — | — | — | — | — | [2m 48s](../../../jobs/8220/2026-10-03__01-23-07/text-export-normalization-bash-ubuntu7-8220) |
| timezone-log-merge | — | — | — | — | — | — | — | — | [3m 07s](../../../jobs/8220/2026-10-03__01-23-07/timezone-log-merge-bash-ubuntu7-8220) |
| transactional-schema-upgrade | — | — | — | — | — | — | — | — | [4m 45s](../../../jobs/8220/2026-10-03__01-23-07/transactional-schema-upgrade-bash-ubuntu7-8220) |
| unix-socket-access-boundary | — | — | — | — | — | — | — | — | [3m 26s](../../../jobs/8220/2026-10-03__01-23-07/unix-socket-access-boundary-bash-ubuntu7-8220) |
| web-authentication-boundary | — | — | — | — | — | — | — | — | [5m 25s](../../../jobs/8220/2026-10-03__01-23-07/web-authentication-boundary-bash-ubuntu7-8220) |
| webdav-document-locks | — | — | — | — | — | — | — | — | [3m 58s](../../../jobs/8220/2026-10-03__01-23-07/webdav-document-locks-bash-ubuntu7-8220) |
| working-directory-independent-launch | — | — | — | — | — | — | — | — | [2m 27s](../../../jobs/8220/2026-10-03__01-23-07/working-directory-independent-launch-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 4m 34s |

Cluster provisioning is not a meaningful part of these times: median 568 ms across 60 clusters, about 0.23% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | — | — | — | — | — | — | — | — | — |
| application-log-rotation | — | — | — | — | — | — | — | — | — |
| custom-ca-trust | — | — | — | — | — | — | — | — | — |
| host-firewall-baseline | — | — | — | — | — | — | — | — | — |
| kernel-network-hardening | — | — | — | — | — | — | — | — | — |
| repair-application-permissions | — | — | — | — | — | — | — | — | — |
| scheduled-maintenance | — | — | — | — | — | — | — | — | — |
| ssh-key-only | — | — | — | — | — | — | — | — | — |
| sticky-drop-directory | — | — | — | — | — | — | — | — | — |
| unprivileged-service | — | — | — | — | — | — | — | — | — |
| mandatory-access-control-port | — | — | — | — | — | — | — | — | — |
| kernel-module-blacklist | — | — | — | — | — | — | — | — | — |
| boot-kernel-parameter | — | — | — | — | — | — | — | — | — |
| mount-option-hardening | — | — | — | — | — | — | — | — | — |
| service-sandboxing | — | — | — | — | — | — | — | — | — |
| password-complexity-policy | — | — | — | — | — | — | — | — | — |
| sudo-command-logging | — | — | — | — | — | — | — | — | — |
| cron-access-control | — | — | — | — | — | — | — | — | — |
| ssh-host-certificate | — | — | — | — | — | — | — | — | — |
| disk-quota | — | — | — | — | — | — | — | — | — |
| encrypted-volume | — | — | — | — | — | — | — | — | — |
| lvm-extend | — | — | — | — | — | — | — | — | — |
| filesystem-snapshot-rollback | — | — | — | — | — | — | — | — | — |
| zram-swap | — | — | — | — | — | — | — | — | — |
| package-version-hold | — | — | — | — | — | — | — | — | — |
| local-package-repository | — | — | — | — | — | — | — | — | — |
| oom-protection | — | — | — | — | — | — | — | — | — |
| rootless-container-service | — | — | — | — | — | — | — | — | — |
| certificate-rotation | — | — | — | — | — | — | — | — | — |
| file-integrity-baseline | — | — | — | — | — | — | — | — | — |
| archive-member-safety | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/archive-member-safety-bash-ubuntu7-8220) |
| atomic-release-publication | — | — | — | — | — | — | — | — | [0.880](../../../jobs/8220/2026-10-03__01-23-07/atomic-release-publication-bash-ubuntu7-8220) |
| batch-exclusive-lock | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/batch-exclusive-lock-bash-ubuntu7-8220) |
| cgi-report-execution | — | — | — | — | — | — | — | — | [0.900](../../../jobs/8220/2026-10-03__01-23-07/cgi-report-execution-bash-ubuntu7-8220) |
| child-process-reaping | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8220/2026-10-03__01-23-07/child-process-reaping-bash-ubuntu7-8220) |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8220/2026-10-03__01-23-07/cross-file-accounting-reconciliation-bash-ubuntu7-8220) |
| deleted-open-file-recovery | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8220/2026-10-03__01-23-07/deleted-open-file-recovery-bash-ubuntu7-8220) |
| fifo-worker-reconnection | — | — | — | — | — | — | — | — | [0.720](../../../jobs/8220/2026-10-03__01-23-07/fifo-worker-reconnection-bash-ubuntu7-8220) |
| file-descriptor-leak | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8220/2026-10-03__01-23-07/file-descriptor-leak-bash-ubuntu7-8220) |
| filename-encoding-migration | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8220/2026-10-03__01-23-07/filename-encoding-migration-bash-ubuntu7-8220) |
| fixed-width-import-recovery | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8220/2026-10-03__01-23-07/fixed-width-import-recovery-bash-ubuntu7-8220) |
| hardlink-aware-deduplication | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/hardlink-aware-deduplication-bash-ubuntu7-8220) |
| incremental-archive-chain | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/incremental-archive-chain-bash-ubuntu7-8220) |
| inherited-directory-acls | — | — | — | — | — | — | — | — | [0.880](../../../jobs/8220/2026-10-03__01-23-07/inherited-directory-acls-bash-ubuntu7-8220) |
| inode-cache-retention | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/inode-cache-retention-bash-ubuntu7-8220) |
| large-counter-overflow | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8220/2026-10-03__01-23-07/large-counter-overflow-bash-ubuntu7-8220) |
| mail-filter-routing | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/mail-filter-routing-bash-ubuntu7-8220) |
| mail-spool-deduplication | — | — | — | — | — | — | — | — | [0.860](../../../jobs/8220/2026-10-03__01-23-07/mail-spool-deduplication-bash-ubuntu7-8220) |
| minimal-environment-job | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/minimal-environment-job-bash-ubuntu7-8220) |
| name-based-web-tenants | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8220/2026-10-03__01-23-07/name-based-web-tenants-bash-ubuntu7-8220) |
| numeric-record-ordering | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8220/2026-10-03__01-23-07/numeric-record-ordering-bash-ubuntu7-8220) |
| permanent-url-migration | — | — | — | — | — | — | — | — | [0.950](../../../jobs/8220/2026-10-03__01-23-07/permanent-url-migration-bash-ubuntu7-8220) |
| posix-shell-installer | — | — | — | — | — | — | — | — | [0.920](../../../jobs/8220/2026-10-03__01-23-07/posix-shell-installer-bash-ubuntu7-8220) |
| postgresql-sequence-repair | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/postgresql-sequence-repair-bash-ubuntu7-8220) |
| print-spool-recovery | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8220/2026-10-03__01-23-07/print-spool-recovery-bash-ubuntu7-8220) |
| privacy-safe-support-export | — | — | — | — | — | — | — | — | [0.900](../../../jobs/8220/2026-10-03__01-23-07/privacy-safe-support-export-bash-ubuntu7-8220) |
| relative-symlink-relocation | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/relative-symlink-relocation-bash-ubuntu7-8220) |
| selective-tape-restore | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/selective-tape-restore-bash-ubuntu7-8220) |
| signal-driven-config-reload | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8220/2026-10-03__01-23-07/signal-driven-config-reload-bash-ubuntu7-8220) |
| sparse-image-copy | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/sparse-image-copy-bash-ubuntu7-8220) |
| sqlite-lock-contention | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8220/2026-10-03__01-23-07/sqlite-lock-contention-bash-ubuntu7-8220) |
| stale-pidfile-startup | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8220/2026-10-03__01-23-07/stale-pidfile-startup-bash-ubuntu7-8220) |
| temporary-file-symlink-defense | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/temporary-file-symlink-defense-bash-ubuntu7-8220) |
| text-export-normalization | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/text-export-normalization-bash-ubuntu7-8220) |
| timezone-log-merge | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/timezone-log-merge-bash-ubuntu7-8220) |
| transactional-schema-upgrade | — | — | — | — | — | — | — | — | [0.950](../../../jobs/8220/2026-10-03__01-23-07/transactional-schema-upgrade-bash-ubuntu7-8220) |
| unix-socket-access-boundary | — | — | — | — | — | — | — | — | [0.920](../../../jobs/8220/2026-10-03__01-23-07/unix-socket-access-boundary-bash-ubuntu7-8220) |
| web-authentication-boundary | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8220/2026-10-03__01-23-07/web-authentication-boundary-bash-ubuntu7-8220) |
| webdav-document-locks | — | — | — | — | — | — | — | — | [0.950](../../../jobs/8220/2026-10-03__01-23-07/webdav-document-locks-bash-ubuntu7-8220) |
| working-directory-independent-launch | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/working-directory-independent-launch-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 0.957 |
