# multi-node-os-comparison: command execution summary

Scope: `8220/2026-10-03__01-23-07`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | — | — |
| centralized-log-collector | — | — | — | — | — | — | — | — | — |
| ssh-controller-access | — | — | — | — | — | — | — | — | — |
| internal-ca-tls | — | — | — | — | — | — | — | — | — |
| internal-time-sync | — | — | — | — | — | — | — | — | — |
| load-balanced-web-tier | — | — | — | — | — | — | — | — | — |
| network-scoped-firewall | — | — | — | — | — | — | — | — | — |
| config-sync | — | — | — | — | — | — | — | — | — |
| scheduled-backup | — | — | — | — | — | — | — | — | — |
| internal-dns-resolution | — | — | — | — | — | — | — | — | — |
| database-reader-writer-roles | — | — | — | — | — | — | — | — | [36/12](../../../jobs/8220/2026-10-03__01-23-07/database-reader-writer-roles-bash-ubuntu7-8220) |
| forward-proxy-destination-policy | — | — | — | — | — | — | — | — | [35/0](../../../jobs/8220/2026-10-03__01-23-07/forward-proxy-destination-policy-bash-ubuntu7-8220) |
| ftp-dropbox-confinement | — | — | — | — | — | — | — | — | [35/4](../../../jobs/8220/2026-10-03__01-23-07/ftp-dropbox-confinement-bash-ubuntu7-8220) |
| http-upload-size-boundary | — | — | — | — | — | — | — | — | [27/3](../../../jobs/8220/2026-10-03__01-23-07/http-upload-size-boundary-bash-ubuntu7-8220) |
| imap-maildir-cutover | — | — | — | — | — | — | — | — | [29/7](../../../jobs/8220/2026-10-03__01-23-07/imap-maildir-cutover-bash-ubuntu7-8220) |
| inetd-request-activation | — | — | — | — | — | — | — | — | [32/5](../../../jobs/8220/2026-10-03__01-23-07/inetd-request-activation-bash-ubuntu7-8220) |
| kerberos-service-identity | — | — | — | — | — | — | — | — | [50/6](../../../jobs/8220/2026-10-03__01-23-07/kerberos-service-identity-bash-ubuntu7-8220) |
| ldap-attribute-privacy | — | — | — | — | — | — | — | — | [35/1](../../../jobs/8220/2026-10-03__01-23-07/ldap-attribute-privacy-bash-ubuntu7-8220) |
| ldap-directory-import | — | — | — | — | — | — | — | — | [43/4](../../../jobs/8220/2026-10-03__01-23-07/ldap-directory-import-bash-ubuntu7-8220) |
| mysql-relational-import | — | — | — | — | — | — | — | — | [23/3](../../../jobs/8220/2026-10-03__01-23-07/mysql-relational-import-bash-ubuntu7-8220) |
| mysql-replication-catchup | — | — | — | — | — | — | — | — | [76/6](../../../jobs/8220/2026-10-03__01-23-07/mysql-replication-catchup-bash-ubuntu7-8220) |
| radius-network-authentication | — | — | — | — | — | — | — | — | [41/7](../../../jobs/8220/2026-10-03__01-23-07/radius-network-authentication-bash-ubuntu7-8220) |
| rsync-module-publication | — | — | — | — | — | — | — | — | [23/3](../../../jobs/8220/2026-10-03__01-23-07/rsync-module-publication-bash-ubuntu7-8220) |
| samba-team-share | — | — | — | — | — | — | — | — | [37/7](../../../jobs/8220/2026-10-03__01-23-07/samba-team-share-bash-ubuntu7-8220) |
| smtp-alias-delivery | — | — | — | — | — | — | — | — | [27/8](../../../jobs/8220/2026-10-03__01-23-07/smtp-alias-delivery-bash-ubuntu7-8220) |
| snmp-readonly-monitoring | — | — | — | — | — | — | — | — | [27/5](../../../jobs/8220/2026-10-03__01-23-07/snmp-readonly-monitoring-bash-ubuntu7-8220) |
| ssh-forced-command-ingest | — | — | — | — | — | — | — | — | [28/11](../../../jobs/8220/2026-10-03__01-23-07/ssh-forced-command-ingest-bash-ubuntu7-8220) |
| ssh-local-service-tunnel | — | — | — | — | — | — | — | — | [29/3](../../../jobs/8220/2026-10-03__01-23-07/ssh-local-service-tunnel-bash-ubuntu7-8220) |
| tftp-firmware-distribution | — | — | — | — | — | — | — | — | [34/5](../../../jobs/8220/2026-10-03__01-23-07/tftp-firmware-distribution-bash-ubuntu7-8220) |
| udp-meter-ingestion | — | — | — | — | — | — | — | — | [25/5](../../../jobs/8220/2026-10-03__01-23-07/udp-meter-ingestion-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 34.6/5.2 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | — | — |
| centralized-log-collector | — | — | — | — | — | — | — | — | — |
| ssh-controller-access | — | — | — | — | — | — | — | — | — |
| internal-ca-tls | — | — | — | — | — | — | — | — | — |
| internal-time-sync | — | — | — | — | — | — | — | — | — |
| load-balanced-web-tier | — | — | — | — | — | — | — | — | — |
| network-scoped-firewall | — | — | — | — | — | — | — | — | — |
| config-sync | — | — | — | — | — | — | — | — | — |
| scheduled-backup | — | — | — | — | — | — | — | — | — |
| internal-dns-resolution | — | — | — | — | — | — | — | — | — |
| database-reader-writer-roles | — | — | — | — | — | — | — | — | [7m 02s](../../../jobs/8220/2026-10-03__01-23-07/database-reader-writer-roles-bash-ubuntu7-8220) |
| forward-proxy-destination-policy | — | — | — | — | — | — | — | — | [5m 17s](../../../jobs/8220/2026-10-03__01-23-07/forward-proxy-destination-policy-bash-ubuntu7-8220) |
| ftp-dropbox-confinement | — | — | — | — | — | — | — | — | [8m 40s](../../../jobs/8220/2026-10-03__01-23-07/ftp-dropbox-confinement-bash-ubuntu7-8220) |
| http-upload-size-boundary | — | — | — | — | — | — | — | — | [5m 22s](../../../jobs/8220/2026-10-03__01-23-07/http-upload-size-boundary-bash-ubuntu7-8220) |
| imap-maildir-cutover | — | — | — | — | — | — | — | — | [5m 40s](../../../jobs/8220/2026-10-03__01-23-07/imap-maildir-cutover-bash-ubuntu7-8220) |
| inetd-request-activation | — | — | — | — | — | — | — | — | [4m 19s](../../../jobs/8220/2026-10-03__01-23-07/inetd-request-activation-bash-ubuntu7-8220) |
| kerberos-service-identity | — | — | — | — | — | — | — | — | [12m 03s](../../../jobs/8220/2026-10-03__01-23-07/kerberos-service-identity-bash-ubuntu7-8220) |
| ldap-attribute-privacy | — | — | — | — | — | — | — | — | [8m 47s](../../../jobs/8220/2026-10-03__01-23-07/ldap-attribute-privacy-bash-ubuntu7-8220) |
| ldap-directory-import | — | — | — | — | — | — | — | — | [6m 05s](../../../jobs/8220/2026-10-03__01-23-07/ldap-directory-import-bash-ubuntu7-8220) |
| mysql-relational-import | — | — | — | — | — | — | — | — | [5m 12s](../../../jobs/8220/2026-10-03__01-23-07/mysql-relational-import-bash-ubuntu7-8220) |
| mysql-replication-catchup | — | — | — | — | — | — | — | — | [9m 35s](../../../jobs/8220/2026-10-03__01-23-07/mysql-replication-catchup-bash-ubuntu7-8220) |
| radius-network-authentication | — | — | — | — | — | — | — | — | [7m 25s](../../../jobs/8220/2026-10-03__01-23-07/radius-network-authentication-bash-ubuntu7-8220) |
| rsync-module-publication | — | — | — | — | — | — | — | — | [4m 09s](../../../jobs/8220/2026-10-03__01-23-07/rsync-module-publication-bash-ubuntu7-8220) |
| samba-team-share | — | — | — | — | — | — | — | — | [7m 17s](../../../jobs/8220/2026-10-03__01-23-07/samba-team-share-bash-ubuntu7-8220) |
| smtp-alias-delivery | — | — | — | — | — | — | — | — | [5m 09s](../../../jobs/8220/2026-10-03__01-23-07/smtp-alias-delivery-bash-ubuntu7-8220) |
| snmp-readonly-monitoring | — | — | — | — | — | — | — | — | [4m 39s](../../../jobs/8220/2026-10-03__01-23-07/snmp-readonly-monitoring-bash-ubuntu7-8220) |
| ssh-forced-command-ingest | — | — | — | — | — | — | — | — | [5m 44s](../../../jobs/8220/2026-10-03__01-23-07/ssh-forced-command-ingest-bash-ubuntu7-8220) |
| ssh-local-service-tunnel | — | — | — | — | — | — | — | — | [6m 07s](../../../jobs/8220/2026-10-03__01-23-07/ssh-local-service-tunnel-bash-ubuntu7-8220) |
| tftp-firmware-distribution | — | — | — | — | — | — | — | — | [5m 30s](../../../jobs/8220/2026-10-03__01-23-07/tftp-firmware-distribution-bash-ubuntu7-8220) |
| udp-meter-ingestion | — | — | — | — | — | — | — | — | [5m 14s](../../../jobs/8220/2026-10-03__01-23-07/udp-meter-ingestion-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 6m 28s |

Cluster provisioning is not a meaningful part of these times: median 568 ms across 60 clusters, about 0.23% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | ubuntu7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | — | — |
| centralized-log-collector | — | — | — | — | — | — | — | — | — |
| ssh-controller-access | — | — | — | — | — | — | — | — | — |
| internal-ca-tls | — | — | — | — | — | — | — | — | — |
| internal-time-sync | — | — | — | — | — | — | — | — | — |
| load-balanced-web-tier | — | — | — | — | — | — | — | — | — |
| network-scoped-firewall | — | — | — | — | — | — | — | — | — |
| config-sync | — | — | — | — | — | — | — | — | — |
| scheduled-backup | — | — | — | — | — | — | — | — | — |
| internal-dns-resolution | — | — | — | — | — | — | — | — | — |
| database-reader-writer-roles | — | — | — | — | — | — | — | — | [0.660](../../../jobs/8220/2026-10-03__01-23-07/database-reader-writer-roles-bash-ubuntu7-8220) |
| forward-proxy-destination-policy | — | — | — | — | — | — | — | — | [0.960](../../../jobs/8220/2026-10-03__01-23-07/forward-proxy-destination-policy-bash-ubuntu7-8220) |
| ftp-dropbox-confinement | — | — | — | — | — | — | — | — | [0.890](../../../jobs/8220/2026-10-03__01-23-07/ftp-dropbox-confinement-bash-ubuntu7-8220) |
| http-upload-size-boundary | — | — | — | — | — | — | — | — | [0.820](../../../jobs/8220/2026-10-03__01-23-07/http-upload-size-boundary-bash-ubuntu7-8220) |
| imap-maildir-cutover | — | — | — | — | — | — | — | — | [0.630](../../../jobs/8220/2026-10-03__01-23-07/imap-maildir-cutover-bash-ubuntu7-8220) |
| inetd-request-activation | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8220/2026-10-03__01-23-07/inetd-request-activation-bash-ubuntu7-8220) |
| kerberos-service-identity | — | — | — | — | — | — | — | — | [0.720](../../../jobs/8220/2026-10-03__01-23-07/kerberos-service-identity-bash-ubuntu7-8220) |
| ldap-attribute-privacy | — | — | — | — | — | — | — | — | [1.000](../../../jobs/8220/2026-10-03__01-23-07/ldap-attribute-privacy-bash-ubuntu7-8220) |
| ldap-directory-import | — | — | — | — | — | — | — | — | [0.780](../../../jobs/8220/2026-10-03__01-23-07/ldap-directory-import-bash-ubuntu7-8220) |
| mysql-relational-import | — | — | — | — | — | — | — | — | [0.920](../../../jobs/8220/2026-10-03__01-23-07/mysql-relational-import-bash-ubuntu7-8220) |
| mysql-replication-catchup | — | — | — | — | — | — | — | — | [0.940](../../../jobs/8220/2026-10-03__01-23-07/mysql-replication-catchup-bash-ubuntu7-8220) |
| radius-network-authentication | — | — | — | — | — | — | — | — | [0.860](../../../jobs/8220/2026-10-03__01-23-07/radius-network-authentication-bash-ubuntu7-8220) |
| rsync-module-publication | — | — | — | — | — | — | — | — | [0.880](../../../jobs/8220/2026-10-03__01-23-07/rsync-module-publication-bash-ubuntu7-8220) |
| samba-team-share | — | — | — | — | — | — | — | — | [0.980](../../../jobs/8220/2026-10-03__01-23-07/samba-team-share-bash-ubuntu7-8220) |
| smtp-alias-delivery | — | — | — | — | — | — | — | — | [0.980](../../../jobs/8220/2026-10-03__01-23-07/smtp-alias-delivery-bash-ubuntu7-8220) |
| snmp-readonly-monitoring | — | — | — | — | — | — | — | — | [0.840](../../../jobs/8220/2026-10-03__01-23-07/snmp-readonly-monitoring-bash-ubuntu7-8220) |
| ssh-forced-command-ingest | — | — | — | — | — | — | — | — | [0.900](../../../jobs/8220/2026-10-03__01-23-07/ssh-forced-command-ingest-bash-ubuntu7-8220) |
| ssh-local-service-tunnel | — | — | — | — | — | — | — | — | [0.950](../../../jobs/8220/2026-10-03__01-23-07/ssh-local-service-tunnel-bash-ubuntu7-8220) |
| tftp-firmware-distribution | — | — | — | — | — | — | — | — | [0.950](../../../jobs/8220/2026-10-03__01-23-07/tftp-firmware-distribution-bash-ubuntu7-8220) |
| udp-meter-ingestion | — | — | — | — | — | — | — | — | [0.930](../../../jobs/8220/2026-10-03__01-23-07/udp-meter-ingestion-bash-ubuntu7-8220) |
| **Average** | — | — | — | — | — | — | — | — | 0.877 |
