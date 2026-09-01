# InfraSet: An Open Dataset of LLM-Executed Infrastructure Tasks

The industry is increasingly using LLMs to operate infrastructure, either directly or with a human in the loop.
Yet there is little public empirical data showing what happens when LLMs operate real systems, whether in
greenfield, brownfield, end-of-life, or distributed environments. Perhaps LLMs perform remarkably well. Perhaps
they fail in subtle ways. We do not yet have enough evidence to know either way.

InfraSet is a dataset of executed infrastructure tasks and traces, created to build that evidence. It currently
contains 42 tasks, and we hope the community will join us and help expand it. Results can also be explored on
[the InfraSet dataset on Hugging Face](https://huggingface.co/datasets/infraset/infraset).

## Execution summary

This table summarizes the recorded [jobs](https://github.com/open-sudo/infraset/tree/main/jobs). Metrics and times are averages across recorded trials. `Commands` reports successful/failed executor commands from the provider-captured audit. Unfinished or indeterminate command records are excluded from both values. A failed command records an unsuccessful attempt; it does not by itself mean that the final task outcome failed.

`Reward` measures the supported outcome. `Operational hygiene` measures attributable residue or unrelated regression found by applicable global checks. A hygiene score of `1.000` means all applicable checks passed; `0.000` means none passed.

The current dataset contains 42 tasks, 84 trials, and 4014 completed executor commands: 3840 successful and 174 failed.

| Task | Environment | Trials | Commands | Reward | Evaluation complete | Coverage | Functionality | Hygiene | Provisioning time | Execution time |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bind-dnssec-alma9 | almalinux9 x4 | 2 | 104/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.945 | 1.24s | 7m 28s |
| disk-full-recovery-centos-stream10 | centos-stream10 | 2 | 17/1 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.95s | 1m 47s |
| etcd-mtls-centos-stream10 | centos-stream10 x4 | 2 | 111/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.980 | 1.64s | 9m 26s |
| haproxy-nodejs-ubuntu16 | ubuntu16.04 | 2 | 33/3 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.67s | 3m 41s |
| kernel-network-stack-migration | ubuntu16.04 + ubuntu24.04 | 2 | 70/3 | 0.929 | 1.000 | 1.000 | 0.929 | 1.000 | 0.90s | 7m 23s |
| loki-cascading-failure-ubuntu24 | ubuntu24.04 x4 | 2 | 55/3 | 0.964 | 1.000 | 1.000 | 0.964 | 1.000 | 1.04s | 4m 10s |
| mariadb-galera-ubuntu16 | ubuntu16.04 x3 | 2 | 174/9 | 1.000 | 1.000 | 1.000 | 1.000 | 0.950 | 0.85s | 10m 44s |
| mariadb-galera-ubuntu24 | ubuntu24.04 x3 | 2 | 120/0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.950 | 0.91s | 24m 13s |
| mariadb-migration-ubuntu16-ubuntu24 | ubuntu16.04 + ubuntu24.04 | 2 | 28/4 | 0.500 | 0.500 | 0.500 | 0.500 | 0.750 | 1.00s | 23m 23s |
| minio-distributed-ubuntu24 | ubuntu24.04 x4 | 2 | 158/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.910 | 1.09s | 6m 51s |
| nfs-ubuntu24 | ubuntu24.04 x3 | 2 | 57/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.940 | 1.02s | 3m 04s |
| nginx-alma-alpine | almalinux9 x2 + alpine x2 | 2 | 84/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.850 | 1.04s | 3m 25s |
| nginx-haproxy | ubuntu24.04 x4 | 2 | 69/0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.850 | 0.98s | 3m 31s |
| nginx-rhel10-port-6700 | rhel10.0 | 2 | 20/0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.930 | 0.71s | 2m 47s |
| nginx-rhel7-port-6700 | rhel7.9 | 2 | 33/5 | 0.500 | 1.000 | 1.000 | 0.500 | 0.975 | 0.65s | 11m 39s |
| nginx-rhel8-port-6700 | rhel8.8 | 2 | 20/0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.890 | 0.65s | 1m 53s |
| nginx-rhel9-port-6500 | rhel9.8 | 2 | 25/0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.900 | 0.69s | 1m 35s |
| nginx-tls-certificate-rotation-debian13 | debian13 x2 | 2 | 21/1 | 0.917 | 1.000 | 1.000 | 0.917 | 0.900 | 0.79s | 4m 09s |
| nginx-ubuntu24-cluster | ubuntu24.04 x3 | 2 | 21/0 | 0.500 | 1.000 | 1.000 | 0.500 | 1.000 | 0.88s | 5m 47s |
| nodejs-rootless-podman-centos-stream10 | centos-stream10 | 2 | 45/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.965 | 0.89s | 7m 16s |
| opentelemetry-collector-routing | ubuntu24.04 x3 | 2 | 141/2 | 1.000 | 1.000 | 1.000 | 1.000 | 0.800 | 0.90s | 9m 14s |
| openwrt-guest-isolation | openwrt + ubuntu24.04 x3 | 2 | 116/11 | 1.000 | 1.000 | 1.000 | 1.000 | 0.835 | 1.01s | 7m 47s |
| opnsense-three-zone | opnsense + ubuntu24.04 x3 | 2 | 134/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.685 | 1.65s | 8m 35s |
| postgresql-ha-vyos-dual-lan | vyos + ubuntu24.04 x3 | 2 | 176/7 | 1.000 | 1.000 | 1.000 | 1.000 | 0.930 | 1.19s | 12m 11s |
| postgresql-replication-alma9 | almalinux9 x3 | 2 | 132/2 | 0.938 | 1.000 | 1.000 | 0.938 | 0.940 | 1.05s | 8m 20s |
| prometheus-node-exporter-ubuntu24 | ubuntu24.04 x4 | 2 | 136/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.950 | 1.31s | 5m 35s |
| prometheus-thanos-objectstorage | ubuntu24.04 x4 | 2 | 153/7 | 1.000 | 1.000 | 1.000 | 1.000 | 0.940 | 0.94s | 14m 02s |
| redis-sentinel-ubuntu24 | ubuntu24.04 x3 | 2 | 110/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.960 | 0.98s | 7m 57s |
| rhel8-offline-package-repository | rhel8.8 x2 | 2 | 49/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.900 | 0.68s | 6m 48s |
| rhel9-drift-remediation | rhel9.8 x4 | 2 | 77/1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.960 | 1.03s | 22m 27s |
| rhel9-ssh-hardening-jumpbox | rhel9.8 + almalinux9 x2 | 2 | 71/1 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.08s | 6m 06s |
| rsyslog-rhel7-rhel10-tls | rhel7.9 + rhel8.8 + rhel9.8 + rhel10.0 | 2 | 183/26 | 1.000 | 1.000 | 1.000 | 1.000 | 0.905 | 0.94s | 12m 41s |
| samba-ad-debian13 | debian13 x4 | 2 | 235/18 | 1.000 | 1.000 | 1.000 | 1.000 | 0.930 | 0.87s | 20m 58s |
| sonic-frr-bgp-transit | sonic + ubuntu24.04 x2 | 2 | 107/4 | 1.000 | 1.000 | 1.000 | 1.000 | 0.940 | 1.75s | 6m 23s |
| ssh-auth-ubuntu24 | ubuntu24.04 x3 | 2 | 113/19 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.96s | 7m 20s |
| static-route-convergence-vyos | vyos + ubuntu24.04 x2 | 2 | 108/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.905 | 1.35s | 7m 04s |
| sudoers-rescue-alma9 | almalinux9 | 2 | 29/0 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.75s | 2m 42s |
| systemd-broken-execstart-alma9 | almalinux9 | 2 | 19/2 | 0.950 | 1.000 | 1.000 | 0.950 | 1.000 | 0.87s | 1m 34s |
| user-password-hash-migration | ubuntu16.04 + ubuntu24.04 | 2 | 64/7 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.79s | 9m 59s |
| vault-raft-auto-unseal | ubuntu24.04 x4 | 2 | 163/5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.920 | 1.40s | 8m 52s |
| vyos-dual-lan-kubernetes | vyos + ubuntu24.04 x3 | 2 | 144/0 | 1.000 | 1.000 | 1.000 | 1.000 | 0.875 | 1.18s | 6m 48s |
| wireguard-vyos-dual-lan | vyos x2 + ubuntu24.04 x2 | 2 | 115/3 | 1.000 | 1.000 | 1.000 | 1.000 | 0.975 | 1.26s | 6m 29s |
