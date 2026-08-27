# Execution summary

This table summarizes the recorded jobs in `jobs/`. `Full passes` counts trials with complete evaluation coverage and successful functional behavior. `Evaluation coverage` and `Operational hygiene` are per-trial averages. `Best score` is the highest per-trial reward; `Provisioning time` and `Mean duration` are averages across recorded trials. A missing job means no result has been recorded yet.

`Operational hygiene` measures whether the evaluator found executor-created
residue, abandoned files, conflicting services, unsafe exposure, or other
unwanted changes. `100%` means the hygiene checks passed; `0%` means they
failed. It is independent of the task's functional result.

| Task | Environment | Runs | Full passes | Best score | Evaluation coverage | Operational hygiene | Provisioning time | Mean duration |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| disk-full-recovery-centos-stream10 | centos-stream10 | 1 | 1/1 | 1.00 | 100% | 100% | 0.97 sec | 8.3 min |
| kernel-network-stack-migration | ubuntu16.04; ubuntu24.04 | 2 | 2/2 | 1.00 | 100% | 100% | 0.77 sec | 14.9 min |
| loki-cascading-failure-ubuntu24 | ubuntu24.04 x4 | 2 | 1/2 | 1.00 | 100% | 100% | 1.05 sec | 8.6 min |
| mariadb-migration-ubuntu16-ubuntu24 | ubuntu16.04; ubuntu24.04 | 8 | 2/8 | 1.00 | 100% | 100% | 0.80 sec | 3.9 min |
| nginx-tls-certificate-rotation-debian13 | debian13 x2 | 2 | 2/2 | 0.75 | 100% | 0% | 0.75 sec | 8.6 min |
| rhel9-drift-remediation | rhel9.8 x4 | 3 | 2/3 | 1.00 | 100% | 50% | 1.03 sec | 9.3 min |
| rhel9-ssh-hardening-jumpbox | rhel9.8; almalinux9 x2 | 2 | 1/2 | 1.00 | 100% | 100% | 0.91 sec | 4.8 min |
| sudoers-rescue-alma9 | almalinux9 | 1 | 1/1 | 1.00 | 100% | 100% | 0.73 sec | 6.2 min |
| systemd-broken-execstart-alma9 | almalinux9 | 1 | 1/1 | 1.00 | 100% | 100% | 0.71 sec | 7.5 min |
| user-password-hash-migration | ubuntu16.04; ubuntu24.04 | 1 | 1/1 | 1.00 | 100% | 100% | 0.93 sec | 16.8 min |
| bind-dnssec-alma9 | almalinux9 x4 | 1 | 0/1 | — | 57% | 100% | 1.35 sec | 12.6 min |
| etcd-mtls-centos-stream10 | centos-stream10 x4 | 2 | 0/2 | — | 50% | 100% | 1.46 sec | 22.3 min |
| haproxy-nodejs-ubuntu16 | ubuntu16.04 | 5 | 3/5 | 1.00 | 92% | 40% | 0.64 sec | 6.5 min |
| ldap-389ds-alma9 | almalinux9 x3 | — | — | — | — | — | — | — |
| mariadb-galera-ubuntu16 | ubuntu16.04 x3 | 2 | 1/2 | 0.88 | 80% | 0% | 0.74 sec | 33.8 min |
| mariadb-galera-ubuntu24 | ubuntu24.04 x3 | 1 | 1/1 | 0.88 | 100% | 0% | 0.95 sec | 15.6 min |
| minio-distributed-ubuntu24 | ubuntu24.04 x4 | 1 | 1/1 | 0.75 | 100% | 0% | 1.31 sec | 22.6 min |
| nfs-ubuntu24 | ubuntu24.04 x3 | 1 | 1/1 | 0.80 | 100% | 0% | 1.22 sec | 14.7 min |
| nginx-alma-alpine | almalinux9 x2; alpine x2 | 1 | 1/1 | 0.92 | 100% | 0% | 1.09 sec | 9.2 min |
| nginx-haproxy | ubuntu24.04 x4 | 1 | 1/1 | 1.00 | 100% | 100% | 0.97 sec | 9.3 min |
| nginx-rhel10-port-6700 | rhel10.0 | 1 | 1/1 | 1.00 | 100% | 100% | 0.89 sec | 7.0 min |
| nginx-rhel7-port-6700 | rhel7.9 | 3 | 1/3 | 0.90 | 100% | 0% | 0.72 sec | 3.1 min |
| nginx-rhel8-port-6700 | rhel8.8 | 1 | 1/1 | 1.00 | 100% | 100% | 0.70 sec | 7.7 min |
| nginx-rhel9-port-6500 | rhel9.8 | 1 | 1/1 | 0.90 | 100% | 0% | 0.68 sec | 5.6 min |
| nginx-ubuntu24-cluster | ubuntu24.04 x3 | 5 | 3/5 | 1.00 | 90% | 100% | 1.29 sec | 4.8 min |
| nodejs-rootless-podman-centos-stream10 | centos-stream10 | 1 | 1/1 | 1.00 | 100% | 100% | 0.92 sec | 10.9 min |
| opentelemetry-collector-routing | ubuntu24.04 x3 | 1 | 1/1 | 0.78 | 100% | 0% | 0.82 sec | 22.2 min |
| openwrt-guest-isolation | openwrt; ubuntu24.04 x3 | 1 | 1/1 | 1.00 | 100% | 100% | 1.16 sec | 12.7 min |
| opnsense-three-zone | opnsense; ubuntu24.04 x3 | 5 | 5/5 | 0.78 | 100% | 0% | 3.38 sec | 15.6 min |
| pacemaker-web-ha-alma9 | almalinux9 x3 | — | — | — | — | — | — | — |
| postgresql-ha-vyos-dual-lan | vyos; ubuntu24.04 x3 | 5 | 4/5 | 1.00 | 89% | 75% | 2.32 sec | 19.7 min |
| postgresql-replication-alma9 | almalinux9 x3 | 1 | 1/1 | 0.80 | 100% | 0% | 1.09 sec | 14.8 min |
| prometheus-node-exporter-ubuntu24 | ubuntu24.04 x4 | 3 | 1/3 | 1.00 | 77% | 50% | 0.95 sec | 14.6 min |
| prometheus-thanos-objectstorage | ubuntu24.04 x4 | 6 | 1/6 | 0.75 | 68% | 0% | 1.45 sec | 25.0 min |
| rabbitmq-quorum-ha | ubuntu24.04 x4 | — | — | — | — | — | — | — |
| rabbitmq-quorum-ubuntu24 | ubuntu24.04 x3 | — | — | — | — | — | — | — |
| redis-sentinel-ubuntu24 | ubuntu24.04 x3 | 1 | 1/1 | 0.75 | 100% | 0% | 1.11 sec | 14.5 min |
| rhel8-offline-package-repository | rhel8.8 x2 | 1 | 1/1 | 1.00 | 100% | — | 0.74 sec | 15.8 min |
| rsyslog-rhel7-rhel10-tls | rhel7.9; rhel8.8; rhel9.8; rhel10.0 | 3 | 0/3 | — | 52% | 0% | 1.05 sec | 20.7 min |
| samba-ad-debian13 | debian13 x4 | 2 | 0/2 | 0.64 | 75% | 0% | 1.17 sec | 21.2 min |
| sonic-frr-bgp-transit | sonic; ubuntu24.04 x2 | 2 | 1/2 | 1.00 | 100% | 100% | 1.38 sec | 17.3 min |
| sonic-mlag-lacp | sonic x2; ubuntu24.04 x2 | — | — | — | — | — | — | — |
| ssh-auth-ubuntu24 | ubuntu24.04 x3 | 5 | 4/5 | 1.00 | 90% | 25% | 1.39 sec | 10.5 min |
| static-route-convergence-vyos | vyos; ubuntu24.04 x2 | 1 | 1/1 | 0.75 | 100% | 0% | 1.00 sec | 13.6 min |
| vault-postgresql-dynamic-secrets | ubuntu24.04 x2 | 1 | 0/1 | — | 55% | — | 0.79 sec | 47.9 min |
| vault-raft-auto-unseal | ubuntu24.04 x4 | 3 | 1/3 | 0.75 | 50% | 0% | 1.11 sec | 18.5 min |
| vyos-dual-lan-kubernetes | vyos; ubuntu24.04 x3 | 2 | 1/2 | 1.00 | 100% | 100% | 1.14 sec | 19.0 min |
| wireguard-vyos-dual-lan | vyos x2; ubuntu24.04 x2 | 2 | 0/2 | — | 71% | 0% | 1.22 sec | 17.7 min |
