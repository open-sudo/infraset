# multi-node-os-comparison: command execution summary

Scope: `6324/2026-10-03__19-28-10`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | [29/2](../../../jobs/6324/2026-10-03__19-28-10/shared-nfs-storage-bash-rhel9-6324) | — | — | — |
| centralized-log-collector | — | — | — | — | [24/0](../../../jobs/6324/2026-10-03__19-28-10/centralized-log-collector-bash-rhel9-6324) | — | — | — |
| ssh-controller-access | — | — | — | — | [23/0](../../../jobs/6324/2026-10-03__19-28-10/ssh-controller-access-bash-rhel9-6324) | — | — | — |
| internal-ca-tls | — | — | — | — | [27/3](../../../jobs/6324/2026-10-03__19-28-10/internal-ca-tls-bash-rhel9-6324) | — | — | — |
| internal-time-sync | — | — | — | — | [26/1](../../../jobs/6324/2026-10-03__19-28-10/internal-time-sync-bash-rhel9-6324) | — | — | — |
| load-balanced-web-tier | — | — | — | — | [29/0](../../../jobs/6324/2026-10-03__19-28-10/load-balanced-web-tier-bash-rhel9-6324) | — | — | — |
| network-scoped-firewall | — | — | — | — | [28/2](../../../jobs/6324/2026-10-03__19-28-10/network-scoped-firewall-bash-rhel9-6324) | — | — | — |
| config-sync | — | — | — | — | [29/0](../../../jobs/6324/2026-10-03__19-28-10/config-sync-bash-rhel9-6324) | — | — | — |
| scheduled-backup | — | — | — | — | [27/2](../../../jobs/6324/2026-10-03__19-28-10/scheduled-backup-bash-rhel9-6324) | — | — | — |
| internal-dns-resolution | — | — | — | — | [20/0](../../../jobs/6324/2026-10-03__19-28-10/internal-dns-resolution-bash-rhel9-6324) | — | — | — |
| database-reader-writer-roles | — | — | — | — | [37/1](../../../jobs/6324/2026-10-03__19-28-10/database-reader-writer-roles-bash-rhel9-6324) | — | — | — |
| forward-proxy-destination-policy | — | — | — | — | [33/1](../../../jobs/6324/2026-10-03__19-28-10/forward-proxy-destination-policy-bash-rhel9-6324) | — | — | — |
| ftp-dropbox-confinement | — | — | — | — | [25/0](../../../jobs/6324/2026-10-03__19-28-10/ftp-dropbox-confinement-bash-rhel9-6324) | — | — | — |
| http-upload-size-boundary | — | — | — | — | [27/1](../../../jobs/6324/2026-10-03__19-28-10/http-upload-size-boundary-bash-rhel9-6324) | — | — | — |
| imap-maildir-cutover | — | — | — | — | [27/0](../../../jobs/6324/2026-10-03__19-28-10/imap-maildir-cutover-bash-rhel9-6324) | — | — | — |
| inetd-request-activation | — | — | — | — | [38/3](../../../jobs/6324/2026-10-03__19-28-10/inetd-request-activation-bash-rhel9-6324) | — | — | — |
| kerberos-service-identity | — | — | — | — | [31/1](../../../jobs/6324/2026-10-03__19-28-10/kerberos-service-identity-bash-rhel9-6324) | — | — | — |
| ldap-attribute-privacy | — | — | — | — | [41/3](../../../jobs/6324/2026-10-03__19-28-10/ldap-attribute-privacy-bash-rhel9-6324) | — | — | — |
| ldap-directory-import | — | — | — | — | [28/1](../../../jobs/6324/2026-10-03__19-28-10/ldap-directory-import-bash-rhel9-6324) | — | — | — |
| mysql-relational-import | — | — | — | — | [32/1](../../../jobs/6324/2026-10-03__19-28-10/mysql-relational-import-bash-rhel9-6324) | — | — | — |
| mysql-replication-catchup | — | — | — | — | [38/1](../../../jobs/6324/2026-10-03__19-28-10/mysql-replication-catchup-bash-rhel9-6324) | — | — | — |
| radius-network-authentication | — | — | — | — | [37/5](../../../jobs/6324/2026-10-03__19-28-10/radius-network-authentication-bash-rhel9-6324) | — | — | — |
| rsync-module-publication | — | — | — | — | [25/2](../../../jobs/6324/2026-10-03__19-28-10/rsync-module-publication-bash-rhel9-6324) | — | — | — |
| samba-team-share | — | — | — | — | [21/0](../../../jobs/6324/2026-10-03__19-28-10/samba-team-share-bash-rhel9-6324) | — | — | — |
| smtp-alias-delivery | — | — | — | — | [28/0](../../../jobs/6324/2026-10-03__19-28-10/smtp-alias-delivery-bash-rhel9-6324) | — | — | — |
| snmp-readonly-monitoring | — | — | — | — | [10/0](../../../jobs/6324/2026-10-03__19-28-10/snmp-readonly-monitoring-bash-rhel9-6324) | — | — | — |
| ssh-forced-command-ingest | — | — | — | — | [28/0](../../../jobs/6324/2026-10-03__19-28-10/ssh-forced-command-ingest-bash-rhel9-6324) | — | — | — |
| ssh-local-service-tunnel | — | — | — | — | [34/4](../../../jobs/6324/2026-10-03__19-28-10/ssh-local-service-tunnel-bash-rhel9-6324) | — | — | — |
| tftp-firmware-distribution | — | — | — | — | [32/1](../../../jobs/6324/2026-10-03__19-28-10/tftp-firmware-distribution-bash-rhel9-6324) | — | — | — |
| udp-meter-ingestion | — | — | — | — | [21/2](../../../jobs/6324/2026-10-03__19-28-10/udp-meter-ingestion-bash-rhel9-6324) | — | — | — |
| **Average** | — | — | — | — | 28.5/1.2 | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | [4m 59s](../../../jobs/6324/2026-10-03__19-28-10/shared-nfs-storage-bash-rhel9-6324) | — | — | — |
| centralized-log-collector | — | — | — | — | [30m 23s](../../../jobs/6324/2026-10-03__19-28-10/centralized-log-collector-bash-rhel9-6324) | — | — | — |
| ssh-controller-access | — | — | — | — | [5m 07s](../../../jobs/6324/2026-10-03__19-28-10/ssh-controller-access-bash-rhel9-6324) | — | — | — |
| internal-ca-tls | — | — | — | — | [7m 12s](../../../jobs/6324/2026-10-03__19-28-10/internal-ca-tls-bash-rhel9-6324) | — | — | — |
| internal-time-sync | — | — | — | — | [4m 57s](../../../jobs/6324/2026-10-03__19-28-10/internal-time-sync-bash-rhel9-6324) | — | — | — |
| load-balanced-web-tier | — | — | — | — | [5m 12s](../../../jobs/6324/2026-10-03__19-28-10/load-balanced-web-tier-bash-rhel9-6324) | — | — | — |
| network-scoped-firewall | — | — | — | — | [5m 01s](../../../jobs/6324/2026-10-03__19-28-10/network-scoped-firewall-bash-rhel9-6324) | — | — | — |
| config-sync | — | — | — | — | [6m 04s](../../../jobs/6324/2026-10-03__19-28-10/config-sync-bash-rhel9-6324) | — | — | — |
| scheduled-backup | — | — | — | — | [5m 55s](../../../jobs/6324/2026-10-03__19-28-10/scheduled-backup-bash-rhel9-6324) | — | — | — |
| internal-dns-resolution | — | — | — | — | [4m 57s](../../../jobs/6324/2026-10-03__19-28-10/internal-dns-resolution-bash-rhel9-6324) | — | — | — |
| database-reader-writer-roles | — | — | — | — | [6m 56s](../../../jobs/6324/2026-10-03__19-28-10/database-reader-writer-roles-bash-rhel9-6324) | — | — | — |
| forward-proxy-destination-policy | — | — | — | — | [6m 38s](../../../jobs/6324/2026-10-03__19-28-10/forward-proxy-destination-policy-bash-rhel9-6324) | — | — | — |
| ftp-dropbox-confinement | — | — | — | — | [5m 13s](../../../jobs/6324/2026-10-03__19-28-10/ftp-dropbox-confinement-bash-rhel9-6324) | — | — | — |
| http-upload-size-boundary | — | — | — | — | [8m 05s](../../../jobs/6324/2026-10-03__19-28-10/http-upload-size-boundary-bash-rhel9-6324) | — | — | — |
| imap-maildir-cutover | — | — | — | — | [6m 49s](../../../jobs/6324/2026-10-03__19-28-10/imap-maildir-cutover-bash-rhel9-6324) | — | — | — |
| inetd-request-activation | — | — | — | — | [8m 11s](../../../jobs/6324/2026-10-03__19-28-10/inetd-request-activation-bash-rhel9-6324) | — | — | — |
| kerberos-service-identity | — | — | — | — | [7m 04s](../../../jobs/6324/2026-10-03__19-28-10/kerberos-service-identity-bash-rhel9-6324) | — | — | — |
| ldap-attribute-privacy | — | — | — | — | [7m 45s](../../../jobs/6324/2026-10-03__19-28-10/ldap-attribute-privacy-bash-rhel9-6324) | — | — | — |
| ldap-directory-import | — | — | — | — | [6m 03s](../../../jobs/6324/2026-10-03__19-28-10/ldap-directory-import-bash-rhel9-6324) | — | — | — |
| mysql-relational-import | — | — | — | — | [6m 46s](../../../jobs/6324/2026-10-03__19-28-10/mysql-relational-import-bash-rhel9-6324) | — | — | — |
| mysql-replication-catchup | — | — | — | — | [8m 30s](../../../jobs/6324/2026-10-03__19-28-10/mysql-replication-catchup-bash-rhel9-6324) | — | — | — |
| radius-network-authentication | — | — | — | — | [9m 33s](../../../jobs/6324/2026-10-03__19-28-10/radius-network-authentication-bash-rhel9-6324) | — | — | — |
| rsync-module-publication | — | — | — | — | [5m 55s](../../../jobs/6324/2026-10-03__19-28-10/rsync-module-publication-bash-rhel9-6324) | — | — | — |
| samba-team-share | — | — | — | — | [5m 50s](../../../jobs/6324/2026-10-03__19-28-10/samba-team-share-bash-rhel9-6324) | — | — | — |
| smtp-alias-delivery | — | — | — | — | [5m 33s](../../../jobs/6324/2026-10-03__19-28-10/smtp-alias-delivery-bash-rhel9-6324) | — | — | — |
| snmp-readonly-monitoring | — | — | — | — | [41m 34s](../../../jobs/6324/2026-10-03__19-28-10/snmp-readonly-monitoring-bash-rhel9-6324) | — | — | — |
| ssh-forced-command-ingest | — | — | — | — | [6m 42s](../../../jobs/6324/2026-10-03__19-28-10/ssh-forced-command-ingest-bash-rhel9-6324) | — | — | — |
| ssh-local-service-tunnel | — | — | — | — | [7m 20s](../../../jobs/6324/2026-10-03__19-28-10/ssh-local-service-tunnel-bash-rhel9-6324) | — | — | — |
| tftp-firmware-distribution | — | — | — | — | [6m 24s](../../../jobs/6324/2026-10-03__19-28-10/tftp-firmware-distribution-bash-rhel9-6324) | — | — | — |
| udp-meter-ingestion | — | — | — | — | [4m 55s](../../../jobs/6324/2026-10-03__19-28-10/udp-meter-ingestion-bash-rhel9-6324) | — | — | — |
| **Average** | — | — | — | — | 8m 23s | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 790 ms across 99 clusters, about 0.34% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/shared-nfs-storage-bash-rhel9-6324) | — | — | — |
| centralized-log-collector | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/centralized-log-collector-bash-rhel9-6324) | — | — | — |
| ssh-controller-access | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/ssh-controller-access-bash-rhel9-6324) | — | — | — |
| internal-ca-tls | — | — | — | — | [0.740](../../../jobs/6324/2026-10-03__19-28-10/internal-ca-tls-bash-rhel9-6324) | — | — | — |
| internal-time-sync | — | — | — | — | [0.960](../../../jobs/6324/2026-10-03__19-28-10/internal-time-sync-bash-rhel9-6324) | — | — | — |
| load-balanced-web-tier | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/load-balanced-web-tier-bash-rhel9-6324) | — | — | — |
| network-scoped-firewall | — | — | — | — | [0.920](../../../jobs/6324/2026-10-03__19-28-10/network-scoped-firewall-bash-rhel9-6324) | — | — | — |
| config-sync | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/config-sync-bash-rhel9-6324) | — | — | — |
| scheduled-backup | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/scheduled-backup-bash-rhel9-6324) | — | — | — |
| internal-dns-resolution | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/internal-dns-resolution-bash-rhel9-6324) | — | — | — |
| database-reader-writer-roles | — | — | — | — | [0.960](../../../jobs/6324/2026-10-03__19-28-10/database-reader-writer-roles-bash-rhel9-6324) | — | — | — |
| forward-proxy-destination-policy | — | — | — | — | [0.960](../../../jobs/6324/2026-10-03__19-28-10/forward-proxy-destination-policy-bash-rhel9-6324) | — | — | — |
| ftp-dropbox-confinement | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/ftp-dropbox-confinement-bash-rhel9-6324) | — | — | — |
| http-upload-size-boundary | — | — | — | — | [0.960](../../../jobs/6324/2026-10-03__19-28-10/http-upload-size-boundary-bash-rhel9-6324) | — | — | — |
| imap-maildir-cutover | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/imap-maildir-cutover-bash-rhel9-6324) | — | — | — |
| inetd-request-activation | — | — | — | — | [0.950](../../../jobs/6324/2026-10-03__19-28-10/inetd-request-activation-bash-rhel9-6324) | — | — | — |
| kerberos-service-identity | — | — | — | — | [0.910](../../../jobs/6324/2026-10-03__19-28-10/kerberos-service-identity-bash-rhel9-6324) | — | — | — |
| ldap-attribute-privacy | — | — | — | — | [0.720](../../../jobs/6324/2026-10-03__19-28-10/ldap-attribute-privacy-bash-rhel9-6324) | — | — | — |
| ldap-directory-import | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/ldap-directory-import-bash-rhel9-6324) | — | — | — |
| mysql-relational-import | — | — | — | — | [0.980](../../../jobs/6324/2026-10-03__19-28-10/mysql-relational-import-bash-rhel9-6324) | — | — | — |
| mysql-replication-catchup | — | — | — | — | [0.930](../../../jobs/6324/2026-10-03__19-28-10/mysql-replication-catchup-bash-rhel9-6324) | — | — | — |
| radius-network-authentication | — | — | — | — | [0.720](../../../jobs/6324/2026-10-03__19-28-10/radius-network-authentication-bash-rhel9-6324) | — | — | — |
| rsync-module-publication | — | — | — | — | [0.970](../../../jobs/6324/2026-10-03__19-28-10/rsync-module-publication-bash-rhel9-6324) | — | — | — |
| samba-team-share | — | — | — | — | [0.740](../../../jobs/6324/2026-10-03__19-28-10/samba-team-share-bash-rhel9-6324) | — | — | — |
| smtp-alias-delivery | — | — | — | — | [1.000](../../../jobs/6324/2026-10-03__19-28-10/smtp-alias-delivery-bash-rhel9-6324) | — | — | — |
| snmp-readonly-monitoring | — | — | — | — | [0.950](../../../jobs/6324/2026-10-03__19-28-10/snmp-readonly-monitoring-bash-rhel9-6324) | — | — | — |
| ssh-forced-command-ingest | — | — | — | — | [0.900](../../../jobs/6324/2026-10-03__19-28-10/ssh-forced-command-ingest-bash-rhel9-6324) | — | — | — |
| ssh-local-service-tunnel | — | — | — | — | [0.900](../../../jobs/6324/2026-10-03__19-28-10/ssh-local-service-tunnel-bash-rhel9-6324) | — | — | — |
| tftp-firmware-distribution | — | — | — | — | [0.930](../../../jobs/6324/2026-10-03__19-28-10/tftp-firmware-distribution-bash-rhel9-6324) | — | — | — |
| udp-meter-ingestion | — | — | — | — | [0.930](../../../jobs/6324/2026-10-03__19-28-10/udp-meter-ingestion-bash-rhel9-6324) | — | — | — |
| **Average** | — | — | — | — | 0.934 | — | — | — |
