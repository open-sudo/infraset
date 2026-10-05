# single-node-os-comparison: command execution summary

Scope: `8799/2026-10-03__01-23-07`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
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
| archive-member-safety | — | — | — | — | — | — | — | — | [18/11](../../../jobs/8799/2026-10-03__01-23-07/archive-member-safety-bash-centos5-8799) |
| atomic-release-publication | — | — | — | — | — | — | — | — | [14/6](../../../jobs/8799/2026-10-03__01-23-07/atomic-release-publication-bash-centos5-8799) |
| batch-exclusive-lock | — | — | — | — | — | — | — | — | [14/7](../../../jobs/8799/2026-10-03__01-23-07/batch-exclusive-lock-bash-centos5-8799) |
| cgi-report-execution | — | — | — | — | — | — | — | — | [11/6](../../../jobs/8799/2026-10-03__01-23-07/cgi-report-execution-bash-centos5-8799) |
| child-process-reaping | — | — | — | — | — | — | — | — | [9/6](../../../jobs/8799/2026-10-03__01-23-07/child-process-reaping-bash-centos5-8799) |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | — | — | [11/7](../../../jobs/8799/2026-10-03__01-23-07/cross-file-accounting-reconciliation-bash-centos5-8799) |
| deleted-open-file-recovery | — | — | — | — | — | — | — | — | [22/7](../../../jobs/8799/2026-10-03__01-23-07/deleted-open-file-recovery-bash-centos5-8799) |
| fifo-worker-reconnection | — | — | — | — | — | — | — | — | [16/6](../../../jobs/8799/2026-10-03__01-23-07/fifo-worker-reconnection-bash-centos5-8799) |
| file-descriptor-leak | — | — | — | — | — | — | — | — | [13/8](../../../jobs/8799/2026-10-03__01-23-07/file-descriptor-leak-bash-centos5-8799) |
| filename-encoding-migration | — | — | — | — | — | — | — | — | [12/10](../../../jobs/8799/2026-10-03__01-23-07/filename-encoding-migration-bash-centos5-8799) |
| fixed-width-import-recovery | — | — | — | — | — | — | — | — | [11/7](../../../jobs/8799/2026-10-03__01-23-07/fixed-width-import-recovery-bash-centos5-8799) |
| hardlink-aware-deduplication | — | — | — | — | — | — | — | — | [11/9](../../../jobs/8799/2026-10-03__01-23-07/hardlink-aware-deduplication-bash-centos5-8799) |
| incremental-archive-chain | — | — | — | — | — | — | — | — | [12/10](../../../jobs/8799/2026-10-03__01-23-07/incremental-archive-chain-bash-centos5-8799) |
| inherited-directory-acls | — | — | — | — | — | — | — | — | [7/9](../../../jobs/8799/2026-10-03__01-23-07/inherited-directory-acls-bash-centos5-8799) |
| inode-cache-retention | — | — | — | — | — | — | — | — | [14/8](../../../jobs/8799/2026-10-03__01-23-07/inode-cache-retention-bash-centos5-8799) |
| large-counter-overflow | — | — | — | — | — | — | — | — | [10/7](../../../jobs/8799/2026-10-03__01-23-07/large-counter-overflow-bash-centos5-8799) |
| mail-filter-routing | — | — | — | — | — | — | — | — | [11/18](../../../jobs/8799/2026-10-03__01-23-07/mail-filter-routing-bash-centos5-8799) |
| mail-spool-deduplication | — | — | — | — | — | — | — | — | [13/16](../../../jobs/8799/2026-10-03__01-23-07/mail-spool-deduplication-bash-centos5-8799) |
| minimal-environment-job | — | — | — | — | — | — | — | — | [9/5](../../../jobs/8799/2026-10-03__01-23-07/minimal-environment-job-bash-centos5-8799) |
| name-based-web-tenants | — | — | — | — | — | — | — | — | [11/7](../../../jobs/8799/2026-10-03__01-23-07/name-based-web-tenants-bash-centos5-8799) |
| numeric-record-ordering | — | — | — | — | — | — | — | — | [11/7](../../../jobs/8799/2026-10-03__01-23-07/numeric-record-ordering-bash-centos5-8799) |
| permanent-url-migration | — | — | — | — | — | — | — | — | [17/6](../../../jobs/8799/2026-10-03__01-23-07/permanent-url-migration-bash-centos5-8799) |
| posix-shell-installer | — | — | — | — | — | — | — | — | [12/15](../../../jobs/8799/2026-10-03__01-23-07/posix-shell-installer-bash-centos5-8799) |
| postgresql-sequence-repair | — | — | — | — | — | — | — | — | [15/7](../../../jobs/8799/2026-10-03__01-23-07/postgresql-sequence-repair-bash-centos5-8799) |
| print-spool-recovery | — | — | — | — | — | — | — | — | [27/10](../../../jobs/8799/2026-10-03__01-23-07/print-spool-recovery-bash-centos5-8799) |
| privacy-safe-support-export | — | — | — | — | — | — | — | — | [15/13](../../../jobs/8799/2026-10-03__01-23-07/privacy-safe-support-export-bash-centos5-8799) |
| relative-symlink-relocation | — | — | — | — | — | — | — | — | [11/5](../../../jobs/8799/2026-10-03__01-23-07/relative-symlink-relocation-bash-centos5-8799) |
| selective-tape-restore | — | — | — | — | — | — | — | — | [11/7](../../../jobs/8799/2026-10-03__01-23-07/selective-tape-restore-bash-centos5-8799) |
| signal-driven-config-reload | — | — | — | — | — | — | — | — | [17/8](../../../jobs/8799/2026-10-03__01-23-07/signal-driven-config-reload-bash-centos5-8799) |
| sparse-image-copy | — | — | — | — | — | — | — | — | [13/2](../../../jobs/8799/2026-10-03__01-23-07/sparse-image-copy-bash-centos5-8799) |
| sqlite-lock-contention | — | — | — | — | — | — | — | — | [16/7](../../../jobs/8799/2026-10-03__01-23-07/sqlite-lock-contention-bash-centos5-8799) |
| stale-pidfile-startup | — | — | — | — | — | — | — | — | [16/3](../../../jobs/8799/2026-10-03__01-23-07/stale-pidfile-startup-bash-centos5-8799) |
| temporary-file-symlink-defense | — | — | — | — | — | — | — | — | [11/4](../../../jobs/8799/2026-10-03__01-23-07/temporary-file-symlink-defense-bash-centos5-8799) |
| text-export-normalization | — | — | — | — | — | — | — | — | [13/14](../../../jobs/8799/2026-10-03__01-23-07/text-export-normalization-bash-centos5-8799) |
| timezone-log-merge | — | — | — | — | — | — | — | — | [14/7](../../../jobs/8799/2026-10-03__01-23-07/timezone-log-merge-bash-centos5-8799) |
| transactional-schema-upgrade | — | — | — | — | — | — | — | — | [16/10](../../../jobs/8799/2026-10-03__01-23-07/transactional-schema-upgrade-bash-centos5-8799) |
| unix-socket-access-boundary | — | — | — | — | — | — | — | — | [15/9](../../../jobs/8799/2026-10-03__01-23-07/unix-socket-access-boundary-bash-centos5-8799) |
| web-authentication-boundary | — | — | — | — | — | — | — | — | [13/11](../../../jobs/8799/2026-10-03__01-23-07/web-authentication-boundary-bash-centos5-8799) |
| webdav-document-locks | — | — | — | — | — | — | — | — | [14/11](../../../jobs/8799/2026-10-03__01-23-07/webdav-document-locks-bash-centos5-8799) |
| working-directory-independent-launch | — | — | — | — | — | — | — | — | [12/7](../../../jobs/8799/2026-10-03__01-23-07/working-directory-independent-launch-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 13.4/8.3 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
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
| archive-member-safety | — | — | — | — | — | — | — | — | [5m 56s](../../../jobs/8799/2026-10-03__01-23-07/archive-member-safety-bash-centos5-8799) |
| atomic-release-publication | — | — | — | — | — | — | — | — | [6m 05s](../../../jobs/8799/2026-10-03__01-23-07/atomic-release-publication-bash-centos5-8799) |
| batch-exclusive-lock | — | — | — | — | — | — | — | — | [5m 23s](../../../jobs/8799/2026-10-03__01-23-07/batch-exclusive-lock-bash-centos5-8799) |
| cgi-report-execution | — | — | — | — | — | — | — | — | [5m 12s](../../../jobs/8799/2026-10-03__01-23-07/cgi-report-execution-bash-centos5-8799) |
| child-process-reaping | — | — | — | — | — | — | — | — | [4m 56s](../../../jobs/8799/2026-10-03__01-23-07/child-process-reaping-bash-centos5-8799) |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | — | — | [4m 50s](../../../jobs/8799/2026-10-03__01-23-07/cross-file-accounting-reconciliation-bash-centos5-8799) |
| deleted-open-file-recovery | — | — | — | — | — | — | — | — | [9m 38s](../../../jobs/8799/2026-10-03__01-23-07/deleted-open-file-recovery-bash-centos5-8799) |
| fifo-worker-reconnection | — | — | — | — | — | — | — | — | [9m 43s](../../../jobs/8799/2026-10-03__01-23-07/fifo-worker-reconnection-bash-centos5-8799) |
| file-descriptor-leak | — | — | — | — | — | — | — | — | [6m 13s](../../../jobs/8799/2026-10-03__01-23-07/file-descriptor-leak-bash-centos5-8799) |
| filename-encoding-migration | — | — | — | — | — | — | — | — | [5m 10s](../../../jobs/8799/2026-10-03__01-23-07/filename-encoding-migration-bash-centos5-8799) |
| fixed-width-import-recovery | — | — | — | — | — | — | — | — | [4m 26s](../../../jobs/8799/2026-10-03__01-23-07/fixed-width-import-recovery-bash-centos5-8799) |
| hardlink-aware-deduplication | — | — | — | — | — | — | — | — | [4m 44s](../../../jobs/8799/2026-10-03__01-23-07/hardlink-aware-deduplication-bash-centos5-8799) |
| incremental-archive-chain | — | — | — | — | — | — | — | — | [4m 01s](../../../jobs/8799/2026-10-03__01-23-07/incremental-archive-chain-bash-centos5-8799) |
| inherited-directory-acls | — | — | — | — | — | — | — | — | [4m 55s](../../../jobs/8799/2026-10-03__01-23-07/inherited-directory-acls-bash-centos5-8799) |
| inode-cache-retention | — | — | — | — | — | — | — | — | [5m 03s](../../../jobs/8799/2026-10-03__01-23-07/inode-cache-retention-bash-centos5-8799) |
| large-counter-overflow | — | — | — | — | — | — | — | — | [4m 53s](../../../jobs/8799/2026-10-03__01-23-07/large-counter-overflow-bash-centos5-8799) |
| mail-filter-routing | — | — | — | — | — | — | — | — | [4m 50s](../../../jobs/8799/2026-10-03__01-23-07/mail-filter-routing-bash-centos5-8799) |
| mail-spool-deduplication | — | — | — | — | — | — | — | — | [5m 03s](../../../jobs/8799/2026-10-03__01-23-07/mail-spool-deduplication-bash-centos5-8799) |
| minimal-environment-job | — | — | — | — | — | — | — | — | [5m 23s](../../../jobs/8799/2026-10-03__01-23-07/minimal-environment-job-bash-centos5-8799) |
| name-based-web-tenants | — | — | — | — | — | — | — | — | [4m 40s](../../../jobs/8799/2026-10-03__01-23-07/name-based-web-tenants-bash-centos5-8799) |
| numeric-record-ordering | — | — | — | — | — | — | — | — | [5m 37s](../../../jobs/8799/2026-10-03__01-23-07/numeric-record-ordering-bash-centos5-8799) |
| permanent-url-migration | — | — | — | — | — | — | — | — | [5m 27s](../../../jobs/8799/2026-10-03__01-23-07/permanent-url-migration-bash-centos5-8799) |
| posix-shell-installer | — | — | — | — | — | — | — | — | [4m 11s](../../../jobs/8799/2026-10-03__01-23-07/posix-shell-installer-bash-centos5-8799) |
| postgresql-sequence-repair | — | — | — | — | — | — | — | — | [5m 49s](../../../jobs/8799/2026-10-03__01-23-07/postgresql-sequence-repair-bash-centos5-8799) |
| print-spool-recovery | — | — | — | — | — | — | — | — | [7m 30s](../../../jobs/8799/2026-10-03__01-23-07/print-spool-recovery-bash-centos5-8799) |
| privacy-safe-support-export | — | — | — | — | — | — | — | — | [7m 41s](../../../jobs/8799/2026-10-03__01-23-07/privacy-safe-support-export-bash-centos5-8799) |
| relative-symlink-relocation | — | — | — | — | — | — | — | — | [3m 32s](../../../jobs/8799/2026-10-03__01-23-07/relative-symlink-relocation-bash-centos5-8799) |
| selective-tape-restore | — | — | — | — | — | — | — | — | [3m 57s](../../../jobs/8799/2026-10-03__01-23-07/selective-tape-restore-bash-centos5-8799) |
| signal-driven-config-reload | — | — | — | — | — | — | — | — | [5m 37s](../../../jobs/8799/2026-10-03__01-23-07/signal-driven-config-reload-bash-centos5-8799) |
| sparse-image-copy | — | — | — | — | — | — | — | — | [5m 55s](../../../jobs/8799/2026-10-03__01-23-07/sparse-image-copy-bash-centos5-8799) |
| sqlite-lock-contention | — | — | — | — | — | — | — | — | [5m 59s](../../../jobs/8799/2026-10-03__01-23-07/sqlite-lock-contention-bash-centos5-8799) |
| stale-pidfile-startup | — | — | — | — | — | — | — | — | [7m 02s](../../../jobs/8799/2026-10-03__01-23-07/stale-pidfile-startup-bash-centos5-8799) |
| temporary-file-symlink-defense | — | — | — | — | — | — | — | — | [5m 20s](../../../jobs/8799/2026-10-03__01-23-07/temporary-file-symlink-defense-bash-centos5-8799) |
| text-export-normalization | — | — | — | — | — | — | — | — | [5m 18s](../../../jobs/8799/2026-10-03__01-23-07/text-export-normalization-bash-centos5-8799) |
| timezone-log-merge | — | — | — | — | — | — | — | — | [4m 57s](../../../jobs/8799/2026-10-03__01-23-07/timezone-log-merge-bash-centos5-8799) |
| transactional-schema-upgrade | — | — | — | — | — | — | — | — | [5m 04s](../../../jobs/8799/2026-10-03__01-23-07/transactional-schema-upgrade-bash-centos5-8799) |
| unix-socket-access-boundary | — | — | — | — | — | — | — | — | [5m 38s](../../../jobs/8799/2026-10-03__01-23-07/unix-socket-access-boundary-bash-centos5-8799) |
| web-authentication-boundary | — | — | — | — | — | — | — | — | [7m 21s](../../../jobs/8799/2026-10-03__01-23-07/web-authentication-boundary-bash-centos5-8799) |
| webdav-document-locks | — | — | — | — | — | — | — | — | [6m 12s](../../../jobs/8799/2026-10-03__01-23-07/webdav-document-locks-bash-centos5-8799) |
| working-directory-independent-launch | — | — | — | — | — | — | — | — | [4m 18s](../../../jobs/8799/2026-10-03__01-23-07/working-directory-independent-launch-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 5m 35s |

Cluster provisioning is not a meaningful part of these times: median 689 ms across 60 clusters, about 0.18% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
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
| archive-member-safety | — | — | — | — | — | — | — | — | [0.900](../../../jobs/8799/2026-10-03__01-23-07/archive-member-safety-bash-centos5-8799) |
| atomic-release-publication | — | — | — | — | — | — | — | — | [0.920](../../../jobs/8799/2026-10-03__01-23-07/atomic-release-publication-bash-centos5-8799) |
| batch-exclusive-lock | — | — | — | — | — | — | — | — | [0.820](../../../jobs/8799/2026-10-03__01-23-07/batch-exclusive-lock-bash-centos5-8799) |
| cgi-report-execution | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8799/2026-10-03__01-23-07/cgi-report-execution-bash-centos5-8799) |
| child-process-reaping | — | — | — | — | — | — | — | — | [0.950](../../../jobs/8799/2026-10-03__01-23-07/child-process-reaping-bash-centos5-8799) |
| cross-file-accounting-reconciliation | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-03__01-23-07/cross-file-accounting-reconciliation-bash-centos5-8799) |
| deleted-open-file-recovery | — | — | — | — | — | — | — | — | [0.740](../../../jobs/8799/2026-10-03__01-23-07/deleted-open-file-recovery-bash-centos5-8799) |
| fifo-worker-reconnection | — | — | — | — | — | — | — | — | [0.800](../../../jobs/8799/2026-10-03__01-23-07/fifo-worker-reconnection-bash-centos5-8799) |
| file-descriptor-leak | — | — | — | — | — | — | — | — | [0.840](../../../jobs/8799/2026-10-03__01-23-07/file-descriptor-leak-bash-centos5-8799) |
| filename-encoding-migration | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8799/2026-10-03__01-23-07/filename-encoding-migration-bash-centos5-8799) |
| fixed-width-import-recovery | — | — | — | — | — | — | — | — | [0.880](../../../jobs/8799/2026-10-03__01-23-07/fixed-width-import-recovery-bash-centos5-8799) |
| hardlink-aware-deduplication | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-03__01-23-07/hardlink-aware-deduplication-bash-centos5-8799) |
| incremental-archive-chain | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8799/2026-10-03__01-23-07/incremental-archive-chain-bash-centos5-8799) |
| inherited-directory-acls | — | — | — | — | — | — | — | — | [0.920](../../../jobs/8799/2026-10-03__01-23-07/inherited-directory-acls-bash-centos5-8799) |
| inode-cache-retention | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8799/2026-10-03__01-23-07/inode-cache-retention-bash-centos5-8799) |
| large-counter-overflow | — | — | — | — | — | — | — | — | [0.780](../../../jobs/8799/2026-10-03__01-23-07/large-counter-overflow-bash-centos5-8799) |
| mail-filter-routing | — | — | — | — | — | — | — | — | [0.990](../../../jobs/8799/2026-10-03__01-23-07/mail-filter-routing-bash-centos5-8799) |
| mail-spool-deduplication | — | — | — | — | — | — | — | — | [0.930](../../../jobs/8799/2026-10-03__01-23-07/mail-spool-deduplication-bash-centos5-8799) |
| minimal-environment-job | — | — | — | — | — | — | — | — | [0.920](../../../jobs/8799/2026-10-03__01-23-07/minimal-environment-job-bash-centos5-8799) |
| name-based-web-tenants | — | — | — | — | — | — | — | — | [0.920](../../../jobs/8799/2026-10-03__01-23-07/name-based-web-tenants-bash-centos5-8799) |
| numeric-record-ordering | — | — | — | — | — | — | — | — | [0.870](../../../jobs/8799/2026-10-03__01-23-07/numeric-record-ordering-bash-centos5-8799) |
| permanent-url-migration | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-03__01-23-07/permanent-url-migration-bash-centos5-8799) |
| posix-shell-installer | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-03__01-23-07/posix-shell-installer-bash-centos5-8799) |
| postgresql-sequence-repair | — | — | — | — | — | — | — | — | [0.990](../../../jobs/8799/2026-10-03__01-23-07/postgresql-sequence-repair-bash-centos5-8799) |
| print-spool-recovery | — | — | — | — | — | — | — | — | [0.860](../../../jobs/8799/2026-10-03__01-23-07/print-spool-recovery-bash-centos5-8799) |
| privacy-safe-support-export | — | — | — | — | — | — | — | — | [0.580](../../../jobs/8799/2026-10-03__01-23-07/privacy-safe-support-export-bash-centos5-8799) |
| relative-symlink-relocation | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-03__01-23-07/relative-symlink-relocation-bash-centos5-8799) |
| selective-tape-restore | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8799/2026-10-03__01-23-07/selective-tape-restore-bash-centos5-8799) |
| signal-driven-config-reload | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8799/2026-10-03__01-23-07/signal-driven-config-reload-bash-centos5-8799) |
| sparse-image-copy | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8799/2026-10-03__01-23-07/sparse-image-copy-bash-centos5-8799) |
| sqlite-lock-contention | — | — | — | — | — | — | — | — | [0.700](../../../jobs/8799/2026-10-03__01-23-07/sqlite-lock-contention-bash-centos5-8799) |
| stale-pidfile-startup | — | — | — | — | — | — | — | — | [0.780](../../../jobs/8799/2026-10-03__01-23-07/stale-pidfile-startup-bash-centos5-8799) |
| temporary-file-symlink-defense | — | — | — | — | — | — | — | — | [0.720](../../../jobs/8799/2026-10-03__01-23-07/temporary-file-symlink-defense-bash-centos5-8799) |
| text-export-normalization | — | — | — | — | — | — | — | — | [0.930](../../../jobs/8799/2026-10-03__01-23-07/text-export-normalization-bash-centos5-8799) |
| timezone-log-merge | — | — | — | — | — | — | — | — | [0.930](../../../jobs/8799/2026-10-03__01-23-07/timezone-log-merge-bash-centos5-8799) |
| transactional-schema-upgrade | — | — | — | — | — | — | — | — | [0.840](../../../jobs/8799/2026-10-03__01-23-07/transactional-schema-upgrade-bash-centos5-8799) |
| unix-socket-access-boundary | — | — | — | — | — | — | — | — | [0.840](../../../jobs/8799/2026-10-03__01-23-07/unix-socket-access-boundary-bash-centos5-8799) |
| web-authentication-boundary | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8799/2026-10-03__01-23-07/web-authentication-boundary-bash-centos5-8799) |
| webdav-document-locks | — | — | — | — | — | — | — | — | [0.970](../../../jobs/8799/2026-10-03__01-23-07/webdav-document-locks-bash-centos5-8799) |
| working-directory-independent-launch | — | — | — | — | — | — | — | — | [0.880](../../../jobs/8799/2026-10-03__01-23-07/working-directory-independent-launch-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 0.894 |
