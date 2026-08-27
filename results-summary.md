# Execution summary

This table summarizes the recorded jobs in `jobs/`. `Full passes` counts trials with complete evaluation coverage and successful functional behavior. `Evaluation coverage` and `Operational hygiene` are per-trial averages. `Best score` is the highest per-trial reward; `Provisioning time` and `Mean duration` are averages across recorded trials.

`Operational hygiene` measures whether the evaluator found executor-created residue, abandoned files, conflicting services, unsafe exposure, or other unwanted changes. `100%` means all applicable hygiene checks passed; `0%` means none passed.

| Task | Environment | Runs | Full passes | Best score | Evaluation coverage | Operational hygiene | Provisioning time | Mean duration |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| disk-full-recovery-centos-stream10 | — | 1 | 1/1 | 1.00 | 100% | 100% | 0.97 sec | 8.3 min |
| kernel-network-stack-migration | — | 2 | 2/2 | 1.00 | 100% | 100% | 0.77 sec | 14.9 min |
| loki-cascading-failure-ubuntu24 | — | 2 | 1/2 | 1.00 | 100% | 100% | 1.05 sec | 8.6 min |
| mariadb-migration-ubuntu16-ubuntu24 | — | 1 | 1/1 | 1.00 | 100% | 100% | 1.01 sec | 15.8 min |
| nginx-tls-certificate-rotation-debian13 | — | 2 | 2/2 | 0.75 | 100% | 0% | 0.75 sec | 8.6 min |
| rhel9-drift-remediation | — | 3 | 2/3 | 1.00 | 100% | 50% | 1.03 sec | 9.3 min |
| rhel9-ssh-hardening-jumpbox | — | 2 | 1/2 | 1.00 | 100% | 100% | 0.91 sec | 4.8 min |
| sudoers-rescue-alma9 | — | 1 | 1/1 | 1.00 | 100% | 100% | 0.73 sec | 6.2 min |
| systemd-broken-execstart-alma9 | — | 1 | 1/1 | 1.00 | 100% | 100% | 0.71 sec | 7.5 min |
| user-password-hash-migration | — | 1 | 1/1 | 1.00 | 100% | 100% | 0.93 sec | 16.8 min |
| bind-dnssec-alma9 | — | 1 | 0/1 | — | 57% | 100% | 1.35 sec | 12.6 min |
| etcd-mtls-centos-stream10 | — | 2 | 0/2 | — | 50% | 100% | 1.46 sec | 22.3 min |
| haproxy-nodejs-ubuntu16 | — | 5 | 3/5 | 1.00 | 92% | 40% | 0.64 sec | 6.5 min |
| mariadb-galera-ubuntu16 | — | 2 | 1/2 | 0.88 | 80% | 0% | 0.74 sec | 33.8 min |
| mariadb-galera-ubuntu24 | — | 1 | 1/1 | 0.88 | 100% | 0% | 1.12 sec | 14.2 min |
| minio-distributed-ubuntu24 | — | 1 | 1/1 | 0.75 | 100% | 0% | 1.31 sec | 22.6 min |
| nfs-ubuntu24 | — | 1 | 1/1 | 0.80 | 100% | 0% | 1.22 sec | 14.7 min |
| nginx-alma-alpine | — | 1 | 1/1 | 0.92 | 100% | 0% | 1.09 sec | 9.2 min |
| nginx-haproxy | — | 1 | 1/1 | 1.00 | 100% | 100% | 0.97 sec | 9.3 min |
| nginx-rhel10-port-6700 | — | 1 | 1/1 | 1.00 | 100% | 100% | 0.89 sec | 7.0 min |
| nginx-rhel7-port-6700 | — | 3 | 1/3 | 0.90 | 100% | 0% | 0.72 sec | 3.1 min |
| nginx-rhel8-port-6700 | — | 1 | 1/1 | 1.00 | 100% | 100% | 0.70 sec | 7.7 min |
| nginx-rhel9-port-6500 | — | 1 | 1/1 | 0.90 | 100% | 0% | 0.68 sec | 5.6 min |
| nginx-ubuntu24-cluster | — | 5 | 3/5 | 1.00 | 90% | 100% | 1.29 sec | 4.8 min |
| nodejs-rootless-podman-centos-stream10 | — | 1 | 1/1 | 1.00 | 100% | 100% | 0.92 sec | 10.9 min |
| opentelemetry-collector-routing | — | 1 | 1/1 | 0.78 | 100% | 0% | 0.82 sec | 22.2 min |
| openwrt-guest-isolation | — | 1 | 1/1 | 1.00 | 100% | 100% | 1.16 sec | 12.7 min |
| opnsense-three-zone | — | 5 | 5/5 | 0.78 | 100% | 0% | 3.38 sec | 15.6 min |
| postgresql-ha-vyos-dual-lan | — | 5 | 4/5 | 1.00 | 89% | 75% | 2.32 sec | 19.7 min |
| postgresql-replication-alma9 | — | 1 | 1/1 | 0.80 | 100% | 0% | 1.09 sec | 14.8 min |
| prometheus-node-exporter-ubuntu24 | — | 3 | 1/3 | 1.00 | 77% | 50% | 0.95 sec | 14.6 min |
| prometheus-thanos-objectstorage | — | 6 | 1/6 | 0.75 | 68% | 0% | 1.45 sec | 25.0 min |
| redis-sentinel-ubuntu24 | — | 1 | 1/1 | 0.75 | 100% | 0% | 1.11 sec | 14.5 min |
| rhel8-offline-package-repository | — | 1 | 1/1 | 1.00 | 100% | — | 0.74 sec | 15.8 min |
| rsyslog-rhel7-rhel10-tls | — | 3 | 0/3 | — | 52% | 0% | 1.05 sec | 20.7 min |
| samba-ad-debian13 | — | 2 | 0/2 | 0.64 | 75% | 0% | 1.17 sec | 21.2 min |
| sonic-frr-bgp-transit | — | 2 | 1/2 | 1.00 | 100% | 100% | 1.38 sec | 17.3 min |
| ssh-auth-ubuntu24 | — | 5 | 4/5 | 1.00 | 90% | 25% | 1.39 sec | 10.5 min |
| static-route-convergence-vyos | — | 1 | 1/1 | 0.75 | 100% | 0% | 1.00 sec | 13.6 min |
| vault-raft-auto-unseal | — | 3 | 1/3 | 0.75 | 50% | 0% | 1.11 sec | 18.5 min |
| vyos-dual-lan-kubernetes | — | 2 | 1/2 | 1.00 | 100% | 100% | 1.14 sec | 19.0 min |
| wireguard-vyos-dual-lan | — | 2 | 0/2 | — | 71% | 0% | 1.22 sec | 17.7 min |

