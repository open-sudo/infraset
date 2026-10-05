# multi-node-os-comparison: command execution summary

Scope: `3922/2026-10-03__22-34-06`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [39/1](../../../jobs/3922/2026-10-03__22-34-06/shared-nfs-storage-bash-rhel10-3922) | — | — |
| centralized-log-collector | — | — | — | — | — | [27/0](../../../jobs/3922/2026-10-03__22-34-06/centralized-log-collector-bash-rhel10-3922) | — | — |
| ssh-controller-access | — | — | — | — | — | [22/0](../../../jobs/3922/2026-10-03__22-34-06/ssh-controller-access-bash-rhel10-3922) | — | — |
| internal-ca-tls | — | — | — | — | — | [28/1](../../../jobs/3922/2026-10-03__22-34-06/internal-ca-tls-bash-rhel10-3922) | — | — |
| internal-time-sync | — | — | — | — | — | [19/3](../../../jobs/3922/2026-10-03__22-34-06/internal-time-sync-bash-rhel10-3922) | — | — |
| load-balanced-web-tier | — | — | — | — | — | [39/0](../../../jobs/3922/2026-10-03__22-34-06/load-balanced-web-tier-bash-rhel10-3922) | — | — |
| network-scoped-firewall | — | — | — | — | — | [25/0](../../../jobs/3922/2026-10-03__22-34-06/network-scoped-firewall-bash-rhel10-3922) | — | — |
| config-sync | — | — | — | — | — | [26/2](../../../jobs/3922/2026-10-03__22-34-06/config-sync-bash-rhel10-3922) | — | — |
| scheduled-backup | — | — | — | — | — | [28/0](../../../jobs/3922/2026-10-03__22-34-06/scheduled-backup-bash-rhel10-3922) | — | — |
| internal-dns-resolution | — | — | — | — | — | [30/2](../../../jobs/3922/2026-10-03__22-34-06/internal-dns-resolution-bash-rhel10-3922) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [30/1](../../../jobs/3922/2026-10-03__22-34-06/database-reader-writer-roles-bash-rhel10-3922) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [25/0](../../../jobs/3922/2026-10-03__22-34-06/forward-proxy-destination-policy-bash-rhel10-3922) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [43/1](../../../jobs/3922/2026-10-03__22-34-06/ftp-dropbox-confinement-bash-rhel10-3922) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [25/0](../../../jobs/3922/2026-10-03__22-34-06/http-upload-size-boundary-bash-rhel10-3922) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [26/1](../../../jobs/3922/2026-10-03__22-34-06/imap-maildir-cutover-bash-rhel10-3922) | — | — |
| inetd-request-activation | — | — | — | — | — | [38/0](../../../jobs/3922/2026-10-03__22-34-06/inetd-request-activation-bash-rhel10-3922) | — | — |
| kerberos-service-identity | — | — | — | — | — | [29/0](../../../jobs/3922/2026-10-03__22-34-06/kerberos-service-identity-bash-rhel10-3922) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [35/2](../../../jobs/3922/2026-10-03__22-34-06/ldap-attribute-privacy-bash-rhel10-3922) | — | — |
| ldap-directory-import | — | — | — | — | — | [34/3](../../../jobs/3922/2026-10-03__22-34-06/ldap-directory-import-bash-rhel10-3922) | — | — |
| mysql-relational-import | — | — | — | — | — | [32/0](../../../jobs/3922/2026-10-03__22-34-06/mysql-relational-import-bash-rhel10-3922) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [33/0](../../../jobs/3922/2026-10-03__22-34-06/mysql-replication-catchup-bash-rhel10-3922) | — | — |
| radius-network-authentication | — | — | — | — | — | [32/4](../../../jobs/3922/2026-10-03__22-34-06/radius-network-authentication-bash-rhel10-3922) | — | — |
| rsync-module-publication | — | — | — | — | — | [33/1](../../../jobs/3922/2026-10-03__22-34-06/rsync-module-publication-bash-rhel10-3922) | — | — |
| samba-team-share | — | — | — | — | — | [32/1](../../../jobs/3922/2026-10-03__22-34-06/samba-team-share-bash-rhel10-3922) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [26/0](../../../jobs/3922/2026-10-03__22-34-06/smtp-alias-delivery-bash-rhel10-3922) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [24/1](../../../jobs/3922/2026-10-03__22-34-06/snmp-readonly-monitoring-bash-rhel10-3922) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [28/1](../../../jobs/3922/2026-10-03__22-34-06/ssh-forced-command-ingest-bash-rhel10-3922) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [39/5](../../../jobs/3922/2026-10-03__22-34-06/ssh-local-service-tunnel-bash-rhel10-3922) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [24/3](../../../jobs/3922/2026-10-03__22-34-06/tftp-firmware-distribution-bash-rhel10-3922) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [30/3](../../../jobs/3922/2026-10-03__22-34-06/udp-meter-ingestion-bash-rhel10-3922) | — | — |
| **Average** | — | — | — | — | — | 30.0/1.2 | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [4m 50s](../../../jobs/3922/2026-10-03__22-34-06/shared-nfs-storage-bash-rhel10-3922) | — | — |
| centralized-log-collector | — | — | — | — | — | [4m 51s](../../../jobs/3922/2026-10-03__22-34-06/centralized-log-collector-bash-rhel10-3922) | — | — |
| ssh-controller-access | — | — | — | — | — | [4m 36s](../../../jobs/3922/2026-10-03__22-34-06/ssh-controller-access-bash-rhel10-3922) | — | — |
| internal-ca-tls | — | — | — | — | — | [6m 30s](../../../jobs/3922/2026-10-03__22-34-06/internal-ca-tls-bash-rhel10-3922) | — | — |
| internal-time-sync | — | — | — | — | — | [5m 03s](../../../jobs/3922/2026-10-03__22-34-06/internal-time-sync-bash-rhel10-3922) | — | — |
| load-balanced-web-tier | — | — | — | — | — | [5m 39s](../../../jobs/3922/2026-10-03__22-34-06/load-balanced-web-tier-bash-rhel10-3922) | — | — |
| network-scoped-firewall | — | — | — | — | — | [5m 52s](../../../jobs/3922/2026-10-03__22-34-06/network-scoped-firewall-bash-rhel10-3922) | — | — |
| config-sync | — | — | — | — | — | [5m 19s](../../../jobs/3922/2026-10-03__22-34-06/config-sync-bash-rhel10-3922) | — | — |
| scheduled-backup | — | — | — | — | — | [5m 19s](../../../jobs/3922/2026-10-03__22-34-06/scheduled-backup-bash-rhel10-3922) | — | — |
| internal-dns-resolution | — | — | — | — | — | [5m 18s](../../../jobs/3922/2026-10-03__22-34-06/internal-dns-resolution-bash-rhel10-3922) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [6m 26s](../../../jobs/3922/2026-10-03__22-34-06/database-reader-writer-roles-bash-rhel10-3922) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [4m 50s](../../../jobs/3922/2026-10-03__22-34-06/forward-proxy-destination-policy-bash-rhel10-3922) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [8m 08s](../../../jobs/3922/2026-10-03__22-34-06/ftp-dropbox-confinement-bash-rhel10-3922) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [6m 47s](../../../jobs/3922/2026-10-03__22-34-06/http-upload-size-boundary-bash-rhel10-3922) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [4m 31s](../../../jobs/3922/2026-10-03__22-34-06/imap-maildir-cutover-bash-rhel10-3922) | — | — |
| inetd-request-activation | — | — | — | — | — | [9m 14s](../../../jobs/3922/2026-10-03__22-34-06/inetd-request-activation-bash-rhel10-3922) | — | — |
| kerberos-service-identity | — | — | — | — | — | [6m 16s](../../../jobs/3922/2026-10-03__22-34-06/kerberos-service-identity-bash-rhel10-3922) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [7m 53s](../../../jobs/3922/2026-10-03__22-34-06/ldap-attribute-privacy-bash-rhel10-3922) | — | — |
| ldap-directory-import | — | — | — | — | — | [5m 58s](../../../jobs/3922/2026-10-03__22-34-06/ldap-directory-import-bash-rhel10-3922) | — | — |
| mysql-relational-import | — | — | — | — | — | [5m 59s](../../../jobs/3922/2026-10-03__22-34-06/mysql-relational-import-bash-rhel10-3922) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [7m 52s](../../../jobs/3922/2026-10-03__22-34-06/mysql-replication-catchup-bash-rhel10-3922) | — | — |
| radius-network-authentication | — | — | — | — | — | [8m 44s](../../../jobs/3922/2026-10-03__22-34-06/radius-network-authentication-bash-rhel10-3922) | — | — |
| rsync-module-publication | — | — | — | — | — | [6m 07s](../../../jobs/3922/2026-10-03__22-34-06/rsync-module-publication-bash-rhel10-3922) | — | — |
| samba-team-share | — | — | — | — | — | [5m 37s](../../../jobs/3922/2026-10-03__22-34-06/samba-team-share-bash-rhel10-3922) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [4m 31s](../../../jobs/3922/2026-10-03__22-34-06/smtp-alias-delivery-bash-rhel10-3922) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [5m 12s](../../../jobs/3922/2026-10-03__22-34-06/snmp-readonly-monitoring-bash-rhel10-3922) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [6m 39s](../../../jobs/3922/2026-10-03__22-34-06/ssh-forced-command-ingest-bash-rhel10-3922) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [7m 56s](../../../jobs/3922/2026-10-03__22-34-06/ssh-local-service-tunnel-bash-rhel10-3922) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [7m 36s](../../../jobs/3922/2026-10-03__22-34-06/tftp-firmware-distribution-bash-rhel10-3922) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [5m 54s](../../../jobs/3922/2026-10-03__22-34-06/udp-meter-ingestion-bash-rhel10-3922) | — | — |
| **Average** | — | — | — | — | — | 6m 11s | — | — |

