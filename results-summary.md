# Execution summary

This table summarizes the recorded jobs in `jobs/`. A **successful run** means the trial reached full evaluation coverage, passed the functional evaluation, and was publication-eligible. `Best score` is the highest per-trial reward recorded; `Mean duration` is the average trial wall-clock time. A missing job means no result has been recorded yet.

| Task | Category | Environment | Runs | Successful | Best score | Mean duration | Takeaway |
|---|---|---|---:|---:|---:|---:|---|
| disk-full-recovery-centos-stream10 | brownfield | centos-stream10 | 1 | 1/1 | 1.00 | 8.3 min | All recorded runs reached full functional, publishable evaluation. |
| kernel-network-stack-migration | brownfield | ubuntu16.04; ubuntu24.04 | 2 | 2/2 | 1.00 | 14.9 min | All recorded runs reached full functional, publishable evaluation. |
| loki-cascading-failure-ubuntu24 | brownfield | ubuntu24.04 x4 | 2 | 1/2 | 1.00 | 8.6 min | Mixed outcomes: 1 of 2 runs were fully functional and publishable. |
| mariadb-migration-ubuntu16-ubuntu24 | brownfield | ubuntu16.04; ubuntu24.04 | 8 | 2/8 | 1.00 | 3.9 min | Mixed outcomes: 2 of 8 runs were fully functional and publishable. |
| nginx-tls-certificate-rotation-debian13 | brownfield | debian13 x2 | 2 | 2/2 | 0.75 | 8.6 min | All recorded runs reached full functional, publishable evaluation. |
| rhel9-drift-remediation | brownfield | rhel9.8 x4 | 3 | 2/3 | 1.00 | 9.3 min | Mixed outcomes: 2 of 3 runs were fully functional and publishable. |
| rhel9-ssh-hardening-jumpbox | brownfield | rhel9.8; almalinux9 x2 | 2 | 1/2 | 1.00 | 4.8 min | Mixed outcomes: 1 of 2 runs were fully functional and publishable. |
| sudoers-rescue-alma9 | brownfield | almalinux9 | 1 | 1/1 | 1.00 | 6.2 min | All recorded runs reached full functional, publishable evaluation. |
| systemd-broken-execstart-alma9 | brownfield | almalinux9 | 1 | 1/1 | 1.00 | 7.5 min | All recorded runs reached full functional, publishable evaluation. |
| user-password-hash-migration | brownfield | ubuntu16.04; ubuntu24.04 | 1 | 1/1 | 1.00 | 16.8 min | All recorded runs reached full functional, publishable evaluation. |
| bind-dnssec-alma9 | greenfield | almalinux9 x4 | 1 | 0/1 | — | 12.6 min | Functional behavior appeared in 1 of 1 runs, but none reached full publishable evaluation. |
| etcd-mtls-centos-stream10 | greenfield | centos-stream10 x4 | 2 | 0/2 | — | 22.3 min | Functional behavior appeared in 2 of 2 runs, but none reached full publishable evaluation. |
| haproxy-nodejs-ubuntu16 | greenfield | ubuntu16.04 | 5 | 3/5 | 1.00 | 6.5 min | Mixed outcomes: 3 of 5 runs were fully functional and publishable. |
| ldap-389ds-alma9 | greenfield | almalinux9 x3 | — | — | — | — | No recorded execution. |
| mariadb-galera-ubuntu16 | greenfield | ubuntu16.04 x3 | 2 | 1/2 | 0.88 | 33.8 min | Mixed outcomes: 1 of 2 runs were fully functional and publishable. |
| mariadb-galera-ubuntu24 | greenfield | ubuntu24.04 x3 | 1 | 1/1 | 0.88 | 15.6 min | All recorded runs reached full functional, publishable evaluation. |
| minio-distributed-ubuntu24 | greenfield | ubuntu24.04 x4 | 1 | 1/1 | 0.75 | 22.6 min | All recorded runs reached full functional, publishable evaluation. |
| nfs-ubuntu24 | greenfield | ubuntu24.04 x3 | 1 | 1/1 | 0.80 | 14.7 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-alma-alpine | greenfield | almalinux9 x2; alpine x2 | 1 | 1/1 | 0.92 | 9.2 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-haproxy | greenfield | ubuntu24.04 x4 | 1 | 1/1 | 1.00 | 9.3 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-rhel10-port-6700 | greenfield | rhel10.0 | 1 | 1/1 | 1.00 | 7.0 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-rhel7-port-6700 | greenfield | rhel7.9 | 3 | 1/3 | 0.90 | 3.1 min | Mixed outcomes: 1 of 3 runs were fully functional and publishable. |
| nginx-rhel8-port-6700 | greenfield | rhel8.8 | 1 | 1/1 | 1.00 | 7.7 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-rhel9-port-6500 | greenfield | rhel9.8 | 1 | 1/1 | 0.90 | 5.6 min | All recorded runs reached full functional, publishable evaluation. |
| nginx-ubuntu24-cluster | greenfield | ubuntu24.04 x3 | 5 | 3/5 | 1.00 | 4.8 min | Mixed outcomes: 3 of 5 runs were fully functional and publishable. |
| nodejs-rootless-podman-centos-stream10 | greenfield | centos-stream10 | 1 | 1/1 | 1.00 | 10.9 min | All recorded runs reached full functional, publishable evaluation. |
| opentelemetry-collector-routing | greenfield | ubuntu24.04 x3 | 1 | 1/1 | 0.78 | 22.2 min | All recorded runs reached full functional, publishable evaluation. |
| openwrt-guest-isolation | greenfield | openwrt; ubuntu24.04 x3 | 1 | 1/1 | 1.00 | 12.7 min | All recorded runs reached full functional, publishable evaluation. |
| opnsense-three-zone | greenfield | opnsense; ubuntu24.04 x3 | 5 | 5/5 | 0.78 | 15.6 min | All recorded runs reached full functional, publishable evaluation. |
| pacemaker-web-ha-alma9 | greenfield | almalinux9 x3 | — | — | — | — | No recorded execution. |
| postgresql-ha-vyos-dual-lan | greenfield | vyos; ubuntu24.04 x3 | 5 | 4/5 | 1.00 | 19.7 min | Mixed outcomes: 4 of 5 runs were fully functional and publishable. |
| postgresql-replication-alma9 | greenfield | almalinux9 x3 | 1 | 1/1 | 0.80 | 14.8 min | All recorded runs reached full functional, publishable evaluation. |
| prometheus-node-exporter-ubuntu24 | greenfield | ubuntu24.04 x4 | 3 | 1/3 | 1.00 | 14.6 min | Mixed outcomes: 1 of 3 runs were fully functional and publishable. |
| prometheus-thanos-objectstorage | greenfield | ubuntu24.04 x4 | 6 | 1/6 | 0.75 | 25.0 min | Mixed outcomes: 1 of 6 runs were fully functional and publishable. |
| rabbitmq-quorum-ha | greenfield | ubuntu24.04 x4 | — | — | — | — | No recorded execution. |
| rabbitmq-quorum-ubuntu24 | greenfield | ubuntu24.04 x3 | — | — | — | — | No recorded execution. |
| redis-sentinel-ubuntu24 | greenfield | ubuntu24.04 x3 | 1 | 1/1 | 0.75 | 14.5 min | All recorded runs reached full functional, publishable evaluation. |
| rhel8-offline-package-repository | greenfield | rhel8.8 x2 | 1 | 1/1 | 1.00 | 15.8 min | All recorded runs reached full functional, publishable evaluation. |
| rsyslog-rhel7-rhel10-tls | greenfield | rhel7.9; rhel8.8; rhel9.8; rhel10.0 | 3 | 0/3 | — | 20.7 min | Functional behavior appeared in 3 of 3 runs, but none reached full publishable evaluation. |
| samba-ad-debian13 | greenfield | debian13 x4 | 2 | 0/2 | 0.64 | 21.2 min | Recorded runs did not demonstrate the required functionality. |
| sonic-frr-bgp-transit | greenfield | sonic; ubuntu24.04 x2 | 2 | 1/2 | 1.00 | 17.3 min | Mixed outcomes: 1 of 2 runs were fully functional and publishable. |
| sonic-mlag-lacp | greenfield | sonic x2; ubuntu24.04 x2 | — | — | — | — | No recorded execution. |
| ssh-auth-ubuntu24 | greenfield | ubuntu24.04 x3 | 5 | 4/5 | 1.00 | 10.5 min | Mixed outcomes: 4 of 5 runs were fully functional and publishable. |
| static-route-convergence-vyos | greenfield | vyos; ubuntu24.04 x2 | 1 | 1/1 | 0.75 | 13.6 min | All recorded runs reached full functional, publishable evaluation. |
| vault-postgresql-dynamic-secrets | greenfield | ubuntu24.04 x2 | 1 | 0/1 | — | 47.9 min | Recorded runs did not demonstrate the required functionality. |
| vault-raft-auto-unseal | greenfield | ubuntu24.04 x4 | 3 | 1/3 | 0.75 | 18.5 min | Mixed outcomes: 1 of 3 runs were fully functional and publishable. |
| vyos-dual-lan-kubernetes | greenfield | vyos; ubuntu24.04 x3 | 2 | 1/2 | 1.00 | 19.0 min | Mixed outcomes: 1 of 2 runs were fully functional and publishable. |
| wireguard-vyos-dual-lan | greenfield | vyos x2; ubuntu24.04 x2 | 2 | 0/2 | — | 17.7 min | Functional behavior appeared in 2 of 2 runs, but none reached full publishable evaluation. |

