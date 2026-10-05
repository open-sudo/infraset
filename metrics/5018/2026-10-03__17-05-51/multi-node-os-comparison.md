# multi-node-os-comparison: command execution summary

Scope: `5018/2026-10-03__17-05-51`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | [33/1](../../../jobs/5018/2026-10-03__17-05-51/shared-nfs-storage-bash-alpine-5018) | — | — | — | — | — | — | — |
| centralized-log-collector | [28/2](../../../jobs/5018/2026-10-03__17-05-51/centralized-log-collector-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-controller-access | [23/2](../../../jobs/5018/2026-10-03__17-05-51/ssh-controller-access-bash-alpine-5018) | — | — | — | — | — | — | — |
| internal-ca-tls | [33/2](../../../jobs/5018/2026-10-03__17-05-51/internal-ca-tls-bash-alpine-5018) | — | — | — | — | — | — | — |
| internal-time-sync | [23/0](../../../jobs/5018/2026-10-03__17-05-51/internal-time-sync-bash-alpine-5018) | — | — | — | — | — | — | — |
| load-balanced-web-tier | [31/2](../../../jobs/5018/2026-10-03__17-05-51/load-balanced-web-tier-bash-alpine-5018) | — | — | — | — | — | — | — |
| network-scoped-firewall | [34/0](../../../jobs/5018/2026-10-03__17-05-51/network-scoped-firewall-bash-alpine-5018) | — | — | — | — | — | — | — |
| config-sync | [26/0](../../../jobs/5018/2026-10-03__17-05-51/config-sync-bash-alpine-5018) | — | — | — | — | — | — | — |
| scheduled-backup | [40/4](../../../jobs/5018/2026-10-03__17-05-51/scheduled-backup-bash-alpine-5018) | — | — | — | — | — | — | — |
| internal-dns-resolution | [31/4](../../../jobs/5018/2026-10-03__17-05-51/internal-dns-resolution-bash-alpine-5018) | — | — | — | — | — | — | — |
| database-reader-writer-roles | [36/0](../../../jobs/5018/2026-10-03__17-05-51/database-reader-writer-roles-bash-alpine-5018) | — | — | — | — | — | — | — |
| forward-proxy-destination-policy | [30/4](../../../jobs/5018/2026-10-03__17-05-51/forward-proxy-destination-policy-bash-alpine-5018) | — | — | — | — | — | — | — |
| ftp-dropbox-confinement | [28/3](../../../jobs/5018/2026-10-03__17-05-51/ftp-dropbox-confinement-bash-alpine-5018) | — | — | — | — | — | — | — |
| http-upload-size-boundary | [25/1](../../../jobs/5018/2026-10-03__17-05-51/http-upload-size-boundary-bash-alpine-5018) | — | — | — | — | — | — | — |
| imap-maildir-cutover | [37/5](../../../jobs/5018/2026-10-03__17-05-51/imap-maildir-cutover-bash-alpine-5018) | — | — | — | — | — | — | — |
| inetd-request-activation | [20/1](../../../jobs/5018/2026-10-03__17-05-51/inetd-request-activation-bash-alpine-5018) | — | — | — | — | — | — | — |
| kerberos-service-identity | [41/6](../../../jobs/5018/2026-10-03__17-05-51/kerberos-service-identity-bash-alpine-5018) | — | — | — | — | — | — | — |
| ldap-attribute-privacy | [29/3](../../../jobs/5018/2026-10-03__17-05-51/ldap-attribute-privacy-bash-alpine-5018) | — | — | — | — | — | — | — |
| ldap-directory-import | [34/3](../../../jobs/5018/2026-10-03__17-05-51/ldap-directory-import-bash-alpine-5018) | — | — | — | — | — | — | — |
| mysql-relational-import | [33/3](../../../jobs/5018/2026-10-03__17-05-51/mysql-relational-import-bash-alpine-5018) | — | — | — | — | — | — | — |
| mysql-replication-catchup | [37/5](../../../jobs/5018/2026-10-03__17-05-51/mysql-replication-catchup-bash-alpine-5018) | — | — | — | — | — | — | — |
| radius-network-authentication | [38/2](../../../jobs/5018/2026-10-03__17-05-51/radius-network-authentication-bash-alpine-5018) | — | — | — | — | — | — | — |
| rsync-module-publication | [24/1](../../../jobs/5018/2026-10-03__17-05-51/rsync-module-publication-bash-alpine-5018) | — | — | — | — | — | — | — |
| samba-team-share | [25/2](../../../jobs/5018/2026-10-03__17-05-51/samba-team-share-bash-alpine-5018) | — | — | — | — | — | — | — |
| smtp-alias-delivery | [28/2](../../../jobs/5018/2026-10-03__17-05-51/smtp-alias-delivery-bash-alpine-5018) | — | — | — | — | — | — | — |
| snmp-readonly-monitoring | [24/3](../../../jobs/5018/2026-10-03__17-05-51/snmp-readonly-monitoring-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-forced-command-ingest | [34/4](../../../jobs/5018/2026-10-03__17-05-51/ssh-forced-command-ingest-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-local-service-tunnel | [50/4](../../../jobs/5018/2026-10-03__17-05-51/ssh-local-service-tunnel-bash-alpine-5018) | — | — | — | — | — | — | — |
| tftp-firmware-distribution | [34/4](../../../jobs/5018/2026-10-03__17-05-51/tftp-firmware-distribution-bash-alpine-5018) | — | — | — | — | — | — | — |
| udp-meter-ingestion | [37/3](../../../jobs/5018/2026-10-03__17-05-51/udp-meter-ingestion-bash-alpine-5018) | — | — | — | — | — | — | — |
| **Average** | 31.5/2.5 | — | — | — | — | — | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | [5m 46s](../../../jobs/5018/2026-10-03__17-05-51/shared-nfs-storage-bash-alpine-5018) | — | — | — | — | — | — | — |
| centralized-log-collector | [4m 41s](../../../jobs/5018/2026-10-03__17-05-51/centralized-log-collector-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-controller-access | [4m 26s](../../../jobs/5018/2026-10-03__17-05-51/ssh-controller-access-bash-alpine-5018) | — | — | — | — | — | — | — |
| internal-ca-tls | [5m 01s](../../../jobs/5018/2026-10-03__17-05-51/internal-ca-tls-bash-alpine-5018) | — | — | — | — | — | — | — |
| internal-time-sync | [4m 15s](../../../jobs/5018/2026-10-03__17-05-51/internal-time-sync-bash-alpine-5018) | — | — | — | — | — | — | — |
| load-balanced-web-tier | [30m 00s](../../../jobs/5018/2026-10-03__17-05-51/load-balanced-web-tier-bash-alpine-5018) | — | — | — | — | — | — | — |
| network-scoped-firewall | [6m 08s](../../../jobs/5018/2026-10-03__17-05-51/network-scoped-firewall-bash-alpine-5018) | — | — | — | — | — | — | — |
| config-sync | [6m 45s](../../../jobs/5018/2026-10-03__17-05-51/config-sync-bash-alpine-5018) | — | — | — | — | — | — | — |
| scheduled-backup | [9m 26s](../../../jobs/5018/2026-10-03__17-05-51/scheduled-backup-bash-alpine-5018) | — | — | — | — | — | — | — |
| internal-dns-resolution | [5m 13s](../../../jobs/5018/2026-10-03__17-05-51/internal-dns-resolution-bash-alpine-5018) | — | — | — | — | — | — | — |
| database-reader-writer-roles | [6m 03s](../../../jobs/5018/2026-10-03__17-05-51/database-reader-writer-roles-bash-alpine-5018) | — | — | — | — | — | — | — |
| forward-proxy-destination-policy | [6m 33s](../../../jobs/5018/2026-10-03__17-05-51/forward-proxy-destination-policy-bash-alpine-5018) | — | — | — | — | — | — | — |
| ftp-dropbox-confinement | [6m 32s](../../../jobs/5018/2026-10-03__17-05-51/ftp-dropbox-confinement-bash-alpine-5018) | — | — | — | — | — | — | — |
| http-upload-size-boundary | [6m 09s](../../../jobs/5018/2026-10-03__17-05-51/http-upload-size-boundary-bash-alpine-5018) | — | — | — | — | — | — | — |
| imap-maildir-cutover | [6m 43s](../../../jobs/5018/2026-10-03__17-05-51/imap-maildir-cutover-bash-alpine-5018) | — | — | — | — | — | — | — |
| inetd-request-activation | [4m 29s](../../../jobs/5018/2026-10-03__17-05-51/inetd-request-activation-bash-alpine-5018) | — | — | — | — | — | — | — |
| kerberos-service-identity | [6m 41s](../../../jobs/5018/2026-10-03__17-05-51/kerberos-service-identity-bash-alpine-5018) | — | — | — | — | — | — | — |
| ldap-attribute-privacy | [6m 37s](../../../jobs/5018/2026-10-03__17-05-51/ldap-attribute-privacy-bash-alpine-5018) | — | — | — | — | — | — | — |
| ldap-directory-import | [4m 18s](../../../jobs/5018/2026-10-03__17-05-51/ldap-directory-import-bash-alpine-5018) | — | — | — | — | — | — | — |
| mysql-relational-import | [6m 27s](../../../jobs/5018/2026-10-03__17-05-51/mysql-relational-import-bash-alpine-5018) | — | — | — | — | — | — | — |
| mysql-replication-catchup | [7m 44s](../../../jobs/5018/2026-10-03__17-05-51/mysql-replication-catchup-bash-alpine-5018) | — | — | — | — | — | — | — |
| radius-network-authentication | [6m 21s](../../../jobs/5018/2026-10-03__17-05-51/radius-network-authentication-bash-alpine-5018) | — | — | — | — | — | — | — |
| rsync-module-publication | [5m 07s](../../../jobs/5018/2026-10-03__17-05-51/rsync-module-publication-bash-alpine-5018) | — | — | — | — | — | — | — |
| samba-team-share | [6m 52s](../../../jobs/5018/2026-10-03__17-05-51/samba-team-share-bash-alpine-5018) | — | — | — | — | — | — | — |
| smtp-alias-delivery | [13m 20s](../../../jobs/5018/2026-10-03__17-05-51/smtp-alias-delivery-bash-alpine-5018) | — | — | — | — | — | — | — |
| snmp-readonly-monitoring | [4m 21s](../../../jobs/5018/2026-10-03__17-05-51/snmp-readonly-monitoring-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-forced-command-ingest | [5m 56s](../../../jobs/5018/2026-10-03__17-05-51/ssh-forced-command-ingest-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-local-service-tunnel | [11m 32s](../../../jobs/5018/2026-10-03__17-05-51/ssh-local-service-tunnel-bash-alpine-5018) | — | — | — | — | — | — | — |
| tftp-firmware-distribution | [6m 04s](../../../jobs/5018/2026-10-03__17-05-51/tftp-firmware-distribution-bash-alpine-5018) | — | — | — | — | — | — | — |
| udp-meter-ingestion | [10m 09s](../../../jobs/5018/2026-10-03__17-05-51/udp-meter-ingestion-bash-alpine-5018) | — | — | — | — | — | — | — |
| **Average** | 7m 19s | — | — | — | — | — | — | — |

Cluster provisioning is not a meaningful part of these times: median 712 ms across 100 clusters, about 0.31% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | [1.000](../../../jobs/5018/2026-10-03__17-05-51/shared-nfs-storage-bash-alpine-5018) | — | — | — | — | — | — | — |
| centralized-log-collector | [0.940](../../../jobs/5018/2026-10-03__17-05-51/centralized-log-collector-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-controller-access | [0.880](../../../jobs/5018/2026-10-03__17-05-51/ssh-controller-access-bash-alpine-5018) | — | — | — | — | — | — | — |
| internal-ca-tls | [0.500](../../../jobs/5018/2026-10-03__17-05-51/internal-ca-tls-bash-alpine-5018) | — | — | — | — | — | — | — |
| internal-time-sync | [0.960](../../../jobs/5018/2026-10-03__17-05-51/internal-time-sync-bash-alpine-5018) | — | — | — | — | — | — | — |
| load-balanced-web-tier | [0.960](../../../jobs/5018/2026-10-03__17-05-51/load-balanced-web-tier-bash-alpine-5018) | — | — | — | — | — | — | — |
| network-scoped-firewall | [0.840](../../../jobs/5018/2026-10-03__17-05-51/network-scoped-firewall-bash-alpine-5018) | — | — | — | — | — | — | — |
| config-sync | [0.820](../../../jobs/5018/2026-10-03__17-05-51/config-sync-bash-alpine-5018) | — | — | — | — | — | — | — |
| scheduled-backup | [0.500](../../../jobs/5018/2026-10-03__17-05-51/scheduled-backup-bash-alpine-5018) | — | — | — | — | — | — | — |
| internal-dns-resolution | [1.000](../../../jobs/5018/2026-10-03__17-05-51/internal-dns-resolution-bash-alpine-5018) | — | — | — | — | — | — | — |
| database-reader-writer-roles | [0.870](../../../jobs/5018/2026-10-03__17-05-51/database-reader-writer-roles-bash-alpine-5018) | — | — | — | — | — | — | — |
| forward-proxy-destination-policy | [0.920](../../../jobs/5018/2026-10-03__17-05-51/forward-proxy-destination-policy-bash-alpine-5018) | — | — | — | — | — | — | — |
| ftp-dropbox-confinement | [0.900](../../../jobs/5018/2026-10-03__17-05-51/ftp-dropbox-confinement-bash-alpine-5018) | — | — | — | — | — | — | — |
| http-upload-size-boundary | [0.880](../../../jobs/5018/2026-10-03__17-05-51/http-upload-size-boundary-bash-alpine-5018) | — | — | — | — | — | — | — |
| imap-maildir-cutover | [0.580](../../../jobs/5018/2026-10-03__17-05-51/imap-maildir-cutover-bash-alpine-5018) | — | — | — | — | — | — | — |
| inetd-request-activation | [0.860](../../../jobs/5018/2026-10-03__17-05-51/inetd-request-activation-bash-alpine-5018) | — | — | — | — | — | — | — |
| kerberos-service-identity | [0.620](../../../jobs/5018/2026-10-03__17-05-51/kerberos-service-identity-bash-alpine-5018) | — | — | — | — | — | — | — |
| ldap-attribute-privacy | [0.620](../../../jobs/5018/2026-10-03__17-05-51/ldap-attribute-privacy-bash-alpine-5018) | — | — | — | — | — | — | — |
| ldap-directory-import | [0.930](../../../jobs/5018/2026-10-03__17-05-51/ldap-directory-import-bash-alpine-5018) | — | — | — | — | — | — | — |
| mysql-relational-import | [0.900](../../../jobs/5018/2026-10-03__17-05-51/mysql-relational-import-bash-alpine-5018) | — | — | — | — | — | — | — |
| mysql-replication-catchup | [0.760](../../../jobs/5018/2026-10-03__17-05-51/mysql-replication-catchup-bash-alpine-5018) | — | — | — | — | — | — | — |
| radius-network-authentication | [0.820](../../../jobs/5018/2026-10-03__17-05-51/radius-network-authentication-bash-alpine-5018) | — | — | — | — | — | — | — |
| rsync-module-publication | [0.940](../../../jobs/5018/2026-10-03__17-05-51/rsync-module-publication-bash-alpine-5018) | — | — | — | — | — | — | — |
| samba-team-share | [0.760](../../../jobs/5018/2026-10-03__17-05-51/samba-team-share-bash-alpine-5018) | — | — | — | — | — | — | — |
| smtp-alias-delivery | [0.960](../../../jobs/5018/2026-10-03__17-05-51/smtp-alias-delivery-bash-alpine-5018) | — | — | — | — | — | — | — |
| snmp-readonly-monitoring | [0.850](../../../jobs/5018/2026-10-03__17-05-51/snmp-readonly-monitoring-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-forced-command-ingest | [0.940](../../../jobs/5018/2026-10-03__17-05-51/ssh-forced-command-ingest-bash-alpine-5018) | — | — | — | — | — | — | — |
| ssh-local-service-tunnel | [0.880](../../../jobs/5018/2026-10-03__17-05-51/ssh-local-service-tunnel-bash-alpine-5018) | — | — | — | — | — | — | — |
| tftp-firmware-distribution | [0.820](../../../jobs/5018/2026-10-03__17-05-51/tftp-firmware-distribution-bash-alpine-5018) | — | — | — | — | — | — | — |
| udp-meter-ingestion | [0.890](../../../jobs/5018/2026-10-03__17-05-51/udp-meter-ingestion-bash-alpine-5018) | — | — | — | — | — | — | — |
| **Average** | 0.837 | — | — | — | — | — | — | — |
