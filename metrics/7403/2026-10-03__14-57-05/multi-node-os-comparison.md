# multi-node-os-comparison: command execution summary

Scope: `7403/2026-10-03__14-57-05`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [29/4](../../../jobs/7403/2026-10-03__14-57-05/shared-nfs-storage-bash-ubuntu24-7403) |
| centralized-log-collector | — | — | — | — | — | — | — | [27/0](../../../jobs/7403/2026-10-03__14-57-05/centralized-log-collector-bash-ubuntu24-7403) |
| ssh-controller-access | — | — | — | — | — | — | — | [23/4](../../../jobs/7403/2026-10-03__14-57-05/ssh-controller-access-bash-ubuntu24-7403) |
| internal-ca-tls | — | — | — | — | — | — | — | [29/4](../../../jobs/7403/2026-10-03__14-57-05/internal-ca-tls-bash-ubuntu24-7403) |
| internal-time-sync | — | — | — | — | — | — | — | [21/0](../../../jobs/7403/2026-10-03__14-57-05/internal-time-sync-bash-ubuntu24-7403) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [32/2](../../../jobs/7403/2026-10-03__14-57-05/load-balanced-web-tier-bash-ubuntu24-7403) |
| network-scoped-firewall | — | — | — | — | — | — | — | [32/1](../../../jobs/7403/2026-10-03__14-57-05/network-scoped-firewall-bash-ubuntu24-7403) |
| config-sync | — | — | — | — | — | — | — | [25/2](../../../jobs/7403/2026-10-03__14-57-05/config-sync-bash-ubuntu24-7403) |
| scheduled-backup | — | — | — | — | — | — | — | [24/1](../../../jobs/7403/2026-10-03__14-57-05/scheduled-backup-bash-ubuntu24-7403) |
| internal-dns-resolution | — | — | — | — | — | — | — | [27/0](../../../jobs/7403/2026-10-03__14-57-05/internal-dns-resolution-bash-ubuntu24-7403) |
| database-reader-writer-roles | — | — | — | — | — | — | — | [27/0](../../../jobs/7403/2026-10-03__14-57-05/database-reader-writer-roles-bash-ubuntu24-7403) |
| forward-proxy-destination-policy | — | — | — | — | — | — | — | [22/0](../../../jobs/7403/2026-10-03__14-57-05/forward-proxy-destination-policy-bash-ubuntu24-7403) |
| ftp-dropbox-confinement | — | — | — | — | — | — | — | [23/1](../../../jobs/7403/2026-10-03__14-57-05/ftp-dropbox-confinement-bash-ubuntu24-7403) |
| http-upload-size-boundary | — | — | — | — | — | — | — | [21/1](../../../jobs/7403/2026-10-03__14-57-05/http-upload-size-boundary-bash-ubuntu24-7403) |
| imap-maildir-cutover | — | — | — | — | — | — | — | [30/5](../../../jobs/7403/2026-10-03__14-57-05/imap-maildir-cutover-bash-ubuntu24-7403) |
| inetd-request-activation | — | — | — | — | — | — | — | [26/0](../../../jobs/7403/2026-10-03__14-57-05/inetd-request-activation-bash-ubuntu24-7403) |
| kerberos-service-identity | — | — | — | — | — | — | — | [32/0](../../../jobs/7403/2026-10-03__14-57-05/kerberos-service-identity-bash-ubuntu24-7403) |
| ldap-attribute-privacy | — | — | — | — | — | — | — | [31/1](../../../jobs/7403/2026-10-03__14-57-05/ldap-attribute-privacy-bash-ubuntu24-7403) |
| ldap-directory-import | — | — | — | — | — | — | — | [35/1](../../../jobs/7403/2026-10-03__14-57-05/ldap-directory-import-bash-ubuntu24-7403) |
| mysql-relational-import | — | — | — | — | — | — | — | [52/1](../../../jobs/7403/2026-10-03__14-57-05/mysql-relational-import-bash-ubuntu24-7403) |
| mysql-replication-catchup | — | — | — | — | — | — | — | [48/5](../../../jobs/7403/2026-10-03__14-57-05/mysql-replication-catchup-bash-ubuntu24-7403) |
| radius-network-authentication | — | — | — | — | — | — | — | [24/0](../../../jobs/7403/2026-10-03__14-57-05/radius-network-authentication-bash-ubuntu24-7403) |
| rsync-module-publication | — | — | — | — | — | — | — | [18/0](../../../jobs/7403/2026-10-03__14-57-05/rsync-module-publication-bash-ubuntu24-7403) |
| samba-team-share | — | — | — | — | — | — | — | [15/0](../../../jobs/7403/2026-10-03__14-57-05/samba-team-share-bash-ubuntu24-7403) |
| smtp-alias-delivery | — | — | — | — | — | — | — | [23/0](../../../jobs/7403/2026-10-03__14-57-05/smtp-alias-delivery-bash-ubuntu24-7403) |
| snmp-readonly-monitoring | — | — | — | — | — | — | — | [19/0](../../../jobs/7403/2026-10-03__14-57-05/snmp-readonly-monitoring-bash-ubuntu24-7403) |
| ssh-forced-command-ingest | — | — | — | — | — | — | — | [29/2](../../../jobs/7403/2026-10-03__14-57-05/ssh-forced-command-ingest-bash-ubuntu24-7403) |
| ssh-local-service-tunnel | — | — | — | — | — | — | — | [29/2](../../../jobs/7403/2026-10-03__14-57-05/ssh-local-service-tunnel-bash-ubuntu24-7403) |
| tftp-firmware-distribution | — | — | — | — | — | — | — | [27/0](../../../jobs/7403/2026-10-03__14-57-05/tftp-firmware-distribution-bash-ubuntu24-7403) |
| udp-meter-ingestion | — | — | — | — | — | — | — | [35/3](../../../jobs/7403/2026-10-03__14-57-05/udp-meter-ingestion-bash-ubuntu24-7403) |
| **Average** | — | — | — | — | — | — | — | 27.8/1.3 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [4m 02s](../../../jobs/7403/2026-10-03__14-57-05/shared-nfs-storage-bash-ubuntu24-7403) |
| centralized-log-collector | — | — | — | — | — | — | — | [3m 29s](../../../jobs/7403/2026-10-03__14-57-05/centralized-log-collector-bash-ubuntu24-7403) |
| ssh-controller-access | — | — | — | — | — | — | — | [3m 33s](../../../jobs/7403/2026-10-03__14-57-05/ssh-controller-access-bash-ubuntu24-7403) |
| internal-ca-tls | — | — | — | — | — | — | — | [5m 11s](../../../jobs/7403/2026-10-03__14-57-05/internal-ca-tls-bash-ubuntu24-7403) |
| internal-time-sync | — | — | — | — | — | — | — | [4m 43s](../../../jobs/7403/2026-10-03__14-57-05/internal-time-sync-bash-ubuntu24-7403) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [4m 06s](../../../jobs/7403/2026-10-03__14-57-05/load-balanced-web-tier-bash-ubuntu24-7403) |
| network-scoped-firewall | — | — | — | — | — | — | — | [4m 16s](../../../jobs/7403/2026-10-03__14-57-05/network-scoped-firewall-bash-ubuntu24-7403) |
| config-sync | — | — | — | — | — | — | — | [6m 26s](../../../jobs/7403/2026-10-03__14-57-05/config-sync-bash-ubuntu24-7403) |
| scheduled-backup | — | — | — | — | — | — | — | [5m 04s](../../../jobs/7403/2026-10-03__14-57-05/scheduled-backup-bash-ubuntu24-7403) |
| internal-dns-resolution | — | — | — | — | — | — | — | [19m 41s](../../../jobs/7403/2026-10-03__14-57-05/internal-dns-resolution-bash-ubuntu24-7403) |
| database-reader-writer-roles | — | — | — | — | — | — | — | [5m 28s](../../../jobs/7403/2026-10-03__14-57-05/database-reader-writer-roles-bash-ubuntu24-7403) |
| forward-proxy-destination-policy | — | — | — | — | — | — | — | [4m 53s](../../../jobs/7403/2026-10-03__14-57-05/forward-proxy-destination-policy-bash-ubuntu24-7403) |
| ftp-dropbox-confinement | — | — | — | — | — | — | — | [5m 13s](../../../jobs/7403/2026-10-03__14-57-05/ftp-dropbox-confinement-bash-ubuntu24-7403) |
| http-upload-size-boundary | — | — | — | — | — | — | — | [3m 59s](../../../jobs/7403/2026-10-03__14-57-05/http-upload-size-boundary-bash-ubuntu24-7403) |
| imap-maildir-cutover | — | — | — | — | — | — | — | [6m 13s](../../../jobs/7403/2026-10-03__14-57-05/imap-maildir-cutover-bash-ubuntu24-7403) |
| inetd-request-activation | — | — | — | — | — | — | — | [4m 18s](../../../jobs/7403/2026-10-03__14-57-05/inetd-request-activation-bash-ubuntu24-7403) |
| kerberos-service-identity | — | — | — | — | — | — | — | [6m 23s](../../../jobs/7403/2026-10-03__14-57-05/kerberos-service-identity-bash-ubuntu24-7403) |
| ldap-attribute-privacy | — | — | — | — | — | — | — | [6m 00s](../../../jobs/7403/2026-10-03__14-57-05/ldap-attribute-privacy-bash-ubuntu24-7403) |
| ldap-directory-import | — | — | — | — | — | — | — | [5m 03s](../../../jobs/7403/2026-10-03__14-57-05/ldap-directory-import-bash-ubuntu24-7403) |
| mysql-relational-import | — | — | — | — | — | — | — | [5m 34s](../../../jobs/7403/2026-10-03__14-57-05/mysql-relational-import-bash-ubuntu24-7403) |
| mysql-replication-catchup | — | — | — | — | — | — | — | [9m 49s](../../../jobs/7403/2026-10-03__14-57-05/mysql-replication-catchup-bash-ubuntu24-7403) |
| radius-network-authentication | — | — | — | — | — | — | — | [5m 55s](../../../jobs/7403/2026-10-03__14-57-05/radius-network-authentication-bash-ubuntu24-7403) |
| rsync-module-publication | — | — | — | — | — | — | — | [3m 35s](../../../jobs/7403/2026-10-03__14-57-05/rsync-module-publication-bash-ubuntu24-7403) |
| samba-team-share | — | — | — | — | — | — | — | [3m 22s](../../../jobs/7403/2026-10-03__14-57-05/samba-team-share-bash-ubuntu24-7403) |
| smtp-alias-delivery | — | — | — | — | — | — | — | [3m 47s](../../../jobs/7403/2026-10-03__14-57-05/smtp-alias-delivery-bash-ubuntu24-7403) |
| snmp-readonly-monitoring | — | — | — | — | — | — | — | [2m 51s](../../../jobs/7403/2026-10-03__14-57-05/snmp-readonly-monitoring-bash-ubuntu24-7403) |
| ssh-forced-command-ingest | — | — | — | — | — | — | — | [5m 16s](../../../jobs/7403/2026-10-03__14-57-05/ssh-forced-command-ingest-bash-ubuntu24-7403) |
| ssh-local-service-tunnel | — | — | — | — | — | — | — | [5m 04s](../../../jobs/7403/2026-10-03__14-57-05/ssh-local-service-tunnel-bash-ubuntu24-7403) |
| tftp-firmware-distribution | — | — | — | — | — | — | — | [5m 10s](../../../jobs/7403/2026-10-03__14-57-05/tftp-firmware-distribution-bash-ubuntu24-7403) |
| udp-meter-ingestion | — | — | — | — | — | — | — | [6m 07s](../../../jobs/7403/2026-10-03__14-57-05/udp-meter-ingestion-bash-ubuntu24-7403) |
| **Average** | — | — | — | — | — | — | — | 5m 29s |

