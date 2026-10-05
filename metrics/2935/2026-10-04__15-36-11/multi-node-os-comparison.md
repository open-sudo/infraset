# multi-node-os-comparison: command execution summary

Scope: `2935/2026-10-04__15-36-11`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [44/2](../../../jobs/2935/2026-10-04__15-36-11/shared-nfs-storage-bash-rhel10-2935) | — | — |
| centralized-log-collector | — | — | — | — | — | [24/0](../../../jobs/2935/2026-10-04__15-36-11/centralized-log-collector-bash-rhel10-2935) | — | — |
| ssh-controller-access | — | — | — | — | — | [29/1](../../../jobs/2935/2026-10-04__15-36-11/ssh-controller-access-bash-rhel10-2935) | — | — |
| internal-ca-tls | — | — | — | — | — | [26/4](../../../jobs/2935/2026-10-04__15-36-11/internal-ca-tls-bash-rhel10-2935) | — | — |
| internal-time-sync | — | — | — | — | — | [21/0](../../../jobs/2935/2026-10-04__15-36-11/internal-time-sync-bash-rhel10-2935) | — | — |
| load-balanced-web-tier | — | — | — | — | — | [62/1](../../../jobs/2935/2026-10-04__15-36-11/load-balanced-web-tier-bash-rhel10-2935) | — | — |
| network-scoped-firewall | — | — | — | — | — | [38/0](../../../jobs/2935/2026-10-04__15-36-11/network-scoped-firewall-bash-rhel10-2935) | — | — |
| config-sync | — | — | — | — | — | [29/2](../../../jobs/2935/2026-10-04__15-36-11/config-sync-bash-rhel10-2935) | — | — |
| scheduled-backup | — | — | — | — | — | [28/1](../../../jobs/2935/2026-10-04__15-36-11/scheduled-backup-bash-rhel10-2935) | — | — |
| internal-dns-resolution | — | — | — | — | — | [29/3](../../../jobs/2935/2026-10-04__15-36-11/internal-dns-resolution-bash-rhel10-2935) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [32/1](../../../jobs/2935/2026-10-04__15-36-11/database-reader-writer-roles-bash-rhel10-2935) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [33/1](../../../jobs/2935/2026-10-04__15-36-11/forward-proxy-destination-policy-bash-rhel10-2935) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [34/4](../../../jobs/2935/2026-10-04__15-36-11/ftp-dropbox-confinement-bash-rhel10-2935) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [26/0](../../../jobs/2935/2026-10-04__15-36-11/http-upload-size-boundary-bash-rhel10-2935) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [25/2](../../../jobs/2935/2026-10-04__15-36-11/imap-maildir-cutover-bash-rhel10-2935) | — | — |
| inetd-request-activation | — | — | — | — | — | [30/1](../../../jobs/2935/2026-10-04__15-36-11/inetd-request-activation-bash-rhel10-2935) | — | — |
| kerberos-service-identity | — | — | — | — | — | [31/1](../../../jobs/2935/2026-10-04__15-36-11/kerberos-service-identity-bash-rhel10-2935) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [33/1](../../../jobs/2935/2026-10-04__15-36-11/ldap-attribute-privacy-bash-rhel10-2935) | — | — |
| ldap-directory-import | — | — | — | — | — | [38/9](../../../jobs/2935/2026-10-04__15-36-11/ldap-directory-import-bash-rhel10-2935) | — | — |
| mysql-relational-import | — | — | — | — | — | [34/3](../../../jobs/2935/2026-10-04__15-36-11/mysql-relational-import-bash-rhel10-2935) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [40/1](../../../jobs/2935/2026-10-04__15-36-11/mysql-replication-catchup-bash-rhel10-2935) | — | — |
| radius-network-authentication | — | — | — | — | — | [32/0](../../../jobs/2935/2026-10-04__15-36-11/radius-network-authentication-bash-rhel10-2935) | — | — |
| rsync-module-publication | — | — | — | — | — | [32/1](../../../jobs/2935/2026-10-04__15-36-11/rsync-module-publication-bash-rhel10-2935) | — | — |
| samba-team-share | — | — | — | — | — | [25/0](../../../jobs/2935/2026-10-04__15-36-11/samba-team-share-bash-rhel10-2935) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [27/1](../../../jobs/2935/2026-10-04__15-36-11/smtp-alias-delivery-bash-rhel10-2935) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [29/2](../../../jobs/2935/2026-10-04__15-36-11/snmp-readonly-monitoring-bash-rhel10-2935) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [28/0](../../../jobs/2935/2026-10-04__15-36-11/ssh-forced-command-ingest-bash-rhel10-2935) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [36/6](../../../jobs/2935/2026-10-04__15-36-11/ssh-local-service-tunnel-bash-rhel10-2935) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [25/2](../../../jobs/2935/2026-10-04__15-36-11/tftp-firmware-distribution-bash-rhel10-2935) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [25/0](../../../jobs/2935/2026-10-04__15-36-11/udp-meter-ingestion-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 31.5/1.7 | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [9m 45s](../../../jobs/2935/2026-10-04__15-36-11/shared-nfs-storage-bash-rhel10-2935) | — | — |
| centralized-log-collector | — | — | — | — | — | [5m 16s](../../../jobs/2935/2026-10-04__15-36-11/centralized-log-collector-bash-rhel10-2935) | — | — |
| ssh-controller-access | — | — | — | — | — | [7m 02s](../../../jobs/2935/2026-10-04__15-36-11/ssh-controller-access-bash-rhel10-2935) | — | — |
| internal-ca-tls | — | — | — | — | — | [9m 19s](../../../jobs/2935/2026-10-04__15-36-11/internal-ca-tls-bash-rhel10-2935) | — | — |
| internal-time-sync | — | — | — | — | — | [6m 04s](../../../jobs/2935/2026-10-04__15-36-11/internal-time-sync-bash-rhel10-2935) | — | — |
| load-balanced-web-tier | — | — | — | — | — | [10m 46s](../../../jobs/2935/2026-10-04__15-36-11/load-balanced-web-tier-bash-rhel10-2935) | — | — |
| network-scoped-firewall | — | — | — | — | — | [17m 37s](../../../jobs/2935/2026-10-04__15-36-11/network-scoped-firewall-bash-rhel10-2935) | — | — |
| config-sync | — | — | — | — | — | [11m 12s](../../../jobs/2935/2026-10-04__15-36-11/config-sync-bash-rhel10-2935) | — | — |
| scheduled-backup | — | — | — | — | — | [8m 33s](../../../jobs/2935/2026-10-04__15-36-11/scheduled-backup-bash-rhel10-2935) | — | — |
| internal-dns-resolution | — | — | — | — | — | [7m 52s](../../../jobs/2935/2026-10-04__15-36-11/internal-dns-resolution-bash-rhel10-2935) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [7m 28s](../../../jobs/2935/2026-10-04__15-36-11/database-reader-writer-roles-bash-rhel10-2935) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [7m 50s](../../../jobs/2935/2026-10-04__15-36-11/forward-proxy-destination-policy-bash-rhel10-2935) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [9m 47s](../../../jobs/2935/2026-10-04__15-36-11/ftp-dropbox-confinement-bash-rhel10-2935) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [8m 02s](../../../jobs/2935/2026-10-04__15-36-11/http-upload-size-boundary-bash-rhel10-2935) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [7m 49s](../../../jobs/2935/2026-10-04__15-36-11/imap-maildir-cutover-bash-rhel10-2935) | — | — |
| inetd-request-activation | — | — | — | — | — | [7m 57s](../../../jobs/2935/2026-10-04__15-36-11/inetd-request-activation-bash-rhel10-2935) | — | — |
| kerberos-service-identity | — | — | — | — | — | [8m 11s](../../../jobs/2935/2026-10-04__15-36-11/kerberos-service-identity-bash-rhel10-2935) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [8m 51s](../../../jobs/2935/2026-10-04__15-36-11/ldap-attribute-privacy-bash-rhel10-2935) | — | — |
| ldap-directory-import | — | — | — | — | — | [10m 18s](../../../jobs/2935/2026-10-04__15-36-11/ldap-directory-import-bash-rhel10-2935) | — | — |
| mysql-relational-import | — | — | — | — | — | [9m 01s](../../../jobs/2935/2026-10-04__15-36-11/mysql-relational-import-bash-rhel10-2935) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [11m 31s](../../../jobs/2935/2026-10-04__15-36-11/mysql-replication-catchup-bash-rhel10-2935) | — | — |
| radius-network-authentication | — | — | — | — | — | [10m 23s](../../../jobs/2935/2026-10-04__15-36-11/radius-network-authentication-bash-rhel10-2935) | — | — |
| rsync-module-publication | — | — | — | — | — | [6m 50s](../../../jobs/2935/2026-10-04__15-36-11/rsync-module-publication-bash-rhel10-2935) | — | — |
| samba-team-share | — | — | — | — | — | [6m 36s](../../../jobs/2935/2026-10-04__15-36-11/samba-team-share-bash-rhel10-2935) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [7m 41s](../../../jobs/2935/2026-10-04__15-36-11/smtp-alias-delivery-bash-rhel10-2935) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [8m 13s](../../../jobs/2935/2026-10-04__15-36-11/snmp-readonly-monitoring-bash-rhel10-2935) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [8m 19s](../../../jobs/2935/2026-10-04__15-36-11/ssh-forced-command-ingest-bash-rhel10-2935) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [9m 26s](../../../jobs/2935/2026-10-04__15-36-11/ssh-local-service-tunnel-bash-rhel10-2935) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [7m 31s](../../../jobs/2935/2026-10-04__15-36-11/tftp-firmware-distribution-bash-rhel10-2935) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [7m 01s](../../../jobs/2935/2026-10-04__15-36-11/udp-meter-ingestion-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 8m 44s | — | — |

Cluster provisioning is not a meaningful part of these times: median 788 ms across 100 clusters, about 0.25% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/shared-nfs-storage-bash-rhel10-2935) | — | — |
| centralized-log-collector | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/centralized-log-collector-bash-rhel10-2935) | — | — |
| ssh-controller-access | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/ssh-controller-access-bash-rhel10-2935) | — | — |
| internal-ca-tls | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/internal-ca-tls-bash-rhel10-2935) | — | — |
| internal-time-sync | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/internal-time-sync-bash-rhel10-2935) | — | — |
| load-balanced-web-tier | — | — | — | — | — | [0.880](../../../jobs/2935/2026-10-04__15-36-11/load-balanced-web-tier-bash-rhel10-2935) | — | — |
| network-scoped-firewall | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/network-scoped-firewall-bash-rhel10-2935) | — | — |
| config-sync | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/config-sync-bash-rhel10-2935) | — | — |
| scheduled-backup | — | — | — | — | — | [0.960](../../../jobs/2935/2026-10-04__15-36-11/scheduled-backup-bash-rhel10-2935) | — | — |
| internal-dns-resolution | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__15-36-11/internal-dns-resolution-bash-rhel10-2935) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [0.970](../../../jobs/2935/2026-10-04__15-36-11/database-reader-writer-roles-bash-rhel10-2935) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/forward-proxy-destination-policy-bash-rhel10-2935) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [0.820](../../../jobs/2935/2026-10-04__15-36-11/ftp-dropbox-confinement-bash-rhel10-2935) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/http-upload-size-boundary-bash-rhel10-2935) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [0.970](../../../jobs/2935/2026-10-04__15-36-11/imap-maildir-cutover-bash-rhel10-2935) | — | — |
| inetd-request-activation | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/inetd-request-activation-bash-rhel10-2935) | — | — |
| kerberos-service-identity | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/kerberos-service-identity-bash-rhel10-2935) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/ldap-attribute-privacy-bash-rhel10-2935) | — | — |
| ldap-directory-import | — | — | — | — | — | [0.860](../../../jobs/2935/2026-10-04__15-36-11/ldap-directory-import-bash-rhel10-2935) | — | — |
| mysql-relational-import | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/mysql-relational-import-bash-rhel10-2935) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/mysql-replication-catchup-bash-rhel10-2935) | — | — |
| radius-network-authentication | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/radius-network-authentication-bash-rhel10-2935) | — | — |
| rsync-module-publication | — | — | — | — | — | [0.970](../../../jobs/2935/2026-10-04__15-36-11/rsync-module-publication-bash-rhel10-2935) | — | — |
| samba-team-share | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/samba-team-share-bash-rhel10-2935) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/smtp-alias-delivery-bash-rhel10-2935) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/snmp-readonly-monitoring-bash-rhel10-2935) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/ssh-forced-command-ingest-bash-rhel10-2935) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [0.970](../../../jobs/2935/2026-10-04__15-36-11/ssh-local-service-tunnel-bash-rhel10-2935) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/tftp-firmware-distribution-bash-rhel10-2935) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__15-36-11/udp-meter-ingestion-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 0.979 | — | — |
