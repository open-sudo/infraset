# multi-node-os-comparison: command execution summary

Scope: `8799/2026-10-03__01-23-07`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
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
| database-reader-writer-roles | — | — | — | — | — | — | — | — | [51/11](../../../jobs/8799/2026-10-03__01-23-07/database-reader-writer-roles-bash-centos5-8799) |
| forward-proxy-destination-policy | — | — | — | — | — | — | — | — | [24/6](../../../jobs/8799/2026-10-03__01-23-07/forward-proxy-destination-policy-bash-centos5-8799) |
| ftp-dropbox-confinement | — | — | — | — | — | — | — | — | [47/11](../../../jobs/8799/2026-10-03__01-23-07/ftp-dropbox-confinement-bash-centos5-8799) |
| http-upload-size-boundary | — | — | — | — | — | — | — | — | [41/3](../../../jobs/8799/2026-10-03__01-23-07/http-upload-size-boundary-bash-centos5-8799) |
| imap-maildir-cutover | — | — | — | — | — | — | — | — | [39/12](../../../jobs/8799/2026-10-03__01-23-07/imap-maildir-cutover-bash-centos5-8799) |
| inetd-request-activation | — | — | — | — | — | — | — | — | [36/11](../../../jobs/8799/2026-10-03__01-23-07/inetd-request-activation-bash-centos5-8799) |
| kerberos-service-identity | — | — | — | — | — | — | — | — | [46/14](../../../jobs/8799/2026-10-03__01-23-07/kerberos-service-identity-bash-centos5-8799) |
| ldap-attribute-privacy | — | — | — | — | — | — | — | — | [45/15](../../../jobs/8799/2026-10-03__01-23-07/ldap-attribute-privacy-bash-centos5-8799) |
| ldap-directory-import | — | — | — | — | — | — | — | — | [40/6](../../../jobs/8799/2026-10-03__01-23-07/ldap-directory-import-bash-centos5-8799) |
| mysql-relational-import | — | — | — | — | — | — | — | — | [36/7](../../../jobs/8799/2026-10-03__01-23-07/mysql-relational-import-bash-centos5-8799) |
| mysql-replication-catchup | — | — | — | — | — | — | — | — | [82/25](../../../jobs/8799/2026-10-03__01-23-07/mysql-replication-catchup-bash-centos5-8799) |
| radius-network-authentication | — | — | — | — | — | — | — | — | [44/12](../../../jobs/8799/2026-10-03__01-23-07/radius-network-authentication-bash-centos5-8799) |
| rsync-module-publication | — | — | — | — | — | — | — | — | [37/9](../../../jobs/8799/2026-10-03__01-23-07/rsync-module-publication-bash-centos5-8799) |
| samba-team-share | — | — | — | — | — | — | — | — | [39/9](../../../jobs/8799/2026-10-03__01-23-07/samba-team-share-bash-centos5-8799) |
| smtp-alias-delivery | — | — | — | — | — | — | — | — | [40/9](../../../jobs/8799/2026-10-03__01-23-07/smtp-alias-delivery-bash-centos5-8799) |
| snmp-readonly-monitoring | — | — | — | — | — | — | — | — | [33/11](../../../jobs/8799/2026-10-03__01-23-07/snmp-readonly-monitoring-bash-centos5-8799) |
| ssh-forced-command-ingest | — | — | — | — | — | — | — | — | [33/8](../../../jobs/8799/2026-10-03__01-23-07/ssh-forced-command-ingest-bash-centos5-8799) |
| ssh-local-service-tunnel | — | — | — | — | — | — | — | — | [36/16](../../../jobs/8799/2026-10-03__01-23-07/ssh-local-service-tunnel-bash-centos5-8799) |
| tftp-firmware-distribution | — | — | — | — | — | — | — | — | [41/9](../../../jobs/8799/2026-10-03__01-23-07/tftp-firmware-distribution-bash-centos5-8799) |
| udp-meter-ingestion | — | — | — | — | — | — | — | — | [41/9](../../../jobs/8799/2026-10-03__01-23-07/udp-meter-ingestion-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 41.5/10.7 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
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
| database-reader-writer-roles | — | — | — | — | — | — | — | — | [10m 30s](../../../jobs/8799/2026-10-03__01-23-07/database-reader-writer-roles-bash-centos5-8799) |
| forward-proxy-destination-policy | — | — | — | — | — | — | — | — | [8m 39s](../../../jobs/8799/2026-10-03__01-23-07/forward-proxy-destination-policy-bash-centos5-8799) |
| ftp-dropbox-confinement | — | — | — | — | — | — | — | — | [10m 08s](../../../jobs/8799/2026-10-03__01-23-07/ftp-dropbox-confinement-bash-centos5-8799) |
| http-upload-size-boundary | — | — | — | — | — | — | — | — | [9m 27s](../../../jobs/8799/2026-10-03__01-23-07/http-upload-size-boundary-bash-centos5-8799) |
| imap-maildir-cutover | — | — | — | — | — | — | — | — | [14m 52s](../../../jobs/8799/2026-10-03__01-23-07/imap-maildir-cutover-bash-centos5-8799) |
| inetd-request-activation | — | — | — | — | — | — | — | — | [8m 13s](../../../jobs/8799/2026-10-03__01-23-07/inetd-request-activation-bash-centos5-8799) |
| kerberos-service-identity | — | — | — | — | — | — | — | — | [9m 10s](../../../jobs/8799/2026-10-03__01-23-07/kerberos-service-identity-bash-centos5-8799) |
| ldap-attribute-privacy | — | — | — | — | — | — | — | — | [9m 47s](../../../jobs/8799/2026-10-03__01-23-07/ldap-attribute-privacy-bash-centos5-8799) |
| ldap-directory-import | — | — | — | — | — | — | — | — | [7m 41s](../../../jobs/8799/2026-10-03__01-23-07/ldap-directory-import-bash-centos5-8799) |
| mysql-relational-import | — | — | — | — | — | — | — | — | [9m 05s](../../../jobs/8799/2026-10-03__01-23-07/mysql-relational-import-bash-centos5-8799) |
| mysql-replication-catchup | — | — | — | — | — | — | — | — | [16m 19s](../../../jobs/8799/2026-10-03__01-23-07/mysql-replication-catchup-bash-centos5-8799) |
| radius-network-authentication | — | — | — | — | — | — | — | — | [9m 10s](../../../jobs/8799/2026-10-03__01-23-07/radius-network-authentication-bash-centos5-8799) |
| rsync-module-publication | — | — | — | — | — | — | — | — | [10m 26s](../../../jobs/8799/2026-10-03__01-23-07/rsync-module-publication-bash-centos5-8799) |
| samba-team-share | — | — | — | — | — | — | — | — | [9m 25s](../../../jobs/8799/2026-10-03__01-23-07/samba-team-share-bash-centos5-8799) |
| smtp-alias-delivery | — | — | — | — | — | — | — | — | [8m 47s](../../../jobs/8799/2026-10-03__01-23-07/smtp-alias-delivery-bash-centos5-8799) |
| snmp-readonly-monitoring | — | — | — | — | — | — | — | — | [6m 41s](../../../jobs/8799/2026-10-03__01-23-07/snmp-readonly-monitoring-bash-centos5-8799) |
| ssh-forced-command-ingest | — | — | — | — | — | — | — | — | [9m 03s](../../../jobs/8799/2026-10-03__01-23-07/ssh-forced-command-ingest-bash-centos5-8799) |
| ssh-local-service-tunnel | — | — | — | — | — | — | — | — | [9m 44s](../../../jobs/8799/2026-10-03__01-23-07/ssh-local-service-tunnel-bash-centos5-8799) |
| tftp-firmware-distribution | — | — | — | — | — | — | — | — | [8m 53s](../../../jobs/8799/2026-10-03__01-23-07/tftp-firmware-distribution-bash-centos5-8799) |
| udp-meter-ingestion | — | — | — | — | — | — | — | — | [11m 34s](../../../jobs/8799/2026-10-03__01-23-07/udp-meter-ingestion-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 9m 53s |

Cluster provisioning is not a meaningful part of these times: median 689 ms across 60 clusters, about 0.18% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 | centos5 |
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
| database-reader-writer-roles | — | — | — | — | — | — | — | — | [0.620](../../../jobs/8799/2026-10-03__01-23-07/database-reader-writer-roles-bash-centos5-8799) |
| forward-proxy-destination-policy | — | — | — | — | — | — | — | — | [0.900](../../../jobs/8799/2026-10-03__01-23-07/forward-proxy-destination-policy-bash-centos5-8799) |
| ftp-dropbox-confinement | — | — | — | — | — | — | — | — | [0.420](../../../jobs/8799/2026-10-03__01-23-07/ftp-dropbox-confinement-bash-centos5-8799) |
| http-upload-size-boundary | — | — | — | — | — | — | — | — | [0.920](../../../jobs/8799/2026-10-03__01-23-07/http-upload-size-boundary-bash-centos5-8799) |
| imap-maildir-cutover | — | — | — | — | — | — | — | — | [0.620](../../../jobs/8799/2026-10-03__01-23-07/imap-maildir-cutover-bash-centos5-8799) |
| inetd-request-activation | — | — | — | — | — | — | — | — | [0.760](../../../jobs/8799/2026-10-03__01-23-07/inetd-request-activation-bash-centos5-8799) |
| kerberos-service-identity | — | — | — | — | — | — | — | — | [0.930](../../../jobs/8799/2026-10-03__01-23-07/kerberos-service-identity-bash-centos5-8799) |
| ldap-attribute-privacy | — | — | — | — | — | — | — | — | [0.750](../../../jobs/8799/2026-10-03__01-23-07/ldap-attribute-privacy-bash-centos5-8799) |
| ldap-directory-import | — | — | — | — | — | — | — | — | [0.900](../../../jobs/8799/2026-10-03__01-23-07/ldap-directory-import-bash-centos5-8799) |
| mysql-relational-import | — | — | — | — | — | — | — | — | [0.700](../../../jobs/8799/2026-10-03__01-23-07/mysql-relational-import-bash-centos5-8799) |
| mysql-replication-catchup | — | — | — | — | — | — | — | — | [0.580](../../../jobs/8799/2026-10-03__01-23-07/mysql-replication-catchup-bash-centos5-8799) |
| radius-network-authentication | — | — | — | — | — | — | — | — | [0.770](../../../jobs/8799/2026-10-03__01-23-07/radius-network-authentication-bash-centos5-8799) |
| rsync-module-publication | — | — | — | — | — | — | — | — | [0.950](../../../jobs/8799/2026-10-03__01-23-07/rsync-module-publication-bash-centos5-8799) |
| samba-team-share | — | — | — | — | — | — | — | — | [0.720](../../../jobs/8799/2026-10-03__01-23-07/samba-team-share-bash-centos5-8799) |
| smtp-alias-delivery | — | — | — | — | — | — | — | — | [0.880](../../../jobs/8799/2026-10-03__01-23-07/smtp-alias-delivery-bash-centos5-8799) |
| snmp-readonly-monitoring | — | — | — | — | — | — | — | — | [0.820](../../../jobs/8799/2026-10-03__01-23-07/snmp-readonly-monitoring-bash-centos5-8799) |
| ssh-forced-command-ingest | — | — | — | — | — | — | — | — | [0.880](../../../jobs/8799/2026-10-03__01-23-07/ssh-forced-command-ingest-bash-centos5-8799) |
| ssh-local-service-tunnel | — | — | — | — | — | — | — | — | [0.850](../../../jobs/8799/2026-10-03__01-23-07/ssh-local-service-tunnel-bash-centos5-8799) |
| tftp-firmware-distribution | — | — | — | — | — | — | — | — | [0.820](../../../jobs/8799/2026-10-03__01-23-07/tftp-firmware-distribution-bash-centos5-8799) |
| udp-meter-ingestion | — | — | — | — | — | — | — | — | [0.840](../../../jobs/8799/2026-10-03__01-23-07/udp-meter-ingestion-bash-centos5-8799) |
| **Average** | — | — | — | — | — | — | — | — | 0.782 |
