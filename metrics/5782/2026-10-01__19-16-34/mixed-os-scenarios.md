# mixed-os-scenarios: command execution summary

Scope: `5782/2026-10-01__19-16-34`.

Successful/failed executor commands per task per OS/image, from each task's latest recorded job run, split by which node(s) in that task's topology ran each image. Task names link to that run's analysis. Unlike the OS-comparison matrices, each mixed-os-scenarios task has its own bespoke topology, so most rows only populate the column(s) for the image(s) that task actually provisions; `—` means that image was not part of this task's topology.

| Task | AlmaLinux 9 | Alpine Linux | CentOS Stream 10 | Debian 13 | RHEL 10.0 | RHEL 7.9 | RHEL 8.8 | RHEL 9.8 | SONiC | Ubuntu 16.04 | Ubuntu 24.04 | VyOS | openwrt | opnsense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [almalinux9/bind-dnssec-almalinux9](../../../jobs/5782/2026-10-01__19-16-34/bind-dnssec-bash-almalinux9-5782) | 53/0 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [almalinux9/postgresql-replication-almalinux9](../../../jobs/5782/2026-10-01__19-16-34/postgresql-replication-bash-almalinux9-5782) | 39/20 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [almalinux9/sudoers-rescue-almalinux9](../../../jobs/5782/2026-10-01__19-16-34/sudoers-rescue-bash-almalinux9-5782) | 9/2 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [almalinux9/systemd-broken-execstart-almalinux9](../../../jobs/5782/2026-10-01__19-16-34/systemd-broken-execstart-bash-almalinux9-5782) | 12/0 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [centos-stream10/disk-full-recovery-centos-stream10](../../../jobs/5782/2026-10-01__19-16-34/disk-full-recovery-bash-centos-stream10-5782) | — | — | 11/0 | — | — | — | — | — | — | — | — | — | — | — |
| [centos-stream10/etcd-mtls-centos-stream10](../../../jobs/5782/2026-10-01__19-16-34/etcd-mtls-bash-centos-stream10-5782) | — | — | 54/0 | — | — | — | — | — | — | — | — | — | — | — |
| [centos-stream10/nodejs-rootless-podman-centos-stream10](../../../jobs/5782/2026-10-01__19-16-34/nodejs-rootless-podman-bash-centos-stream10-5782) | — | — | 14/0 | — | — | — | — | — | — | — | — | — | — | — |
| [debian13/nginx-tls-certificate-rotation-debian13](../../../jobs/5782/2026-10-01__19-16-34/nginx-tls-certificate-rotation-bash-debian13-5782) | — | — | — | 24/0 | — | — | — | — | — | — | — | — | — | — |
| [debian13/samba-ad-debian13](../../../jobs/5782/2026-10-01__19-16-34/samba-ad-bash-debian13-5782) | — | — | — | 83/3 | — | — | — | — | — | — | — | — | — | — |
| [mixed/kernel-network-stack-migration-mixed](../../../jobs/5782/2026-10-01__19-16-34/kernel-network-stack-migration-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | 14/1 | 12/0 | — | — | — |
| [mixed/mariadb-migration-ubuntu16-ubuntu24-mixed](../../../jobs/5782/2026-10-01__19-16-34/mariadb-migration-ubuntu16-ubuntu24-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | 12/3 | 22/1 | — | — | — |
| [mixed/nginx-alma-alpine-mixed](../../../jobs/5782/2026-10-01__19-16-34/nginx-alma-alpine-bash-mixed-5782) | 22/4 | 19/0 | — | — | — | — | — | — | — | — | — | — | — | — |
| [mixed/openwrt-guest-isolation-mixed](../../../jobs/5782/2026-10-01__19-16-34/openwrt-guest-isolation-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 50/1 | — | 18/0 | — |
| [mixed/opnsense-three-zone-mixed](../../../jobs/5782/2026-10-01__19-16-34/opnsense-three-zone-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 50/1 | — | — | 29/0 |
| [mixed/postgresql-ha-vyos-dual-lan-mixed](../../../jobs/5782/2026-10-01__19-16-34/postgresql-ha-vyos-dual-lan-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 79/8 | 14/1 | — | — |
| [mixed/rhel9-ssh-hardening-jumpbox-mixed](../../../jobs/5782/2026-10-01__19-16-34/rhel9-ssh-hardening-jumpbox-bash-mixed-5782) | 20/2 | — | — | — | — | — | — | 12/1 | — | — | — | — | — | — |
| [mixed/rsyslog-rhel7-rhel10-tls-mixed](../../../jobs/5782/2026-10-01__19-16-34/rsyslog-rhel7-rhel10-tls-bash-mixed-5782) | — | — | — | — | 31/3 | 20/2 | 21/2 | 20/2 | — | — | — | — | — | — |
| [mixed/sonic-frr-bgp-transit-mixed](../../../jobs/5782/2026-10-01__19-16-34/sonic-frr-bgp-transit-bash-mixed-5782) | — | — | — | — | — | — | — | — | 23/1 | — | 33/0 | — | — | — |
| [mixed/static-route-convergence-vyos-mixed](../../../jobs/5782/2026-10-01__19-16-34/static-route-convergence-vyos-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 26/0 | 12/1 | — | — |
| [mixed/user-password-hash-migration-mixed](../../../jobs/5782/2026-10-01__19-16-34/user-password-hash-migration-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | 0/0 | 0/0 | — | — | — |
| [mixed/vyos-dual-lan-kubernetes-mixed](../../../jobs/5782/2026-10-01__19-16-34/vyos-dual-lan-kubernetes-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 71/1 | 9/0 | — | — |
| [mixed/wireguard-vyos-dual-lan-mixed](../../../jobs/5782/2026-10-01__19-16-34/wireguard-vyos-dual-lan-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 28/1 | 23/0 | — | — |
| [rhel10/nginx-rhel10-port-6700-rhel10](../../../jobs/5782/2026-10-01__19-16-34/nginx-rhel10-port-6700-bash-rhel10-5782) | — | — | — | — | 13/0 | — | — | — | — | — | — | — | — | — |
| [rhel7/nginx-rhel7-port-6700-rhel7](../../../jobs/5782/2026-10-01__19-16-34/nginx-rhel7-port-6700-bash-rhel7-5782) | — | — | — | — | — | 25/3 | — | — | — | — | — | — | — | — |
| [rhel8/nginx-rhel8-port-6700-rhel8](../../../jobs/5782/2026-10-01__19-16-34/nginx-rhel8-port-6700-bash-rhel8-5782) | — | — | — | — | — | — | 11/0 | — | — | — | — | — | — | — |
| [rhel8/rhel8-offline-package-repository-rhel8](../../../jobs/5782/2026-10-01__19-16-34/rhel8-offline-package-repository-bash-rhel8-5782) | — | — | — | — | — | — | 23/0 | — | — | — | — | — | — | — |
| [rhel9/nginx-rhel9-port-6500-rhel9](../../../jobs/5782/2026-10-01__19-16-34/nginx-rhel9-port-6500-bash-rhel9-5782) | — | — | — | — | — | — | — | 10/0 | — | — | — | — | — | — |
| [rhel9/rhel9-drift-remediation-rhel9](../../../jobs/5782/2026-10-01__19-16-34/rhel9-drift-remediation-bash-rhel9-5782) | — | — | — | — | — | — | — | 54/2 | — | — | — | — | — | — |
| [ubuntu16/haproxy-nodejs-ubuntu16](../../../jobs/5782/2026-10-01__19-16-34/haproxy-nodejs-bash-ubuntu16-5782) | — | — | — | — | — | — | — | — | — | 10/1 | — | — | — | — |
| [ubuntu16/mariadb-galera-ubuntu16](../../../jobs/5782/2026-10-01__19-16-34/mariadb-galera-bash-ubuntu16-5782) | — | — | — | — | — | — | — | — | — | 73/10 | — | — | — | — |
| [ubuntu24/loki-cascading-failure-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/loki-cascading-failure-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 39/1 | — | — | — |
| [ubuntu24/mariadb-galera-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/mariadb-galera-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 53/1 | — | — | — |
| [ubuntu24/minio-distributed-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/minio-distributed-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 154/11 | — | — | — |
| [ubuntu24/nfs-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/nfs-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 40/1 | — | — | — |
| [ubuntu24/nginx-haproxy-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/nginx-haproxy-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 56/0 | — | — | — |
| [ubuntu24/nginx-ubuntu24-cluster-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/nginx-ubuntu24-cluster-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 21/0 | — | — | — |
| [ubuntu24/opentelemetry-collector-routing-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/opentelemetry-collector-routing-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 61/10 | — | — | — |
| [ubuntu24/prometheus-node-exporter-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/prometheus-node-exporter-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 53/0 | — | — | — |
| [ubuntu24/prometheus-thanos-objectstorage-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/prometheus-thanos-objectstorage-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 77/3 | — | — | — |
| [ubuntu24/redis-sentinel-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/redis-sentinel-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 69/5 | — | — | — |
| [ubuntu24/ssh-auth-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/ssh-auth-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 46/6 | — | — | — |
| [ubuntu24/vault-raft-auto-unseal-ubuntu24](../../../jobs/5782/2026-10-01__19-16-34/vault-raft-auto-unseal-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 82/4 | — | — | — |
