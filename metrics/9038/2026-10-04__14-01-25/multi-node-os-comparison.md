# multi-node-os-comparison: command execution summary

Scope: `9038/2026-10-04__14-01-25`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [33/1](../../../jobs/9038/2026-10-04__14-01-25/shared-nfs-storage-bash-rhel10-9038) | — | — |
| centralized-log-collector | — | — | — | — | — | [23/3](../../../jobs/9038/2026-10-04__14-01-25/centralized-log-collector-bash-rhel10-9038) | — | — |
| ssh-controller-access | — | — | — | — | — | [25/0](../../../jobs/9038/2026-10-04__14-01-25/ssh-controller-access-bash-rhel10-9038) | — | — |
| internal-ca-tls | — | — | — | — | — | [28/0](../../../jobs/9038/2026-10-04__14-01-25/internal-ca-tls-bash-rhel10-9038) | — | — |
| internal-time-sync | — | — | — | — | — | [0/0](../../../jobs/9038/2026-10-04__14-01-25/internal-time-sync-bash-rhel10-9038) | — | — |
| load-balanced-web-tier | — | — | — | — | — | [44/4](../../../jobs/9038/2026-10-04__14-01-25/load-balanced-web-tier-bash-rhel10-9038) | — | — |
| network-scoped-firewall | — | — | — | — | — | [32/0](../../../jobs/9038/2026-10-04__14-01-25/network-scoped-firewall-bash-rhel10-9038) | — | — |
| config-sync | — | — | — | — | — | [30/3](../../../jobs/9038/2026-10-04__14-01-25/config-sync-bash-rhel10-9038) | — | — |
| scheduled-backup | — | — | — | — | — | [32/2](../../../jobs/9038/2026-10-04__14-01-25/scheduled-backup-bash-rhel10-9038) | — | — |
| internal-dns-resolution | — | — | — | — | — | [33/5](../../../jobs/9038/2026-10-04__14-01-25/internal-dns-resolution-bash-rhel10-9038) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [33/2](../../../jobs/9038/2026-10-04__14-01-25/database-reader-writer-roles-bash-rhel10-9038) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [28/2](../../../jobs/9038/2026-10-04__14-01-25/forward-proxy-destination-policy-bash-rhel10-9038) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [31/3](../../../jobs/9038/2026-10-04__14-01-25/ftp-dropbox-confinement-bash-rhel10-9038) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [31/0](../../../jobs/9038/2026-10-04__14-01-25/http-upload-size-boundary-bash-rhel10-9038) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [22/1](../../../jobs/9038/2026-10-04__14-01-25/imap-maildir-cutover-bash-rhel10-9038) | — | — |
| inetd-request-activation | — | — | — | — | — | [54/3](../../../jobs/9038/2026-10-04__14-01-25/inetd-request-activation-bash-rhel10-9038) | — | — |
| kerberos-service-identity | — | — | — | — | — | [31/2](../../../jobs/9038/2026-10-04__14-01-25/kerberos-service-identity-bash-rhel10-9038) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [34/4](../../../jobs/9038/2026-10-04__14-01-25/ldap-attribute-privacy-bash-rhel10-9038) | — | — |
| ldap-directory-import | — | — | — | — | — | [37/6](../../../jobs/9038/2026-10-04__14-01-25/ldap-directory-import-bash-rhel10-9038) | — | — |
| mysql-relational-import | — | — | — | — | — | [35/2](../../../jobs/9038/2026-10-04__14-01-25/mysql-relational-import-bash-rhel10-9038) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [50/3](../../../jobs/9038/2026-10-04__14-01-25/mysql-replication-catchup-bash-rhel10-9038) | — | — |
| radius-network-authentication | — | — | — | — | — | [34/0](../../../jobs/9038/2026-10-04__14-01-25/radius-network-authentication-bash-rhel10-9038) | — | — |
| rsync-module-publication | — | — | — | — | — | [26/2](../../../jobs/9038/2026-10-04__14-01-25/rsync-module-publication-bash-rhel10-9038) | — | — |
| samba-team-share | — | — | — | — | — | [24/2](../../../jobs/9038/2026-10-04__14-01-25/samba-team-share-bash-rhel10-9038) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [25/1](../../../jobs/9038/2026-10-04__14-01-25/smtp-alias-delivery-bash-rhel10-9038) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [24/2](../../../jobs/9038/2026-10-04__14-01-25/snmp-readonly-monitoring-bash-rhel10-9038) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [27/0](../../../jobs/9038/2026-10-04__14-01-25/ssh-forced-command-ingest-bash-rhel10-9038) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [42/4](../../../jobs/9038/2026-10-04__14-01-25/ssh-local-service-tunnel-bash-rhel10-9038) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [35/3](../../../jobs/9038/2026-10-04__14-01-25/tftp-firmware-distribution-bash-rhel10-9038) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [26/0](../../../jobs/9038/2026-10-04__14-01-25/udp-meter-ingestion-bash-rhel10-9038) | — | — |
| **Average** | — | — | — | — | — | 31.0/2.0 | — | — |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [8m 26s](../../../jobs/9038/2026-10-04__14-01-25/shared-nfs-storage-bash-rhel10-9038) | — | — |
| centralized-log-collector | — | — | — | — | — | [32m 21s](../../../jobs/9038/2026-10-04__14-01-25/centralized-log-collector-bash-rhel10-9038) | — | — |
| ssh-controller-access | — | — | — | — | — | [5m 31s](../../../jobs/9038/2026-10-04__14-01-25/ssh-controller-access-bash-rhel10-9038) | — | — |
| internal-ca-tls | — | — | — | — | — | [7m 52s](../../../jobs/9038/2026-10-04__14-01-25/internal-ca-tls-bash-rhel10-9038) | — | — |
| internal-time-sync | — | — | — | — | — | [1m 04s](../../../jobs/9038/2026-10-04__14-01-25/internal-time-sync-bash-rhel10-9038) | — | — |
| load-balanced-web-tier | — | — | — | — | — | [10m 18s](../../../jobs/9038/2026-10-04__14-01-25/load-balanced-web-tier-bash-rhel10-9038) | — | — |
| network-scoped-firewall | — | — | — | — | — | [6m 03s](../../../jobs/9038/2026-10-04__14-01-25/network-scoped-firewall-bash-rhel10-9038) | — | — |
| config-sync | — | — | — | — | — | [9m 07s](../../../jobs/9038/2026-10-04__14-01-25/config-sync-bash-rhel10-9038) | — | — |
| scheduled-backup | — | — | — | — | — | [7m 07s](../../../jobs/9038/2026-10-04__14-01-25/scheduled-backup-bash-rhel10-9038) | — | — |
| internal-dns-resolution | — | — | — | — | — | [10m 01s](../../../jobs/9038/2026-10-04__14-01-25/internal-dns-resolution-bash-rhel10-9038) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [8m 56s](../../../jobs/9038/2026-10-04__14-01-25/database-reader-writer-roles-bash-rhel10-9038) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [8m 41s](../../../jobs/9038/2026-10-04__14-01-25/forward-proxy-destination-policy-bash-rhel10-9038) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [9m 58s](../../../jobs/9038/2026-10-04__14-01-25/ftp-dropbox-confinement-bash-rhel10-9038) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [9m 19s](../../../jobs/9038/2026-10-04__14-01-25/http-upload-size-boundary-bash-rhel10-9038) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [8m 12s](../../../jobs/9038/2026-10-04__14-01-25/imap-maildir-cutover-bash-rhel10-9038) | — | — |
| inetd-request-activation | — | — | — | — | — | [14m 08s](../../../jobs/9038/2026-10-04__14-01-25/inetd-request-activation-bash-rhel10-9038) | — | — |
| kerberos-service-identity | — | — | — | — | — | [8m 56s](../../../jobs/9038/2026-10-04__14-01-25/kerberos-service-identity-bash-rhel10-9038) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [11m 53s](../../../jobs/9038/2026-10-04__14-01-25/ldap-attribute-privacy-bash-rhel10-9038) | — | — |
| ldap-directory-import | — | — | — | — | — | [9m 36s](../../../jobs/9038/2026-10-04__14-01-25/ldap-directory-import-bash-rhel10-9038) | — | — |
| mysql-relational-import | — | — | — | — | — | [8m 10s](../../../jobs/9038/2026-10-04__14-01-25/mysql-relational-import-bash-rhel10-9038) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [12m 09s](../../../jobs/9038/2026-10-04__14-01-25/mysql-replication-catchup-bash-rhel10-9038) | — | — |
| radius-network-authentication | — | — | — | — | — | [9m 42s](../../../jobs/9038/2026-10-04__14-01-25/radius-network-authentication-bash-rhel10-9038) | — | — |
| rsync-module-publication | — | — | — | — | — | [7m 23s](../../../jobs/9038/2026-10-04__14-01-25/rsync-module-publication-bash-rhel10-9038) | — | — |
| samba-team-share | — | — | — | — | — | [8m 38s](../../../jobs/9038/2026-10-04__14-01-25/samba-team-share-bash-rhel10-9038) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [8m 07s](../../../jobs/9038/2026-10-04__14-01-25/smtp-alias-delivery-bash-rhel10-9038) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [8m 16s](../../../jobs/9038/2026-10-04__14-01-25/snmp-readonly-monitoring-bash-rhel10-9038) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [7m 39s](../../../jobs/9038/2026-10-04__14-01-25/ssh-forced-command-ingest-bash-rhel10-9038) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [10m 56s](../../../jobs/9038/2026-10-04__14-01-25/ssh-local-service-tunnel-bash-rhel10-9038) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [8m 23s](../../../jobs/9038/2026-10-04__14-01-25/tftp-firmware-distribution-bash-rhel10-9038) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [6m 24s](../../../jobs/9038/2026-10-04__14-01-25/udp-meter-ingestion-bash-rhel10-9038) | — | — |
| **Average** | — | — | — | — | — | 9m 27s | — | — |

