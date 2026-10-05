# multi-node-os-comparison: command execution summary

Scope: `9622/2026-10-04__09-20-16`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | [25/2](../../../jobs/9622/2026-10-04__09-20-16/shared-nfs-storage-bash-almalinux9-9622) | — | — | — | — | — | — |
| centralized-log-collector | — | [23/0](../../../jobs/9622/2026-10-04__09-20-16/centralized-log-collector-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-controller-access | — | [18/0](../../../jobs/9622/2026-10-04__09-20-16/ssh-controller-access-bash-almalinux9-9622) | — | — | — | — | — | — |
| internal-ca-tls | — | [22/1](../../../jobs/9622/2026-10-04__09-20-16/internal-ca-tls-bash-almalinux9-9622) | — | — | — | — | — | — |
| internal-time-sync | — | [23/1](../../../jobs/9622/2026-10-04__09-20-16/internal-time-sync-bash-almalinux9-9622) | — | — | — | — | — | — |
| load-balanced-web-tier | — | [34/3](../../../jobs/9622/2026-10-04__09-20-16/load-balanced-web-tier-bash-almalinux9-9622) | — | — | — | — | — | — |
| network-scoped-firewall | — | [35/0](../../../jobs/9622/2026-10-04__09-20-16/network-scoped-firewall-bash-almalinux9-9622) | — | — | — | — | — | — |
| config-sync | — | [26/0](../../../jobs/9622/2026-10-04__09-20-16/config-sync-bash-almalinux9-9622) | — | — | — | — | — | — |
| scheduled-backup | — | [22/0](../../../jobs/9622/2026-10-04__09-20-16/scheduled-backup-bash-almalinux9-9622) | — | — | — | — | — | — |
| internal-dns-resolution | — | [30/3](../../../jobs/9622/2026-10-04__09-20-16/internal-dns-resolution-bash-almalinux9-9622) | — | — | — | — | — | — |
| database-reader-writer-roles | — | [25/0](../../../jobs/9622/2026-10-04__09-20-16/database-reader-writer-roles-bash-almalinux9-9622) | — | — | — | — | — | — |
| forward-proxy-destination-policy | — | [24/0](../../../jobs/9622/2026-10-04__09-20-16/forward-proxy-destination-policy-bash-almalinux9-9622) | — | — | — | — | — | — |
| ftp-dropbox-confinement | — | [25/2](../../../jobs/9622/2026-10-04__09-20-16/ftp-dropbox-confinement-bash-almalinux9-9622) | — | — | — | — | — | — |
| http-upload-size-boundary | — | [30/0](../../../jobs/9622/2026-10-04__09-20-16/http-upload-size-boundary-bash-almalinux9-9622) | — | — | — | — | — | — |
| imap-maildir-cutover | — | [19/1](../../../jobs/9622/2026-10-04__09-20-16/imap-maildir-cutover-bash-almalinux9-9622) | — | — | — | — | — | — |
| inetd-request-activation | — | [32/4](../../../jobs/9622/2026-10-04__09-20-16/inetd-request-activation-bash-almalinux9-9622) | — | — | — | — | — | — |
| kerberos-service-identity | — | [31/2](../../../jobs/9622/2026-10-04__09-20-16/kerberos-service-identity-bash-almalinux9-9622) | — | — | — | — | — | — |
| ldap-attribute-privacy | — | [40/5](../../../jobs/9622/2026-10-04__09-20-16/ldap-attribute-privacy-bash-almalinux9-9622) | — | — | — | — | — | — |
| ldap-directory-import | — | [26/4](../../../jobs/9622/2026-10-04__09-20-16/ldap-directory-import-bash-almalinux9-9622) | — | — | — | — | — | — |
| mysql-relational-import | — | [25/0](../../../jobs/9622/2026-10-04__09-20-16/mysql-relational-import-bash-almalinux9-9622) | — | — | — | — | — | — |
| mysql-replication-catchup | — | [37/0](../../../jobs/9622/2026-10-04__09-20-16/mysql-replication-catchup-bash-almalinux9-9622) | — | — | — | — | — | — |
| radius-network-authentication | — | [41/1](../../../jobs/9622/2026-10-04__09-20-16/radius-network-authentication-bash-almalinux9-9622) | — | — | — | — | — | — |
| rsync-module-publication | — | [21/1](../../../jobs/9622/2026-10-04__09-20-16/rsync-module-publication-bash-almalinux9-9622) | — | — | — | — | — | — |
| samba-team-share | — | [21/0](../../../jobs/9622/2026-10-04__09-20-16/samba-team-share-bash-almalinux9-9622) | — | — | — | — | — | — |
| smtp-alias-delivery | — | [22/1](../../../jobs/9622/2026-10-04__09-20-16/smtp-alias-delivery-bash-almalinux9-9622) | — | — | — | — | — | — |
| snmp-readonly-monitoring | — | [23/0](../../../jobs/9622/2026-10-04__09-20-16/snmp-readonly-monitoring-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-forced-command-ingest | — | [23/0](../../../jobs/9622/2026-10-04__09-20-16/ssh-forced-command-ingest-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-local-service-tunnel | — | [31/0](../../../jobs/9622/2026-10-04__09-20-16/ssh-local-service-tunnel-bash-almalinux9-9622) | — | — | — | — | — | — |
| tftp-firmware-distribution | — | [23/3](../../../jobs/9622/2026-10-04__09-20-16/tftp-firmware-distribution-bash-almalinux9-9622) | — | — | — | — | — | — |
| udp-meter-ingestion | — | [23/3](../../../jobs/9622/2026-10-04__09-20-16/udp-meter-ingestion-bash-almalinux9-9622) | — | — | — | — | — | — |
| **Average** | — | 26.7/1.2 | — | — | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | [5m 35s](../../../jobs/9622/2026-10-04__09-20-16/shared-nfs-storage-bash-almalinux9-9622) | — | — | — | — | — | — |
| centralized-log-collector | — | [3m 33s](../../../jobs/9622/2026-10-04__09-20-16/centralized-log-collector-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-controller-access | — | [3m 49s](../../../jobs/9622/2026-10-04__09-20-16/ssh-controller-access-bash-almalinux9-9622) | — | — | — | — | — | — |
| internal-ca-tls | — | [5m 18s](../../../jobs/9622/2026-10-04__09-20-16/internal-ca-tls-bash-almalinux9-9622) | — | — | — | — | — | — |
| internal-time-sync | — | [4m 56s](../../../jobs/9622/2026-10-04__09-20-16/internal-time-sync-bash-almalinux9-9622) | — | — | — | — | — | — |
| load-balanced-web-tier | — | [12m 19s](../../../jobs/9622/2026-10-04__09-20-16/load-balanced-web-tier-bash-almalinux9-9622) | — | — | — | — | — | — |
| network-scoped-firewall | — | [5m 32s](../../../jobs/9622/2026-10-04__09-20-16/network-scoped-firewall-bash-almalinux9-9622) | — | — | — | — | — | — |
| config-sync | — | [6m 35s](../../../jobs/9622/2026-10-04__09-20-16/config-sync-bash-almalinux9-9622) | — | — | — | — | — | — |
| scheduled-backup | — | [4m 59s](../../../jobs/9622/2026-10-04__09-20-16/scheduled-backup-bash-almalinux9-9622) | — | — | — | — | — | — |
| internal-dns-resolution | — | [5m 34s](../../../jobs/9622/2026-10-04__09-20-16/internal-dns-resolution-bash-almalinux9-9622) | — | — | — | — | — | — |
| database-reader-writer-roles | — | [5m 50s](../../../jobs/9622/2026-10-04__09-20-16/database-reader-writer-roles-bash-almalinux9-9622) | — | — | — | — | — | — |
| forward-proxy-destination-policy | — | [5m 45s](../../../jobs/9622/2026-10-04__09-20-16/forward-proxy-destination-policy-bash-almalinux9-9622) | — | — | — | — | — | — |
| ftp-dropbox-confinement | — | [6m 31s](../../../jobs/9622/2026-10-04__09-20-16/ftp-dropbox-confinement-bash-almalinux9-9622) | — | — | — | — | — | — |
| http-upload-size-boundary | — | [6m 08s](../../../jobs/9622/2026-10-04__09-20-16/http-upload-size-boundary-bash-almalinux9-9622) | — | — | — | — | — | — |
| imap-maildir-cutover | — | [5m 17s](../../../jobs/9622/2026-10-04__09-20-16/imap-maildir-cutover-bash-almalinux9-9622) | — | — | — | — | — | — |
| inetd-request-activation | — | [7m 12s](../../../jobs/9622/2026-10-04__09-20-16/inetd-request-activation-bash-almalinux9-9622) | — | — | — | — | — | — |
| kerberos-service-identity | — | [6m 35s](../../../jobs/9622/2026-10-04__09-20-16/kerberos-service-identity-bash-almalinux9-9622) | — | — | — | — | — | — |
| ldap-attribute-privacy | — | [10m 01s](../../../jobs/9622/2026-10-04__09-20-16/ldap-attribute-privacy-bash-almalinux9-9622) | — | — | — | — | — | — |
| ldap-directory-import | — | [6m 41s](../../../jobs/9622/2026-10-04__09-20-16/ldap-directory-import-bash-almalinux9-9622) | — | — | — | — | — | — |
| mysql-relational-import | — | [7m 34s](../../../jobs/9622/2026-10-04__09-20-16/mysql-relational-import-bash-almalinux9-9622) | — | — | — | — | — | — |
| mysql-replication-catchup | — | [8m 26s](../../../jobs/9622/2026-10-04__09-20-16/mysql-replication-catchup-bash-almalinux9-9622) | — | — | — | — | — | — |
| radius-network-authentication | — | [7m 11s](../../../jobs/9622/2026-10-04__09-20-16/radius-network-authentication-bash-almalinux9-9622) | — | — | — | — | — | — |
| rsync-module-publication | — | [8m 48s](../../../jobs/9622/2026-10-04__09-20-16/rsync-module-publication-bash-almalinux9-9622) | — | — | — | — | — | — |
| samba-team-share | — | [5m 18s](../../../jobs/9622/2026-10-04__09-20-16/samba-team-share-bash-almalinux9-9622) | — | — | — | — | — | — |
| smtp-alias-delivery | — | [4m 06s](../../../jobs/9622/2026-10-04__09-20-16/smtp-alias-delivery-bash-almalinux9-9622) | — | — | — | — | — | — |
| snmp-readonly-monitoring | — | [5m 30s](../../../jobs/9622/2026-10-04__09-20-16/snmp-readonly-monitoring-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-forced-command-ingest | — | [5m 13s](../../../jobs/9622/2026-10-04__09-20-16/ssh-forced-command-ingest-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-local-service-tunnel | — | [6m 37s](../../../jobs/9622/2026-10-04__09-20-16/ssh-local-service-tunnel-bash-almalinux9-9622) | — | — | — | — | — | — |
| tftp-firmware-distribution | — | [6m 13s](../../../jobs/9622/2026-10-04__09-20-16/tftp-firmware-distribution-bash-almalinux9-9622) | — | — | — | — | — | — |
| udp-meter-ingestion | — | [5m 45s](../../../jobs/9622/2026-10-04__09-20-16/udp-meter-ingestion-bash-almalinux9-9622) | — | — | — | — | — | — |
| **Average** | — | 6m 18s | — | — | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 1116 ms across 100 clusters, about 0.49% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/shared-nfs-storage-bash-almalinux9-9622) | — | — | — | — | — | — |
| centralized-log-collector | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/centralized-log-collector-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-controller-access | — | [0.970](../../../jobs/9622/2026-10-04__09-20-16/ssh-controller-access-bash-almalinux9-9622) | — | — | — | — | — | — |
| internal-ca-tls | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/internal-ca-tls-bash-almalinux9-9622) | — | — | — | — | — | — |
| internal-time-sync | — | [0.860](../../../jobs/9622/2026-10-04__09-20-16/internal-time-sync-bash-almalinux9-9622) | — | — | — | — | — | — |
| load-balanced-web-tier | — | [0.840](../../../jobs/9622/2026-10-04__09-20-16/load-balanced-web-tier-bash-almalinux9-9622) | — | — | — | — | — | — |
| network-scoped-firewall | — | [0.960](../../../jobs/9622/2026-10-04__09-20-16/network-scoped-firewall-bash-almalinux9-9622) | — | — | — | — | — | — |
| config-sync | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/config-sync-bash-almalinux9-9622) | — | — | — | — | — | — |
| scheduled-backup | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/scheduled-backup-bash-almalinux9-9622) | — | — | — | — | — | — |
| internal-dns-resolution | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/internal-dns-resolution-bash-almalinux9-9622) | — | — | — | — | — | — |
| database-reader-writer-roles | — | [0.960](../../../jobs/9622/2026-10-04__09-20-16/database-reader-writer-roles-bash-almalinux9-9622) | — | — | — | — | — | — |
| forward-proxy-destination-policy | — | [0.970](../../../jobs/9622/2026-10-04__09-20-16/forward-proxy-destination-policy-bash-almalinux9-9622) | — | — | — | — | — | — |
| ftp-dropbox-confinement | — | [0.900](../../../jobs/9622/2026-10-04__09-20-16/ftp-dropbox-confinement-bash-almalinux9-9622) | — | — | — | — | — | — |
| http-upload-size-boundary | — | [0.900](../../../jobs/9622/2026-10-04__09-20-16/http-upload-size-boundary-bash-almalinux9-9622) | — | — | — | — | — | — |
| imap-maildir-cutover | — | [0.880](../../../jobs/9622/2026-10-04__09-20-16/imap-maildir-cutover-bash-almalinux9-9622) | — | — | — | — | — | — |
| inetd-request-activation | — | [0.940](../../../jobs/9622/2026-10-04__09-20-16/inetd-request-activation-bash-almalinux9-9622) | — | — | — | — | — | — |
| kerberos-service-identity | — | [0.960](../../../jobs/9622/2026-10-04__09-20-16/kerberos-service-identity-bash-almalinux9-9622) | — | — | — | — | — | — |
| ldap-attribute-privacy | — | [0.760](../../../jobs/9622/2026-10-04__09-20-16/ldap-attribute-privacy-bash-almalinux9-9622) | — | — | — | — | — | — |
| ldap-directory-import | — | [0.680](../../../jobs/9622/2026-10-04__09-20-16/ldap-directory-import-bash-almalinux9-9622) | — | — | — | — | — | — |
| mysql-relational-import | — | [0.800](../../../jobs/9622/2026-10-04__09-20-16/mysql-relational-import-bash-almalinux9-9622) | — | — | — | — | — | — |
| mysql-replication-catchup | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/mysql-replication-catchup-bash-almalinux9-9622) | — | — | — | — | — | — |
| radius-network-authentication | — | [0.820](../../../jobs/9622/2026-10-04__09-20-16/radius-network-authentication-bash-almalinux9-9622) | — | — | — | — | — | — |
| rsync-module-publication | — | [0.930](../../../jobs/9622/2026-10-04__09-20-16/rsync-module-publication-bash-almalinux9-9622) | — | — | — | — | — | — |
| samba-team-share | — | [0.780](../../../jobs/9622/2026-10-04__09-20-16/samba-team-share-bash-almalinux9-9622) | — | — | — | — | — | — |
| smtp-alias-delivery | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/smtp-alias-delivery-bash-almalinux9-9622) | — | — | — | — | — | — |
| snmp-readonly-monitoring | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/snmp-readonly-monitoring-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-forced-command-ingest | — | [0.970](../../../jobs/9622/2026-10-04__09-20-16/ssh-forced-command-ingest-bash-almalinux9-9622) | — | — | — | — | — | — |
| ssh-local-service-tunnel | — | [0.920](../../../jobs/9622/2026-10-04__09-20-16/ssh-local-service-tunnel-bash-almalinux9-9622) | — | — | — | — | — | — |
| tftp-firmware-distribution | — | [0.780](../../../jobs/9622/2026-10-04__09-20-16/tftp-firmware-distribution-bash-almalinux9-9622) | — | — | — | — | — | — |
| udp-meter-ingestion | — | [1.000](../../../jobs/9622/2026-10-04__09-20-16/udp-meter-ingestion-bash-almalinux9-9622) | — | — | — | — | — | — |
| **Average** | — | 0.919 | — | — | — | — | — | — |
