# mixed-os-scenarios: command execution summary

Scope: `trentina/aggregate`.

Successful/failed executor commands per task per OS/image, from each task's latest recorded job run, split by which node(s) in that task's topology ran each image. Task names link to that run's analysis. Unlike the OS-comparison matrices, each mixed-os-scenarios task has its own bespoke topology, so most rows only populate the column(s) for the image(s) that task actually provisions; `—` means that image was not part of this task's topology.

| Task | AlmaLinux 9 | Alpine Linux | CentOS Stream 10 | Debian 13 | RHEL 10.0 | RHEL 7.9 | RHEL 8.8 | RHEL 9.8 | SONiC | Ubuntu 16.04 | Ubuntu 24.04 | VyOS | openwrt | opnsense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [brownfield/disk-full-recovery-centos-stream10](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/brownfield/disk-full-recovery-centos-stream10/analysis.md) | — | — | 11/0 | — | — | — | — | — | — | — | — | — | — | — |
| [brownfield/kernel-network-stack-migration](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/brownfield/kernel-network-stack-migration/analysis.md) | — | — | — | — | — | — | — | — | — | 20/5 | 18/4 | — | — | — |
| [brownfield/loki-cascading-failure-ubuntu24](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/brownfield/loki-cascading-failure-ubuntu24/analysis.md) | — | — | — | — | — | — | — | — | — | — | 23/2 | — | — | — |
| [brownfield/mariadb-migration-ubuntu16-ubuntu24](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/brownfield/mariadb-migration-ubuntu16-ubuntu24/analysis.md) | — | — | — | — | — | — | — | — | — | 14/2 | 12/3 | — | — | — |
| [brownfield/nginx-tls-certificate-rotation-debian13](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/brownfield/nginx-tls-certificate-rotation-debian13/analysis.md) | — | — | — | 15/0 | — | — | — | — | — | — | — | — | — | — |
| [brownfield/rhel9-drift-remediation](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/brownfield/rhel9-drift-remediation/analysis.md) | — | — | — | — | — | — | — | 38/2 | — | — | — | — | — | — |
| [brownfield/rhel9-ssh-hardening-jumpbox](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/brownfield/rhel9-ssh-hardening-jumpbox/analysis.md) | 19/1 | — | — | — | — | — | — | 16/0 | — | — | — | — | — | — |
| [brownfield/sudoers-rescue-alma9](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/brownfield/sudoers-rescue-alma9/analysis.md) | 11/0 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [brownfield/systemd-broken-execstart-alma9](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/brownfield/systemd-broken-execstart-alma9/analysis.md) | 10/0 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [brownfield/user-password-hash-migration](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/brownfield/user-password-hash-migration/analysis.md) | — | — | — | — | — | — | — | — | — | 12/3 | 14/0 | — | — | — |
| [greenfield/bind-dnssec-alma9](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/bind-dnssec-alma9/analysis.md) | 50/0 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [greenfield/etcd-mtls-centos-stream10](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/etcd-mtls-centos-stream10/analysis.md) | — | — | 61/3 | — | — | — | — | — | — | — | — | — | — | — |
| [greenfield/haproxy-nodejs-ubuntu16](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/haproxy-nodejs-ubuntu16/analysis.md) | — | — | — | — | — | — | — | — | — | 16/1 | — | — | — | — |
| [greenfield/mariadb-galera-ubuntu16](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/mariadb-galera-ubuntu16/analysis.md) | — | — | — | — | — | — | — | — | — | 205/23 | — | — | — | — |
| [greenfield/mariadb-galera-ubuntu24](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/mariadb-galera-ubuntu24/analysis.md) | — | — | — | — | — | — | — | — | — | — | 53/1 | — | — | — |
| [greenfield/minio-distributed-ubuntu24](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/minio-distributed-ubuntu24/analysis.md) | — | — | — | — | — | — | — | — | — | — | 81/5 | — | — | — |
| [greenfield/nfs-ubuntu24](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/nfs-ubuntu24/analysis.md) | — | — | — | — | — | — | — | — | — | — | 42/5 | — | — | — |
| [greenfield/nginx-alma-alpine](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/nginx-alma-alpine/analysis.md) | 34/4 | 23/1 | — | — | — | — | — | — | — | — | — | — | — | — |
| [greenfield/nginx-haproxy](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/nginx-haproxy/analysis.md) | — | — | — | — | — | — | — | — | — | — | 34/5 | — | — | — |
| [greenfield/nginx-rhel10-port-6700](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/nginx-rhel10-port-6700/analysis.md) | — | — | — | — | 12/0 | — | — | — | — | — | — | — | — | — |
| [greenfield/nginx-rhel7-port-6700](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/nginx-rhel7-port-6700/analysis.md) | — | — | — | — | — | 23/5 | — | — | — | — | — | — | — | — |
| [greenfield/nginx-rhel8-port-6700](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/nginx-rhel8-port-6700/analysis.md) | — | — | — | — | — | — | 12/0 | — | — | — | — | — | — | — |
| [greenfield/nginx-rhel9-port-6500](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/nginx-rhel9-port-6500/analysis.md) | — | — | — | — | — | — | — | 12/0 | — | — | — | — | — | — |
| [greenfield/nginx-ubuntu24-cluster](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/nginx-ubuntu24-cluster/analysis.md) | — | — | — | — | — | — | — | — | — | — | 18/3 | — | — | — |
| [greenfield/nodejs-rootless-podman-centos-stream10](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/nodejs-rootless-podman-centos-stream10/analysis.md) | — | — | 13/1 | — | — | — | — | — | — | — | — | — | — | — |
| [greenfield/opentelemetry-collector-routing](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/opentelemetry-collector-routing/analysis.md) | — | — | — | — | — | — | — | — | — | — | 51/2 | — | — | — |
| [greenfield/openwrt-guest-isolation](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/openwrt-guest-isolation/analysis.md) | — | — | — | — | — | — | — | — | — | — | 37/11 | — | 28/1 | — |
| [greenfield/opnsense-three-zone](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/opnsense-three-zone/analysis.md) | — | — | — | — | — | — | — | — | — | — | 43/7 | — | — | 31/4 |
| [greenfield/postgresql-ha-vyos-dual-lan](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/postgresql-ha-vyos-dual-lan/analysis.md) | — | — | — | — | — | — | — | — | — | — | 97/5 | 14/1 | — | — |
| [greenfield/postgresql-replication-alma9](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/postgresql-replication-alma9/analysis.md) | 57/9 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [greenfield/prometheus-node-exporter-ubuntu24](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/prometheus-node-exporter-ubuntu24/analysis.md) | — | — | — | — | — | — | — | — | — | — | 41/3 | — | — | — |
| [greenfield/prometheus-thanos-objectstorage](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/prometheus-thanos-objectstorage/analysis.md) | — | — | — | — | — | — | — | — | — | — | 111/5 | — | — | — |
| [greenfield/redis-sentinel-ubuntu24](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/redis-sentinel-ubuntu24/analysis.md) | — | — | — | — | — | — | — | — | — | — | 70/7 | — | — | — |
| [greenfield/rhel8-offline-package-repository](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/rhel8-offline-package-repository/analysis.md) | — | — | — | — | — | — | 36/1 | — | — | — | — | — | — | — |
| [greenfield/rsyslog-rhel7-rhel10-tls](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/rsyslog-rhel7-rhel10-tls/analysis.md) | — | — | — | — | 35/4 | 20/5 | 21/2 | 22/1 | — | — | — | — | — | — |
| [greenfield/samba-ad-debian13](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/samba-ad-debian13/analysis.md) | — | — | — | 67/2 | — | — | — | — | — | — | — | — | — | — |
| [greenfield/sonic-frr-bgp-transit](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/sonic-frr-bgp-transit/analysis.md) | — | — | — | — | — | — | — | — | 34/6 | — | 42/4 | — | — | — |
| [greenfield/ssh-auth-ubuntu24](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/ssh-auth-ubuntu24/analysis.md) | — | — | — | — | — | — | — | — | — | — | 63/3 | — | — | — |
| [greenfield/static-route-convergence-vyos](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/static-route-convergence-vyos/analysis.md) | — | — | — | — | — | — | — | — | — | — | 57/7 | 19/6 | — | — |
| [greenfield/vault-raft-auto-unseal](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/vault-raft-auto-unseal/analysis.md) | — | — | — | — | — | — | — | — | — | — | 112/11 | — | — | — |
| [greenfield/vyos-dual-lan-kubernetes](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/vyos-dual-lan-kubernetes/analysis.md) | — | — | — | — | — | — | — | — | — | — | 74/5 | 9/1 | — | — |
| [greenfield/wireguard-vyos-dual-lan](../../../jobs/trentina/mixed-os-scenarios/2026-09-27__21-43-06/greenfield/wireguard-vyos-dual-lan/analysis.md) | — | — | — | — | — | — | — | — | — | — | 27/7 | 44/3 | — | — |
