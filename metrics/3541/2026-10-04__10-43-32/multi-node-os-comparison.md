# multi-node-os-comparison: command execution summary

Scope: `3541/2026-10-04__10-43-32`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | [24/6](../../../jobs/3541/2026-10-04__10-43-32/shared-nfs-storage-bash-ubuntu16-3541) | — |
| centralized-log-collector | — | — | — | — | — | — | [25/4](../../../jobs/3541/2026-10-04__10-43-32/centralized-log-collector-bash-ubuntu16-3541) | — |
| ssh-controller-access | — | — | — | — | — | — | [14/4](../../../jobs/3541/2026-10-04__10-43-32/ssh-controller-access-bash-ubuntu16-3541) | — |
| internal-ca-tls | — | — | — | — | — | — | [24/8](../../../jobs/3541/2026-10-04__10-43-32/internal-ca-tls-bash-ubuntu16-3541) | — |
| internal-time-sync | — | — | — | — | — | — | [34/3](../../../jobs/3541/2026-10-04__10-43-32/internal-time-sync-bash-ubuntu16-3541) | — |
| load-balanced-web-tier | — | — | — | — | — | — | [32/5](../../../jobs/3541/2026-10-04__10-43-32/load-balanced-web-tier-bash-ubuntu16-3541) | — |
| network-scoped-firewall | — | — | — | — | — | — | [44/7](../../../jobs/3541/2026-10-04__10-43-32/network-scoped-firewall-bash-ubuntu16-3541) | — |
| config-sync | — | — | — | — | — | — | [27/2](../../../jobs/3541/2026-10-04__10-43-32/config-sync-bash-ubuntu16-3541) | — |
| scheduled-backup | — | — | — | — | — | — | [20/3](../../../jobs/3541/2026-10-04__10-43-32/scheduled-backup-bash-ubuntu16-3541) | — |
| internal-dns-resolution | — | — | — | — | — | — | [19/2](../../../jobs/3541/2026-10-04__10-43-32/internal-dns-resolution-bash-ubuntu16-3541) | — |
| database-reader-writer-roles | — | — | — | — | — | — | [25/0](../../../jobs/3541/2026-10-04__10-43-32/database-reader-writer-roles-bash-ubuntu16-3541) | — |
| forward-proxy-destination-policy | — | — | — | — | — | — | [22/9](../../../jobs/3541/2026-10-04__10-43-32/forward-proxy-destination-policy-bash-ubuntu16-3541) | — |
| ftp-dropbox-confinement | — | — | — | — | — | — | [21/4](../../../jobs/3541/2026-10-04__10-43-32/ftp-dropbox-confinement-bash-ubuntu16-3541) | — |
| http-upload-size-boundary | — | — | — | — | — | — | [26/4](../../../jobs/3541/2026-10-04__10-43-32/http-upload-size-boundary-bash-ubuntu16-3541) | — |
| imap-maildir-cutover | — | — | — | — | — | — | [19/5](../../../jobs/3541/2026-10-04__10-43-32/imap-maildir-cutover-bash-ubuntu16-3541) | — |
| inetd-request-activation | — | — | — | — | — | — | [25/3](../../../jobs/3541/2026-10-04__10-43-32/inetd-request-activation-bash-ubuntu16-3541) | — |
| kerberos-service-identity | — | — | — | — | — | — | [27/5](../../../jobs/3541/2026-10-04__10-43-32/kerberos-service-identity-bash-ubuntu16-3541) | — |
| ldap-attribute-privacy | — | — | — | — | — | — | [24/4](../../../jobs/3541/2026-10-04__10-43-32/ldap-attribute-privacy-bash-ubuntu16-3541) | — |
| ldap-directory-import | — | — | — | — | — | — | [20/4](../../../jobs/3541/2026-10-04__10-43-32/ldap-directory-import-bash-ubuntu16-3541) | — |
| mysql-relational-import | — | — | — | — | — | — | [31/3](../../../jobs/3541/2026-10-04__10-43-32/mysql-relational-import-bash-ubuntu16-3541) | — |
| mysql-replication-catchup | — | — | — | — | — | — | [45/10](../../../jobs/3541/2026-10-04__10-43-32/mysql-replication-catchup-bash-ubuntu16-3541) | — |
| radius-network-authentication | — | — | — | — | — | — | [26/3](../../../jobs/3541/2026-10-04__10-43-32/radius-network-authentication-bash-ubuntu16-3541) | — |
| rsync-module-publication | — | — | — | — | — | — | [21/4](../../../jobs/3541/2026-10-04__10-43-32/rsync-module-publication-bash-ubuntu16-3541) | — |
| samba-team-share | — | — | — | — | — | — | [20/6](../../../jobs/3541/2026-10-04__10-43-32/samba-team-share-bash-ubuntu16-3541) | — |
| smtp-alias-delivery | — | — | — | — | — | — | [35/2](../../../jobs/3541/2026-10-04__10-43-32/smtp-alias-delivery-bash-ubuntu16-3541) | — |
| snmp-readonly-monitoring | — | — | — | — | — | — | [23/4](../../../jobs/3541/2026-10-04__10-43-32/snmp-readonly-monitoring-bash-ubuntu16-3541) | — |
| ssh-forced-command-ingest | — | — | — | — | — | — | [26/4](../../../jobs/3541/2026-10-04__10-43-32/ssh-forced-command-ingest-bash-ubuntu16-3541) | — |
| ssh-local-service-tunnel | — | — | — | — | — | — | [24/7](../../../jobs/3541/2026-10-04__10-43-32/ssh-local-service-tunnel-bash-ubuntu16-3541) | — |
| tftp-firmware-distribution | — | — | — | — | — | — | [18/4](../../../jobs/3541/2026-10-04__10-43-32/tftp-firmware-distribution-bash-ubuntu16-3541) | — |
| udp-meter-ingestion | — | — | — | — | — | — | [24/3](../../../jobs/3541/2026-10-04__10-43-32/udp-meter-ingestion-bash-ubuntu16-3541) | — |
| **Average** | — | — | — | — | — | — | 25.5/4.4 | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | [7m 59s](../../../jobs/3541/2026-10-04__10-43-32/shared-nfs-storage-bash-ubuntu16-3541) | — |
| centralized-log-collector | — | — | — | — | — | — | [5m 45s](../../../jobs/3541/2026-10-04__10-43-32/centralized-log-collector-bash-ubuntu16-3541) | — |
| ssh-controller-access | — | — | — | — | — | — | [3m 58s](../../../jobs/3541/2026-10-04__10-43-32/ssh-controller-access-bash-ubuntu16-3541) | — |
| internal-ca-tls | — | — | — | — | — | — | [6m 33s](../../../jobs/3541/2026-10-04__10-43-32/internal-ca-tls-bash-ubuntu16-3541) | — |
| internal-time-sync | — | — | — | — | — | — | [12m 49s](../../../jobs/3541/2026-10-04__10-43-32/internal-time-sync-bash-ubuntu16-3541) | — |
| load-balanced-web-tier | — | — | — | — | — | — | [4m 55s](../../../jobs/3541/2026-10-04__10-43-32/load-balanced-web-tier-bash-ubuntu16-3541) | — |
| network-scoped-firewall | — | — | — | — | — | — | [8m 02s](../../../jobs/3541/2026-10-04__10-43-32/network-scoped-firewall-bash-ubuntu16-3541) | — |
| config-sync | — | — | — | — | — | — | [5m 50s](../../../jobs/3541/2026-10-04__10-43-32/config-sync-bash-ubuntu16-3541) | — |
| scheduled-backup | — | — | — | — | — | — | [4m 02s](../../../jobs/3541/2026-10-04__10-43-32/scheduled-backup-bash-ubuntu16-3541) | — |
| internal-dns-resolution | — | — | — | — | — | — | [3m 43s](../../../jobs/3541/2026-10-04__10-43-32/internal-dns-resolution-bash-ubuntu16-3541) | — |
| database-reader-writer-roles | — | — | — | — | — | — | [7m 34s](../../../jobs/3541/2026-10-04__10-43-32/database-reader-writer-roles-bash-ubuntu16-3541) | — |
| forward-proxy-destination-policy | — | — | — | — | — | — | [6m 17s](../../../jobs/3541/2026-10-04__10-43-32/forward-proxy-destination-policy-bash-ubuntu16-3541) | — |
| ftp-dropbox-confinement | — | — | — | — | — | — | [5m 12s](../../../jobs/3541/2026-10-04__10-43-32/ftp-dropbox-confinement-bash-ubuntu16-3541) | — |
| http-upload-size-boundary | — | — | — | — | — | — | [5m 36s](../../../jobs/3541/2026-10-04__10-43-32/http-upload-size-boundary-bash-ubuntu16-3541) | — |
| imap-maildir-cutover | — | — | — | — | — | — | [5m 37s](../../../jobs/3541/2026-10-04__10-43-32/imap-maildir-cutover-bash-ubuntu16-3541) | — |
| inetd-request-activation | — | — | — | — | — | — | [7m 47s](../../../jobs/3541/2026-10-04__10-43-32/inetd-request-activation-bash-ubuntu16-3541) | — |
| kerberos-service-identity | — | — | — | — | — | — | [8m 26s](../../../jobs/3541/2026-10-04__10-43-32/kerberos-service-identity-bash-ubuntu16-3541) | — |
| ldap-attribute-privacy | — | — | — | — | — | — | [7m 11s](../../../jobs/3541/2026-10-04__10-43-32/ldap-attribute-privacy-bash-ubuntu16-3541) | — |
| ldap-directory-import | — | — | — | — | — | — | [4m 45s](../../../jobs/3541/2026-10-04__10-43-32/ldap-directory-import-bash-ubuntu16-3541) | — |
| mysql-relational-import | — | — | — | — | — | — | [5m 52s](../../../jobs/3541/2026-10-04__10-43-32/mysql-relational-import-bash-ubuntu16-3541) | — |
| mysql-replication-catchup | — | — | — | — | — | — | [11m 08s](../../../jobs/3541/2026-10-04__10-43-32/mysql-replication-catchup-bash-ubuntu16-3541) | — |
| radius-network-authentication | — | — | — | — | — | — | [6m 57s](../../../jobs/3541/2026-10-04__10-43-32/radius-network-authentication-bash-ubuntu16-3541) | — |
| rsync-module-publication | — | — | — | — | — | — | [4m 58s](../../../jobs/3541/2026-10-04__10-43-32/rsync-module-publication-bash-ubuntu16-3541) | — |
| samba-team-share | — | — | — | — | — | — | [5m 59s](../../../jobs/3541/2026-10-04__10-43-32/samba-team-share-bash-ubuntu16-3541) | — |
| smtp-alias-delivery | — | — | — | — | — | — | [5m 52s](../../../jobs/3541/2026-10-04__10-43-32/smtp-alias-delivery-bash-ubuntu16-3541) | — |
| snmp-readonly-monitoring | — | — | — | — | — | — | [7m 19s](../../../jobs/3541/2026-10-04__10-43-32/snmp-readonly-monitoring-bash-ubuntu16-3541) | — |
| ssh-forced-command-ingest | — | — | — | — | — | — | [6m 56s](../../../jobs/3541/2026-10-04__10-43-32/ssh-forced-command-ingest-bash-ubuntu16-3541) | — |
| ssh-local-service-tunnel | — | — | — | — | — | — | [5m 11s](../../../jobs/3541/2026-10-04__10-43-32/ssh-local-service-tunnel-bash-ubuntu16-3541) | — |
| tftp-firmware-distribution | — | — | — | — | — | — | [4m 06s](../../../jobs/3541/2026-10-04__10-43-32/tftp-firmware-distribution-bash-ubuntu16-3541) | — |
| udp-meter-ingestion | — | — | — | — | — | — | [32m 10s](../../../jobs/3541/2026-10-04__10-43-32/udp-meter-ingestion-bash-ubuntu16-3541) | — |
| **Average** | — | — | — | — | — | — | 7m 17s | — |