Cluster provisioning is not a meaningful part of these times: median 846 ms across 100 clusters, about 0.37% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [0.900](../../../jobs/3922/2026-10-03__22-34-06/shared-nfs-storage-bash-rhel10-3922) | — | — |
| centralized-log-collector | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/centralized-log-collector-bash-rhel10-3922) | — | — |
| ssh-controller-access | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/ssh-controller-access-bash-rhel10-3922) | — | — |
| internal-ca-tls | — | — | — | — | — | [0.780](../../../jobs/3922/2026-10-03__22-34-06/internal-ca-tls-bash-rhel10-3922) | — | — |
| internal-time-sync | — | — | — | — | — | [0.880](../../../jobs/3922/2026-10-03__22-34-06/internal-time-sync-bash-rhel10-3922) | — | — |
| load-balanced-web-tier | — | — | — | — | — | [0.960](../../../jobs/3922/2026-10-03__22-34-06/load-balanced-web-tier-bash-rhel10-3922) | — | — |
| network-scoped-firewall | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/network-scoped-firewall-bash-rhel10-3922) | — | — |
| config-sync | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/config-sync-bash-rhel10-3922) | — | — |
| scheduled-backup | — | — | — | — | — | [0.990](../../../jobs/3922/2026-10-03__22-34-06/scheduled-backup-bash-rhel10-3922) | — | — |
| internal-dns-resolution | — | — | — | — | — | [0.780](../../../jobs/3922/2026-10-03__22-34-06/internal-dns-resolution-bash-rhel10-3922) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [0.840](../../../jobs/3922/2026-10-03__22-34-06/database-reader-writer-roles-bash-rhel10-3922) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [0.960](../../../jobs/3922/2026-10-03__22-34-06/forward-proxy-destination-policy-bash-rhel10-3922) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/ftp-dropbox-confinement-bash-rhel10-3922) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [0.900](../../../jobs/3922/2026-10-03__22-34-06/http-upload-size-boundary-bash-rhel10-3922) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [0.780](../../../jobs/3922/2026-10-03__22-34-06/imap-maildir-cutover-bash-rhel10-3922) | — | — |
| inetd-request-activation | — | — | — | — | — | [0.770](../../../jobs/3922/2026-10-03__22-34-06/inetd-request-activation-bash-rhel10-3922) | — | — |
| kerberos-service-identity | — | — | — | — | — | [0.700](../../../jobs/3922/2026-10-03__22-34-06/kerberos-service-identity-bash-rhel10-3922) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [0.840](../../../jobs/3922/2026-10-03__22-34-06/ldap-attribute-privacy-bash-rhel10-3922) | — | — |
| ldap-directory-import | — | — | — | — | — | [0.990](../../../jobs/3922/2026-10-03__22-34-06/ldap-directory-import-bash-rhel10-3922) | — | — |
| mysql-relational-import | — | — | — | — | — | [0.840](../../../jobs/3922/2026-10-03__22-34-06/mysql-relational-import-bash-rhel10-3922) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/mysql-replication-catchup-bash-rhel10-3922) | — | — |
| radius-network-authentication | — | — | — | — | — | [0.910](../../../jobs/3922/2026-10-03__22-34-06/radius-network-authentication-bash-rhel10-3922) | — | — |
| rsync-module-publication | — | — | — | — | — | [0.820](../../../jobs/3922/2026-10-03__22-34-06/rsync-module-publication-bash-rhel10-3922) | — | — |
| samba-team-share | — | — | — | — | — | [0.920](../../../jobs/3922/2026-10-03__22-34-06/samba-team-share-bash-rhel10-3922) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [0.960](../../../jobs/3922/2026-10-03__22-34-06/smtp-alias-delivery-bash-rhel10-3922) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [0.990](../../../jobs/3922/2026-10-03__22-34-06/snmp-readonly-monitoring-bash-rhel10-3922) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [0.900](../../../jobs/3922/2026-10-03__22-34-06/ssh-forced-command-ingest-bash-rhel10-3922) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [0.820](../../../jobs/3922/2026-10-03__22-34-06/ssh-local-service-tunnel-bash-rhel10-3922) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [0.920](../../../jobs/3922/2026-10-03__22-34-06/tftp-firmware-distribution-bash-rhel10-3922) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [1.000](../../../jobs/3922/2026-10-03__22-34-06/udp-meter-ingestion-bash-rhel10-3922) | — | — |
| **Average** | — | — | — | — | — | 0.905 | — | — |
