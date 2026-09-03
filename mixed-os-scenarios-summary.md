# mixed-os-scenarios: command execution summary

Successful/failed executor commands per task per OS/image, from each task's latest recorded job run, split by which node(s) in that task's topology ran each image. Task names link to that run's analysis. Unlike the OS-comparison matrices, each mixed-os-scenarios task has its own bespoke topology, so most rows only populate the column(s) for the image(s) that task actually provisions; `—` means that image was not part of this task's topology.

| Task | AlmaLinux 9 | Alpine Linux | CentOS Stream 10 | Debian 13 | RHEL 10.0 | RHEL 7.9 | RHEL 8.8 | RHEL 9.8 | SONiC | Ubuntu 16.04 | Ubuntu 24.04 | VyOS | openwrt | opnsense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [bind-dnssec-alma9](jobs/mixed-os-scenarios/bind-dnssec-alma9/2026-09-02__10-00-14/analysis.md) | 199/10 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [disk-full-recovery-centos-stream10](jobs/mixed-os-scenarios/disk-full-recovery-centos-stream10/2026-09-02__10-00-14/analysis.md) | — | — | 41/3 | — | — | — | — | — | — | — | — | — | — | — |
| [etcd-mtls-centos-stream10](jobs/mixed-os-scenarios/etcd-mtls-centos-stream10/2026-09-02__10-00-14/analysis.md) | — | — | 211/55 | — | — | — | — | — | — | — | — | — | — | — |
| [haproxy-nodejs-ubuntu16](jobs/mixed-os-scenarios/haproxy-nodejs-ubuntu16/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | 54/5 | — | — | — | — |
| [kernel-network-stack-migration](jobs/mixed-os-scenarios/kernel-network-stack-migration/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | 69/5 | 58/5 | — | — | — |
| [loki-cascading-failure-ubuntu24](jobs/mixed-os-scenarios/loki-cascading-failure-ubuntu24/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 149/14 | — | — | — |
| [mariadb-galera-ubuntu16](jobs/mixed-os-scenarios/mariadb-galera-ubuntu16/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | 281/22 | — | — | — | — |
| [mariadb-galera-ubuntu24](jobs/mixed-os-scenarios/mariadb-galera-ubuntu24/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 152/7 | — | — | — |
| [mariadb-migration-ubuntu16-ubuntu24](jobs/mixed-os-scenarios/mariadb-migration-ubuntu16-ubuntu24/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | 43/6 | 62/5 | — | — | — |
| [minio-distributed-ubuntu24](jobs/mixed-os-scenarios/minio-distributed-ubuntu24/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 304/39 | — | — | — |
| [nfs-ubuntu24](jobs/mixed-os-scenarios/nfs-ubuntu24/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 159/17 | — | — | — |
| [nginx-alma-alpine](jobs/mixed-os-scenarios/nginx-alma-alpine/2026-09-02__10-00-14/analysis.md) | 50/1 | 40/24 | — | — | — | — | — | — | — | — | — | — | — | — |
| [nginx-haproxy](jobs/mixed-os-scenarios/nginx-haproxy/2026-09-02__23-57-29/analysis.md) | — | — | — | — | — | — | — | — | — | — | 0/0 | — | — | — |
| [nginx-rhel10-port-6700](jobs/mixed-os-scenarios/nginx-rhel10-port-6700/2026-09-02__10-00-14/analysis.md) | — | — | — | — | 39/7 | — | — | — | — | — | — | — | — | — |
| [nginx-rhel7-port-6700](jobs/mixed-os-scenarios/nginx-rhel7-port-6700/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | 102/9 | — | — | — | — | — | — | — | — |
| [nginx-rhel8-port-6700](jobs/mixed-os-scenarios/nginx-rhel8-port-6700/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | 43/3 | — | — | — | — | — | — | — |
| [nginx-rhel9-port-6500](jobs/mixed-os-scenarios/nginx-rhel9-port-6500/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | 46/7 | — | — | — | — | — | — |
| [nginx-tls-certificate-rotation-debian13](jobs/mixed-os-scenarios/nginx-tls-certificate-rotation-debian13/2026-09-02__10-00-14/analysis.md) | — | — | — | 97/17 | — | — | — | — | — | — | — | — | — | — |
| [nginx-ubuntu24-cluster](jobs/mixed-os-scenarios/nginx-ubuntu24-cluster/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 94/9 | — | — | — |
| [nodejs-rootless-podman-centos-stream10](jobs/mixed-os-scenarios/nodejs-rootless-podman-centos-stream10/2026-09-02__10-00-14/analysis.md) | — | — | 58/11 | — | — | — | — | — | — | — | — | — | — | — |
| [opentelemetry-collector-routing](jobs/mixed-os-scenarios/opentelemetry-collector-routing/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 206/45 | — | — | — |
| [openwrt-guest-isolation](jobs/mixed-os-scenarios/openwrt-guest-isolation/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 143/15 | — | 81/8 | — |
| [opnsense-three-zone](jobs/mixed-os-scenarios/opnsense-three-zone/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 153/16 | — | — | 79/10 |
| [postgresql-ha-vyos-dual-lan](jobs/mixed-os-scenarios/postgresql-ha-vyos-dual-lan/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 274/18 | 29/19 | — | — |
| [postgresql-replication-alma9](jobs/mixed-os-scenarios/postgresql-replication-alma9/2026-09-02__10-00-14/analysis.md) | 285/20 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [prometheus-node-exporter-ubuntu24](jobs/mixed-os-scenarios/prometheus-node-exporter-ubuntu24/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 191/8 | — | — | — |
| [prometheus-thanos-objectstorage](jobs/mixed-os-scenarios/prometheus-thanos-objectstorage/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 301/5 | — | — | — |
| [redis-sentinel-ubuntu24](jobs/mixed-os-scenarios/redis-sentinel-ubuntu24/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 233/46 | — | — | — |
| [rhel8-offline-package-repository](jobs/mixed-os-scenarios/rhel8-offline-package-repository/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | 136/17 | — | — | — | — | — | — | — |
| [rhel9-drift-remediation](jobs/mixed-os-scenarios/rhel9-drift-remediation/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | 148/15 | — | — | — | — | — | — |
| [rhel9-ssh-hardening-jumpbox](jobs/mixed-os-scenarios/rhel9-ssh-hardening-jumpbox/2026-09-02__10-00-14/analysis.md) | 71/4 | — | — | — | — | — | — | 50/2 | — | — | — | — | — | — |
| [rsyslog-rhel7-rhel10-tls](jobs/mixed-os-scenarios/rsyslog-rhel7-rhel10-tls/2026-09-02__10-00-14/analysis.md) | — | — | — | — | 108/9 | 69/9 | 78/5 | 71/5 | — | — | — | — | — | — |
| [samba-ad-debian13](jobs/mixed-os-scenarios/samba-ad-debian13/2026-09-02__10-00-14/analysis.md) | — | — | — | 294/60 | — | — | — | — | — | — | — | — | — | — |
| [sonic-frr-bgp-transit](jobs/mixed-os-scenarios/sonic-frr-bgp-transit/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | 80/27 | — | 119/6 | — | — | — |
| [ssh-auth-ubuntu24](jobs/mixed-os-scenarios/ssh-auth-ubuntu24/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 154/21 | — | — | — |
| [static-route-convergence-vyos](jobs/mixed-os-scenarios/static-route-convergence-vyos/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 120/8 | 47/12 | — | — |
| [sudoers-rescue-alma9](jobs/mixed-os-scenarios/sudoers-rescue-alma9/2026-09-02__10-00-14/analysis.md) | 32/4 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [systemd-broken-execstart-alma9](jobs/mixed-os-scenarios/systemd-broken-execstart-alma9/2026-09-02__10-00-14/analysis.md) | 58/5 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [user-password-hash-migration](jobs/mixed-os-scenarios/user-password-hash-migration/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | 39/8 | 66/6 | — | — | — |
| [vault-raft-auto-unseal](jobs/mixed-os-scenarios/vault-raft-auto-unseal/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 312/34 | — | — | — |
| [vyos-dual-lan-kubernetes](jobs/mixed-os-scenarios/vyos-dual-lan-kubernetes/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 299/155 | 45/23 | — | — |
| [wireguard-vyos-dual-lan](jobs/mixed-os-scenarios/wireguard-vyos-dual-lan/2026-09-02__10-00-14/analysis.md) | — | — | — | — | — | — | — | — | — | — | 69/4 | 84/23 | — | — |
