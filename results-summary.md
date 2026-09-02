# InfraSet: An Open Dataset of LLM-Executed Infrastructure Tasks

The industry is increasingly using LLMs to operate infrastructure, either directly or with a human in the loop.
Yet there is little public empirical data showing what happens when LLMs operate real systems, whether in
greenfield, brownfield, end-of-life, or distributed environments. Perhaps LLMs perform remarkably well. Perhaps
they fail in subtle ways. We do not yet have enough evidence to know either way.

InfraSet is a dataset of executed infrastructure tasks and traces, created to build that evidence. It currently
contains 42 tasks, and we hope the community will join us and help expand it. Results can also be explored on
[the InfraSet dataset on Hugging Face](https://huggingface.co/datasets/infraset/infraset).

## Execution summary

This table summarizes the recorded [jobs](https://github.com/open-sudo/infraset/tree/main/jobs). Metrics and times are averages across recorded trials. `Commands` reports successful/failed executor commands read directly from the provider-captured audit. Unfinished or indeterminate command records are excluded from both values. `0/0 (none issued)` means an audit was captured but contains no command request; `audit unavailable` means no canonical or per-attempt audit artifact exists. A failed command records an unsuccessful attempt; it does not by itself mean that the final task outcome failed.

`Reward` measures the supported outcome. `Operational hygiene` measures unnecessary mutations during execution, attributable residue, and unrelated regression. A hygiene score of `1.000` means the verifier found none of these problems; `0.000` means the execution received no hygiene credit.

The current dataset contains 42 tasks and 7938 completed executor commands: 6984 successful and 954 failed.

| Task | Environment | Commands | Reward | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| [bind-dnssec-alma9](https://github.com/open-sudo/infraset/blob/main/jobs/bind-dnssec-alma9/2026-09-02__10-00-14/analysis.md) | 4 almalinux9 | 199/10 | 1.000 | 1.000 | 1.000 | 0.990 | 1.33s | 9m 05s |
| [disk-full-recovery-centos-stream10](https://github.com/open-sudo/infraset/blob/main/jobs/disk-full-recovery-centos-stream10/2026-09-02__10-00-14/analysis.md) | centos-stream10 | 41/3 | 1.000 | 1.000 | 1.000 | 1.000 | 1.00s | 2m 21s |
| [etcd-mtls-centos-stream10](https://github.com/open-sudo/infraset/blob/main/jobs/etcd-mtls-centos-stream10/2026-09-02__10-00-14/analysis.md) | 4 centos-stream10 | 211/55 | 1.000 | 1.000 | 1.000 | 0.877 | 1.45s | 12m 28s |
| [haproxy-nodejs-ubuntu16](https://github.com/open-sudo/infraset/blob/main/jobs/haproxy-nodejs-ubuntu16/2026-09-02__10-00-14/analysis.md) | ubuntu16.04 | 54/5 | 1.000 | 1.000 | 1.000 | 0.973 | 0.69s | 3m 02s |
| [kernel-network-stack-migration](https://github.com/open-sudo/infraset/blob/main/jobs/kernel-network-stack-migration/2026-09-02__10-00-14/analysis.md) | ubuntu16.04 + ubuntu24.04 | 127/10 | 1.000 | 1.000 | 1.000 | 0.993 | 0.81s | 10m 04s |
| [loki-cascading-failure-ubuntu24](https://github.com/open-sudo/infraset/blob/main/jobs/loki-cascading-failure-ubuntu24/2026-09-02__10-00-14/analysis.md) | 4 ubuntu24.04 | 149/14 | 0.972 | 1.000 | 0.972 | 0.993 | 1.03s | 6m 33s |
| [mariadb-galera-ubuntu16](https://github.com/open-sudo/infraset/blob/main/jobs/mariadb-galera-ubuntu16/2026-09-02__10-00-14/analysis.md) | 3 ubuntu16.04 | 281/22 | 1.000 | 1.000 | 1.000 | 0.840 | 0.93s | 11m 37s |
| [mariadb-galera-ubuntu24](https://github.com/open-sudo/infraset/blob/main/jobs/mariadb-galera-ubuntu24/2026-09-02__10-00-14/analysis.md) | 3 ubuntu24.04 | 152/7 | 1.000 | 1.000 | 1.000 | 0.970 | 0.99s | 7m 26s |
| [mariadb-migration-ubuntu16-ubuntu24](https://github.com/open-sudo/infraset/blob/main/jobs/mariadb-migration-ubuntu16-ubuntu24/2026-09-02__10-00-14/analysis.md) | ubuntu16.04 + ubuntu24.04 | 105/11 | 1.000 | 1.000 | 1.000 | 0.983 | 1.02s | 10m 09s |
| [minio-distributed-ubuntu24](https://github.com/open-sudo/infraset/blob/main/jobs/minio-distributed-ubuntu24/2026-09-02__10-00-14/analysis.md) | 4 ubuntu24.04 | 304/39 | 1.000 | 1.000 | 1.000 | 0.877 | 1.02s | 13m 03s |
| [nfs-ubuntu24](https://github.com/open-sudo/infraset/blob/main/jobs/nfs-ubuntu24/2026-09-02__10-00-14/analysis.md) | 3 ubuntu24.04 | 159/17 | 1.000 | 1.000 | 1.000 | 0.990 | 0.98s | 6m 00s |
| [nginx-alma-alpine](https://github.com/open-sudo/infraset/blob/main/jobs/nginx-alma-alpine/2026-09-02__10-00-14/analysis.md) | 2 almalinux9 + 2 alpine | 90/25 | 0.667 | 0.667 | 0.667 | 0.893 | 1.36s | 20m 48s |
| [nginx-haproxy](https://github.com/open-sudo/infraset/blob/main/jobs/nginx-haproxy/2026-09-02__10-00-14/analysis.md) | 4 ubuntu24.04 | 109/1 | 0.667 | 0.889 | 0.667 | 1.000 | 0.91s | 13m 26s |
| [nginx-rhel10-port-6700](https://github.com/open-sudo/infraset/blob/main/jobs/nginx-rhel10-port-6700/2026-09-02__10-00-14/analysis.md) | rhel10.0 | 39/7 | 1.000 | 1.000 | 1.000 | 0.950 | 0.83s | 1m 56s |
| [nginx-rhel7-port-6700](https://github.com/open-sudo/infraset/blob/main/jobs/nginx-rhel7-port-6700/2026-09-02__10-00-14/analysis.md) | rhel7.9 | 102/9 | 1.000 | 1.000 | 1.000 | 0.937 | 0.79s | 8m 01s |
| [nginx-rhel8-port-6700](https://github.com/open-sudo/infraset/blob/main/jobs/nginx-rhel8-port-6700/2026-09-02__10-00-14/analysis.md) | rhel8.8 | 43/3 | 1.000 | 1.000 | 1.000 | 0.937 | 0.77s | 2m 26s |
| [nginx-rhel9-port-6500](https://github.com/open-sudo/infraset/blob/main/jobs/nginx-rhel9-port-6500/2026-09-02__10-00-14/analysis.md) | rhel9.8 | 46/7 | 1.000 | 1.000 | 1.000 | 0.930 | 0.78s | 1m 56s |
| [nginx-tls-certificate-rotation-debian13](https://github.com/open-sudo/infraset/blob/main/jobs/nginx-tls-certificate-rotation-debian13/2026-09-02__10-00-14/analysis.md) | 2 debian13 | 97/17 | 1.000 | 1.000 | 1.000 | 0.990 | 0.79s | 11m 56s |
| [nginx-ubuntu24-cluster](https://github.com/open-sudo/infraset/blob/main/jobs/nginx-ubuntu24-cluster/2026-09-02__10-00-14/analysis.md) | 3 ubuntu24.04 | 94/9 | 1.000 | 1.000 | 1.000 | 0.977 | 0.97s | 3m 33s |
| [nodejs-rootless-podman-centos-stream10](https://github.com/open-sudo/infraset/blob/main/jobs/nodejs-rootless-podman-centos-stream10/2026-09-02__10-00-14/analysis.md) | centos-stream10 | 58/11 | 1.000 | 1.000 | 1.000 | 0.977 | 0.97s | 3m 56s |
| [opentelemetry-collector-routing](https://github.com/open-sudo/infraset/blob/main/jobs/opentelemetry-collector-routing/2026-09-02__10-00-14/analysis.md) | 3 ubuntu24.04 | 206/45 | 1.000 | 1.000 | 1.000 | 0.890 | 0.95s | 12m 22s |
| [openwrt-guest-isolation](https://github.com/open-sudo/infraset/blob/main/jobs/openwrt-guest-isolation/2026-09-02__10-00-14/analysis.md) | openwrt + 3 ubuntu24.04 | 224/23 | 1.000 | 1.000 | 1.000 | 0.917 | 0.87s | 11m 02s |
| [opnsense-three-zone](https://github.com/open-sudo/infraset/blob/main/jobs/opnsense-three-zone/2026-09-02__10-00-14/analysis.md) | opnsense + 3 ubuntu24.04 | 232/26 | 1.000 | 1.000 | 1.000 | 0.800 | 1.71s | 11m 27s |
| [postgresql-ha-vyos-dual-lan](https://github.com/open-sudo/infraset/blob/main/jobs/postgresql-ha-vyos-dual-lan/2026-09-02__10-00-14/analysis.md) | vyos + 3 ubuntu24.04 | 303/37 | 1.000 | 1.000 | 1.000 | 0.943 | 1.28s | 13m 50s |
| [postgresql-replication-alma9](https://github.com/open-sudo/infraset/blob/main/jobs/postgresql-replication-alma9/2026-09-02__10-00-14/analysis.md) | 3 almalinux9 | 285/20 | 1.000 | 1.000 | 1.000 | 0.963 | 1.10s | 17m 20s |
| [prometheus-node-exporter-ubuntu24](https://github.com/open-sudo/infraset/blob/main/jobs/prometheus-node-exporter-ubuntu24/2026-09-02__10-00-14/analysis.md) | 4 ubuntu24.04 | 191/8 | 1.000 | 1.000 | 1.000 | 0.967 | 0.98s | 7m 20s |
| [prometheus-thanos-objectstorage](https://github.com/open-sudo/infraset/blob/main/jobs/prometheus-thanos-objectstorage/2026-09-02__10-00-14/analysis.md) | 4 ubuntu24.04 | 301/5 | 1.000 | 1.000 | 1.000 | 0.787 | 1.03s | 14m 17s |
| [redis-sentinel-ubuntu24](https://github.com/open-sudo/infraset/blob/main/jobs/redis-sentinel-ubuntu24/2026-09-02__10-00-14/analysis.md) | 3 ubuntu24.04 | 233/46 | 1.000 | 1.000 | 1.000 | 0.983 | 1.01s | 11m 30s |
| [rhel8-offline-package-repository](https://github.com/open-sudo/infraset/blob/main/jobs/rhel8-offline-package-repository/2026-09-02__10-00-14/analysis.md) | 2 rhel8.8 | 136/17 | 1.000 | 1.000 | 1.000 | 0.973 | 0.96s | 8m 31s |
| [rhel9-drift-remediation](https://github.com/open-sudo/infraset/blob/main/jobs/rhel9-drift-remediation/2026-09-02__10-00-14/analysis.md) | 4 rhel9.8 | 148/15 | 1.000 | 1.000 | 1.000 | 0.967 | 1.30s | 7m 43s |
| [rhel9-ssh-hardening-jumpbox](https://github.com/open-sudo/infraset/blob/main/jobs/rhel9-ssh-hardening-jumpbox/2026-09-02__10-00-14/analysis.md) | rhel9.8 + 2 almalinux9 | 121/6 | 0.958 | 1.000 | 0.958 | 0.963 | 1.14s | 6m 45s |
| [rsyslog-rhel7-rhel10-tls](https://github.com/open-sudo/infraset/blob/main/jobs/rsyslog-rhel7-rhel10-tls/2026-09-02__10-00-14/analysis.md) | rhel7.9 + rhel8.8 + rhel9.8 + rhel10.0 | 326/28 | 1.000 | 1.000 | 1.000 | 0.817 | 1.38s | 14m 25s |
| [samba-ad-debian13](https://github.com/open-sudo/infraset/blob/main/jobs/samba-ad-debian13/2026-09-02__10-00-14/analysis.md) | 4 debian13 | 294/60 | 0.976 | 1.000 | 0.976 | 0.897 | 1.27s | 14m 39s |
| [sonic-frr-bgp-transit](https://github.com/open-sudo/infraset/blob/main/jobs/sonic-frr-bgp-transit/2026-09-02__10-00-14/analysis.md) | sonic + 2 ubuntu24.04 | 199/33 | 1.000 | 1.000 | 1.000 | 0.780 | 1.60s | 13m 31s |
| [ssh-auth-ubuntu24](https://github.com/open-sudo/infraset/blob/main/jobs/ssh-auth-ubuntu24/2026-09-02__10-00-14/analysis.md) | 3 ubuntu24.04 | 154/21 | 0.958 | 1.000 | 0.958 | 0.993 | 0.96s | 7m 44s |
| [static-route-convergence-vyos](https://github.com/open-sudo/infraset/blob/main/jobs/static-route-convergence-vyos/2026-09-02__10-00-14/analysis.md) | vyos + 2 ubuntu24.04 | 167/20 | 1.000 | 1.000 | 1.000 | 0.907 | 1.07s | 9m 15s |
| [sudoers-rescue-alma9](https://github.com/open-sudo/infraset/blob/main/jobs/sudoers-rescue-alma9/2026-09-02__10-00-14/analysis.md) | almalinux9 | 32/4 | 1.000 | 1.000 | 1.000 | 0.990 | 0.87s | 2m 18s |
| [systemd-broken-execstart-alma9](https://github.com/open-sudo/infraset/blob/main/jobs/systemd-broken-execstart-alma9/2026-09-02__10-00-14/analysis.md) | almalinux9 | 58/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.72s | 2m 35s |
| [user-password-hash-migration](https://github.com/open-sudo/infraset/blob/main/jobs/user-password-hash-migration/2026-09-02__10-00-14/analysis.md) | ubuntu16.04 + ubuntu24.04 | 105/14 | 1.000 | 1.000 | 1.000 | 0.910 | 0.87s | 9m 57s |
| [vault-raft-auto-unseal](https://github.com/open-sudo/infraset/blob/main/jobs/vault-raft-auto-unseal/2026-09-02__10-00-14/analysis.md) | 4 ubuntu24.04 | 312/34 | 1.000 | 1.000 | 1.000 | 0.733 | 1.04s | 12m 10s |
| [vyos-dual-lan-kubernetes](https://github.com/open-sudo/infraset/blob/main/jobs/vyos-dual-lan-kubernetes/2026-09-02__10-00-14/analysis.md) | vyos + 3 ubuntu24.04 | 344/178 | 1.000 | 1.000 | 1.000 | 0.873 | 1.22s | 16m 02s |
| [wireguard-vyos-dual-lan](https://github.com/open-sudo/infraset/blob/main/jobs/wireguard-vyos-dual-lan/2026-09-02__10-00-14/analysis.md) | 2 vyos + 2 ubuntu24.04 | 153/27 | 0.667 | 0.667 | 0.667 | 0.943 | 1.48s | 26m 06s |
