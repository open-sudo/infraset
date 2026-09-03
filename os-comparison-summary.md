# OS Comparison: Task Execution Results

Results across 50 infrastructure tasks executed on each OS by an LLM agent (Codex / gpt-5.6-sol). Metrics are averages across recorded trials. `Reward` measures the supported outcome. `Hygiene` measures unnecessary mutations, attributable residue, and unrelated regression (1.000 = no problems found). Tasks without a job folder were not yet executed.

## Operating systems

- [AlmaLinux 9](#almalinux-9)
- [Alpine Linux](#alpine-linux)
- [Arch Linux](#arch-linux)
- [CentOS Stream 10](#centos-stream-10)
- [Debian 13](#debian-13)
- [RHEL 7.9](#rhel-79)
- [RHEL 8.8](#rhel-88)
- [RHEL 9.8](#rhel-98)
- [RHEL 10.0](#rhel-100)
- [Ubuntu 16.04](#ubuntu-1604)
- [Ubuntu 24.04](#ubuntu-2404)

## Commands by task and OS

Successful/failed executor commands per task per OS. `0/0` means the audit was captured but no managed-node commands were issued.

| Task | AlmaLinux 9 | Alpine | Arch | CentOS S10 | Debian 13 | RHEL 7.9 | RHEL 8.8 | RHEL 9.8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| account-resource-limits | 10/1 | 21/6 | 13/4 | 8/3 | 14/2 | 10/5 | 10/3 | 0/0 |
| admin-account | 7/2 | 10/8 | 17/2 | 9/2 | 13/2 | 15/2 | 14/2 | 0/0 |
| application-log-rotation | 13/2 | 12/6 | 21/1 | 11/2 | 13/2 | 0/0 | 17/1 | 0/0 |
| audit-sensitive-file | 21/6 | 26/7 | 21/3 | 19/4 | 14/5 | 0/0 | 20/4 | 0/0 |
| boot-service | 8/2 | 6/11 | 9/4 | 11/3 | 8/1 | 0/0 | 8/2 | 0/0 |
| caching-dns-resolver | 14/1 | 15/6 | 10/3 | 14/3 | 11/2 | 25/0 | 36/1 | 0/0 |
| custom-ca-trust | 8/1 | 7/4 | 12/4 | 8/2 | 9/3 | 11/3 | 13/4 | 0/0 |
| disable-core-dumps | 14/3 | 13/8 | 16/0 | 26/3 | 32/3 | 26/4 | 39/9 | 0/0 |
| graceful-service-shutdown | 17/2 | 23/6 | 15/3 | 13/2 | 10/3 | 0/0 | 13/1 | 0/0 |
| host-firewall-baseline | 23/2 | 0/0 | 23/6 | 25/3 | 16/3 | 40/2 | 29/1 | 0/0 |
| https-web-service | 12/2 | 12/10 | 13/2 | 13/3 | 18/3 | 15/3 | 12/3 | 0/0 |
| kernel-network-hardening | 8/2 | 9/7 | 10/2 | 11/1 | 12/2 | 18/3 | 15/3 | 0/0 |
| local-log-retention | 9/1 | 15/8 | 11/1 | 15/3 | 13/3 | 20/7 | 22/2 | 0/0 |
| login-banner | 13/2 | 12/9 | 22/8 | 15/1 | 14/4 | 14/1 | 11/1 | 0/0 |
| login-lockout | 24/1 | 41/8 | 22/1 | 36/2 | 34/2 | 23/1 | 28/2 | 0/0 |
| loopback-only-service | 12/2 | 10/3 | 10/1 | 15/1 | 11/2 | 12/3 | 12/3 | 0/0 |
| mariadb-local-service | 13/1 | 16/11 | 22/3 | 8/2 | 13/2 | 23/2 | 14/2 | 0/0 |
| password-aging | 8/2 | 8/7 | 10/3 | 9/1 | 13/1 | 9/3 | 8/3 | 0/0 |
| persistent-bind-mount | 11/1 | 8/4 | 14/3 | 9/2 | 12/2 | 8/3 | 11/2 | 0/0 |
| persistent-dns-settings | 10/2 | 13/7 | 14/4 | 8/2 | 0/0 | 10/7 | 10/1 | 0/0 |
| redis-persistent-service | 23/4 | 15/12 | 25/5 | 26/2 | 19/3 | 27/1 | 28/3 | 0/0 |
| repair-application-permissions | 14/1 | 14/7 | 12/3 | 18/2 | 11/2 | 0/0 | 13/1 | 0/0 |
| restore-latest-backup | 10/2 | 10/3 | 11/3 | 7/3 | 14/3 | 0/0 | 11/3 | 0/0 |
| restricted-sudo | 15/2 | 14/9 | 12/3 | 13/3 | 14/3 | 13/8 | 15/1 | 0/0 |
| reverse-proxy | 22/2 | 15/11 | 11/4 | 24/4 | 17/3 | 14/3 | 17/2 | 0/0 |
| scheduled-backup | 18/2 | 10/10 | 15/3 | 13/2 | 12/3 | 0/0 | 15/3 | 0/0 |
| scheduled-maintenance | 11/1 | 12/8 | 17/5 | 30/2 | 14/1 | 0/0 | 13/3 | 0/0 |
| secure-umask | 14/0 | 7/10 | 12/5 | 14/2 | 13/4 | 9/2 | 4/0 | 0/0 |
| security-updates | 32/3 | 15/6 | 15/4 | 26/1 | 17/1 | 0/0 | 5/0 | 0/0 |
| separate-authentication-logs | 15/1 | 13/8 | 18/5 | 20/5 | 17/3 | 15/4 | 0/0 | 0/0 |
| service-account | 7/1 | 9/7 | 8/2 | 11/1 | 9/2 | 10/5 | 0/0 | 0/0 |
| service-dependency | 13/0 | 29/5 | 11/2 | 25/2 | 16/2 | 0/0 | 0/0 | 0/0 |
| service-resource-limits | 15/3 | 16/9 | 1/1 | 18/3 | 0/0 | 0/0 | 0/0 | 0/0 |
| service-restart-on-failure | 21/1 | 16/10 | 13/2 | 15/3 | 12/3 | 0/0 | 0/0 | 0/0 |
| setgid-workspace | 11/2 | 9/4 | 9/3 | 8/1 | 11/3 | 8/5 | 0/0 | 0/0 |
| sftp-only-account | 15/2 | 14/10 | 19/6 | 20/5 | 18/4 | 25/5 | 0/0 | 0/0 |
| shared-directory-acl | 9/2 | 14/9 | 15/4 | 11/0 | 17/1 | 15/6 | 0/0 | 0/0 |
| shared-group-directory | 11/1 | 9/5 | 10/3 | 16/1 | 6/3 | 0/0 | 0/0 | 0/0 |
| ssh-group-access | 14/1 | 17/9 | 16/5 | 11/2 | 14/3 | 7/3 | 0/0 | 0/0 |
| ssh-key-only | 13/0 | 16/11 | 14/2 | 11/2 | 5/0 | 0/0 | 0/0 | 0/0 |
| ssh-rate-limiting | 28/4 | 0/0 | 28/3 | 18/1 | 25/3 | 23/12 | 0/0 | 0/0 |
| static-web-service | 12/2 | 11/9 | 7/1 | 13/3 | 8/2 | 9/3 | 0/0 | 0/0 |
| sticky-drop-directory | 0/0 | 9/8 | 10/2 | 0/0 | 12/2 | 9/0 | 0/0 | 0/0 |
| swap-file | 11/1 | 11/7 | 7/2 | 12/8 | 11/4 | 11/1 | 0/0 | 0/0 |
| system-hostname | 9/0 | 6/10 | 12/5 | 9/2 | 10/2 | 7/6 | 0/0 | 0/0 |
| system-locale | 10/1 | 18/10 | 13/3 | 15/2 | 12/2 | 24/3 | 0/0 | 0/0 |
| system-timezone | 7/1 | 8/9 | 7/2 | 7/1 | 8/4 | 6/3 | 0/0 | 0/0 |
| temporary-file-cleanup | 11/1 | 12/10 | 20/4 | 13/1 | 15/5 | 0/0 | 0/0 | 0/0 |
| time-synchronization | 15/0 | 7/7 | 12/7 | 12/1 | 18/3 | 8/5 | 0/0 | 0/0 |
| unprivileged-service | 11/0 | 12/5 | 12/3 | 13/1 | 10/2 | 0/0 | 0/0 | 0/0 |

## AlmaLinux 9

*50/50 tasks executed.*

| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/account-resource-limits-almalinux9/2026-09-02__18-26-38) | 10/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.81s | 1m 35s |
| [admin-account](https://github.com/open-sudo/infraset/tree/main/jobs/admin-account-almalinux9/2026-09-02__18-26-38) | 7/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.78s | 2m 13s |
| [application-log-rotation](https://github.com/open-sudo/infraset/tree/main/jobs/application-log-rotation-almalinux9/2026-09-02__18-26-38) | 13/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.94s | 3m 10s |
| [audit-sensitive-file](https://github.com/open-sudo/infraset/tree/main/jobs/audit-sensitive-file-almalinux9/2026-09-02__18-26-38) | 21/6 | 1.000 | 1.000 | 1.000 | 1.000 | 0.90s | 4m 28s |
| [boot-service](https://github.com/open-sudo/infraset/tree/main/jobs/boot-service-almalinux9/2026-09-02__18-26-38) | 8/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.94s | 1m 24s |
| [caching-dns-resolver](https://github.com/open-sudo/infraset/tree/main/jobs/caching-dns-resolver-almalinux9/2026-09-02__18-26-38) | 14/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.89s | 2m 54s |
| [custom-ca-trust](https://github.com/open-sudo/infraset/tree/main/jobs/custom-ca-trust-almalinux9/2026-09-02__18-26-38) | 8/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.76s | 1m 38s |
| [disable-core-dumps](https://github.com/open-sudo/infraset/tree/main/jobs/disable-core-dumps-almalinux9/2026-09-02__18-26-38) | 14/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.73s | 4m 39s |
| [graceful-service-shutdown](https://github.com/open-sudo/infraset/tree/main/jobs/graceful-service-shutdown-almalinux9/2026-09-02__18-26-38) | 17/2 | 1.000 | 1.000 | 1.000 | 0.970 | 0.85s | 3m 13s |
| [host-firewall-baseline](https://github.com/open-sudo/infraset/tree/main/jobs/host-firewall-baseline-almalinux9/2026-09-02__18-26-38) | 23/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.85s | 2m 46s |
| [https-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/https-web-service-almalinux9/2026-09-02__18-26-38) | 12/2 | 1.000 | 1.000 | 1.000 | 0.920 | 0.78s | 2m 22s |
| [kernel-network-hardening](https://github.com/open-sudo/infraset/tree/main/jobs/kernel-network-hardening-almalinux9/2026-09-02__18-26-38) | 8/2 | 0.750 | 1.000 | 0.750 | 1.000 | 0.73s | 2m 14s |
| [local-log-retention](https://github.com/open-sudo/infraset/tree/main/jobs/local-log-retention-almalinux9/2026-09-02__18-26-38) | 9/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.79s | 2m 12s |
| [login-banner](https://github.com/open-sudo/infraset/tree/main/jobs/login-banner-almalinux9/2026-09-02__18-26-38) | 13/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.76s | 2m 09s |
| [login-lockout](https://github.com/open-sudo/infraset/tree/main/jobs/login-lockout-almalinux9/2026-09-02__18-26-38) | 24/1 | 1.000 | 1.000 | 1.000 | 0.990 | 0.76s | 10m 50s |
| [loopback-only-service](https://github.com/open-sudo/infraset/tree/main/jobs/loopback-only-service-almalinux9/2026-09-02__18-26-38) | 12/2 | 1.000 | 1.000 | 1.000 | 0.970 | 0.76s | 1m 52s |
| [mariadb-local-service](https://github.com/open-sudo/infraset/tree/main/jobs/mariadb-local-service-almalinux9/2026-09-02__18-26-38) | 13/1 | 1.000 | 1.000 | 1.000 | 0.900 | 0.69s | 3m 00s |
| [password-aging](https://github.com/open-sudo/infraset/tree/main/jobs/password-aging-almalinux9/2026-09-02__18-26-38) | 8/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.73s | 2m 01s |
| [persistent-bind-mount](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-bind-mount-almalinux9/2026-09-02__18-26-38) | 11/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.70s | 1m 38s |
| [persistent-dns-settings](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-dns-settings-almalinux9/2026-09-02__18-26-38) | 10/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.87s | 1m 34s |
| [redis-persistent-service](https://github.com/open-sudo/infraset/tree/main/jobs/redis-persistent-service-almalinux9/2026-09-02__18-26-38) | 23/4 | 1.000 | 1.000 | 1.000 | 0.780 | 0.70s | 4m 24s |
| [repair-application-permissions](https://github.com/open-sudo/infraset/tree/main/jobs/repair-application-permissions-almalinux9/2026-09-02__18-26-38) | 14/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.74s | 2m 50s |
| [restore-latest-backup](https://github.com/open-sudo/infraset/tree/main/jobs/restore-latest-backup-almalinux9/2026-09-02__18-26-38) | 10/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.73s | 1m 42s |
| [restricted-sudo](https://github.com/open-sudo/infraset/tree/main/jobs/restricted-sudo-almalinux9/2026-09-02__18-26-38) | 15/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.80s | 2m 31s |
| [reverse-proxy](https://github.com/open-sudo/infraset/tree/main/jobs/reverse-proxy-almalinux9/2026-09-02__18-26-38) | 22/2 | 1.000 | 1.000 | 1.000 | 0.880 | 0.71s | 3m 34s |
| [scheduled-backup](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-backup-almalinux9/2026-09-02__18-26-38) | 18/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.72s | 3m 30s |
| [scheduled-maintenance](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-maintenance-almalinux9/2026-09-02__18-26-38) | 11/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.81s | 2m 39s |
| [secure-umask](https://github.com/open-sudo/infraset/tree/main/jobs/secure-umask-almalinux9/2026-09-02__18-26-38) | 14/0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.77s | 3m 22s |
| [security-updates](https://github.com/open-sudo/infraset/tree/main/jobs/security-updates-almalinux9/2026-09-02__18-26-38) | 32/3 | 1.000 | 1.000 | 1.000 | 0.900 | 0.72s | 4m 02s |
| [separate-authentication-logs](https://github.com/open-sudo/infraset/tree/main/jobs/separate-authentication-logs-almalinux9/2026-09-02__18-26-38) | 15/1 | 1.000 | 1.000 | 1.000 | 0.970 | 0.76s | 2m 25s |
| [service-account](https://github.com/open-sudo/infraset/tree/main/jobs/service-account-almalinux9/2026-09-02__18-26-38) | 7/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.73s | 1m 29s |
| [service-dependency](https://github.com/open-sudo/infraset/tree/main/jobs/service-dependency-almalinux9/2026-09-02__18-26-38) | 13/0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.76s | 2m 20s |
| [service-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/service-resource-limits-almalinux9/2026-09-02__18-26-38) | 15/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.80s | 2m 30s |
| [service-restart-on-failure](https://github.com/open-sudo/infraset/tree/main/jobs/service-restart-on-failure-almalinux9/2026-09-02__18-26-38) | 21/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.79s | 2m 28s |
| [setgid-workspace](https://github.com/open-sudo/infraset/tree/main/jobs/setgid-workspace-almalinux9/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.74s | 1m 57s |
| [sftp-only-account](https://github.com/open-sudo/infraset/tree/main/jobs/sftp-only-account-almalinux9/2026-09-02__18-26-38) | 15/2 | 1.000 | 1.000 | 1.000 | 0.960 | 0.81s | 4m 39s |
| [shared-directory-acl](https://github.com/open-sudo/infraset/tree/main/jobs/shared-directory-acl-almalinux9/2026-09-02__18-26-38) | 9/2 | 1.000 | 1.000 | 1.000 | 0.970 | 0.75s | 2m 27s |
| [shared-group-directory](https://github.com/open-sudo/infraset/tree/main/jobs/shared-group-directory-almalinux9/2026-09-02__18-26-38) | 11/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.68s | 2m 16s |
| [ssh-group-access](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-group-access-almalinux9/2026-09-02__18-26-38) | 14/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.71s | 3m 32s |
| [ssh-key-only](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-key-only-almalinux9/2026-09-02__18-26-38) | 13/0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.76s | 2m 48s |
| [ssh-rate-limiting](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-rate-limiting-almalinux9/2026-09-02__18-26-38) | 28/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.78s | 4m 29s |
| [static-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/static-web-service-almalinux9/2026-09-02__18-26-38) | 12/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.79s | 2m 06s |
| [sticky-drop-directory](https://github.com/open-sudo/infraset/tree/main/jobs/sticky-drop-directory-almalinux9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 1.000 | 0.79s | 103m 53s |
| [swap-file](https://github.com/open-sudo/infraset/tree/main/jobs/swap-file-almalinux9/2026-09-02__18-26-38) | 11/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.74s | 1m 25s |
| [system-hostname](https://github.com/open-sudo/infraset/tree/main/jobs/system-hostname-almalinux9/2026-09-02__18-26-38) | 9/0 | 1.000 | 1.000 | 1.000 | 0.980 | 0.76s | 1m 32s |
| [system-locale](https://github.com/open-sudo/infraset/tree/main/jobs/system-locale-almalinux9/2026-09-02__18-26-38) | 10/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.75s | 2m 08s |
| [system-timezone](https://github.com/open-sudo/infraset/tree/main/jobs/system-timezone-almalinux9/2026-09-02__18-26-38) | 7/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.78s | 0m 53s |
| [temporary-file-cleanup](https://github.com/open-sudo/infraset/tree/main/jobs/temporary-file-cleanup-almalinux9/2026-09-02__18-26-38) | 11/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.79s | 2m 33s |
| [time-synchronization](https://github.com/open-sudo/infraset/tree/main/jobs/time-synchronization-almalinux9/2026-09-02__18-26-38) | 15/0 | 1.000 | 1.000 | 1.000 | 0.880 | 0.82s | 3m 17s |
| [unprivileged-service](https://github.com/open-sudo/infraset/tree/main/jobs/unprivileged-service-almalinux9/2026-09-02__18-26-38) | 11/0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.69s | 2m 21s |

## Alpine Linux

*50/50 tasks executed.*

| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/account-resource-limits-alpine/2026-09-02__18-26-38) | 21/6 | 1.000 | 1.000 | 1.000 | 0.970 | 0.64s | 5m 21s |
| [admin-account](https://github.com/open-sudo/infraset/tree/main/jobs/admin-account-alpine/2026-09-02__18-26-38) | 10/8 | 1.000 | 1.000 | 1.000 | 0.960 | 0.57s | 2m 47s |
| [application-log-rotation](https://github.com/open-sudo/infraset/tree/main/jobs/application-log-rotation-alpine/2026-09-02__18-26-38) | 12/6 | 1.000 | 1.000 | 1.000 | 1.000 | 0.60s | 2m 49s |
| [audit-sensitive-file](https://github.com/open-sudo/infraset/tree/main/jobs/audit-sensitive-file-alpine/2026-09-02__18-26-38) | 26/7 | 1.000 | 1.000 | 1.000 | 0.970 | 0.61s | 3m 55s |
| [boot-service](https://github.com/open-sudo/infraset/tree/main/jobs/boot-service-alpine/2026-09-02__18-26-38) | 6/11 | 1.000 | 1.000 | 1.000 | 0.960 | 0.64s | 2m 08s |
| [caching-dns-resolver](https://github.com/open-sudo/infraset/tree/main/jobs/caching-dns-resolver-alpine/2026-09-02__18-26-38) | 15/6 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 3m 18s |
| [custom-ca-trust](https://github.com/open-sudo/infraset/tree/main/jobs/custom-ca-trust-alpine/2026-09-02__18-26-38) | 7/4 | 1.000 | 1.000 | 1.000 | 0.960 | 0.58s | 1m 50s |
| [disable-core-dumps](https://github.com/open-sudo/infraset/tree/main/jobs/disable-core-dumps-alpine/2026-09-02__18-26-38) | 13/8 | 0.750 | 1.000 | 0.750 | 0.950 | 0.61s | 4m 26s |
| [graceful-service-shutdown](https://github.com/open-sudo/infraset/tree/main/jobs/graceful-service-shutdown-alpine/2026-09-02__18-26-38) | 23/6 | 1.000 | 1.000 | 1.000 | 0.940 | 0.60s | 3m 46s |
| [host-firewall-baseline](https://github.com/open-sudo/infraset/tree/main/jobs/host-firewall-baseline-alpine/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 1.000 | 0.63s | 26m 14s |
| [https-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/https-web-service-alpine/2026-09-02__18-26-38) | 12/10 | 1.000 | 1.000 | 1.000 | 0.980 | 0.62s | 2m 54s |
| [kernel-network-hardening](https://github.com/open-sudo/infraset/tree/main/jobs/kernel-network-hardening-alpine/2026-09-02__18-26-38) | 9/7 | 1.000 | 1.000 | 1.000 | 0.950 | 0.60s | 2m 31s |
| [local-log-retention](https://github.com/open-sudo/infraset/tree/main/jobs/local-log-retention-alpine/2026-09-02__18-26-38) | 15/8 | 1.000 | 1.000 | 1.000 | 0.920 | 0.67s | 4m 01s |
| [login-banner](https://github.com/open-sudo/infraset/tree/main/jobs/login-banner-alpine/2026-09-02__18-26-38) | 12/9 | 1.000 | 1.000 | 1.000 | 0.900 | 0.62s | 2m 50s |
| [login-lockout](https://github.com/open-sudo/infraset/tree/main/jobs/login-lockout-alpine/2026-09-02__18-26-38) | 41/8 | 1.000 | 1.000 | 1.000 | 1.000 | 0.55s | 12m 03s |
| [loopback-only-service](https://github.com/open-sudo/infraset/tree/main/jobs/loopback-only-service-alpine/2026-09-02__18-26-38) | 10/3 | 1.000 | 1.000 | 1.000 | 0.960 | 0.62s | 2m 17s |
| [mariadb-local-service](https://github.com/open-sudo/infraset/tree/main/jobs/mariadb-local-service-alpine/2026-09-02__18-26-38) | 16/11 | 1.000 | 1.000 | 1.000 | 0.970 | 0.64s | 3m 37s |
| [password-aging](https://github.com/open-sudo/infraset/tree/main/jobs/password-aging-alpine/2026-09-02__18-26-38) | 8/7 | 1.000 | 1.000 | 1.000 | 0.960 | 0.68s | 2m 22s |
| [persistent-bind-mount](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-bind-mount-alpine/2026-09-02__18-26-38) | 8/4 | 1.000 | 1.000 | 1.000 | 0.970 | 0.64s | 2m 01s |
| [persistent-dns-settings](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-dns-settings-alpine/2026-09-02__18-26-38) | 13/7 | 1.000 | 1.000 | 1.000 | 0.930 | 0.60s | 2m 48s |
| [redis-persistent-service](https://github.com/open-sudo/infraset/tree/main/jobs/redis-persistent-service-alpine/2026-09-02__18-26-38) | 15/12 | 1.000 | 1.000 | 1.000 | 0.970 | 0.57s | 3m 30s |
| [repair-application-permissions](https://github.com/open-sudo/infraset/tree/main/jobs/repair-application-permissions-alpine/2026-09-02__18-26-38) | 14/7 | 1.000 | 1.000 | 1.000 | 1.000 | 0.57s | 2m 50s |
| [restore-latest-backup](https://github.com/open-sudo/infraset/tree/main/jobs/restore-latest-backup-alpine/2026-09-02__18-26-38) | 10/3 | 1.000 | 1.000 | 1.000 | 0.970 | 0.61s | 2m 43s |
| [restricted-sudo](https://github.com/open-sudo/infraset/tree/main/jobs/restricted-sudo-alpine/2026-09-02__18-26-38) | 14/9 | 1.000 | 1.000 | 1.000 | 0.960 | 0.65s | 3m 08s |
| [reverse-proxy](https://github.com/open-sudo/infraset/tree/main/jobs/reverse-proxy-alpine/2026-09-02__18-26-38) | 15/11 | 1.000 | 1.000 | 1.000 | 0.970 | 0.64s | 2m 56s |
| [scheduled-backup](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-backup-alpine/2026-09-02__18-26-38) | 10/10 | 1.000 | 1.000 | 1.000 | 1.000 | 0.59s | 3m 12s |
| [scheduled-maintenance](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-maintenance-alpine/2026-09-02__18-26-38) | 12/8 | 1.000 | 1.000 | 1.000 | 0.950 | 0.60s | 2m 58s |
| [secure-umask](https://github.com/open-sudo/infraset/tree/main/jobs/secure-umask-alpine/2026-09-02__18-26-38) | 7/10 | 1.000 | 1.000 | 1.000 | 0.970 | 0.62s | 2m 09s |
| [security-updates](https://github.com/open-sudo/infraset/tree/main/jobs/security-updates-alpine/2026-09-02__18-26-38) | 15/6 | 1.000 | 1.000 | 1.000 | 0.960 | 0.60s | 2m 36s |
| [separate-authentication-logs](https://github.com/open-sudo/infraset/tree/main/jobs/separate-authentication-logs-alpine/2026-09-02__18-26-38) | 13/8 | 1.000 | 1.000 | 1.000 | 0.980 | 0.59s | 3m 14s |
| [service-account](https://github.com/open-sudo/infraset/tree/main/jobs/service-account-alpine/2026-09-02__18-26-38) | 9/7 | 1.000 | 1.000 | 1.000 | 0.960 | 0.59s | 2m 12s |
| [service-dependency](https://github.com/open-sudo/infraset/tree/main/jobs/service-dependency-alpine/2026-09-02__18-26-38) | 29/5 | 1.000 | 1.000 | 1.000 | 0.900 | 0.67s | 6m 24s |
| [service-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/service-resource-limits-alpine/2026-09-02__18-26-38) | 16/9 | 1.000 | 1.000 | 1.000 | 0.970 | 0.57s | 3m 28s |
| [service-restart-on-failure](https://github.com/open-sudo/infraset/tree/main/jobs/service-restart-on-failure-alpine/2026-09-02__18-26-38) | 16/10 | 1.000 | 1.000 | 1.000 | 0.980 | 0.62s | 3m 15s |
| [setgid-workspace](https://github.com/open-sudo/infraset/tree/main/jobs/setgid-workspace-alpine/2026-09-02__18-26-38) | 9/4 | 1.000 | 1.000 | 1.000 | 0.950 | 0.58s | 2m 22s |
| [sftp-only-account](https://github.com/open-sudo/infraset/tree/main/jobs/sftp-only-account-alpine/2026-09-02__18-26-38) | 14/10 | 1.000 | 1.000 | 1.000 | 0.800 | 0.63s | 4m 00s |
| [shared-directory-acl](https://github.com/open-sudo/infraset/tree/main/jobs/shared-directory-acl-alpine/2026-09-02__18-26-38) | 14/9 | 1.000 | 1.000 | 1.000 | 0.940 | 0.59s | 3m 55s |
| [shared-group-directory](https://github.com/open-sudo/infraset/tree/main/jobs/shared-group-directory-alpine/2026-09-02__18-26-38) | 9/5 | 1.000 | 1.000 | 1.000 | 0.950 | 0.57s | 2m 33s |
| [ssh-group-access](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-group-access-alpine/2026-09-02__18-26-38) | 17/9 | 1.000 | 1.000 | 1.000 | 1.000 | 0.62s | 3m 59s |
| [ssh-key-only](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-key-only-alpine/2026-09-02__18-26-38) | 16/11 | 1.000 | 1.000 | 1.000 | 0.970 | 0.61s | 4m 18s |
| [ssh-rate-limiting](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-rate-limiting-alpine/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.500 | 0.000 | 1.000 | 0.58s | 27m 53s |
| [static-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/static-web-service-alpine/2026-09-02__18-26-38) | 11/9 | 1.000 | 1.000 | 1.000 | 0.880 | 0.64s | 1m 57s |
| [sticky-drop-directory](https://github.com/open-sudo/infraset/tree/main/jobs/sticky-drop-directory-alpine/2026-09-02__18-26-38) | 9/8 | 1.000 | 1.000 | 1.000 | 0.900 | 0.60s | 2m 06s |
| [swap-file](https://github.com/open-sudo/infraset/tree/main/jobs/swap-file-alpine/2026-09-02__18-26-38) | 11/7 | 1.000 | 1.000 | 1.000 | 0.970 | 0.57s | 1m 54s |
| [system-hostname](https://github.com/open-sudo/infraset/tree/main/jobs/system-hostname-alpine/2026-09-02__18-26-38) | 6/10 | 1.000 | 1.000 | 1.000 | 0.960 | 0.64s | 1m 38s |
| [system-locale](https://github.com/open-sudo/infraset/tree/main/jobs/system-locale-alpine/2026-09-02__18-26-38) | 18/10 | 1.000 | 1.000 | 1.000 | 0.970 | 0.69s | 3m 03s |
| [system-timezone](https://github.com/open-sudo/infraset/tree/main/jobs/system-timezone-alpine/2026-09-02__18-26-38) | 8/9 | 1.000 | 1.000 | 1.000 | 1.000 | 0.57s | 1m 47s |
| [temporary-file-cleanup](https://github.com/open-sudo/infraset/tree/main/jobs/temporary-file-cleanup-alpine/2026-09-02__18-26-38) | 12/10 | 1.000 | 1.000 | 1.000 | 1.000 | 0.56s | 2m 36s |
| [time-synchronization](https://github.com/open-sudo/infraset/tree/main/jobs/time-synchronization-alpine/2026-09-02__18-26-38) | 7/7 | 1.000 | 1.000 | 1.000 | 0.960 | 0.61s | 2m 00s |
| [unprivileged-service](https://github.com/open-sudo/infraset/tree/main/jobs/unprivileged-service-alpine/2026-09-02__18-26-38) | 12/5 | 1.000 | 1.000 | 1.000 | 0.940 | 0.64s | 2m 19s |

## Arch Linux

*50/50 tasks executed.*

| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/account-resource-limits-archlinux/2026-09-02__18-26-38) | 13/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 2m 13s |
| [admin-account](https://github.com/open-sudo/infraset/tree/main/jobs/admin-account-archlinux/2026-09-02__18-26-38) | 17/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.68s | 2m 23s |
| [application-log-rotation](https://github.com/open-sudo/infraset/tree/main/jobs/application-log-rotation-archlinux/2026-09-02__18-26-38) | 21/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.58s | 2m 34s |
| [audit-sensitive-file](https://github.com/open-sudo/infraset/tree/main/jobs/audit-sensitive-file-archlinux/2026-09-02__18-26-38) | 21/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.59s | 3m 09s |
| [boot-service](https://github.com/open-sudo/infraset/tree/main/jobs/boot-service-archlinux/2026-09-02__18-26-38) | 9/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 1m 46s |
| [caching-dns-resolver](https://github.com/open-sudo/infraset/tree/main/jobs/caching-dns-resolver-archlinux/2026-09-02__18-26-38) | 10/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 1m 53s |
| [custom-ca-trust](https://github.com/open-sudo/infraset/tree/main/jobs/custom-ca-trust-archlinux/2026-09-02__18-26-38) | 12/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 2m 32s |
| [disable-core-dumps](https://github.com/open-sudo/infraset/tree/main/jobs/disable-core-dumps-archlinux/2026-09-02__18-26-38) | 16/0 | 1.000 | 1.000 | 1.000 | 0.980 | 0.66s | 3m 44s |
| [graceful-service-shutdown](https://github.com/open-sudo/infraset/tree/main/jobs/graceful-service-shutdown-archlinux/2026-09-02__18-26-38) | 15/3 | 1.000 | 1.000 | 1.000 | 0.970 | 0.65s | 2m 36s |
| [host-firewall-baseline](https://github.com/open-sudo/infraset/tree/main/jobs/host-firewall-baseline-archlinux/2026-09-02__18-26-38) | 23/6 | 1.000 | 1.000 | 1.000 | 1.000 | 0.59s | 3m 31s |
| [https-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/https-web-service-archlinux/2026-09-02__18-26-38) | 13/2 | 1.000 | 1.000 | 1.000 | 0.980 | 0.61s | 2m 20s |
| [kernel-network-hardening](https://github.com/open-sudo/infraset/tree/main/jobs/kernel-network-hardening-archlinux/2026-09-02__18-26-38) | 10/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.71s | 2m 29s |
| [local-log-retention](https://github.com/open-sudo/infraset/tree/main/jobs/local-log-retention-archlinux/2026-09-02__18-26-38) | 11/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.65s | 2m 13s |
| [login-banner](https://github.com/open-sudo/infraset/tree/main/jobs/login-banner-archlinux/2026-09-02__18-26-38) | 22/8 | 1.000 | 1.000 | 1.000 | 1.000 | 0.68s | 2m 32s |
| [login-lockout](https://github.com/open-sudo/infraset/tree/main/jobs/login-lockout-archlinux/2026-09-02__18-26-38) | 22/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.61s | 11m 15s |
| [loopback-only-service](https://github.com/open-sudo/infraset/tree/main/jobs/loopback-only-service-archlinux/2026-09-02__18-26-38) | 10/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 1m 45s |
| [mariadb-local-service](https://github.com/open-sudo/infraset/tree/main/jobs/mariadb-local-service-archlinux/2026-09-02__18-26-38) | 22/3 | 1.000 | 1.000 | 1.000 | 0.740 | 0.59s | 3m 32s |
| [password-aging](https://github.com/open-sudo/infraset/tree/main/jobs/password-aging-archlinux/2026-09-02__18-26-38) | 10/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.69s | 1m 46s |
| [persistent-bind-mount](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-bind-mount-archlinux/2026-09-02__18-26-38) | 14/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 2m 11s |
| [persistent-dns-settings](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-dns-settings-archlinux/2026-09-02__18-26-38) | 14/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.65s | 2m 19s |
| [redis-persistent-service](https://github.com/open-sudo/infraset/tree/main/jobs/redis-persistent-service-archlinux/2026-09-02__18-26-38) | 25/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 4m 48s |
| [repair-application-permissions](https://github.com/open-sudo/infraset/tree/main/jobs/repair-application-permissions-archlinux/2026-09-02__18-26-38) | 12/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.60s | 2m 06s |
| [restore-latest-backup](https://github.com/open-sudo/infraset/tree/main/jobs/restore-latest-backup-archlinux/2026-09-02__18-26-38) | 11/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.61s | 2m 06s |
| [restricted-sudo](https://github.com/open-sudo/infraset/tree/main/jobs/restricted-sudo-archlinux/2026-09-02__18-26-38) | 12/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.66s | 2m 29s |
| [reverse-proxy](https://github.com/open-sudo/infraset/tree/main/jobs/reverse-proxy-archlinux/2026-09-02__18-26-38) | 11/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.61s | 2m 17s |
| [scheduled-backup](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-backup-archlinux/2026-09-02__18-26-38) | 15/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.65s | 2m 58s |
| [scheduled-maintenance](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-maintenance-archlinux/2026-09-02__18-26-38) | 17/5 | 1.000 | 1.000 | 1.000 | 0.950 | 0.63s | 3m 14s |
| [secure-umask](https://github.com/open-sudo/infraset/tree/main/jobs/secure-umask-archlinux/2026-09-02__18-26-38) | 12/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.69s | 1m 48s |
| [security-updates](https://github.com/open-sudo/infraset/tree/main/jobs/security-updates-archlinux/2026-09-02__18-26-38) | 15/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 2m 37s |
| [separate-authentication-logs](https://github.com/open-sudo/infraset/tree/main/jobs/separate-authentication-logs-archlinux/2026-09-02__18-26-38) | 18/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 3m 02s |
| [service-account](https://github.com/open-sudo/infraset/tree/main/jobs/service-account-archlinux/2026-09-02__18-26-38) | 8/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 1m 20s |
| [service-dependency](https://github.com/open-sudo/infraset/tree/main/jobs/service-dependency-archlinux/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.61s | 2m 27s |
| [service-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/service-resource-limits-archlinux/2026-09-02__18-26-38) | 1/1 | 0.000 | 1.000 | 0.000 | 1.000 | 0.62s | 20m 20s |
| [service-restart-on-failure](https://github.com/open-sudo/infraset/tree/main/jobs/service-restart-on-failure-archlinux/2026-09-02__18-26-38) | 13/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 2m 22s |
| [setgid-workspace](https://github.com/open-sudo/infraset/tree/main/jobs/setgid-workspace-archlinux/2026-09-02__18-26-38) | 9/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.60s | 1m 59s |
| [sftp-only-account](https://github.com/open-sudo/infraset/tree/main/jobs/sftp-only-account-archlinux/2026-09-02__18-26-38) | 19/6 | 1.000 | 1.000 | 1.000 | 0.920 | 0.76s | 3m 53s |
| [shared-directory-acl](https://github.com/open-sudo/infraset/tree/main/jobs/shared-directory-acl-archlinux/2026-09-02__18-26-38) | 15/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.65s | 3m 11s |
| [shared-group-directory](https://github.com/open-sudo/infraset/tree/main/jobs/shared-group-directory-archlinux/2026-09-02__18-26-38) | 10/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.71s | 2m 11s |
| [ssh-group-access](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-group-access-archlinux/2026-09-02__18-26-38) | 16/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.62s | 3m 35s |
| [ssh-key-only](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-key-only-archlinux/2026-09-02__18-26-38) | 14/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 2m 58s |
| [ssh-rate-limiting](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-rate-limiting-archlinux/2026-09-02__18-26-38) | 28/3 | 1.000 | 1.000 | 1.000 | 0.980 | 0.72s | 5m 08s |
| [static-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/static-web-service-archlinux/2026-09-02__18-26-38) | 7/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.56s | 1m 45s |
| [sticky-drop-directory](https://github.com/open-sudo/infraset/tree/main/jobs/sticky-drop-directory-archlinux/2026-09-02__18-26-38) | 10/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.59s | 1m 53s |
| [swap-file](https://github.com/open-sudo/infraset/tree/main/jobs/swap-file-archlinux/2026-09-02__18-26-38) | 7/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.59s | 1m 27s |
| [system-hostname](https://github.com/open-sudo/infraset/tree/main/jobs/system-hostname-archlinux/2026-09-02__18-26-38) | 12/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 1m 26s |
| [system-locale](https://github.com/open-sudo/infraset/tree/main/jobs/system-locale-archlinux/2026-09-02__18-26-38) | 13/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.62s | 1m 48s |
| [system-timezone](https://github.com/open-sudo/infraset/tree/main/jobs/system-timezone-archlinux/2026-09-02__18-26-38) | 7/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.65s | 1m 06s |
| [temporary-file-cleanup](https://github.com/open-sudo/infraset/tree/main/jobs/temporary-file-cleanup-archlinux/2026-09-02__18-26-38) | 20/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 3m 06s |
| [time-synchronization](https://github.com/open-sudo/infraset/tree/main/jobs/time-synchronization-archlinux/2026-09-02__18-26-38) | 12/7 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 3m 23s |
| [unprivileged-service](https://github.com/open-sudo/infraset/tree/main/jobs/unprivileged-service-archlinux/2026-09-02__18-26-38) | 12/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.59s | 2m 00s |

## CentOS Stream 10

*50/50 tasks executed.*

| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/account-resource-limits-centos-stream10/2026-09-02__18-26-38) | 8/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.86s | 1m 30s |
| [admin-account](https://github.com/open-sudo/infraset/tree/main/jobs/admin-account-centos-stream10/2026-09-02__18-26-38) | 9/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.88s | 2m 06s |
| [application-log-rotation](https://github.com/open-sudo/infraset/tree/main/jobs/application-log-rotation-centos-stream10/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 0.960 | 0.87s | 3m 02s |
| [audit-sensitive-file](https://github.com/open-sudo/infraset/tree/main/jobs/audit-sensitive-file-centos-stream10/2026-09-02__18-26-38) | 19/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.83s | 3m 29s |
| [boot-service](https://github.com/open-sudo/infraset/tree/main/jobs/boot-service-centos-stream10/2026-09-02__18-26-38) | 11/3 | 1.000 | 1.000 | 1.000 | 0.980 | 0.85s | 1m 56s |
| [caching-dns-resolver](https://github.com/open-sudo/infraset/tree/main/jobs/caching-dns-resolver-centos-stream10/2026-09-02__18-26-38) | 14/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.80s | 2m 42s |
| [custom-ca-trust](https://github.com/open-sudo/infraset/tree/main/jobs/custom-ca-trust-centos-stream10/2026-09-02__18-26-38) | 8/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.95s | 1m 35s |
| [disable-core-dumps](https://github.com/open-sudo/infraset/tree/main/jobs/disable-core-dumps-centos-stream10/2026-09-02__18-26-38) | 26/3 | 1.000 | 1.000 | 1.000 | 0.960 | 0.94s | 4m 30s |
| [graceful-service-shutdown](https://github.com/open-sudo/infraset/tree/main/jobs/graceful-service-shutdown-centos-stream10/2026-09-02__18-26-38) | 13/2 | 1.000 | 1.000 | 1.000 | 0.970 | 1.05s | 2m 39s |
| [host-firewall-baseline](https://github.com/open-sudo/infraset/tree/main/jobs/host-firewall-baseline-centos-stream10/2026-09-02__18-26-38) | 25/3 | 1.000 | 1.000 | 1.000 | 1.000 | 1.05s | 5m 04s |
| [https-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/https-web-service-centos-stream10/2026-09-02__18-26-38) | 13/3 | 1.000 | 1.000 | 1.000 | 0.940 | 0.91s | 2m 49s |
| [kernel-network-hardening](https://github.com/open-sudo/infraset/tree/main/jobs/kernel-network-hardening-centos-stream10/2026-09-02__18-26-38) | 11/1 | 1.000 | 1.000 | 1.000 | 1.000 | 1.02s | 2m 18s |
| [local-log-retention](https://github.com/open-sudo/infraset/tree/main/jobs/local-log-retention-centos-stream10/2026-09-02__18-26-38) | 15/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.92s | 3m 33s |
| [login-banner](https://github.com/open-sudo/infraset/tree/main/jobs/login-banner-centos-stream10/2026-09-02__18-26-38) | 15/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.84s | 2m 02s |
| [login-lockout](https://github.com/open-sudo/infraset/tree/main/jobs/login-lockout-centos-stream10/2026-09-02__18-26-38) | 36/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.96s | 9m 00s |
| [loopback-only-service](https://github.com/open-sudo/infraset/tree/main/jobs/loopback-only-service-centos-stream10/2026-09-02__18-26-38) | 15/1 | 1.000 | 1.000 | 1.000 | 1.000 | 1.07s | 2m 39s |
| [mariadb-local-service](https://github.com/open-sudo/infraset/tree/main/jobs/mariadb-local-service-centos-stream10/2026-09-02__18-26-38) | 8/2 | 1.000 | 1.000 | 1.000 | 0.900 | 0.91s | 2m 48s |
| [password-aging](https://github.com/open-sudo/infraset/tree/main/jobs/password-aging-centos-stream10/2026-09-02__18-26-38) | 9/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.87s | 1m 29s |
| [persistent-bind-mount](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-bind-mount-centos-stream10/2026-09-02__18-26-38) | 9/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.91s | 1m 50s |
| [persistent-dns-settings](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-dns-settings-centos-stream10/2026-09-02__18-26-38) | 8/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.98s | 1m 21s |
| [redis-persistent-service](https://github.com/open-sudo/infraset/tree/main/jobs/redis-persistent-service-centos-stream10/2026-09-02__18-26-38) | 26/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.96s | 4m 32s |
| [repair-application-permissions](https://github.com/open-sudo/infraset/tree/main/jobs/repair-application-permissions-centos-stream10/2026-09-02__18-26-38) | 18/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.87s | 3m 02s |
| [restore-latest-backup](https://github.com/open-sudo/infraset/tree/main/jobs/restore-latest-backup-centos-stream10/2026-09-02__18-26-38) | 7/3 | 1.000 | 1.000 | 1.000 | 1.000 | 1.06s | 1m 41s |
| [restricted-sudo](https://github.com/open-sudo/infraset/tree/main/jobs/restricted-sudo-centos-stream10/2026-09-02__18-26-38) | 13/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.91s | 3m 32s |
| [reverse-proxy](https://github.com/open-sudo/infraset/tree/main/jobs/reverse-proxy-centos-stream10/2026-09-02__18-26-38) | 24/4 | 1.000 | 1.000 | 1.000 | 0.980 | 0.93s | 3m 16s |
| [scheduled-backup](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-backup-centos-stream10/2026-09-02__18-26-38) | 13/2 | 1.000 | 1.000 | 1.000 | 0.970 | 0.90s | 3m 10s |
| [scheduled-maintenance](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-maintenance-centos-stream10/2026-09-02__18-26-38) | 30/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.85s | 3m 11s |
| [secure-umask](https://github.com/open-sudo/infraset/tree/main/jobs/secure-umask-centos-stream10/2026-09-02__18-26-38) | 14/2 | 1.000 | 1.000 | 1.000 | 0.960 | 0.90s | 2m 29s |
| [security-updates](https://github.com/open-sudo/infraset/tree/main/jobs/security-updates-centos-stream10/2026-09-02__18-26-38) | 26/1 | 1.000 | 1.000 | 1.000 | 0.980 | 1.05s | 5m 08s |
| [separate-authentication-logs](https://github.com/open-sudo/infraset/tree/main/jobs/separate-authentication-logs-centos-stream10/2026-09-02__18-26-38) | 20/5 | 1.000 | 1.000 | 1.000 | 0.980 | 1.03s | 3m 13s |
| [service-account](https://github.com/open-sudo/infraset/tree/main/jobs/service-account-centos-stream10/2026-09-02__18-26-38) | 11/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.93s | 2m 05s |
| [service-dependency](https://github.com/open-sudo/infraset/tree/main/jobs/service-dependency-centos-stream10/2026-09-02__18-26-38) | 25/2 | 1.000 | 1.000 | 1.000 | 0.960 | 1.70s | 5m 24s |
| [service-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/service-resource-limits-centos-stream10/2026-09-02__18-26-38) | 18/3 | 1.000 | 1.000 | 1.000 | 0.880 | 0.97s | 4m 29s |
| [service-restart-on-failure](https://github.com/open-sudo/infraset/tree/main/jobs/service-restart-on-failure-centos-stream10/2026-09-02__18-26-38) | 15/3 | 1.000 | 1.000 | 1.000 | 0.970 | 0.85s | 2m 23s |
| [setgid-workspace](https://github.com/open-sudo/infraset/tree/main/jobs/setgid-workspace-centos-stream10/2026-09-02__18-26-38) | 8/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.91s | 1m 29s |
| [sftp-only-account](https://github.com/open-sudo/infraset/tree/main/jobs/sftp-only-account-centos-stream10/2026-09-02__18-26-38) | 20/5 | 1.000 | 1.000 | 1.000 | 0.880 | 1.01s | 4m 19s |
| [shared-directory-acl](https://github.com/open-sudo/infraset/tree/main/jobs/shared-directory-acl-centos-stream10/2026-09-02__18-26-38) | 11/0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.87s | 2m 33s |
| [shared-group-directory](https://github.com/open-sudo/infraset/tree/main/jobs/shared-group-directory-centos-stream10/2026-09-02__18-26-38) | 16/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.94s | 2m 49s |
| [ssh-group-access](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-group-access-centos-stream10/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.84s | 2m 14s |
| [ssh-key-only](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-key-only-centos-stream10/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.91s | 2m 41s |
| [ssh-rate-limiting](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-rate-limiting-centos-stream10/2026-09-02__18-26-38) | 18/1 | 1.000 | 1.000 | 1.000 | 0.980 | 0.86s | 3m 45s |
| [static-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/static-web-service-centos-stream10/2026-09-02__18-26-38) | 13/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.89s | 1m 37s |
| [sticky-drop-directory](https://github.com/open-sudo/infraset/tree/main/jobs/sticky-drop-directory-centos-stream10/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.82s | — |
| [swap-file](https://github.com/open-sudo/infraset/tree/main/jobs/swap-file-centos-stream10/2026-09-02__18-26-38) | 12/8 | 1.000 | 1.000 | 1.000 | 1.000 | 1.08s | 2m 40s |
| [system-hostname](https://github.com/open-sudo/infraset/tree/main/jobs/system-hostname-centos-stream10/2026-09-02__18-26-38) | 9/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.90s | 1m 21s |
| [system-locale](https://github.com/open-sudo/infraset/tree/main/jobs/system-locale-centos-stream10/2026-09-02__18-26-38) | 15/2 | 1.000 | 1.000 | 1.000 | 0.980 | 0.94s | 2m 18s |
| [system-timezone](https://github.com/open-sudo/infraset/tree/main/jobs/system-timezone-centos-stream10/2026-09-02__18-26-38) | 7/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.96s | 1m 16s |
| [temporary-file-cleanup](https://github.com/open-sudo/infraset/tree/main/jobs/temporary-file-cleanup-centos-stream10/2026-09-02__18-26-38) | 13/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.98s | 2m 31s |
| [time-synchronization](https://github.com/open-sudo/infraset/tree/main/jobs/time-synchronization-centos-stream10/2026-09-02__18-26-38) | 12/1 | 1.000 | 1.000 | 1.000 | 0.930 | 0.92s | 1m 55s |
| [unprivileged-service](https://github.com/open-sudo/infraset/tree/main/jobs/unprivileged-service-centos-stream10/2026-09-02__18-26-38) | 13/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.93s | 2m 05s |

## Debian 13

*50/50 tasks executed.*

| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/account-resource-limits-debian13/2026-09-02__18-26-38) | 14/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 2m 39s |
| [admin-account](https://github.com/open-sudo/infraset/tree/main/jobs/admin-account-debian13/2026-09-02__18-26-38) | 13/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.60s | 2m 48s |
| [application-log-rotation](https://github.com/open-sudo/infraset/tree/main/jobs/application-log-rotation-debian13/2026-09-02__18-26-38) | 13/2 | 1.000 | 1.000 | 1.000 | 0.960 | 0.65s | 2m 34s |
| [audit-sensitive-file](https://github.com/open-sudo/infraset/tree/main/jobs/audit-sensitive-file-debian13/2026-09-02__18-26-38) | 14/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.95s | 2m 54s |
| [boot-service](https://github.com/open-sudo/infraset/tree/main/jobs/boot-service-debian13/2026-09-02__18-26-38) | 8/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.62s | 1m 52s |
| [caching-dns-resolver](https://github.com/open-sudo/infraset/tree/main/jobs/caching-dns-resolver-debian13/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.65s | 1m 37s |
| [custom-ca-trust](https://github.com/open-sudo/infraset/tree/main/jobs/custom-ca-trust-debian13/2026-09-02__18-26-38) | 9/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.69s | 2m 17s |
| [disable-core-dumps](https://github.com/open-sudo/infraset/tree/main/jobs/disable-core-dumps-debian13/2026-09-02__18-26-38) | 32/3 | 1.000 | 1.000 | 1.000 | 0.720 | 0.64s | 4m 32s |
| [graceful-service-shutdown](https://github.com/open-sudo/infraset/tree/main/jobs/graceful-service-shutdown-debian13/2026-09-02__18-26-38) | 10/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 2m 54s |
| [host-firewall-baseline](https://github.com/open-sudo/infraset/tree/main/jobs/host-firewall-baseline-debian13/2026-09-02__18-26-38) | 16/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 3m 17s |
| [https-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/https-web-service-debian13/2026-09-02__18-26-38) | 18/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 2m 32s |
| [kernel-network-hardening](https://github.com/open-sudo/infraset/tree/main/jobs/kernel-network-hardening-debian13/2026-09-02__18-26-38) | 12/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 2m 10s |
| [local-log-retention](https://github.com/open-sudo/infraset/tree/main/jobs/local-log-retention-debian13/2026-09-02__18-26-38) | 13/3 | 1.000 | 1.000 | 1.000 | 0.650 | 0.68s | 2m 43s |
| [login-banner](https://github.com/open-sudo/infraset/tree/main/jobs/login-banner-debian13/2026-09-02__18-26-38) | 14/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.73s | 2m 59s |
| [login-lockout](https://github.com/open-sudo/infraset/tree/main/jobs/login-lockout-debian13/2026-09-02__18-26-38) | 34/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.60s | 10m 43s |
| [loopback-only-service](https://github.com/open-sudo/infraset/tree/main/jobs/loopback-only-service-debian13/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.85s | 2m 00s |
| [mariadb-local-service](https://github.com/open-sudo/infraset/tree/main/jobs/mariadb-local-service-debian13/2026-09-02__18-26-38) | 13/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.66s | 2m 43s |
| [password-aging](https://github.com/open-sudo/infraset/tree/main/jobs/password-aging-debian13/2026-09-02__18-26-38) | 13/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.70s | 2m 12s |
| [persistent-bind-mount](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-bind-mount-debian13/2026-09-02__18-26-38) | 12/2 | 1.000 | 1.000 | 1.000 | 0.970 | 0.68s | 18m 45s |
| [persistent-dns-settings](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-dns-settings-debian13/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 1.000 | 0.73s | 51m 56s |
| [redis-persistent-service](https://github.com/open-sudo/infraset/tree/main/jobs/redis-persistent-service-debian13/2026-09-02__18-26-38) | 19/3 | 1.000 | 1.000 | 1.000 | 0.820 | 0.66s | 3m 53s |
| [repair-application-permissions](https://github.com/open-sudo/infraset/tree/main/jobs/repair-application-permissions-debian13/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 2m 19s |
| [restore-latest-backup](https://github.com/open-sudo/infraset/tree/main/jobs/restore-latest-backup-debian13/2026-09-02__18-26-38) | 14/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.70s | 2m 33s |
| [restricted-sudo](https://github.com/open-sudo/infraset/tree/main/jobs/restricted-sudo-debian13/2026-09-02__18-26-38) | 14/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 2m 37s |
| [reverse-proxy](https://github.com/open-sudo/infraset/tree/main/jobs/reverse-proxy-debian13/2026-09-02__18-26-38) | 17/3 | 1.000 | 1.000 | 1.000 | 0.760 | 0.63s | 2m 26s |
| [scheduled-backup](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-backup-debian13/2026-09-02__18-26-38) | 12/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 3m 16s |
| [scheduled-maintenance](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-maintenance-debian13/2026-09-02__18-26-38) | 14/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.60s | 2m 45s |
| [secure-umask](https://github.com/open-sudo/infraset/tree/main/jobs/secure-umask-debian13/2026-09-02__18-26-38) | 13/4 | 1.000 | 1.000 | 1.000 | 0.980 | 0.66s | 3m 45s |
| [security-updates](https://github.com/open-sudo/infraset/tree/main/jobs/security-updates-debian13/2026-09-02__18-26-38) | 17/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.73s | 4m 13s |
| [separate-authentication-logs](https://github.com/open-sudo/infraset/tree/main/jobs/separate-authentication-logs-debian13/2026-09-02__18-26-38) | 17/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.85s | 2m 49s |
| [service-account](https://github.com/open-sudo/infraset/tree/main/jobs/service-account-debian13/2026-09-02__18-26-38) | 9/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 1m 36s |
| [service-dependency](https://github.com/open-sudo/infraset/tree/main/jobs/service-dependency-debian13/2026-09-02__18-26-38) | 16/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.69s | 3m 13s |
| [service-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/service-resource-limits-debian13/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 1.000 | 0.63s | 24m 40s |
| [service-restart-on-failure](https://github.com/open-sudo/infraset/tree/main/jobs/service-restart-on-failure-debian13/2026-09-02__18-26-38) | 12/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.78s | 2m 09s |
| [setgid-workspace](https://github.com/open-sudo/infraset/tree/main/jobs/setgid-workspace-debian13/2026-09-02__18-26-38) | 11/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.72s | 2m 02s |
| [sftp-only-account](https://github.com/open-sudo/infraset/tree/main/jobs/sftp-only-account-debian13/2026-09-02__18-26-38) | 18/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.62s | 3m 40s |
| [shared-directory-acl](https://github.com/open-sudo/infraset/tree/main/jobs/shared-directory-acl-debian13/2026-09-02__18-26-38) | 17/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.68s | 2m 54s |
| [shared-group-directory](https://github.com/open-sudo/infraset/tree/main/jobs/shared-group-directory-debian13/2026-09-02__18-26-38) | 6/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 2m 07s |
| [ssh-group-access](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-group-access-debian13/2026-09-02__18-26-38) | 14/3 | 1.000 | 1.000 | 1.000 | 0.840 | 0.72s | 3m 48s |
| [ssh-key-only](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-key-only-debian13/2026-09-02__18-26-38) | 5/0 | 0.000 | 0.500 | 0.000 | 0.620 | 0.67s | 20m 31s |
| [ssh-rate-limiting](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-rate-limiting-debian13/2026-09-02__18-26-38) | 25/3 | 1.000 | 1.000 | 1.000 | 0.980 | 0.74s | 5m 33s |
| [static-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/static-web-service-debian13/2026-09-02__18-26-38) | 8/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 1m 28s |
| [sticky-drop-directory](https://github.com/open-sudo/infraset/tree/main/jobs/sticky-drop-directory-debian13/2026-09-02__18-26-38) | 12/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 1m 56s |
| [swap-file](https://github.com/open-sudo/infraset/tree/main/jobs/swap-file-debian13/2026-09-02__18-26-38) | 11/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.66s | 2m 08s |
| [system-hostname](https://github.com/open-sudo/infraset/tree/main/jobs/system-hostname-debian13/2026-09-02__18-26-38) | 10/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.65s | 1m 54s |
| [system-locale](https://github.com/open-sudo/infraset/tree/main/jobs/system-locale-debian13/2026-09-02__18-26-38) | 12/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 2m 38s |
| [system-timezone](https://github.com/open-sudo/infraset/tree/main/jobs/system-timezone-debian13/2026-09-02__18-26-38) | 8/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 2m 05s |
| [temporary-file-cleanup](https://github.com/open-sudo/infraset/tree/main/jobs/temporary-file-cleanup-debian13/2026-09-02__18-26-38) | 15/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 2m 46s |
| [time-synchronization](https://github.com/open-sudo/infraset/tree/main/jobs/time-synchronization-debian13/2026-09-02__18-26-38) | 18/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.62s | 2m 31s |
| [unprivileged-service](https://github.com/open-sudo/infraset/tree/main/jobs/unprivileged-service-debian13/2026-09-02__18-26-38) | 10/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 2m 09s |

## RHEL 7.9

*50/50 tasks executed.*

| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/account-resource-limits-rhel7/2026-09-02__18-26-38) | 10/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 2m 59s |
| [admin-account](https://github.com/open-sudo/infraset/tree/main/jobs/admin-account-rhel7/2026-09-02__18-26-38) | 15/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.59s | 3m 06s |
| [application-log-rotation](https://github.com/open-sudo/infraset/tree/main/jobs/application-log-rotation-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.86s | — |
| [audit-sensitive-file](https://github.com/open-sudo/infraset/tree/main/jobs/audit-sensitive-file-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.64s | — |
| [boot-service](https://github.com/open-sudo/infraset/tree/main/jobs/boot-service-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.66s | — |
| [caching-dns-resolver](https://github.com/open-sudo/infraset/tree/main/jobs/caching-dns-resolver-rhel7/2026-09-02__18-26-38) | 25/0 | 1.000 | 1.000 | 1.000 | 0.950 | 0.66s | 7m 58s |
| [custom-ca-trust](https://github.com/open-sudo/infraset/tree/main/jobs/custom-ca-trust-rhel7/2026-09-02__18-26-38) | 11/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.79s | 2m 58s |
| [disable-core-dumps](https://github.com/open-sudo/infraset/tree/main/jobs/disable-core-dumps-rhel7/2026-09-02__18-26-38) | 26/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.97s | 5m 11s |
| [graceful-service-shutdown](https://github.com/open-sudo/infraset/tree/main/jobs/graceful-service-shutdown-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.72s | — |
| [host-firewall-baseline](https://github.com/open-sudo/infraset/tree/main/jobs/host-firewall-baseline-rhel7/2026-09-02__18-26-38) | 40/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.74s | 8m 05s |
| [https-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/https-web-service-rhel7/2026-09-02__18-26-38) | 15/3 | 1.000 | 1.000 | 1.000 | 1.000 | 1.00s | 4m 12s |
| [kernel-network-hardening](https://github.com/open-sudo/infraset/tree/main/jobs/kernel-network-hardening-rhel7/2026-09-02__18-26-38) | 18/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.73s | 4m 11s |
| [local-log-retention](https://github.com/open-sudo/infraset/tree/main/jobs/local-log-retention-rhel7/2026-09-02__18-26-38) | 20/7 | 1.000 | 1.000 | 1.000 | 0.950 | 0.81s | 6m 38s |
| [login-banner](https://github.com/open-sudo/infraset/tree/main/jobs/login-banner-rhel7/2026-09-02__18-26-38) | 14/1 | 1.000 | 1.000 | 1.000 | 0.950 | 0.94s | 5m 13s |
| [login-lockout](https://github.com/open-sudo/infraset/tree/main/jobs/login-lockout-rhel7/2026-09-02__18-26-38) | 23/1 | 0.750 | 1.000 | 0.750 | 0.980 | 0.68s | 8m 33s |
| [loopback-only-service](https://github.com/open-sudo/infraset/tree/main/jobs/loopback-only-service-rhel7/2026-09-02__18-26-38) | 12/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.73s | 3m 23s |
| [mariadb-local-service](https://github.com/open-sudo/infraset/tree/main/jobs/mariadb-local-service-rhel7/2026-09-02__18-26-38) | 23/2 | 1.000 | 1.000 | 1.000 | 0.840 | 0.94s | 5m 23s |
| [password-aging](https://github.com/open-sudo/infraset/tree/main/jobs/password-aging-rhel7/2026-09-02__18-26-38) | 9/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.98s | 2m 55s |
| [persistent-bind-mount](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-bind-mount-rhel7/2026-09-02__18-26-38) | 8/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 2m 55s |
| [persistent-dns-settings](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-dns-settings-rhel7/2026-09-02__18-26-38) | 10/7 | 1.000 | 1.000 | 1.000 | 1.000 | 0.97s | 3m 27s |
| [redis-persistent-service](https://github.com/open-sudo/infraset/tree/main/jobs/redis-persistent-service-rhel7/2026-09-02__18-26-38) | 27/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.76s | 7m 16s |
| [repair-application-permissions](https://github.com/open-sudo/infraset/tree/main/jobs/repair-application-permissions-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.99s | — |
| [restore-latest-backup](https://github.com/open-sudo/infraset/tree/main/jobs/restore-latest-backup-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.61s | — |
| [restricted-sudo](https://github.com/open-sudo/infraset/tree/main/jobs/restricted-sudo-rhel7/2026-09-02__18-26-38) | 13/8 | 1.000 | 1.000 | 1.000 | 1.000 | 0.70s | 4m 43s |
| [reverse-proxy](https://github.com/open-sudo/infraset/tree/main/jobs/reverse-proxy-rhel7/2026-09-02__18-26-38) | 14/3 | 1.000 | 1.000 | 1.000 | 0.900 | 1.09s | 3m 55s |
| [scheduled-backup](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-backup-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.70s | — |
| [scheduled-maintenance](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-maintenance-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.79s | — |
| [secure-umask](https://github.com/open-sudo/infraset/tree/main/jobs/secure-umask-rhel7/2026-09-02__18-26-38) | 9/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.94s | 3m 48s |
| [security-updates](https://github.com/open-sudo/infraset/tree/main/jobs/security-updates-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.92s | — |
| [separate-authentication-logs](https://github.com/open-sudo/infraset/tree/main/jobs/separate-authentication-logs-rhel7/2026-09-02__18-26-38) | 15/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.90s | 3m 23s |
| [service-account](https://github.com/open-sudo/infraset/tree/main/jobs/service-account-rhel7/2026-09-02__18-26-38) | 10/5 | 1.000 | 1.000 | 1.000 | 1.000 | 1.17s | 3m 12s |
| [service-dependency](https://github.com/open-sudo/infraset/tree/main/jobs/service-dependency-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.79s | — |
| [service-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/service-resource-limits-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.71s | — |
| [service-restart-on-failure](https://github.com/open-sudo/infraset/tree/main/jobs/service-restart-on-failure-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.84s | — |
| [setgid-workspace](https://github.com/open-sudo/infraset/tree/main/jobs/setgid-workspace-rhel7/2026-09-02__18-26-38) | 8/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.65s | 3m 50s |
| [sftp-only-account](https://github.com/open-sudo/infraset/tree/main/jobs/sftp-only-account-rhel7/2026-09-02__18-26-38) | 25/5 | 1.000 | 1.000 | 1.000 | 0.960 | 0.66s | 6m 42s |
| [shared-directory-acl](https://github.com/open-sudo/infraset/tree/main/jobs/shared-directory-acl-rhel7/2026-09-02__18-26-38) | 15/6 | 1.000 | 1.000 | 1.000 | 0.860 | 0.63s | 4m 46s |
| [shared-group-directory](https://github.com/open-sudo/infraset/tree/main/jobs/shared-group-directory-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 1.000 | 0.90s | 26m 04s |
| [ssh-group-access](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-group-access-rhel7/2026-09-02__18-26-38) | 7/3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.98s | 3m 09s |
| [ssh-key-only](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-key-only-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.05s | 25m 46s |
| [ssh-rate-limiting](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-rate-limiting-rhel7/2026-09-02__18-26-38) | 23/12 | 1.000 | 1.000 | 1.000 | 1.000 | 0.89s | 7m 11s |
| [static-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/static-web-service-rhel7/2026-09-02__18-26-38) | 9/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.87s | 2m 32s |
| [sticky-drop-directory](https://github.com/open-sudo/infraset/tree/main/jobs/sticky-drop-directory-rhel7/2026-09-02__18-26-38) | 9/0 | 1.000 | 1.000 | 1.000 | 0.950 | 0.70s | 2m 26s |
| [swap-file](https://github.com/open-sudo/infraset/tree/main/jobs/swap-file-rhel7/2026-09-02__18-26-38) | 11/1 | 1.000 | 1.000 | 1.000 | 1.000 | 1.01s | 2m 36s |
| [system-hostname](https://github.com/open-sudo/infraset/tree/main/jobs/system-hostname-rhel7/2026-09-02__18-26-38) | 7/6 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 3m 38s |
| [system-locale](https://github.com/open-sudo/infraset/tree/main/jobs/system-locale-rhel7/2026-09-02__18-26-38) | 24/3 | 1.000 | 1.000 | 1.000 | 0.980 | 0.82s | 4m 38s |
| [system-timezone](https://github.com/open-sudo/infraset/tree/main/jobs/system-timezone-rhel7/2026-09-02__18-26-38) | 6/3 | 1.000 | 1.000 | 1.000 | 0.960 | 0.62s | 2m 01s |
| [temporary-file-cleanup](https://github.com/open-sudo/infraset/tree/main/jobs/temporary-file-cleanup-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.80s | — |
| [time-synchronization](https://github.com/open-sudo/infraset/tree/main/jobs/time-synchronization-rhel7/2026-09-02__18-26-38) | 8/5 | 1.000 | 1.000 | 1.000 | 0.920 | 0.61s | 2m 49s |
| [unprivileged-service](https://github.com/open-sudo/infraset/tree/main/jobs/unprivileged-service-rhel7/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.92s | — |

## RHEL 8.8

*50/50 tasks executed.*

| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/account-resource-limits-rhel8/2026-09-02__18-26-38) | 10/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.80s | 2m 05s |
| [admin-account](https://github.com/open-sudo/infraset/tree/main/jobs/admin-account-rhel8/2026-09-02__18-26-38) | 14/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.73s | 2m 21s |
| [application-log-rotation](https://github.com/open-sudo/infraset/tree/main/jobs/application-log-rotation-rhel8/2026-09-02__18-26-38) | 17/1 | 1.000 | 1.000 | 1.000 | 1.000 | 1.08s | 3m 45s |
| [audit-sensitive-file](https://github.com/open-sudo/infraset/tree/main/jobs/audit-sensitive-file-rhel8/2026-09-02__18-26-38) | 20/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.98s | 3m 17s |
| [boot-service](https://github.com/open-sudo/infraset/tree/main/jobs/boot-service-rhel8/2026-09-02__18-26-38) | 8/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.81s | 1m 41s |
| [caching-dns-resolver](https://github.com/open-sudo/infraset/tree/main/jobs/caching-dns-resolver-rhel8/2026-09-02__18-26-38) | 36/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.76s | 5m 06s |
| [custom-ca-trust](https://github.com/open-sudo/infraset/tree/main/jobs/custom-ca-trust-rhel8/2026-09-02__18-26-38) | 13/4 | 1.000 | 1.000 | 1.000 | 0.950 | 1.13s | 3m 17s |
| [disable-core-dumps](https://github.com/open-sudo/infraset/tree/main/jobs/disable-core-dumps-rhel8/2026-09-02__18-26-38) | 39/9 | 1.000 | 1.000 | 1.000 | 0.980 | 0.73s | 5m 15s |
| [graceful-service-shutdown](https://github.com/open-sudo/infraset/tree/main/jobs/graceful-service-shutdown-rhel8/2026-09-02__18-26-38) | 13/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.63s | 2m 13s |
| [host-firewall-baseline](https://github.com/open-sudo/infraset/tree/main/jobs/host-firewall-baseline-rhel8/2026-09-02__18-26-38) | 29/1 | 1.000 | 1.000 | 1.000 | 1.000 | 1.07s | 3m 20s |
| [https-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/https-web-service-rhel8/2026-09-02__18-26-38) | 12/3 | 1.000 | 1.000 | 1.000 | 0.980 | 0.65s | 2m 22s |
| [kernel-network-hardening](https://github.com/open-sudo/infraset/tree/main/jobs/kernel-network-hardening-rhel8/2026-09-02__18-26-38) | 15/3 | 1.000 | 1.000 | 1.000 | 0.970 | 1.37s | 3m 16s |
| [local-log-retention](https://github.com/open-sudo/infraset/tree/main/jobs/local-log-retention-rhel8/2026-09-02__18-26-38) | 22/2 | 1.000 | 1.000 | 1.000 | 0.960 | 0.94s | 4m 02s |
| [login-banner](https://github.com/open-sudo/infraset/tree/main/jobs/login-banner-rhel8/2026-09-02__18-26-38) | 11/1 | 1.000 | 1.000 | 1.000 | 0.980 | 0.68s | 1m 54s |
| [login-lockout](https://github.com/open-sudo/infraset/tree/main/jobs/login-lockout-rhel8/2026-09-02__18-26-38) | 28/2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.31s | 9m 53s |
| [loopback-only-service](https://github.com/open-sudo/infraset/tree/main/jobs/loopback-only-service-rhel8/2026-09-02__18-26-38) | 12/3 | 1.000 | 1.000 | 1.000 | 0.960 | 0.69s | 2m 12s |
| [mariadb-local-service](https://github.com/open-sudo/infraset/tree/main/jobs/mariadb-local-service-rhel8/2026-09-02__18-26-38) | 14/2 | 1.000 | 1.000 | 1.000 | 0.840 | 1.18s | 3m 24s |
| [password-aging](https://github.com/open-sudo/infraset/tree/main/jobs/password-aging-rhel8/2026-09-02__18-26-38) | 8/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.81s | 2m 04s |
| [persistent-bind-mount](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-bind-mount-rhel8/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.14s | 1m 50s |
| [persistent-dns-settings](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-dns-settings-rhel8/2026-09-02__18-26-38) | 10/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.69s | 1m 36s |
| [redis-persistent-service](https://github.com/open-sudo/infraset/tree/main/jobs/redis-persistent-service-rhel8/2026-09-02__18-26-38) | 28/3 | 1.000 | 1.000 | 1.000 | 0.800 | 0.70s | 5m 52s |
| [repair-application-permissions](https://github.com/open-sudo/infraset/tree/main/jobs/repair-application-permissions-rhel8/2026-09-02__18-26-38) | 13/1 | 1.000 | 1.000 | 1.000 | 1.000 | 1.12s | 2m 57s |
| [restore-latest-backup](https://github.com/open-sudo/infraset/tree/main/jobs/restore-latest-backup-rhel8/2026-09-02__18-26-38) | 11/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.70s | 2m 11s |
| [restricted-sudo](https://github.com/open-sudo/infraset/tree/main/jobs/restricted-sudo-rhel8/2026-09-02__18-26-38) | 15/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.68s | 3m 45s |
| [reverse-proxy](https://github.com/open-sudo/infraset/tree/main/jobs/reverse-proxy-rhel8/2026-09-02__18-26-38) | 17/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.82s | 3m 09s |
| [scheduled-backup](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-backup-rhel8/2026-09-02__18-26-38) | 15/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.81s | 2m 57s |
| [scheduled-maintenance](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-maintenance-rhel8/2026-09-02__18-26-38) | 13/3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.90s | 2m 17s |
| [secure-umask](https://github.com/open-sudo/infraset/tree/main/jobs/secure-umask-rhel8/2026-09-02__18-26-38) | 4/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 1m 02s |
| [security-updates](https://github.com/open-sudo/infraset/tree/main/jobs/security-updates-rhel8/2026-09-02__18-26-38) | 5/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.70s | 0m 46s |
| [separate-authentication-logs](https://github.com/open-sudo/infraset/tree/main/jobs/separate-authentication-logs-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.88s | 0m 15s |
| [service-account](https://github.com/open-sudo/infraset/tree/main/jobs/service-account-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.76s | 0m 13s |
| [service-dependency](https://github.com/open-sudo/infraset/tree/main/jobs/service-dependency-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.67s | 0m 11s |
| [service-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/service-resource-limits-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.77s | 0m 13s |
| [service-restart-on-failure](https://github.com/open-sudo/infraset/tree/main/jobs/service-restart-on-failure-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.61s | 0m 19s |
| [setgid-workspace](https://github.com/open-sudo/infraset/tree/main/jobs/setgid-workspace-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.64s | 0m 16s |
| [sftp-only-account](https://github.com/open-sudo/infraset/tree/main/jobs/sftp-only-account-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 10s |
| [shared-directory-acl](https://github.com/open-sudo/infraset/tree/main/jobs/shared-directory-acl-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.67s | 0m 18s |
| [shared-group-directory](https://github.com/open-sudo/infraset/tree/main/jobs/shared-group-directory-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.66s | 0m 18s |
| [ssh-group-access](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-group-access-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.06s | 0m 17s |
| [ssh-key-only](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-key-only-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.64s | 0m 14s |
| [ssh-rate-limiting](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-rate-limiting-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.05s | 0m 13s |
| [static-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/static-web-service-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.78s | 0m 12s |
| [sticky-drop-directory](https://github.com/open-sudo/infraset/tree/main/jobs/sticky-drop-directory-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.75s | 0m 17s |
| [swap-file](https://github.com/open-sudo/infraset/tree/main/jobs/swap-file-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.63s | 0m 20s |
| [system-hostname](https://github.com/open-sudo/infraset/tree/main/jobs/system-hostname-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.63s | 0m 22s |
| [system-locale](https://github.com/open-sudo/infraset/tree/main/jobs/system-locale-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.65s | 0m 16s |
| [system-timezone](https://github.com/open-sudo/infraset/tree/main/jobs/system-timezone-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.83s | 0m 17s |
| [temporary-file-cleanup](https://github.com/open-sudo/infraset/tree/main/jobs/temporary-file-cleanup-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 37s |
| [time-synchronization](https://github.com/open-sudo/infraset/tree/main/jobs/time-synchronization-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.63s | 0m 23s |
| [unprivileged-service](https://github.com/open-sudo/infraset/tree/main/jobs/unprivileged-service-rhel8/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 21s |

## RHEL 9.8

*50/50 tasks executed.*

| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/account-resource-limits-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.74s | 0m 11s |
| [admin-account](https://github.com/open-sudo/infraset/tree/main/jobs/admin-account-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.66s | 0m 10s |
| [application-log-rotation](https://github.com/open-sudo/infraset/tree/main/jobs/application-log-rotation-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.76s | 0m 09s |
| [audit-sensitive-file](https://github.com/open-sudo/infraset/tree/main/jobs/audit-sensitive-file-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.29s | 0m 10s |
| [boot-service](https://github.com/open-sudo/infraset/tree/main/jobs/boot-service-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.72s | 0m 10s |
| [caching-dns-resolver](https://github.com/open-sudo/infraset/tree/main/jobs/caching-dns-resolver-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.84s | 0m 10s |
| [custom-ca-trust](https://github.com/open-sudo/infraset/tree/main/jobs/custom-ca-trust-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.65s | 0m 11s |
| [disable-core-dumps](https://github.com/open-sudo/infraset/tree/main/jobs/disable-core-dumps-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 17s |
| [graceful-service-shutdown](https://github.com/open-sudo/infraset/tree/main/jobs/graceful-service-shutdown-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.08s | 0m 17s |
| [host-firewall-baseline](https://github.com/open-sudo/infraset/tree/main/jobs/host-firewall-baseline-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.69s | 0m 12s |
| [https-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/https-web-service-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 24s |
| [kernel-network-hardening](https://github.com/open-sudo/infraset/tree/main/jobs/kernel-network-hardening-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.99s | 0m 38s |
| [local-log-retention](https://github.com/open-sudo/infraset/tree/main/jobs/local-log-retention-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.88s | 0m 39s |
| [login-banner](https://github.com/open-sudo/infraset/tree/main/jobs/login-banner-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.75s | 0m 35s |
| [login-lockout](https://github.com/open-sudo/infraset/tree/main/jobs/login-lockout-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.87s | 0m 23s |
| [loopback-only-service](https://github.com/open-sudo/infraset/tree/main/jobs/loopback-only-service-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.85s | 0m 33s |
| [mariadb-local-service](https://github.com/open-sudo/infraset/tree/main/jobs/mariadb-local-service-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.67s | 0m 37s |
| [password-aging](https://github.com/open-sudo/infraset/tree/main/jobs/password-aging-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.76s | 0m 23s |
| [persistent-bind-mount](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-bind-mount-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.69s | 0m 23s |
| [persistent-dns-settings](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-dns-settings-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.71s | 0m 46s |
| [redis-persistent-service](https://github.com/open-sudo/infraset/tree/main/jobs/redis-persistent-service-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.78s | 0m 15s |
| [repair-application-permissions](https://github.com/open-sudo/infraset/tree/main/jobs/repair-application-permissions-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.83s | 0m 15s |
| [restore-latest-backup](https://github.com/open-sudo/infraset/tree/main/jobs/restore-latest-backup-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 21s |
| [restricted-sudo](https://github.com/open-sudo/infraset/tree/main/jobs/restricted-sudo-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 26s |
| [reverse-proxy](https://github.com/open-sudo/infraset/tree/main/jobs/reverse-proxy-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.18s | 0m 19s |
| [scheduled-backup](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-backup-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.26s | 0m 12s |
| [scheduled-maintenance](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-maintenance-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.71s | 0m 09s |
| [secure-umask](https://github.com/open-sudo/infraset/tree/main/jobs/secure-umask-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.70s | 0m 15s |
| [security-updates](https://github.com/open-sudo/infraset/tree/main/jobs/security-updates-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.79s | 0m 11s |
| [separate-authentication-logs](https://github.com/open-sudo/infraset/tree/main/jobs/separate-authentication-logs-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.76s | 0m 15s |
| [service-account](https://github.com/open-sudo/infraset/tree/main/jobs/service-account-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.74s | 0m 13s |
| [service-dependency](https://github.com/open-sudo/infraset/tree/main/jobs/service-dependency-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.10s | 0m 16s |
| [service-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/service-resource-limits-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.96s | 0m 09s |
| [service-restart-on-failure](https://github.com/open-sudo/infraset/tree/main/jobs/service-restart-on-failure-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.78s | 0m 22s |
| [setgid-workspace](https://github.com/open-sudo/infraset/tree/main/jobs/setgid-workspace-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.86s | 0m 41s |
| [sftp-only-account](https://github.com/open-sudo/infraset/tree/main/jobs/sftp-only-account-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.80s | 0m 27s |
| [shared-directory-acl](https://github.com/open-sudo/infraset/tree/main/jobs/shared-directory-acl-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.82s | 0m 19s |
| [shared-group-directory](https://github.com/open-sudo/infraset/tree/main/jobs/shared-group-directory-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.19s | 0m 17s |
| [ssh-group-access](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-group-access-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 17s |
| [ssh-key-only](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-key-only-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.81s | 0m 19s |
| [ssh-rate-limiting](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-rate-limiting-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.31s | 0m 16s |
| [static-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/static-web-service-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.78s | 0m 15s |
| [sticky-drop-directory](https://github.com/open-sudo/infraset/tree/main/jobs/sticky-drop-directory-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.73s | 0m 14s |
| [swap-file](https://github.com/open-sudo/infraset/tree/main/jobs/swap-file-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.75s | 0m 21s |
| [system-hostname](https://github.com/open-sudo/infraset/tree/main/jobs/system-hostname-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.72s | 0m 16s |
| [system-locale](https://github.com/open-sudo/infraset/tree/main/jobs/system-locale-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.79s | 0m 16s |
| [system-timezone](https://github.com/open-sudo/infraset/tree/main/jobs/system-timezone-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.66s | 0m 17s |
| [temporary-file-cleanup](https://github.com/open-sudo/infraset/tree/main/jobs/temporary-file-cleanup-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.82s | 0m 11s |
| [time-synchronization](https://github.com/open-sudo/infraset/tree/main/jobs/time-synchronization-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.72s | 0m 44s |
| [unprivileged-service](https://github.com/open-sudo/infraset/tree/main/jobs/unprivileged-service-rhel9/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.76s | 0m 41s |

## RHEL 10.0

*50/50 tasks executed.*

| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/account-resource-limits-rhel10/2026-09-02__18-26-38) | 12/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.75s | 2m 11s |
| [admin-account](https://github.com/open-sudo/infraset/tree/main/jobs/admin-account-rhel10/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.74s | — |
| [application-log-rotation](https://github.com/open-sudo/infraset/tree/main/jobs/application-log-rotation-rhel10/2026-09-02__18-26-38) | 15/2 | 1.000 | 1.000 | 1.000 | 0.970 | 0.80s | 2m 37s |
| [audit-sensitive-file](https://github.com/open-sudo/infraset/tree/main/jobs/audit-sensitive-file-rhel10/2026-09-02__18-26-38) | 19/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 3m 28s |
| [boot-service](https://github.com/open-sudo/infraset/tree/main/jobs/boot-service-rhel10/2026-09-02__18-26-38) | 9/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.64s | 1m 48s |
| [caching-dns-resolver](https://github.com/open-sudo/infraset/tree/main/jobs/caching-dns-resolver-rhel10/2026-09-02__18-26-38) | 20/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.73s | 4m 48s |
| [custom-ca-trust](https://github.com/open-sudo/infraset/tree/main/jobs/custom-ca-trust-rhel10/2026-09-02__18-26-38) | 9/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.70s | 2m 24s |
| [disable-core-dumps](https://github.com/open-sudo/infraset/tree/main/jobs/disable-core-dumps-rhel10/2026-09-02__18-26-38) | 23/3 | 1.000 | 1.000 | 1.000 | 0.970 | 1.11s | 5m 04s |
| [graceful-service-shutdown](https://github.com/open-sudo/infraset/tree/main/jobs/graceful-service-shutdown-rhel10/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.72s | — |
| [host-firewall-baseline](https://github.com/open-sudo/infraset/tree/main/jobs/host-firewall-baseline-rhel10/2026-09-02__18-26-38) | 14/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.69s | 3m 33s |
| [https-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/https-web-service-rhel10/2026-09-02__18-26-38) | 13/3 | 1.000 | 1.000 | 1.000 | 0.900 | 0.67s | 2m 15s |
| [kernel-network-hardening](https://github.com/open-sudo/infraset/tree/main/jobs/kernel-network-hardening-rhel10/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.90s | 1m 59s |
| [local-log-retention](https://github.com/open-sudo/infraset/tree/main/jobs/local-log-retention-rhel10/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.81s | 2m 10s |
| [login-banner](https://github.com/open-sudo/infraset/tree/main/jobs/login-banner-rhel10/2026-09-02__18-26-38) | 13/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.74s | 2m 46s |
| [login-lockout](https://github.com/open-sudo/infraset/tree/main/jobs/login-lockout-rhel10/2026-09-02__18-26-38) | 28/4 | 1.000 | 1.000 | 1.000 | 0.970 | 1.01s | 10m 59s |
| [loopback-only-service](https://github.com/open-sudo/infraset/tree/main/jobs/loopback-only-service-rhel10/2026-09-02__18-26-38) | 13/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 2m 18s |
| [mariadb-local-service](https://github.com/open-sudo/infraset/tree/main/jobs/mariadb-local-service-rhel10/2026-09-02__18-26-38) | 14/5 | 1.000 | 1.000 | 1.000 | 0.780 | 0.66s | 5m 16s |
| [password-aging](https://github.com/open-sudo/infraset/tree/main/jobs/password-aging-rhel10/2026-09-02__18-26-38) | 9/2 | 1.000 | 1.000 | 1.000 | 0.900 | 0.71s | 2m 03s |
| [persistent-bind-mount](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-bind-mount-rhel10/2026-09-02__18-26-38) | 10/3 | 1.000 | 1.000 | 1.000 | 0.970 | 0.78s | 1m 38s |
| [persistent-dns-settings](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-dns-settings-rhel10/2026-09-02__18-26-38) | 13/2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.11s | 1m 41s |
| [redis-persistent-service](https://github.com/open-sudo/infraset/tree/main/jobs/redis-persistent-service-rhel10/2026-09-02__18-26-38) | 15/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.66s | 3m 17s |
| [repair-application-permissions](https://github.com/open-sudo/infraset/tree/main/jobs/repair-application-permissions-rhel10/2026-09-02__18-26-38) | 13/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.77s | 2m 57s |
| [restore-latest-backup](https://github.com/open-sudo/infraset/tree/main/jobs/restore-latest-backup-rhel10/2026-09-02__18-26-38) | 15/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.76s | 1m 57s |
| [restricted-sudo](https://github.com/open-sudo/infraset/tree/main/jobs/restricted-sudo-rhel10/2026-09-02__18-26-38) | 18/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.79s | 3m 25s |
| [reverse-proxy](https://github.com/open-sudo/infraset/tree/main/jobs/reverse-proxy-rhel10/2026-09-02__18-26-38) | 20/3 | 1.000 | 1.000 | 1.000 | 0.800 | 0.81s | 3m 24s |
| [scheduled-backup](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-backup-rhel10/2026-09-02__18-26-38) | 17/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.76s | 3m 11s |
| [scheduled-maintenance](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-maintenance-rhel10/2026-09-02__18-26-38) | 12/1 | 1.000 | 1.000 | 1.000 | 1.000 | 1.13s | 2m 23s |
| [secure-umask](https://github.com/open-sudo/infraset/tree/main/jobs/secure-umask-rhel10/2026-09-02__18-26-38) | 9/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.69s | 2m 18s |
| [security-updates](https://github.com/open-sudo/infraset/tree/main/jobs/security-updates-rhel10/2026-09-02__18-26-38) | 19/3 | 1.000 | 1.000 | 1.000 | 0.950 | 0.68s | 3m 28s |
| [separate-authentication-logs](https://github.com/open-sudo/infraset/tree/main/jobs/separate-authentication-logs-rhel10/2026-09-02__18-26-38) | 16/3 | 1.000 | 1.000 | 1.000 | 1.000 | 1.19s | 2m 53s |
| [service-account](https://github.com/open-sudo/infraset/tree/main/jobs/service-account-rhel10/2026-09-02__18-26-38) | 7/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.81s | 1m 27s |
| [service-dependency](https://github.com/open-sudo/infraset/tree/main/jobs/service-dependency-rhel10/2026-09-02__18-26-38) | 13/3 | 1.000 | 1.000 | 1.000 | 1.000 | 1.22s | 2m 25s |
| [service-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/service-resource-limits-rhel10/2026-09-02__18-26-38) | 14/3 | 1.000 | 1.000 | 1.000 | 0.860 | 1.13s | 5m 17s |
| [service-restart-on-failure](https://github.com/open-sudo/infraset/tree/main/jobs/service-restart-on-failure-rhel10/2026-09-02__18-26-38) | 13/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.71s | 2m 20s |
| [setgid-workspace](https://github.com/open-sudo/infraset/tree/main/jobs/setgid-workspace-rhel10/2026-09-02__18-26-38) | 7/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.74s | 1m 40s |
| [sftp-only-account](https://github.com/open-sudo/infraset/tree/main/jobs/sftp-only-account-rhel10/2026-09-02__18-26-38) | 18/2 | 1.000 | 1.000 | 1.000 | 0.900 | 0.73s | 4m 55s |
| [shared-directory-acl](https://github.com/open-sudo/infraset/tree/main/jobs/shared-directory-acl-rhel10/2026-09-02__18-26-38) | 11/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.74s | 2m 56s |
| [shared-group-directory](https://github.com/open-sudo/infraset/tree/main/jobs/shared-group-directory-rhel10/2026-09-02__18-26-38) | 8/2 | 1.000 | 1.000 | 1.000 | 0.940 | 1.05s | 2m 01s |
| [ssh-group-access](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-group-access-rhel10/2026-09-02__18-26-38) | 17/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.65s | 3m 47s |
| [ssh-key-only](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-key-only-rhel10/2026-09-02__18-26-38) | 23/2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.11s | 3m 16s |
| [ssh-rate-limiting](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-rate-limiting-rhel10/2026-09-02__18-26-38) | 22/2 | 1.000 | 1.000 | 1.000 | 0.970 | 0.71s | 5m 06s |
| [static-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/static-web-service-rhel10/2026-09-02__18-26-38) | 10/3 | 1.000 | 1.000 | 1.000 | 1.000 | 1.15s | 1m 49s |
| [sticky-drop-directory](https://github.com/open-sudo/infraset/tree/main/jobs/sticky-drop-directory-rhel10/2026-09-02__18-26-38) | 10/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.79s | 2m 00s |
| [swap-file](https://github.com/open-sudo/infraset/tree/main/jobs/swap-file-rhel10/2026-09-02__18-26-38) | 12/2 | 1.000 | 1.000 | 1.000 | 0.970 | 1.22s | 2m 12s |
| [system-hostname](https://github.com/open-sudo/infraset/tree/main/jobs/system-hostname-rhel10/2026-09-02__18-26-38) | 8/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.73s | 1m 33s |
| [system-locale](https://github.com/open-sudo/infraset/tree/main/jobs/system-locale-rhel10/2026-09-02__18-26-38) | 11/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.78s | 2m 45s |
| [system-timezone](https://github.com/open-sudo/infraset/tree/main/jobs/system-timezone-rhel10/2026-09-02__18-26-38) | 11/2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.23s | 1m 26s |
| [temporary-file-cleanup](https://github.com/open-sudo/infraset/tree/main/jobs/temporary-file-cleanup-rhel10/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.04s | — |
| [time-synchronization](https://github.com/open-sudo/infraset/tree/main/jobs/time-synchronization-rhel10/2026-09-02__18-26-38) | 16/3 | 1.000 | 1.000 | 1.000 | 0.970 | 0.70s | 2m 19s |
| [unprivileged-service](https://github.com/open-sudo/infraset/tree/main/jobs/unprivileged-service-rhel10/2026-09-02__18-26-38) | 17/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.98s | 2m 32s |

## Ubuntu 16.04

*50/50 tasks executed.*

| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/account-resource-limits-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.60s | — |
| [admin-account](https://github.com/open-sudo/infraset/tree/main/jobs/admin-account-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.76s | 0m 27s |
| [application-log-rotation](https://github.com/open-sudo/infraset/tree/main/jobs/application-log-rotation-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | — |
| [audit-sensitive-file](https://github.com/open-sudo/infraset/tree/main/jobs/audit-sensitive-file-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.51s | — |
| [boot-service](https://github.com/open-sudo/infraset/tree/main/jobs/boot-service-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.57s | — |
| [caching-dns-resolver](https://github.com/open-sudo/infraset/tree/main/jobs/caching-dns-resolver-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.52s | 0m 35s |
| [custom-ca-trust](https://github.com/open-sudo/infraset/tree/main/jobs/custom-ca-trust-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.51s | 0m 08s |
| [disable-core-dumps](https://github.com/open-sudo/infraset/tree/main/jobs/disable-core-dumps-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.49s | 0m 29s |
| [graceful-service-shutdown](https://github.com/open-sudo/infraset/tree/main/jobs/graceful-service-shutdown-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.55s | — |
| [host-firewall-baseline](https://github.com/open-sudo/infraset/tree/main/jobs/host-firewall-baseline-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.50s | 0m 15s |
| [https-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/https-web-service-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.67s | 0m 19s |
| [kernel-network-hardening](https://github.com/open-sudo/infraset/tree/main/jobs/kernel-network-hardening-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.46s | 0m 17s |
| [local-log-retention](https://github.com/open-sudo/infraset/tree/main/jobs/local-log-retention-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.49s | 0m 13s |
| [login-banner](https://github.com/open-sudo/infraset/tree/main/jobs/login-banner-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.58s | 0m 35s |
| [login-lockout](https://github.com/open-sudo/infraset/tree/main/jobs/login-lockout-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.58s | 0m 31s |
| [loopback-only-service](https://github.com/open-sudo/infraset/tree/main/jobs/loopback-only-service-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.54s | 0m 44s |
| [mariadb-local-service](https://github.com/open-sudo/infraset/tree/main/jobs/mariadb-local-service-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.54s | 0m 10s |
| [password-aging](https://github.com/open-sudo/infraset/tree/main/jobs/password-aging-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.53s | 0m 28s |
| [persistent-bind-mount](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-bind-mount-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.53s | 0m 27s |
| [persistent-dns-settings](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-dns-settings-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.57s | 0m 32s |
| [redis-persistent-service](https://github.com/open-sudo/infraset/tree/main/jobs/redis-persistent-service-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.54s | 0m 29s |
| [repair-application-permissions](https://github.com/open-sudo/infraset/tree/main/jobs/repair-application-permissions-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.53s | — |
| [restore-latest-backup](https://github.com/open-sudo/infraset/tree/main/jobs/restore-latest-backup-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.51s | — |
| [restricted-sudo](https://github.com/open-sudo/infraset/tree/main/jobs/restricted-sudo-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.54s | 0m 31s |
| [reverse-proxy](https://github.com/open-sudo/infraset/tree/main/jobs/reverse-proxy-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.67s | 0m 36s |
| [scheduled-backup](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-backup-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.51s | — |
| [scheduled-maintenance](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-maintenance-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.47s | — |
| [secure-umask](https://github.com/open-sudo/infraset/tree/main/jobs/secure-umask-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.53s | 0m 13s |
| [security-updates](https://github.com/open-sudo/infraset/tree/main/jobs/security-updates-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.57s | — |
| [separate-authentication-logs](https://github.com/open-sudo/infraset/tree/main/jobs/separate-authentication-logs-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.62s | — |
| [service-account](https://github.com/open-sudo/infraset/tree/main/jobs/service-account-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.50s | 0m 49s |
| [service-dependency](https://github.com/open-sudo/infraset/tree/main/jobs/service-dependency-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.60s | — |
| [service-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/service-resource-limits-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.52s | — |
| [service-restart-on-failure](https://github.com/open-sudo/infraset/tree/main/jobs/service-restart-on-failure-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.54s | — |
| [setgid-workspace](https://github.com/open-sudo/infraset/tree/main/jobs/setgid-workspace-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.48s | 0m 40s |
| [sftp-only-account](https://github.com/open-sudo/infraset/tree/main/jobs/sftp-only-account-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.54s | 0m 10s |
| [shared-directory-acl](https://github.com/open-sudo/infraset/tree/main/jobs/shared-directory-acl-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.60s | 0m 11s |
| [shared-group-directory](https://github.com/open-sudo/infraset/tree/main/jobs/shared-group-directory-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.56s | 0m 08s |
| [ssh-group-access](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-group-access-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.48s | 0m 22s |
| [ssh-key-only](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-key-only-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.67s | 0m 20s |
| [ssh-rate-limiting](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-rate-limiting-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.58s | 0m 10s |
| [static-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/static-web-service-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.51s | 0m 08s |
| [sticky-drop-directory](https://github.com/open-sudo/infraset/tree/main/jobs/sticky-drop-directory-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.62s | 0m 52s |
| [swap-file](https://github.com/open-sudo/infraset/tree/main/jobs/swap-file-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.55s | 0m 20s |
| [system-hostname](https://github.com/open-sudo/infraset/tree/main/jobs/system-hostname-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.49s | 0m 44s |
| [system-locale](https://github.com/open-sudo/infraset/tree/main/jobs/system-locale-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.54s | 0m 08s |
| [system-timezone](https://github.com/open-sudo/infraset/tree/main/jobs/system-timezone-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.55s | 0m 42s |
| [temporary-file-cleanup](https://github.com/open-sudo/infraset/tree/main/jobs/temporary-file-cleanup-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.49s | — |
| [time-synchronization](https://github.com/open-sudo/infraset/tree/main/jobs/time-synchronization-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.54s | 0m 47s |
| [unprivileged-service](https://github.com/open-sudo/infraset/tree/main/jobs/unprivileged-service-ubuntu16/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.55s | — |

## Ubuntu 24.04

*50/50 tasks executed.*

| Task | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/account-resource-limits-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 1m 23s |
| [admin-account](https://github.com/open-sudo/infraset/tree/main/jobs/admin-account-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.72s | 0m 08s |
| [application-log-rotation](https://github.com/open-sudo/infraset/tree/main/jobs/application-log-rotation-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.89s | 0m 08s |
| [audit-sensitive-file](https://github.com/open-sudo/infraset/tree/main/jobs/audit-sensitive-file-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.66s | 0m 29s |
| [boot-service](https://github.com/open-sudo/infraset/tree/main/jobs/boot-service-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.67s | 0m 27s |
| [caching-dns-resolver](https://github.com/open-sudo/infraset/tree/main/jobs/caching-dns-resolver-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.69s | 0m 08s |
| [custom-ca-trust](https://github.com/open-sudo/infraset/tree/main/jobs/custom-ca-trust-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.61s | 0m 08s |
| [disable-core-dumps](https://github.com/open-sudo/infraset/tree/main/jobs/disable-core-dumps-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.97s | 0m 51s |
| [graceful-service-shutdown](https://github.com/open-sudo/infraset/tree/main/jobs/graceful-service-shutdown-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.72s | 0m 15s |
| [host-firewall-baseline](https://github.com/open-sudo/infraset/tree/main/jobs/host-firewall-baseline-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.69s | 0m 51s |
| [https-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/https-web-service-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.70s | 0m 08s |
| [kernel-network-hardening](https://github.com/open-sudo/infraset/tree/main/jobs/kernel-network-hardening-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.69s | 0m 09s |
| [local-log-retention](https://github.com/open-sudo/infraset/tree/main/jobs/local-log-retention-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.65s | 0m 56s |
| [login-banner](https://github.com/open-sudo/infraset/tree/main/jobs/login-banner-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.61s | 1m 02s |
| [login-lockout](https://github.com/open-sudo/infraset/tree/main/jobs/login-lockout-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.79s | 0m 08s |
| [loopback-only-service](https://github.com/open-sudo/infraset/tree/main/jobs/loopback-only-service-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.85s | 0m 50s |
| [mariadb-local-service](https://github.com/open-sudo/infraset/tree/main/jobs/mariadb-local-service-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.66s | 0m 42s |
| [password-aging](https://github.com/open-sudo/infraset/tree/main/jobs/password-aging-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.80s | 0m 31s |
| [persistent-bind-mount](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-bind-mount-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.66s | 0m 29s |
| [persistent-dns-settings](https://github.com/open-sudo/infraset/tree/main/jobs/persistent-dns-settings-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.66s | 0m 30s |
| [redis-persistent-service](https://github.com/open-sudo/infraset/tree/main/jobs/redis-persistent-service-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.71s | 0m 40s |
| [repair-application-permissions](https://github.com/open-sudo/infraset/tree/main/jobs/repair-application-permissions-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.93s | 0m 46s |
| [restore-latest-backup](https://github.com/open-sudo/infraset/tree/main/jobs/restore-latest-backup-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 47s |
| [restricted-sudo](https://github.com/open-sudo/infraset/tree/main/jobs/restricted-sudo-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.66s | 0m 37s |
| [reverse-proxy](https://github.com/open-sudo/infraset/tree/main/jobs/reverse-proxy-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.64s | 0m 27s |
| [scheduled-backup](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-backup-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 59s |
| [scheduled-maintenance](https://github.com/open-sudo/infraset/tree/main/jobs/scheduled-maintenance-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.90s | 0m 59s |
| [secure-umask](https://github.com/open-sudo/infraset/tree/main/jobs/secure-umask-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.70s | 0m 52s |
| [security-updates](https://github.com/open-sudo/infraset/tree/main/jobs/security-updates-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.76s | 0m 29s |
| [separate-authentication-logs](https://github.com/open-sudo/infraset/tree/main/jobs/separate-authentication-logs-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 24s |
| [service-account](https://github.com/open-sudo/infraset/tree/main/jobs/service-account-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.66s | 0m 12s |
| [service-dependency](https://github.com/open-sudo/infraset/tree/main/jobs/service-dependency-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.81s | 0m 11s |
| [service-resource-limits](https://github.com/open-sudo/infraset/tree/main/jobs/service-resource-limits-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.65s | 0m 40s |
| [service-restart-on-failure](https://github.com/open-sudo/infraset/tree/main/jobs/service-restart-on-failure-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.69s | 0m 10s |
| [setgid-workspace](https://github.com/open-sudo/infraset/tree/main/jobs/setgid-workspace-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.81s | 0m 09s |
| [sftp-only-account](https://github.com/open-sudo/infraset/tree/main/jobs/sftp-only-account-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.93s | 0m 10s |
| [shared-directory-acl](https://github.com/open-sudo/infraset/tree/main/jobs/shared-directory-acl-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.74s | 0m 10s |
| [shared-group-directory](https://github.com/open-sudo/infraset/tree/main/jobs/shared-group-directory-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.76s | 0m 26s |
| [ssh-group-access](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-group-access-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.73s | 0m 08s |
| [ssh-key-only](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-key-only-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.70s | 0m 11s |
| [ssh-rate-limiting](https://github.com/open-sudo/infraset/tree/main/jobs/ssh-rate-limiting-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.90s | 0m 44s |
| [static-web-service](https://github.com/open-sudo/infraset/tree/main/jobs/static-web-service-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.70s | 0m 13s |
| [sticky-drop-directory](https://github.com/open-sudo/infraset/tree/main/jobs/sticky-drop-directory-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.75s | 0m 15s |
| [swap-file](https://github.com/open-sudo/infraset/tree/main/jobs/swap-file-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.77s | 0m 15s |
| [system-hostname](https://github.com/open-sudo/infraset/tree/main/jobs/system-hostname-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.67s | 0m 43s |
| [system-locale](https://github.com/open-sudo/infraset/tree/main/jobs/system-locale-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.18s | 0m 40s |
| [system-timezone](https://github.com/open-sudo/infraset/tree/main/jobs/system-timezone-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.76s | 0m 35s |
| [temporary-file-cleanup](https://github.com/open-sudo/infraset/tree/main/jobs/temporary-file-cleanup-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.68s | 0m 11s |
| [time-synchronization](https://github.com/open-sudo/infraset/tree/main/jobs/time-synchronization-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.74s | 0m 07s |
| [unprivileged-service](https://github.com/open-sudo/infraset/tree/main/jobs/unprivileged-service-ubuntu24/2026-09-02__18-26-38) | 0/0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.66s | 0m 08s |
