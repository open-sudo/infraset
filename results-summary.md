# Execution summary

This table summarizes the recorded jobs in `jobs/`. A **successful run** means the trial reached full evaluation coverage, passed the functional evaluation, and was publication-eligible. `Best score` is the highest per-trial reward recorded; `Provisioning time` and `Mean duration` are averages across recorded trials. A missing job means no result has been recorded yet.

| Task | Environment | Runs | Successful | Best score | Provisioning time | Mean duration | Takeaway |
|---|---|---:|---:|---:|---:|---:|---|
| disk-full-recovery-centos-stream10 | centos-stream10 | 1 | 1/1 | 1.00 | 0.97 sec | 8.3 min | All recorded runs reached full functional, publishable evaluation. |
| kernel-network-stack-migration | ubuntu16.04; ubuntu24.04 | 2 | 2/2 | 1.00 | 0.77 sec | 14.9 min | All recorded runs reached full functional, publishable evaluation. |
| loki-cascading-failure-ubuntu24 | ubuntu24.04 x4 | 2 | 1/2 | 1.00 | 1.05 sec | 8.6 min | Mixed outcomes: 1 of 2 runs were fully functional and publishable. |
| mariadb-migration-ubuntu16-ubuntu24 | ubuntu16.04; ubuntu24.04 | 8 | 2/8 | 1.00 | 0.80 sec | 3.9 min | Mixed outcomes: 2 of 8 runs were fully functional and publishable. |
| nginx-tls-certificate-rotation-debian13 | debian13 x2 | 2 | 2/2 | 0.75 | 0.75 sec | 8.6 min | All recorded runs reached full functional, publishable evaluation. |
| rhel9-drift-remediation | rhel9.8 x4 | 3 | 2/3 | 1.00 | 1.03 sec | 9.3 min | Mixed outcomes: 2 of 3 runs were fully functional and publishable. |
| rhel9-ssh-hardening-jumpbox | rhel9.8; almalinux9 x2 | 2 | 1/2 | 1.00 | 0.91 sec | 4.8 min | Mixed outcomes: 1 of 2 runs were fully functional and publishable. |
| sudoers-rescue-alma9 | almalinux9 | 1 | 1/1 | 1.00 | 0.73 sec | 6.2 min | All recorded runs reached full functional, publishable evaluation. |
| systemd-broken-execstart-alma9 | almalinux9 | 1 | 1/1 | 1.00 | 0.71 sec | 7.5 min | All recorded runs reached full functional, publishable evaluation. |
| user-password-hash-migration | ubuntu16.04; ubuntu24.04 | 1 | 1/1 | 1.00 | 0.93 sec | 16.8 min | All recorded runs reached full functional, publishable evaluation. |
| bind-dnssec-alma9 | almalinux9 x4 | 1 | 0/1 | — | 1.35 sec | 12.6 min | Functional behavior appeared in 1 of 1 runs, but none reached full publishable evaluation. |
| etcd-mtls-centos-stream10 | centos-stream10 x4 | 2 | 0/2 | — | 1.46 sec | 22.3 min | Functional behavior appeared in 2 of 2 runs, but none reached full publishable evaluation. |
| haproxy-nodejs-ubuntu16 | ubuntu16.04 | 5 | 3/5 | 1.00 | 0.64 sec | 6.5 min | Mixed outcomes: 3 of 5 runs were fully functional and publishable. |
| ldap-389ds-alma9 | almalinux9 x3 | — | — | — | — | — | No recorded execution. |
| mariadb-galera-ubuntu16 | ubuntu16.04 x3 | 2 | 1/2 | 0.88 | 0.74 sec | 33.8 min | Mixed outcomes: 1 of 2 runs were fully functional and publishable. |
| mariadb-galera-ubuntu24 | ubuntu24.04 x3 | 1 | 1/1 | 0.88 | 0.95 sec | 15.6 min | All recorded runs reached full functional, publishable evaluation. |
| minio-distributed-ubuntu24 | ubuntu24.04 x4 | 1 | 1/1 | 0.75 | 1.31 sec | 22.6 min | All recorded runs reached full functional, publishable evaluation. |
| nfs-ubuntu24 | ubuntu24.04 x3 | 1 | 1/1 | 0.80 | 1.22 sec | 14.7 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-alma-alpine | almalinux9 x2; alpine x2 | 1 | 1/1 | 0.92 | 1.09 sec | 9.2 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-haproxy | ubuntu24.04 x4 | 1 | 1/1 | 1.00 | 0.97 sec | 9.3 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-rhel10-port-6700 | rhel10.0 | 1 | 1/1 | 1.00 | 0.89 sec | 7.0 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-rhel7-port-6700 | rhel7.9 | 3 | 1/3 | 0.90 | 0.72 sec | 3.1 min | Mixed outcomes: 1 of 3 runs were fully functional and publishable. |
| nginx-rhel8-port-6700 | rhel8.8 | 1 | 1/1 | 1.00 | 0.70 sec | 7.7 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-rhel9-port-6500 | rhel9.8 | 1 | 1/1 | 0.90 | 0.68 sec | 5.6 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-ubuntu24-cluster | ubuntu24.04 x3 | 5 | 3/5 | 1.00 | 1.29 sec | 4.8 min | Mixed outcomes: 3 of 5 runs were fully functional and publishable. |
| nodejs-rootless-podman-centos-stream10 | centos-stream10 | 1 | 1/1 | 1.00 | 0.92 sec | 10.9 min | All recorded runs reached full functional, publishable evaluation. |
| opentelemetry-collector-routing | ubuntu24.04 x3 | 1 | 1/1 | 0.78 | 0.82 sec | 22.2 min | All recorded runs reached full functional, publishable evaluation. |
| openwrt-guest-isolation | openwrt; ubuntu24.04 x3 | 1 | 1/1 | 1.00 | 1.16 sec | 12.7 min | All recorded runs reached full functional, publishable evaluation. |
| opnsense-three-zone | opnsense; ubuntu24.04 x3 | 5 | 5/5 | 0.78 | 3.38 sec | 15.6 min | All recorded runs reached full functional, publishable evaluation. |
| pacemaker-web-ha-alma9 | almalinux9 x3 | — | — | — | — | — | No recorded execution. |
| postgresql-ha-vyos-dual-lan | vyos; ubuntu24.04 x3 | 5 | 4/5 | 1.00 | 2.32 sec | 19.7 min | Mixed outcomes: 4 of 5 runs were fully functional and publishable. |
| postgresql-replication-alma9 | almalinux9 x3 | 1 | 1/1 | 0.80 | 1.09 sec | 14.8 min | All recorded runs reached full functional, publishable evaluation. |
| prometheus-node-exporter-ubuntu24 | ubuntu24.04 x4 | 3 | 1/3 | 1.00 | 0.95 sec | 14.6 min | Mixed outcomes: 1 of 3 runs were fully functional and publishable. |
| prometheus-thanos-objectstorage | ubuntu24.04 x4 | 6 | 1/6 | 0.75 | 1.45 sec | 25.0 min | Mixed outcomes: 1 of 6 runs were fully functional and publishable. |
| rabbitmq-quorum-ha | ubuntu24.04 x4 | — | — | — | — | — | No recorded execution. |
| rabbitmq-quorum-ubuntu24 | ubuntu24.04 x3 | — | — | — | — | — | No recorded execution. |
| redis-sentinel-ubuntu24 | ubuntu24.04 x3 | 1 | 1/1 | 0.75 | 1.11 sec | 14.5 min | All recorded runs reached full functional, publishable evaluation. |
| rhel8-offline-package-repository | rhel8.8 x2 | 1 | 1/1 | 1.00 | 0.74 sec | 15.8 min | All recorded runs reached full functional, publishable evaluation. |
| rsyslog-rhel7-rhel10-tls | rhel7.9; rhel8.8; rhel9.8; rhel10.0 | 3 | 0/3 | — | 1.05 sec | 20.7 min | Functional behavior appeared in 3 of 3 runs, but none reached full publishable evaluation. |
| samba-ad-debian13 | debian13 x4 | 2 | 0/2 | 0.64 | 1.17 sec | 21.2 min | Recorded runs did not demonstrate the required functionality. |
| sonic-frr-bgp-transit | sonic; ubuntu24.04 x2 | 2 | 1/2 | 1.00 | 1.38 sec | 17.3 min | Mixed outcomes: 1 of 2 runs were fully functional and publishable. |
| sonic-mlag-lacp | sonic x2; ubuntu24.04 x2 | — | — | — | — | — | No recorded execution. |
| ssh-auth-ubuntu24 | ubuntu24.04 x3 | 5 | 4/5 | 1.00 | 1.39 sec | 10.5 min | Mixed outcomes: 4 of 5 runs were fully functional and publishable. |
| static-route-convergence-vyos | vyos; ubuntu24.04 x2 | 1 | 1/1 | 0.75 | 1.00 sec | 13.6 min | All recorded runs reached full functional, publishable evaluation. |
| vault-postgresql-dynamic-secrets | ubuntu24.04 x2 | 1 | 0/1 | — | 0.79 sec | 47.9 min | Recorded runs did not demonstrate the required functionality. |
| vault-raft-auto-unseal | ubuntu24.04 x4 | 3 | 1/3 | 0.75 | 1.11 sec | 18.5 min | Mixed outcomes: 1 of 3 runs were fully functional and publishable. |
| vyos-dual-lan-kubernetes | vyos; ubuntu24.04 x3 | 2 | 1/2 | 1.00 | 1.14 sec | 19.0 min | Mixed outcomes: 1 of 2 runs were fully functional and publishable. |
| wireguard-vyos-dual-lan | vyos x2; ubuntu24.04 x2 | 2 | 0/2 | — | 1.22 sec | 17.7 min | Functional behavior appeared in 2 of 2 runs, but none reached full publishable evaluation. |

