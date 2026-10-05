# mixed-os-scenarios: command execution summary

Scope: `5782/2026-10-02__08-42-41`.

Successful/failed executor commands per task per OS/image, from each task's latest recorded job run, split by which node(s) in that task's topology ran each image. Task names link to that run's analysis. Unlike the OS-comparison matrices, each mixed-os-scenarios task has its own bespoke topology, so most rows only populate the column(s) for the image(s) that task actually provisions; `—` means that image was not part of this task's topology.

| Task | AlmaLinux 9 | Alpine Linux | CentOS Stream 10 | Debian 13 | RHEL 10.0 | RHEL 7.9 | RHEL 8.8 | RHEL 9.8 | SONiC | Ubuntu 16.04 | Ubuntu 24.04 | VyOS | openwrt | opnsense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [almalinux9/bind-dnssec-almalinux9](../../../jobs/5782/2026-10-02__08-42-41/bind-dnssec-bash-almalinux9-5782) | 51/0 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [almalinux9/postgresql-replication-almalinux9](../../../jobs/5782/2026-10-02__08-42-41/postgresql-replication-bash-almalinux9-5782) | 59/3 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [almalinux9/sudoers-rescue-almalinux9](../../../jobs/5782/2026-10-02__08-42-41/sudoers-rescue-bash-almalinux9-5782) | 13/0 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [almalinux9/systemd-broken-execstart-almalinux9](../../../jobs/5782/2026-10-02__08-42-41/systemd-broken-execstart-bash-almalinux9-5782) | 13/0 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| [centos-stream10/disk-full-recovery-centos-stream10](../../../jobs/5782/2026-10-02__08-42-41/disk-full-recovery-bash-centos-stream10-5782) | — | — | 9/0 | — | — | — | — | — | — | — | — | — | — | — |
| [centos-stream10/etcd-mtls-centos-stream10](../../../jobs/5782/2026-10-02__08-42-41/etcd-mtls-bash-centos-stream10-5782) | — | — | 54/5 | — | — | — | — | — | — | — | — | — | — | — |
| [centos-stream10/nodejs-rootless-podman-centos-stream10](../../../jobs/5782/2026-10-02__08-42-41/nodejs-rootless-podman-bash-centos-stream10-5782) | — | — | 12/0 | — | — | — | — | — | — | — | — | — | — | — |
| [debian13/nginx-tls-certificate-rotation-debian13](../../../jobs/5782/2026-10-02__08-42-41/nginx-tls-certificate-rotation-bash-debian13-5782) | — | — | — | 21/0 | — | — | — | — | — | — | — | — | — | — |
| [debian13/samba-ad-debian13](../../../jobs/5782/2026-10-02__08-42-41/samba-ad-bash-debian13-5782) | — | — | — | 84/3 | — | — | — | — | — | — | — | — | — | — |
| [mixed/kernel-network-stack-migration-mixed](../../../jobs/5782/2026-10-02__08-42-41/kernel-network-stack-migration-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | 18/0 | 12/1 | — | — | — |
| [mixed/mariadb-migration-ubuntu16-ubuntu24-mixed](../../../jobs/5782/2026-10-02__08-42-41/mariadb-migration-ubuntu16-ubuntu24-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | 13/4 | 19/1 | — | — | — |
| [mixed/nginx-alma-alpine-mixed](../../../jobs/5782/2026-10-02__08-42-41/nginx-alma-alpine-bash-mixed-5782) | 18/0 | 16/0 | — | — | — | — | — | — | — | — | — | — | — | — |
| [mixed/openwrt-guest-isolation-mixed](../../../jobs/5782/2026-10-02__08-42-41/openwrt-guest-isolation-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 55/1 | — | 21/1 | — |
| [mixed/opnsense-three-zone-mixed](../../../jobs/5782/2026-10-02__08-42-41/opnsense-three-zone-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 52/2 | — | — | 17/0 |
| [mixed/postgresql-ha-vyos-dual-lan-mixed](../../../jobs/5782/2026-10-02__08-42-41/postgresql-ha-vyos-dual-lan-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 65/1 | 7/0 | — | — |
| [mixed/rhel9-ssh-hardening-jumpbox-mixed](../../../jobs/5782/2026-10-02__08-42-41/rhel9-ssh-hardening-jumpbox-bash-mixed-5782) | 20/0 | — | — | — | — | — | — | 12/0 | — | — | — | — | — | — |
| [mixed/rsyslog-rhel7-rhel10-tls-mixed](../../../jobs/5782/2026-10-02__08-42-41/rsyslog-rhel7-rhel10-tls-bash-mixed-5782) | — | — | — | — | 37/4 | 26/3 | 23/1 | 23/1 | — | — | — | — | — | — |
| [mixed/sonic-frr-bgp-transit-mixed](../../../jobs/5782/2026-10-02__08-42-41/sonic-frr-bgp-transit-bash-mixed-5782) | — | — | — | — | — | — | — | — | 19/1 | — | 21/0 | — | — | — |
| [mixed/static-route-convergence-vyos-mixed](../../../jobs/5782/2026-10-02__08-42-41/static-route-convergence-vyos-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 27/0 | 16/1 | — | — |
| [mixed/user-password-hash-migration-mixed](../../../jobs/5782/2026-10-02__08-42-41/user-password-hash-migration-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | 11/2 | 13/2 | — | — | — |
| [mixed/vyos-dual-lan-kubernetes-mixed](../../../jobs/5782/2026-10-02__08-42-41/vyos-dual-lan-kubernetes-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 52/5 | 9/0 | — | — |
| [mixed/wireguard-vyos-dual-lan-mixed](../../../jobs/5782/2026-10-02__08-42-41/wireguard-vyos-dual-lan-bash-mixed-5782) | — | — | — | — | — | — | — | — | — | — | 24/1 | 36/2 | — | — |
| [rhel10/nginx-rhel10-port-6700-rhel10](../../../jobs/5782/2026-10-02__08-42-41/nginx-rhel10-port-6700-bash-rhel10-5782) | — | — | — | — | 14/0 | — | — | — | — | — | — | — | — | — |
| [rhel7/nginx-rhel7-port-6700-rhel7](../../../jobs/5782/2026-10-02__08-42-41/nginx-rhel7-port-6700-bash-rhel7-5782) | — | — | — | — | — | 24/9 | — | — | — | — | — | — | — | — |
| [rhel8/nginx-rhel8-port-6700-rhel8](../../../jobs/5782/2026-10-02__08-42-41/nginx-rhel8-port-6700-bash-rhel8-5782) | — | — | — | — | — | — | 13/0 | — | — | — | — | — | — | — |
| [rhel8/rhel8-offline-package-repository-rhel8](../../../jobs/5782/2026-10-02__08-42-41/rhel8-offline-package-repository-bash-rhel8-5782) | — | — | — | — | — | — | 30/0 | — | — | — | — | — | — | — |
| [rhel9/nginx-rhel9-port-6500-rhel9](../../../jobs/5782/2026-10-02__08-42-41/nginx-rhel9-port-6500-bash-rhel9-5782) | — | — | — | — | — | — | — | 10/0 | — | — | — | — | — | — |
| [rhel9/rhel9-drift-remediation-rhel9](../../../jobs/5782/2026-10-02__08-42-41/rhel9-drift-remediation-bash-rhel9-5782) | — | — | — | — | — | — | — | 37/1 | — | — | — | — | — | — |
| [ubuntu16/haproxy-nodejs-ubuntu16](../../../jobs/5782/2026-10-02__08-42-41/haproxy-nodejs-bash-ubuntu16-5782) | — | — | — | — | — | — | — | — | — | 13/1 | — | — | — | — |
| [ubuntu16/mariadb-galera-ubuntu16](../../../jobs/5782/2026-10-02__08-42-41/mariadb-galera-bash-ubuntu16-5782) | — | — | — | — | — | — | — | — | — | 69/13 | — | — | — | — |
| [ubuntu24/loki-cascading-failure-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/loki-cascading-failure-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 40/2 | — | — | — |
| [ubuntu24/mariadb-galera-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/mariadb-galera-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 49/1 | — | — | — |
| [ubuntu24/minio-distributed-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/minio-distributed-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 80/10 | — | — | — |
| [ubuntu24/nfs-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/nfs-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 34/2 | — | — | — |
| [ubuntu24/nginx-haproxy-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/nginx-haproxy-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 39/0 | — | — | — |
| [ubuntu24/nginx-ubuntu24-cluster-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/nginx-ubuntu24-cluster-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 28/0 | — | — | — |
| [ubuntu24/opentelemetry-collector-routing-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/opentelemetry-collector-routing-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 87/8 | — | — | — |
| [ubuntu24/prometheus-node-exporter-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/prometheus-node-exporter-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 53/0 | — | — | — |
| [ubuntu24/prometheus-thanos-objectstorage-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/prometheus-thanos-objectstorage-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 74/10 | — | — | — |
| [ubuntu24/redis-sentinel-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/redis-sentinel-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 48/1 | — | — | — |
| [ubuntu24/ssh-auth-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/ssh-auth-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 50/6 | — | — | — |
| [ubuntu24/vault-raft-auto-unseal-ubuntu24](../../../jobs/5782/2026-10-02__08-42-41/vault-raft-auto-unseal-bash-ubuntu24-5782) | — | — | — | — | — | — | — | — | — | — | 73/5 | — | — | — |
