# multi-node-os-comparison: command execution summary

Scope: `8350/2026-10-04__12-08-09`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [29/10](../../../jobs/8350/2026-10-04__12-08-09/shared-nfs-storage-bash-rhel7-8350) | — | — | — | — |
| centralized-log-collector | — | — | — | [23/4](../../../jobs/8350/2026-10-04__12-08-09/centralized-log-collector-bash-rhel7-8350) | — | — | — | — |
| ssh-controller-access | — | — | — | [30/1](../../../jobs/8350/2026-10-04__12-08-09/ssh-controller-access-bash-rhel7-8350) | — | — | — | — |
| internal-ca-tls | — | — | — | [31/4](../../../jobs/8350/2026-10-04__12-08-09/internal-ca-tls-bash-rhel7-8350) | — | — | — | — |
| internal-time-sync | — | — | — | [21/0](../../../jobs/8350/2026-10-04__12-08-09/internal-time-sync-bash-rhel7-8350) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [32/0](../../../jobs/8350/2026-10-04__12-08-09/load-balanced-web-tier-bash-rhel7-8350) | — | — | — | — |
| network-scoped-firewall | — | — | — | [28/3](../../../jobs/8350/2026-10-04__12-08-09/network-scoped-firewall-bash-rhel7-8350) | — | — | — | — |
| config-sync | — | — | — | [28/0](../../../jobs/8350/2026-10-04__12-08-09/config-sync-bash-rhel7-8350) | — | — | — | — |
| scheduled-backup | — | — | — | [23/3](../../../jobs/8350/2026-10-04__12-08-09/scheduled-backup-bash-rhel7-8350) | — | — | — | — |
| internal-dns-resolution | — | — | — | [18/3](../../../jobs/8350/2026-10-04__12-08-09/internal-dns-resolution-bash-rhel7-8350) | — | — | — | — |
| database-reader-writer-roles | — | — | — | [50/9](../../../jobs/8350/2026-10-04__12-08-09/database-reader-writer-roles-bash-rhel7-8350) | — | — | — | — |
| forward-proxy-destination-policy | — | — | — | [23/0](../../../jobs/8350/2026-10-04__12-08-09/forward-proxy-destination-policy-bash-rhel7-8350) | — | — | — | — |
| ftp-dropbox-confinement | — | — | — | [25/9](../../../jobs/8350/2026-10-04__12-08-09/ftp-dropbox-confinement-bash-rhel7-8350) | — | — | — | — |
| http-upload-size-boundary | — | — | — | [22/4](../../../jobs/8350/2026-10-04__12-08-09/http-upload-size-boundary-bash-rhel7-8350) | — | — | — | — |
| imap-maildir-cutover | — | — | — | [27/8](../../../jobs/8350/2026-10-04__12-08-09/imap-maildir-cutover-bash-rhel7-8350) | — | — | — | — |
| inetd-request-activation | — | — | — | [31/5](../../../jobs/8350/2026-10-04__12-08-09/inetd-request-activation-bash-rhel7-8350) | — | — | — | — |
| kerberos-service-identity | — | — | — | [39/3](../../../jobs/8350/2026-10-04__12-08-09/kerberos-service-identity-bash-rhel7-8350) | — | — | — | — |
| ldap-attribute-privacy | — | — | — | [40/3](../../../jobs/8350/2026-10-04__12-08-09/ldap-attribute-privacy-bash-rhel7-8350) | — | — | — | — |
| ldap-directory-import | — | — | — | [31/7](../../../jobs/8350/2026-10-04__12-08-09/ldap-directory-import-bash-rhel7-8350) | — | — | — | — |
| mysql-relational-import | — | — | — | [32/1](../../../jobs/8350/2026-10-04__12-08-09/mysql-relational-import-bash-rhel7-8350) | — | — | — | — |
| mysql-replication-catchup | — | — | — | [40/6](../../../jobs/8350/2026-10-04__12-08-09/mysql-replication-catchup-bash-rhel7-8350) | — | — | — | — |
| radius-network-authentication | — | — | — | [39/2](../../../jobs/8350/2026-10-04__12-08-09/radius-network-authentication-bash-rhel7-8350) | — | — | — | — |
| rsync-module-publication | — | — | — | [28/8](../../../jobs/8350/2026-10-04__12-08-09/rsync-module-publication-bash-rhel7-8350) | — | — | — | — |
| samba-team-share | — | — | — | [50/3](../../../jobs/8350/2026-10-04__12-08-09/samba-team-share-bash-rhel7-8350) | — | — | — | — |
| smtp-alias-delivery | — | — | — | [20/2](../../../jobs/8350/2026-10-04__12-08-09/smtp-alias-delivery-bash-rhel7-8350) | — | — | — | — |
| snmp-readonly-monitoring | — | — | — | [26/3](../../../jobs/8350/2026-10-04__12-08-09/snmp-readonly-monitoring-bash-rhel7-8350) | — | — | — | — |
| ssh-forced-command-ingest | — | — | — | [29/9](../../../jobs/8350/2026-10-04__12-08-09/ssh-forced-command-ingest-bash-rhel7-8350) | — | — | — | — |
| ssh-local-service-tunnel | — | — | — | [28/0](../../../jobs/8350/2026-10-04__12-08-09/ssh-local-service-tunnel-bash-rhel7-8350) | — | — | — | — |
| tftp-firmware-distribution | — | — | — | [31/7](../../../jobs/8350/2026-10-04__12-08-09/tftp-firmware-distribution-bash-rhel7-8350) | — | — | — | — |
| udp-meter-ingestion | — | — | — | [24/4](../../../jobs/8350/2026-10-04__12-08-09/udp-meter-ingestion-bash-rhel7-8350) | — | — | — | — |
| **Average** | — | — | — | 29.9/4.0 | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [11m 34s](../../../jobs/8350/2026-10-04__12-08-09/shared-nfs-storage-bash-rhel7-8350) | — | — | — | — |
| centralized-log-collector | — | — | — | [7m 28s](../../../jobs/8350/2026-10-04__12-08-09/centralized-log-collector-bash-rhel7-8350) | — | — | — | — |
| ssh-controller-access | — | — | — | [6m 59s](../../../jobs/8350/2026-10-04__12-08-09/ssh-controller-access-bash-rhel7-8350) | — | — | — | — |
| internal-ca-tls | — | — | — | [8m 21s](../../../jobs/8350/2026-10-04__12-08-09/internal-ca-tls-bash-rhel7-8350) | — | — | — | — |
| internal-time-sync | — | — | — | [6m 42s](../../../jobs/8350/2026-10-04__12-08-09/internal-time-sync-bash-rhel7-8350) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [8m 04s](../../../jobs/8350/2026-10-04__12-08-09/load-balanced-web-tier-bash-rhel7-8350) | — | — | — | — |
| network-scoped-firewall | — | — | — | [9m 51s](../../../jobs/8350/2026-10-04__12-08-09/network-scoped-firewall-bash-rhel7-8350) | — | — | — | — |
| config-sync | — | — | — | [10m 34s](../../../jobs/8350/2026-10-04__12-08-09/config-sync-bash-rhel7-8350) | — | — | — | — |
| scheduled-backup | — | — | — | [7m 34s](../../../jobs/8350/2026-10-04__12-08-09/scheduled-backup-bash-rhel7-8350) | — | — | — | — |
| internal-dns-resolution | — | — | — | [9m 11s](../../../jobs/8350/2026-10-04__12-08-09/internal-dns-resolution-bash-rhel7-8350) | — | — | — | — |
| database-reader-writer-roles | — | — | — | [17m 24s](../../../jobs/8350/2026-10-04__12-08-09/database-reader-writer-roles-bash-rhel7-8350) | — | — | — | — |
| forward-proxy-destination-policy | — | — | — | [8m 30s](../../../jobs/8350/2026-10-04__12-08-09/forward-proxy-destination-policy-bash-rhel7-8350) | — | — | — | — |
| ftp-dropbox-confinement | — | — | — | [13m 43s](../../../jobs/8350/2026-10-04__12-08-09/ftp-dropbox-confinement-bash-rhel7-8350) | — | — | — | — |
| http-upload-size-boundary | — | — | — | [9m 26s](../../../jobs/8350/2026-10-04__12-08-09/http-upload-size-boundary-bash-rhel7-8350) | — | — | — | — |
| imap-maildir-cutover | — | — | — | [10m 38s](../../../jobs/8350/2026-10-04__12-08-09/imap-maildir-cutover-bash-rhel7-8350) | — | — | — | — |
| inetd-request-activation | — | — | — | [8m 35s](../../../jobs/8350/2026-10-04__12-08-09/inetd-request-activation-bash-rhel7-8350) | — | — | — | — |
| kerberos-service-identity | — | — | — | [9m 40s](../../../jobs/8350/2026-10-04__12-08-09/kerberos-service-identity-bash-rhel7-8350) | — | — | — | — |
| ldap-attribute-privacy | — | — | — | [40m 31s](../../../jobs/8350/2026-10-04__12-08-09/ldap-attribute-privacy-bash-rhel7-8350) | — | — | — | — |
| ldap-directory-import | — | — | — | [12m 00s](../../../jobs/8350/2026-10-04__12-08-09/ldap-directory-import-bash-rhel7-8350) | — | — | — | — |
| mysql-relational-import | — | — | — | [14m 50s](../../../jobs/8350/2026-10-04__12-08-09/mysql-relational-import-bash-rhel7-8350) | — | — | — | — |
| mysql-replication-catchup | — | — | — | [18m 05s](../../../jobs/8350/2026-10-04__12-08-09/mysql-replication-catchup-bash-rhel7-8350) | — | — | — | — |
| radius-network-authentication | — | — | — | [17m 30s](../../../jobs/8350/2026-10-04__12-08-09/radius-network-authentication-bash-rhel7-8350) | — | — | — | — |
| rsync-module-publication | — | — | — | [10m 06s](../../../jobs/8350/2026-10-04__12-08-09/rsync-module-publication-bash-rhel7-8350) | — | — | — | — |
| samba-team-share | — | — | — | [14m 47s](../../../jobs/8350/2026-10-04__12-08-09/samba-team-share-bash-rhel7-8350) | — | — | — | — |
| smtp-alias-delivery | — | — | — | [8m 47s](../../../jobs/8350/2026-10-04__12-08-09/smtp-alias-delivery-bash-rhel7-8350) | — | — | — | — |
| snmp-readonly-monitoring | — | — | — | [11m 51s](../../../jobs/8350/2026-10-04__12-08-09/snmp-readonly-monitoring-bash-rhel7-8350) | — | — | — | — |
| ssh-forced-command-ingest | — | — | — | [12m 48s](../../../jobs/8350/2026-10-04__12-08-09/ssh-forced-command-ingest-bash-rhel7-8350) | — | — | — | — |
| ssh-local-service-tunnel | — | — | — | [8m 29s](../../../jobs/8350/2026-10-04__12-08-09/ssh-local-service-tunnel-bash-rhel7-8350) | — | — | — | — |
| tftp-firmware-distribution | — | — | — | [10m 08s](../../../jobs/8350/2026-10-04__12-08-09/tftp-firmware-distribution-bash-rhel7-8350) | — | — | — | — |
| udp-meter-ingestion | — | — | — | [8m 48s](../../../jobs/8350/2026-10-04__12-08-09/udp-meter-ingestion-bash-rhel7-8350) | — | — | — | — |
| **Average** | — | — | — | 11m 46s | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 958 ms across 100 clusters, about 0.22% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | [0.940](../../../jobs/8350/2026-10-04__12-08-09/shared-nfs-storage-bash-rhel7-8350) | — | — | — | — |
| centralized-log-collector | — | — | — | [0.960](../../../jobs/8350/2026-10-04__12-08-09/centralized-log-collector-bash-rhel7-8350) | — | — | — | — |
| ssh-controller-access | — | — | — | [0.960](../../../jobs/8350/2026-10-04__12-08-09/ssh-controller-access-bash-rhel7-8350) | — | — | — | — |
| internal-ca-tls | — | — | — | [0.820](../../../jobs/8350/2026-10-04__12-08-09/internal-ca-tls-bash-rhel7-8350) | — | — | — | — |
| internal-time-sync | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/internal-time-sync-bash-rhel7-8350) | — | — | — | — |
| load-balanced-web-tier | — | — | — | [0.940](../../../jobs/8350/2026-10-04__12-08-09/load-balanced-web-tier-bash-rhel7-8350) | — | — | — | — |
| network-scoped-firewall | — | — | — | [0.940](../../../jobs/8350/2026-10-04__12-08-09/network-scoped-firewall-bash-rhel7-8350) | — | — | — | — |
| config-sync | — | — | — | [0.840](../../../jobs/8350/2026-10-04__12-08-09/config-sync-bash-rhel7-8350) | — | — | — | — |
| scheduled-backup | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/scheduled-backup-bash-rhel7-8350) | — | — | — | — |
| internal-dns-resolution | — | — | — | [1.000](../../../jobs/8350/2026-10-04__12-08-09/internal-dns-resolution-bash-rhel7-8350) | — | — | — | — |
| database-reader-writer-roles | — | — | — | [0.760](../../../jobs/8350/2026-10-04__12-08-09/database-reader-writer-roles-bash-rhel7-8350) | — | — | — | — |
| forward-proxy-destination-policy | — | — | — | [0.940](../../../jobs/8350/2026-10-04__12-08-09/forward-proxy-destination-policy-bash-rhel7-8350) | — | — | — | — |
| ftp-dropbox-confinement | — | — | — | [0.720](../../../jobs/8350/2026-10-04__12-08-09/ftp-dropbox-confinement-bash-rhel7-8350) | — | — | — | — |
| http-upload-size-boundary | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/http-upload-size-boundary-bash-rhel7-8350) | — | — | — | — |
| imap-maildir-cutover | — | — | — | [0.580](../../../jobs/8350/2026-10-04__12-08-09/imap-maildir-cutover-bash-rhel7-8350) | — | — | — | — |
| inetd-request-activation | — | — | — | [0.850](../../../jobs/8350/2026-10-04__12-08-09/inetd-request-activation-bash-rhel7-8350) | — | — | — | — |
| kerberos-service-identity | — | — | — | [0.720](../../../jobs/8350/2026-10-04__12-08-09/kerberos-service-identity-bash-rhel7-8350) | — | — | — | — |
| ldap-attribute-privacy | — | — | — | [0.700](../../../jobs/8350/2026-10-04__12-08-09/ldap-attribute-privacy-bash-rhel7-8350) | — | — | — | — |
| ldap-directory-import | — | — | — | [0.780](../../../jobs/8350/2026-10-04__12-08-09/ldap-directory-import-bash-rhel7-8350) | — | — | — | — |
| mysql-relational-import | — | — | — | [0.860](../../../jobs/8350/2026-10-04__12-08-09/mysql-relational-import-bash-rhel7-8350) | — | — | — | — |
| mysql-replication-catchup | — | — | — | [0.840](../../../jobs/8350/2026-10-04__12-08-09/mysql-replication-catchup-bash-rhel7-8350) | — | — | — | — |
| radius-network-authentication | — | — | — | [0.840](../../../jobs/8350/2026-10-04__12-08-09/radius-network-authentication-bash-rhel7-8350) | — | — | — | — |
| rsync-module-publication | — | — | — | [0.840](../../../jobs/8350/2026-10-04__12-08-09/rsync-module-publication-bash-rhel7-8350) | — | — | — | — |
| samba-team-share | — | — | — | [0.520](../../../jobs/8350/2026-10-04__12-08-09/samba-team-share-bash-rhel7-8350) | — | — | — | — |
| smtp-alias-delivery | — | — | — | [0.960](../../../jobs/8350/2026-10-04__12-08-09/smtp-alias-delivery-bash-rhel7-8350) | — | — | — | — |
| snmp-readonly-monitoring | — | — | — | [0.830](../../../jobs/8350/2026-10-04__12-08-09/snmp-readonly-monitoring-bash-rhel7-8350) | — | — | — | — |
| ssh-forced-command-ingest | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/ssh-forced-command-ingest-bash-rhel7-8350) | — | — | — | — |
| ssh-local-service-tunnel | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/ssh-local-service-tunnel-bash-rhel7-8350) | — | — | — | — |
| tftp-firmware-distribution | — | — | — | [0.930](../../../jobs/8350/2026-10-04__12-08-09/tftp-firmware-distribution-bash-rhel7-8350) | — | — | — | — |
| udp-meter-ingestion | — | — | — | [0.900](../../../jobs/8350/2026-10-04__12-08-09/udp-meter-ingestion-bash-rhel7-8350) | — | — | — | — |
| **Average** | — | — | — | 0.852 | — | — | — | — |
