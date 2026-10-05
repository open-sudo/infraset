# multi-node-os-comparison: command execution summary

Scope: `4543/2026-10-03__15-57-02`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | [28/4](../../../jobs/4543/2026-10-03__15-57-02/shared-nfs-storage-bash-centos-stream10-4543) | — | — | — | — | — |
| centralized-log-collector | — | — | [24/1](../../../jobs/4543/2026-10-03__15-57-02/centralized-log-collector-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-controller-access | — | — | [21/0](../../../jobs/4543/2026-10-03__15-57-02/ssh-controller-access-bash-centos-stream10-4543) | — | — | — | — | — |
| internal-ca-tls | — | — | [25/3](../../../jobs/4543/2026-10-03__15-57-02/internal-ca-tls-bash-centos-stream10-4543) | — | — | — | — | — |
| internal-time-sync | — | — | [21/0](../../../jobs/4543/2026-10-03__15-57-02/internal-time-sync-bash-centos-stream10-4543) | — | — | — | — | — |
| load-balanced-web-tier | — | — | [22/0](../../../jobs/4543/2026-10-03__15-57-02/load-balanced-web-tier-bash-centos-stream10-4543) | — | — | — | — | — |
| network-scoped-firewall | — | — | [28/0](../../../jobs/4543/2026-10-03__15-57-02/network-scoped-firewall-bash-centos-stream10-4543) | — | — | — | — | — |
| config-sync | — | — | [29/3](../../../jobs/4543/2026-10-03__15-57-02/config-sync-bash-centos-stream10-4543) | — | — | — | — | — |
| scheduled-backup | — | — | [27/0](../../../jobs/4543/2026-10-03__15-57-02/scheduled-backup-bash-centos-stream10-4543) | — | — | — | — | — |
| internal-dns-resolution | — | — | [18/0](../../../jobs/4543/2026-10-03__15-57-02/internal-dns-resolution-bash-centos-stream10-4543) | — | — | — | — | — |
| database-reader-writer-roles | — | — | [32/1](../../../jobs/4543/2026-10-03__15-57-02/database-reader-writer-roles-bash-centos-stream10-4543) | — | — | — | — | — |
| forward-proxy-destination-policy | — | — | [29/0](../../../jobs/4543/2026-10-03__15-57-02/forward-proxy-destination-policy-bash-centos-stream10-4543) | — | — | — | — | — |
| ftp-dropbox-confinement | — | — | [35/1](../../../jobs/4543/2026-10-03__15-57-02/ftp-dropbox-confinement-bash-centos-stream10-4543) | — | — | — | — | — |
| http-upload-size-boundary | — | — | [28/1](../../../jobs/4543/2026-10-03__15-57-02/http-upload-size-boundary-bash-centos-stream10-4543) | — | — | — | — | — |
| imap-maildir-cutover | — | — | [21/0](../../../jobs/4543/2026-10-03__15-57-02/imap-maildir-cutover-bash-centos-stream10-4543) | — | — | — | — | — |
| inetd-request-activation | — | — | [32/2](../../../jobs/4543/2026-10-03__15-57-02/inetd-request-activation-bash-centos-stream10-4543) | — | — | — | — | — |
| kerberos-service-identity | — | — | [32/1](../../../jobs/4543/2026-10-03__15-57-02/kerberos-service-identity-bash-centos-stream10-4543) | — | — | — | — | — |
| ldap-attribute-privacy | — | — | [22/0](../../../jobs/4543/2026-10-03__15-57-02/ldap-attribute-privacy-bash-centos-stream10-4543) | — | — | — | — | — |
| ldap-directory-import | — | — | [28/1](../../../jobs/4543/2026-10-03__15-57-02/ldap-directory-import-bash-centos-stream10-4543) | — | — | — | — | — |
| mysql-relational-import | — | — | [20/16](../../../jobs/4543/2026-10-03__15-57-02/mysql-relational-import-bash-centos-stream10-4543) | — | — | — | — | — |
| mysql-replication-catchup | — | — | [40/2](../../../jobs/4543/2026-10-03__15-57-02/mysql-replication-catchup-bash-centos-stream10-4543) | — | — | — | — | — |
| radius-network-authentication | — | — | [31/1](../../../jobs/4543/2026-10-03__15-57-02/radius-network-authentication-bash-centos-stream10-4543) | — | — | — | — | — |
| rsync-module-publication | — | — | [28/0](../../../jobs/4543/2026-10-03__15-57-02/rsync-module-publication-bash-centos-stream10-4543) | — | — | — | — | — |
| samba-team-share | — | — | [22/2](../../../jobs/4543/2026-10-03__15-57-02/samba-team-share-bash-centos-stream10-4543) | — | — | — | — | — |
| smtp-alias-delivery | — | — | [37/2](../../../jobs/4543/2026-10-03__15-57-02/smtp-alias-delivery-bash-centos-stream10-4543) | — | — | — | — | — |
| snmp-readonly-monitoring | — | — | [19/0](../../../jobs/4543/2026-10-03__15-57-02/snmp-readonly-monitoring-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-forced-command-ingest | — | — | [25/0](../../../jobs/4543/2026-10-03__15-57-02/ssh-forced-command-ingest-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-local-service-tunnel | — | — | [39/3](../../../jobs/4543/2026-10-03__15-57-02/ssh-local-service-tunnel-bash-centos-stream10-4543) | — | — | — | — | — |
| tftp-firmware-distribution | — | — | [32/1](../../../jobs/4543/2026-10-03__15-57-02/tftp-firmware-distribution-bash-centos-stream10-4543) | — | — | — | — | — |
| udp-meter-ingestion | — | — | [24/1](../../../jobs/4543/2026-10-03__15-57-02/udp-meter-ingestion-bash-centos-stream10-4543) | — | — | — | — | — |
| **Average** | — | — | 27.3/1.5 | — | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | [5m 26s](../../../jobs/4543/2026-10-03__15-57-02/shared-nfs-storage-bash-centos-stream10-4543) | — | — | — | — | — |
| centralized-log-collector | — | — | [3m 50s](../../../jobs/4543/2026-10-03__15-57-02/centralized-log-collector-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-controller-access | — | — | [3m 30s](../../../jobs/4543/2026-10-03__15-57-02/ssh-controller-access-bash-centos-stream10-4543) | — | — | — | — | — |
| internal-ca-tls | — | — | [4m 22s](../../../jobs/4543/2026-10-03__15-57-02/internal-ca-tls-bash-centos-stream10-4543) | — | — | — | — | — |
| internal-time-sync | — | — | [3m 29s](../../../jobs/4543/2026-10-03__15-57-02/internal-time-sync-bash-centos-stream10-4543) | — | — | — | — | — |
| load-balanced-web-tier | — | — | [3m 30s](../../../jobs/4543/2026-10-03__15-57-02/load-balanced-web-tier-bash-centos-stream10-4543) | — | — | — | — | — |
| network-scoped-firewall | — | — | [4m 22s](../../../jobs/4543/2026-10-03__15-57-02/network-scoped-firewall-bash-centos-stream10-4543) | — | — | — | — | — |
| config-sync | — | — | [5m 04s](../../../jobs/4543/2026-10-03__15-57-02/config-sync-bash-centos-stream10-4543) | — | — | — | — | — |
| scheduled-backup | — | — | [4m 34s](../../../jobs/4543/2026-10-03__15-57-02/scheduled-backup-bash-centos-stream10-4543) | — | — | — | — | — |
| internal-dns-resolution | — | — | [3m 45s](../../../jobs/4543/2026-10-03__15-57-02/internal-dns-resolution-bash-centos-stream10-4543) | — | — | — | — | — |
| database-reader-writer-roles | — | — | [5m 18s](../../../jobs/4543/2026-10-03__15-57-02/database-reader-writer-roles-bash-centos-stream10-4543) | — | — | — | — | — |
| forward-proxy-destination-policy | — | — | [5m 14s](../../../jobs/4543/2026-10-03__15-57-02/forward-proxy-destination-policy-bash-centos-stream10-4543) | — | — | — | — | — |
| ftp-dropbox-confinement | — | — | [6m 08s](../../../jobs/4543/2026-10-03__15-57-02/ftp-dropbox-confinement-bash-centos-stream10-4543) | — | — | — | — | — |
| http-upload-size-boundary | — | — | [30m 51s](../../../jobs/4543/2026-10-03__15-57-02/http-upload-size-boundary-bash-centos-stream10-4543) | — | — | — | — | — |
| imap-maildir-cutover | — | — | [4m 26s](../../../jobs/4543/2026-10-03__15-57-02/imap-maildir-cutover-bash-centos-stream10-4543) | — | — | — | — | — |
| inetd-request-activation | — | — | [6m 02s](../../../jobs/4543/2026-10-03__15-57-02/inetd-request-activation-bash-centos-stream10-4543) | — | — | — | — | — |
| kerberos-service-identity | — | — | [5m 56s](../../../jobs/4543/2026-10-03__15-57-02/kerberos-service-identity-bash-centos-stream10-4543) | — | — | — | — | — |
| ldap-attribute-privacy | — | — | [13m 32s](../../../jobs/4543/2026-10-03__15-57-02/ldap-attribute-privacy-bash-centos-stream10-4543) | — | — | — | — | — |
| ldap-directory-import | — | — | [3m 52s](../../../jobs/4543/2026-10-03__15-57-02/ldap-directory-import-bash-centos-stream10-4543) | — | — | — | — | — |
| mysql-relational-import | — | — | [5m 57s](../../../jobs/4543/2026-10-03__15-57-02/mysql-relational-import-bash-centos-stream10-4543) | — | — | — | — | — |
| mysql-replication-catchup | — | — | [8m 12s](../../../jobs/4543/2026-10-03__15-57-02/mysql-replication-catchup-bash-centos-stream10-4543) | — | — | — | — | — |
| radius-network-authentication | — | — | [5m 32s](../../../jobs/4543/2026-10-03__15-57-02/radius-network-authentication-bash-centos-stream10-4543) | — | — | — | — | — |
| rsync-module-publication | — | — | [4m 03s](../../../jobs/4543/2026-10-03__15-57-02/rsync-module-publication-bash-centos-stream10-4543) | — | — | — | — | — |
| samba-team-share | — | — | [3m 59s](../../../jobs/4543/2026-10-03__15-57-02/samba-team-share-bash-centos-stream10-4543) | — | — | — | — | — |
| smtp-alias-delivery | — | — | [3m 59s](../../../jobs/4543/2026-10-03__15-57-02/smtp-alias-delivery-bash-centos-stream10-4543) | — | — | — | — | — |
| snmp-readonly-monitoring | — | — | [3m 26s](../../../jobs/4543/2026-10-03__15-57-02/snmp-readonly-monitoring-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-forced-command-ingest | — | — | [5m 26s](../../../jobs/4543/2026-10-03__15-57-02/ssh-forced-command-ingest-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-local-service-tunnel | — | — | [6m 08s](../../../jobs/4543/2026-10-03__15-57-02/ssh-local-service-tunnel-bash-centos-stream10-4543) | — | — | — | — | — |
| tftp-firmware-distribution | — | — | [5m 31s](../../../jobs/4543/2026-10-03__15-57-02/tftp-firmware-distribution-bash-centos-stream10-4543) | — | — | — | — | — |
| udp-meter-ingestion | — | — | [4m 31s](../../../jobs/4543/2026-10-03__15-57-02/udp-meter-ingestion-bash-centos-stream10-4543) | — | — | — | — | — |
| **Average** | — | — | 6m 00s | — | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 1138 ms across 100 clusters, about 0.59% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/shared-nfs-storage-bash-centos-stream10-4543) | — | — | — | — | — |
| centralized-log-collector | — | — | [0.940](../../../jobs/4543/2026-10-03__15-57-02/centralized-log-collector-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-controller-access | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/ssh-controller-access-bash-centos-stream10-4543) | — | — | — | — | — |
| internal-ca-tls | — | — | [0.910](../../../jobs/4543/2026-10-03__15-57-02/internal-ca-tls-bash-centos-stream10-4543) | — | — | — | — | — |
| internal-time-sync | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/internal-time-sync-bash-centos-stream10-4543) | — | — | — | — | — |
| load-balanced-web-tier | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/load-balanced-web-tier-bash-centos-stream10-4543) | — | — | — | — | — |
| network-scoped-firewall | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/network-scoped-firewall-bash-centos-stream10-4543) | — | — | — | — | — |
| config-sync | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/config-sync-bash-centos-stream10-4543) | — | — | — | — | — |
| scheduled-backup | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/scheduled-backup-bash-centos-stream10-4543) | — | — | — | — | — |
| internal-dns-resolution | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/internal-dns-resolution-bash-centos-stream10-4543) | — | — | — | — | — |
| database-reader-writer-roles | — | — | [0.980](../../../jobs/4543/2026-10-03__15-57-02/database-reader-writer-roles-bash-centos-stream10-4543) | — | — | — | — | — |
| forward-proxy-destination-policy | — | — | [0.940](../../../jobs/4543/2026-10-03__15-57-02/forward-proxy-destination-policy-bash-centos-stream10-4543) | — | — | — | — | — |
| ftp-dropbox-confinement | — | — | [0.860](../../../jobs/4543/2026-10-03__15-57-02/ftp-dropbox-confinement-bash-centos-stream10-4543) | — | — | — | — | — |
| http-upload-size-boundary | — | — | [0.860](../../../jobs/4543/2026-10-03__15-57-02/http-upload-size-boundary-bash-centos-stream10-4543) | — | — | — | — | — |
| imap-maildir-cutover | — | — | [0.840](../../../jobs/4543/2026-10-03__15-57-02/imap-maildir-cutover-bash-centos-stream10-4543) | — | — | — | — | — |
| inetd-request-activation | — | — | [0.920](../../../jobs/4543/2026-10-03__15-57-02/inetd-request-activation-bash-centos-stream10-4543) | — | — | — | — | — |
| kerberos-service-identity | — | — | [0.900](../../../jobs/4543/2026-10-03__15-57-02/kerberos-service-identity-bash-centos-stream10-4543) | — | — | — | — | — |
| ldap-attribute-privacy | — | — | [0.500](../../../jobs/4543/2026-10-03__15-57-02/ldap-attribute-privacy-bash-centos-stream10-4543) | — | — | — | — | — |
| ldap-directory-import | — | — | [1.000](../../../jobs/4543/2026-10-03__15-57-02/ldap-directory-import-bash-centos-stream10-4543) | — | — | — | — | — |
| mysql-relational-import | — | — | [0.920](../../../jobs/4543/2026-10-03__15-57-02/mysql-relational-import-bash-centos-stream10-4543) | — | — | — | — | — |
| mysql-replication-catchup | — | — | [0.950](../../../jobs/4543/2026-10-03__15-57-02/mysql-replication-catchup-bash-centos-stream10-4543) | — | — | — | — | — |
| radius-network-authentication | — | — | [0.920](../../../jobs/4543/2026-10-03__15-57-02/radius-network-authentication-bash-centos-stream10-4543) | — | — | — | — | — |
| rsync-module-publication | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/rsync-module-publication-bash-centos-stream10-4543) | — | — | — | — | — |
| samba-team-share | — | — | [0.940](../../../jobs/4543/2026-10-03__15-57-02/samba-team-share-bash-centos-stream10-4543) | — | — | — | — | — |
| smtp-alias-delivery | — | — | [0.900](../../../jobs/4543/2026-10-03__15-57-02/smtp-alias-delivery-bash-centos-stream10-4543) | — | — | — | — | — |
| snmp-readonly-monitoring | — | — | [0.970](../../../jobs/4543/2026-10-03__15-57-02/snmp-readonly-monitoring-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-forced-command-ingest | — | — | [0.900](../../../jobs/4543/2026-10-03__15-57-02/ssh-forced-command-ingest-bash-centos-stream10-4543) | — | — | — | — | — |
| ssh-local-service-tunnel | — | — | [0.780](../../../jobs/4543/2026-10-03__15-57-02/ssh-local-service-tunnel-bash-centos-stream10-4543) | — | — | — | — | — |
| tftp-firmware-distribution | — | — | [0.880](../../../jobs/4543/2026-10-03__15-57-02/tftp-firmware-distribution-bash-centos-stream10-4543) | — | — | — | — | — |
| udp-meter-ingestion | — | — | [0.910](../../../jobs/4543/2026-10-03__15-57-02/udp-meter-ingestion-bash-centos-stream10-4543) | — | — | — | — | — |
| **Average** | — | — | 0.921 | — | — | — | — | — |