Cluster provisioning is not a meaningful part of these times: median 732 ms across 100 clusters, about 0.27% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | [0.980](../../../jobs/3541/2026-10-04__10-43-32/shared-nfs-storage-bash-ubuntu16-3541) | — |
| centralized-log-collector | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/centralized-log-collector-bash-ubuntu16-3541) | — |
| ssh-controller-access | — | — | — | — | — | — | [0.960](../../../jobs/3541/2026-10-04__10-43-32/ssh-controller-access-bash-ubuntu16-3541) | — |
| internal-ca-tls | — | — | — | — | — | — | [0.960](../../../jobs/3541/2026-10-04__10-43-32/internal-ca-tls-bash-ubuntu16-3541) | — |
| internal-time-sync | — | — | — | — | — | — | [0.980](../../../jobs/3541/2026-10-04__10-43-32/internal-time-sync-bash-ubuntu16-3541) | — |
| load-balanced-web-tier | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/load-balanced-web-tier-bash-ubuntu16-3541) | — |
| network-scoped-firewall | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/network-scoped-firewall-bash-ubuntu16-3541) | — |
| config-sync | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/config-sync-bash-ubuntu16-3541) | — |
| scheduled-backup | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/scheduled-backup-bash-ubuntu16-3541) | — |
| internal-dns-resolution | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/internal-dns-resolution-bash-ubuntu16-3541) | — |
| database-reader-writer-roles | — | — | — | — | — | — | [0.780](../../../jobs/3541/2026-10-04__10-43-32/database-reader-writer-roles-bash-ubuntu16-3541) | — |
| forward-proxy-destination-policy | — | — | — | — | — | — | [0.920](../../../jobs/3541/2026-10-04__10-43-32/forward-proxy-destination-policy-bash-ubuntu16-3541) | — |
| ftp-dropbox-confinement | — | — | — | — | — | — | [0.990](../../../jobs/3541/2026-10-04__10-43-32/ftp-dropbox-confinement-bash-ubuntu16-3541) | — |
| http-upload-size-boundary | — | — | — | — | — | — | [0.900](../../../jobs/3541/2026-10-04__10-43-32/http-upload-size-boundary-bash-ubuntu16-3541) | — |
| imap-maildir-cutover | — | — | — | — | — | — | [0.680](../../../jobs/3541/2026-10-04__10-43-32/imap-maildir-cutover-bash-ubuntu16-3541) | — |
| inetd-request-activation | — | — | — | — | — | — | [0.940](../../../jobs/3541/2026-10-04__10-43-32/inetd-request-activation-bash-ubuntu16-3541) | — |
| kerberos-service-identity | — | — | — | — | — | — | [0.780](../../../jobs/3541/2026-10-04__10-43-32/kerberos-service-identity-bash-ubuntu16-3541) | — |
| ldap-attribute-privacy | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/ldap-attribute-privacy-bash-ubuntu16-3541) | — |
| ldap-directory-import | — | — | — | — | — | — | [0.940](../../../jobs/3541/2026-10-04__10-43-32/ldap-directory-import-bash-ubuntu16-3541) | — |
| mysql-relational-import | — | — | — | — | — | — | [0.820](../../../jobs/3541/2026-10-04__10-43-32/mysql-relational-import-bash-ubuntu16-3541) | — |
| mysql-replication-catchup | — | — | — | — | — | — | [0.900](../../../jobs/3541/2026-10-04__10-43-32/mysql-replication-catchup-bash-ubuntu16-3541) | — |
| radius-network-authentication | — | — | — | — | — | — | [0.900](../../../jobs/3541/2026-10-04__10-43-32/radius-network-authentication-bash-ubuntu16-3541) | — |
| rsync-module-publication | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/rsync-module-publication-bash-ubuntu16-3541) | — |
| samba-team-share | — | — | — | — | — | — | [0.840](../../../jobs/3541/2026-10-04__10-43-32/samba-team-share-bash-ubuntu16-3541) | — |
| smtp-alias-delivery | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/smtp-alias-delivery-bash-ubuntu16-3541) | — |
| snmp-readonly-monitoring | — | — | — | — | — | — | [0.990](../../../jobs/3541/2026-10-04__10-43-32/snmp-readonly-monitoring-bash-ubuntu16-3541) | — |
| ssh-forced-command-ingest | — | — | — | — | — | — | [0.940](../../../jobs/3541/2026-10-04__10-43-32/ssh-forced-command-ingest-bash-ubuntu16-3541) | — |
| ssh-local-service-tunnel | — | — | — | — | — | — | [0.970](../../../jobs/3541/2026-10-04__10-43-32/ssh-local-service-tunnel-bash-ubuntu16-3541) | — |
| tftp-firmware-distribution | — | — | — | — | — | — | [0.940](../../../jobs/3541/2026-10-04__10-43-32/tftp-firmware-distribution-bash-ubuntu16-3541) | — |
| udp-meter-ingestion | — | — | — | — | — | — | [1.000](../../../jobs/3541/2026-10-04__10-43-32/udp-meter-ingestion-bash-ubuntu16-3541) | — |
| **Average** | — | — | — | — | — | — | 0.936 | — |