Cluster provisioning is not a meaningful part of these times: median 1026 ms across 100 clusters, about 0.28% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| shared-nfs-storage | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/shared-nfs-storage-bash-rhel10-9038) | — | — |
| centralized-log-collector | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/centralized-log-collector-bash-rhel10-9038) | — | — |
| ssh-controller-access | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/ssh-controller-access-bash-rhel10-9038) | — | — |
| internal-ca-tls | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/internal-ca-tls-bash-rhel10-9038) | — | — |
| internal-time-sync | — | — | — | — | — | — | — | — |
| load-balanced-web-tier | — | — | — | — | — | [0.970](../../../jobs/9038/2026-10-04__14-01-25/load-balanced-web-tier-bash-rhel10-9038) | — | — |
| network-scoped-firewall | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/network-scoped-firewall-bash-rhel10-9038) | — | — |
| config-sync | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/config-sync-bash-rhel10-9038) | — | — |
| scheduled-backup | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/scheduled-backup-bash-rhel10-9038) | — | — |
| internal-dns-resolution | — | — | — | — | — | [0.960](../../../jobs/9038/2026-10-04__14-01-25/internal-dns-resolution-bash-rhel10-9038) | — | — |
| database-reader-writer-roles | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/database-reader-writer-roles-bash-rhel10-9038) | — | — |
| forward-proxy-destination-policy | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/forward-proxy-destination-policy-bash-rhel10-9038) | — | — |
| ftp-dropbox-confinement | — | — | — | — | — | [0.980](../../../jobs/9038/2026-10-04__14-01-25/ftp-dropbox-confinement-bash-rhel10-9038) | — | — |
| http-upload-size-boundary | — | — | — | — | — | [0.970](../../../jobs/9038/2026-10-04__14-01-25/http-upload-size-boundary-bash-rhel10-9038) | — | — |
| imap-maildir-cutover | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/imap-maildir-cutover-bash-rhel10-9038) | — | — |
| inetd-request-activation | — | — | — | — | — | [0.990](../../../jobs/9038/2026-10-04__14-01-25/inetd-request-activation-bash-rhel10-9038) | — | — |
| kerberos-service-identity | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/kerberos-service-identity-bash-rhel10-9038) | — | — |
| ldap-attribute-privacy | — | — | — | — | — | [0.940](../../../jobs/9038/2026-10-04__14-01-25/ldap-attribute-privacy-bash-rhel10-9038) | — | — |
| ldap-directory-import | — | — | — | — | — | [0.930](../../../jobs/9038/2026-10-04__14-01-25/ldap-directory-import-bash-rhel10-9038) | — | — |
| mysql-relational-import | — | — | — | — | — | [0.980](../../../jobs/9038/2026-10-04__14-01-25/mysql-relational-import-bash-rhel10-9038) | — | — |
| mysql-replication-catchup | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/mysql-replication-catchup-bash-rhel10-9038) | — | — |
| radius-network-authentication | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/radius-network-authentication-bash-rhel10-9038) | — | — |
| rsync-module-publication | — | — | — | — | — | [0.960](../../../jobs/9038/2026-10-04__14-01-25/rsync-module-publication-bash-rhel10-9038) | — | — |
| samba-team-share | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/samba-team-share-bash-rhel10-9038) | — | — |
| smtp-alias-delivery | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/smtp-alias-delivery-bash-rhel10-9038) | — | — |
| snmp-readonly-monitoring | — | — | — | — | — | [1.000](../../../jobs/9038/2026-10-04__14-01-25/snmp-readonly-monitoring-bash-rhel10-9038) | — | — |
| ssh-forced-command-ingest | — | — | — | — | — | [0.980](../../../jobs/9038/2026-10-04__14-01-25/ssh-forced-command-ingest-bash-rhel10-9038) | — | — |
| ssh-local-service-tunnel | — | — | — | — | — | [0.840](../../../jobs/9038/2026-10-04__14-01-25/ssh-local-service-tunnel-bash-rhel10-9038) | — | — |
| tftp-firmware-distribution | — | — | — | — | — | [0.970](../../../jobs/9038/2026-10-04__14-01-25/tftp-firmware-distribution-bash-rhel10-9038) | — | — |
| udp-meter-ingestion | — | — | — | — | — | [0.970](../../../jobs/9038/2026-10-04__14-01-25/udp-meter-ingestion-bash-rhel10-9038) | — | — |
| **Average** | — | — | — | — | — | 0.981 | — | — |
