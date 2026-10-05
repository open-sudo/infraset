# multi-node-os-comparison: command execution summary

Scope: `2935/2026-10-04__17-37-12`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [41/1](../../../jobs/2935/2026-10-04__17-37-12/shared-nfs-storage-bash-rhel10-2935) | — | — |
| centralized-log-collector | — | — | — | — | — | [21/0](../../../jobs/2935/2026-10-04__17-37-12/centralized-log-collector-bash-rhel10-2935) | — | — |
| ssh-controller-access | — | — | — | — | — | [25/4](../../../jobs/2935/2026-10-04__17-37-12/ssh-controller-access-bash-rhel10-2935) | — | — |
| internal-ca-tls | — | — | — | — | — | [36/2](../../../jobs/2935/2026-10-04__17-37-12/internal-ca-tls-bash-rhel10-2935) | — | — |
| internal-time-sync | — | — | — | — | — | [24/0](../../../jobs/2935/2026-10-04__17-37-12/internal-time-sync-bash-rhel10-2935) | — | — |
| load-balanced-web-tier | — | — | — | — | — | [58/0](../../../jobs/2935/2026-10-04__17-37-12/load-balanced-web-tier-bash-rhel10-2935) | — | — |
| network-scoped-firewall | — | — | — | — | — | [40/1](../../../jobs/2935/2026-10-04__17-37-12/network-scoped-firewall-bash-rhel10-2935) | — | — |
| config-sync | — | — | — | — | — | [34/3](../../../jobs/2935/2026-10-04__17-37-12/config-sync-bash-rhel10-2935) | — | — |
| scheduled-backup | — | — | — | — | — | [37/1](../../../jobs/2935/2026-10-04__17-37-12/scheduled-backup-bash-rhel10-2935) | — | — |
| internal-dns-resolution | — | — | — | — | — | [32/3](../../../jobs/2935/2026-10-04__17-37-12/internal-dns-resolution-bash-rhel10-2935) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [34/1](../../../jobs/2935/2026-10-04__17-37-12/database-reader-writer-roles-bash-rhel10-2935) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [30/0](../../../jobs/2935/2026-10-04__17-37-12/forward-proxy-destination-policy-bash-rhel10-2935) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [33/2](../../../jobs/2935/2026-10-04__17-37-12/ftp-dropbox-confinement-bash-rhel10-2935) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [29/0](../../../jobs/2935/2026-10-04__17-37-12/http-upload-size-boundary-bash-rhel10-2935) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [30/4](../../../jobs/2935/2026-10-04__17-37-12/imap-maildir-cutover-bash-rhel10-2935) | — | — |
| inetd-request-activation | — | — | — | — | — | [37/4](../../../jobs/2935/2026-10-04__17-37-12/inetd-request-activation-bash-rhel10-2935) | — | — |
| kerberos-service-identity | — | — | — | — | — | [30/1](../../../jobs/2935/2026-10-04__17-37-12/kerberos-service-identity-bash-rhel10-2935) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [41/6](../../../jobs/2935/2026-10-04__17-37-12/ldap-attribute-privacy-bash-rhel10-2935) | — | — |
| ldap-directory-import | — | — | — | — | — | [27/5](../../../jobs/2935/2026-10-04__17-37-12/ldap-directory-import-bash-rhel10-2935) | — | — |
| mysql-relational-import | — | — | — | — | — | [39/1](../../../jobs/2935/2026-10-04__17-37-12/mysql-relational-import-bash-rhel10-2935) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [40/1](../../../jobs/2935/2026-10-04__17-37-12/mysql-replication-catchup-bash-rhel10-2935) | — | — |
| radius-network-authentication | — | — | — | — | — | [29/2](../../../jobs/2935/2026-10-04__17-37-12/radius-network-authentication-bash-rhel10-2935) | — | — |
| rsync-module-publication | — | — | — | — | — | [38/0](../../../jobs/2935/2026-10-04__17-37-12/rsync-module-publication-bash-rhel10-2935) | — | — |
| samba-team-share | — | — | — | — | — | [32/4](../../../jobs/2935/2026-10-04__17-37-12/samba-team-share-bash-rhel10-2935) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [32/1](../../../jobs/2935/2026-10-04__17-37-12/smtp-alias-delivery-bash-rhel10-2935) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [27/1](../../../jobs/2935/2026-10-04__17-37-12/snmp-readonly-monitoring-bash-rhel10-2935) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [32/2](../../../jobs/2935/2026-10-04__17-37-12/ssh-forced-command-ingest-bash-rhel10-2935) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [35/3](../../../jobs/2935/2026-10-04__17-37-12/ssh-local-service-tunnel-bash-rhel10-2935) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [41/2](../../../jobs/2935/2026-10-04__17-37-12/tftp-firmware-distribution-bash-rhel10-2935) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [37/2](../../../jobs/2935/2026-10-04__17-37-12/udp-meter-ingestion-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 34.0/1.9 | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [10m 08s](../../../jobs/2935/2026-10-04__17-37-12/shared-nfs-storage-bash-rhel10-2935) | — | — |
| centralized-log-collector | — | — | — | — | — | [7m 06s](../../../jobs/2935/2026-10-04__17-37-12/centralized-log-collector-bash-rhel10-2935) | — | — |
| ssh-controller-access | — | — | — | — | — | [6m 54s](../../../jobs/2935/2026-10-04__17-37-12/ssh-controller-access-bash-rhel10-2935) | — | — |
| internal-ca-tls | — | — | — | — | — | [10m 38s](../../../jobs/2935/2026-10-04__17-37-12/internal-ca-tls-bash-rhel10-2935) | — | — |
| internal-time-sync | — | — | — | — | — | [5m 59s](../../../jobs/2935/2026-10-04__17-37-12/internal-time-sync-bash-rhel10-2935) | — | — |
| load-balanced-web-tier | — | — | — | — | — | [11m 08s](../../../jobs/2935/2026-10-04__17-37-12/load-balanced-web-tier-bash-rhel10-2935) | — | — |
| network-scoped-firewall | — | — | — | — | — | [7m 05s](../../../jobs/2935/2026-10-04__17-37-12/network-scoped-firewall-bash-rhel10-2935) | — | — |
| config-sync | — | — | — | — | — | [9m 59s](../../../jobs/2935/2026-10-04__17-37-12/config-sync-bash-rhel10-2935) | — | — |
| scheduled-backup | — | — | — | — | — | [9m 40s](../../../jobs/2935/2026-10-04__17-37-12/scheduled-backup-bash-rhel10-2935) | — | — |
| internal-dns-resolution | — | — | — | — | — | [8m 52s](../../../jobs/2935/2026-10-04__17-37-12/internal-dns-resolution-bash-rhel10-2935) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [9m 07s](../../../jobs/2935/2026-10-04__17-37-12/database-reader-writer-roles-bash-rhel10-2935) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [8m 36s](../../../jobs/2935/2026-10-04__17-37-12/forward-proxy-destination-policy-bash-rhel10-2935) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [8m 32s](../../../jobs/2935/2026-10-04__17-37-12/ftp-dropbox-confinement-bash-rhel10-2935) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [9m 06s](../../../jobs/2935/2026-10-04__17-37-12/http-upload-size-boundary-bash-rhel10-2935) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [13m 02s](../../../jobs/2935/2026-10-04__17-37-12/imap-maildir-cutover-bash-rhel10-2935) | — | — |
| inetd-request-activation | — | — | — | — | — | [10m 42s](../../../jobs/2935/2026-10-04__17-37-12/inetd-request-activation-bash-rhel10-2935) | — | — |
| kerberos-service-identity | — | — | — | — | — | [10m 17s](../../../jobs/2935/2026-10-04__17-37-12/kerberos-service-identity-bash-rhel10-2935) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [16m 18s](../../../jobs/2935/2026-10-04__17-37-12/ldap-attribute-privacy-bash-rhel10-2935) | — | — |
| ldap-directory-import | — | — | — | — | — | [9m 33s](../../../jobs/2935/2026-10-04__17-37-12/ldap-directory-import-bash-rhel10-2935) | — | — |
| mysql-relational-import | — | — | — | — | — | [8m 47s](../../../jobs/2935/2026-10-04__17-37-12/mysql-relational-import-bash-rhel10-2935) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [12m 40s](../../../jobs/2935/2026-10-04__17-37-12/mysql-replication-catchup-bash-rhel10-2935) | — | — |
| radius-network-authentication | — | — | — | — | — | [10m 28s](../../../jobs/2935/2026-10-04__17-37-12/radius-network-authentication-bash-rhel10-2935) | — | — |
| rsync-module-publication | — | — | — | — | — | [9m 46s](../../../jobs/2935/2026-10-04__17-37-12/rsync-module-publication-bash-rhel10-2935) | — | — |
| samba-team-share | — | — | — | — | — | [10m 56s](../../../jobs/2935/2026-10-04__17-37-12/samba-team-share-bash-rhel10-2935) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [9m 18s](../../../jobs/2935/2026-10-04__17-37-12/smtp-alias-delivery-bash-rhel10-2935) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [8m 55s](../../../jobs/2935/2026-10-04__17-37-12/snmp-readonly-monitoring-bash-rhel10-2935) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [10m 13s](../../../jobs/2935/2026-10-04__17-37-12/ssh-forced-command-ingest-bash-rhel10-2935) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [9m 08s](../../../jobs/2935/2026-10-04__17-37-12/ssh-local-service-tunnel-bash-rhel10-2935) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [13m 19s](../../../jobs/2935/2026-10-04__17-37-12/tftp-firmware-distribution-bash-rhel10-2935) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [9m 39s](../../../jobs/2935/2026-10-04__17-37-12/udp-meter-ingestion-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 9m 52s | — | — |

Cluster provisioning is not a meaningful part of these times: median 805 ms across 100 clusters, about 0.22% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/shared-nfs-storage-bash-rhel10-2935) | — | — |
| centralized-log-collector | — | — | — | — | — | [0.990](../../../jobs/2935/2026-10-04__17-37-12/centralized-log-collector-bash-rhel10-2935) | — | — |
| ssh-controller-access | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/ssh-controller-access-bash-rhel10-2935) | — | — |
| internal-ca-tls | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/internal-ca-tls-bash-rhel10-2935) | — | — |
| internal-time-sync | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/internal-time-sync-bash-rhel10-2935) | — | — |
| load-balanced-web-tier | — | — | — | — | — | [0.950](../../../jobs/2935/2026-10-04__17-37-12/load-balanced-web-tier-bash-rhel10-2935) | — | — |
| network-scoped-firewall | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/network-scoped-firewall-bash-rhel10-2935) | — | — |
| config-sync | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/config-sync-bash-rhel10-2935) | — | — |
| scheduled-backup | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/scheduled-backup-bash-rhel10-2935) | — | — |
| internal-dns-resolution | — | — | — | — | — | [0.960](../../../jobs/2935/2026-10-04__17-37-12/internal-dns-resolution-bash-rhel10-2935) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__17-37-12/database-reader-writer-roles-bash-rhel10-2935) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__17-37-12/forward-proxy-destination-policy-bash-rhel10-2935) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [0.940](../../../jobs/2935/2026-10-04__17-37-12/ftp-dropbox-confinement-bash-rhel10-2935) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [0.960](../../../jobs/2935/2026-10-04__17-37-12/http-upload-size-boundary-bash-rhel10-2935) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [0.990](../../../jobs/2935/2026-10-04__17-37-12/imap-maildir-cutover-bash-rhel10-2935) | — | — |
| inetd-request-activation | — | — | — | — | — | [0.970](../../../jobs/2935/2026-10-04__17-37-12/inetd-request-activation-bash-rhel10-2935) | — | — |
| kerberos-service-identity | — | — | — | — | — | [0.990](../../../jobs/2935/2026-10-04__17-37-12/kerberos-service-identity-bash-rhel10-2935) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/ldap-attribute-privacy-bash-rhel10-2935) | — | — |
| ldap-directory-import | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/ldap-directory-import-bash-rhel10-2935) | — | — |
| mysql-relational-import | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__17-37-12/mysql-relational-import-bash-rhel10-2935) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/mysql-replication-catchup-bash-rhel10-2935) | — | — |
| radius-network-authentication | — | — | — | — | — | [0.970](../../../jobs/2935/2026-10-04__17-37-12/radius-network-authentication-bash-rhel10-2935) | — | — |
| rsync-module-publication | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/rsync-module-publication-bash-rhel10-2935) | — | — |
| samba-team-share | — | — | — | — | — | [0.990](../../../jobs/2935/2026-10-04__17-37-12/samba-team-share-bash-rhel10-2935) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/smtp-alias-delivery-bash-rhel10-2935) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/snmp-readonly-monitoring-bash-rhel10-2935) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [0.960](../../../jobs/2935/2026-10-04__17-37-12/ssh-forced-command-ingest-bash-rhel10-2935) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__17-37-12/ssh-local-service-tunnel-bash-rhel10-2935) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [0.980](../../../jobs/2935/2026-10-04__17-37-12/tftp-firmware-distribution-bash-rhel10-2935) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [1.000](../../../jobs/2935/2026-10-04__17-37-12/udp-meter-ingestion-bash-rhel10-2935) | — | — |
| **Average** | — | — | — | — | — | 0.986 | — | — |