Cluster provisioning is not a meaningful part of these times: median 738 ms across 100 clusters, about 0.44% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/shared-nfs-storage-bash-ubuntu24-7403) |
| centralized-log-collector | — | — | — | — | — | — | — | [0.920](../../../jobs/7403/2026-10-03__14-57-05/centralized-log-collector-bash-ubuntu24-7403) |
| ssh-controller-access | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/ssh-controller-access-bash-ubuntu24-7403) |
| internal-ca-tls | — | — | — | — | — | — | — | [0.680](../../../jobs/7403/2026-10-03__14-57-05/internal-ca-tls-bash-ubuntu24-7403) |
| internal-time-sync | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/internal-time-sync-bash-ubuntu24-7403) |
| load-balanced-web-tier | — | — | — | — | — | — | — | [0.970](../../../jobs/7403/2026-10-03__14-57-05/load-balanced-web-tier-bash-ubuntu24-7403) |
| network-scoped-firewall | — | — | — | — | — | — | — | [0.940](../../../jobs/7403/2026-10-03__14-57-05/network-scoped-firewall-bash-ubuntu24-7403) |
| config-sync | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/config-sync-bash-ubuntu24-7403) |
| scheduled-backup | — | — | — | — | — | — | — | [0.900](../../../jobs/7403/2026-10-03__14-57-05/scheduled-backup-bash-ubuntu24-7403) |
| internal-dns-resolution | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/internal-dns-resolution-bash-ubuntu24-7403) |
| database-reader-writer-roles | — | — | — | — | — | — | — | [0.920](../../../jobs/7403/2026-10-03__14-57-05/database-reader-writer-roles-bash-ubuntu24-7403) |
| forward-proxy-destination-policy | — | — | — | — | — | — | — | [0.970](../../../jobs/7403/2026-10-03__14-57-05/forward-proxy-destination-policy-bash-ubuntu24-7403) |
| ftp-dropbox-confinement | — | — | — | — | — | — | — | [0.970](../../../jobs/7403/2026-10-03__14-57-05/ftp-dropbox-confinement-bash-ubuntu24-7403) |
| http-upload-size-boundary | — | — | — | — | — | — | — | [0.900](../../../jobs/7403/2026-10-03__14-57-05/http-upload-size-boundary-bash-ubuntu24-7403) |
| imap-maildir-cutover | — | — | — | — | — | — | — | [0.800](../../../jobs/7403/2026-10-03__14-57-05/imap-maildir-cutover-bash-ubuntu24-7403) |
| inetd-request-activation | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/inetd-request-activation-bash-ubuntu24-7403) |
| kerberos-service-identity | — | — | — | — | — | — | — | [0.780](../../../jobs/7403/2026-10-03__14-57-05/kerberos-service-identity-bash-ubuntu24-7403) |
| ldap-attribute-privacy | — | — | — | — | — | — | — | [0.850](../../../jobs/7403/2026-10-03__14-57-05/ldap-attribute-privacy-bash-ubuntu24-7403) |
| ldap-directory-import | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/ldap-directory-import-bash-ubuntu24-7403) |
| mysql-relational-import | — | — | — | — | — | — | — | [0.940](../../../jobs/7403/2026-10-03__14-57-05/mysql-relational-import-bash-ubuntu24-7403) |
| mysql-replication-catchup | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/mysql-replication-catchup-bash-ubuntu24-7403) |
| radius-network-authentication | — | — | — | — | — | — | — | [0.900](../../../jobs/7403/2026-10-03__14-57-05/radius-network-authentication-bash-ubuntu24-7403) |
| rsync-module-publication | — | — | — | — | — | — | — | [0.950](../../../jobs/7403/2026-10-03__14-57-05/rsync-module-publication-bash-ubuntu24-7403) |
| samba-team-share | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/samba-team-share-bash-ubuntu24-7403) |
| smtp-alias-delivery | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/smtp-alias-delivery-bash-ubuntu24-7403) |
| snmp-readonly-monitoring | — | — | — | — | — | — | — | [1.000](../../../jobs/7403/2026-10-03__14-57-05/snmp-readonly-monitoring-bash-ubuntu24-7403) |
| ssh-forced-command-ingest | — | — | — | — | — | — | — | [0.950](../../../jobs/7403/2026-10-03__14-57-05/ssh-forced-command-ingest-bash-ubuntu24-7403) |
| ssh-local-service-tunnel | — | — | — | — | — | — | — | [0.980](../../../jobs/7403/2026-10-03__14-57-05/ssh-local-service-tunnel-bash-ubuntu24-7403) |
| tftp-firmware-distribution | — | — | — | — | — | — | — | [0.930](../../../jobs/7403/2026-10-03__14-57-05/tftp-firmware-distribution-bash-ubuntu24-7403) |
| udp-meter-ingestion | — | — | — | — | — | — | — | [0.840](../../../jobs/7403/2026-10-03__14-57-05/udp-meter-ingestion-bash-ubuntu24-7403) |
| **Average** | — | — | — | — | — | — | — | 0.936 |
