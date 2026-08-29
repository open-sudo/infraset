# InfraSet: An Open Dataset of LLM-Executed Infrastructure Tasks

The industry is increasingly using LLMs to operate infrastructure, either directly or with a human in the loop.
Yet there is little public empirical data showing what happens when LLMs operate real systems, whether in
greenfield, brownfield, end-of-life, or distributed environments. Perhaps LLMs perform remarkably well. Perhaps
they fail in subtle ways. We do not yet have enough evidence to know either way.

InfraSet is an open dataset of executed infrastructure tasks and traces, created to build that evidence. It currently
contains 42 tasks, and we hope the community will join us and help expand it. Results can also be explored on
[the InfraSet dataset on Hugging Face](https://huggingface.co/datasets/infraset/infraset).

## How InfraSet Works

InfraSet has three main pieces:

- **Harbor** is the execution framework. It runs the AI agent, coordinates the
  task lifecycle, records the agent trace, and runs the evaluator.
- **Antrieb** provides disposable virtual machines, clusters, and networks for
  each task execution.
- **harbor-antrieb** is the bridge between Harbor and Antrieb. It lets Harbor
  provision the required environment and gives the agent and evaluator managed
  access to the systems through their node names.

The main concepts are:

- A **task** is a reusable infrastructure scenario. It contains the candidate
  instructions, environment and topology definition, optional preparation, and
  evaluation logic.
- A **job** is one execution of a task. It records what happened during that
  run, including the agent trace, commands, outputs, evaluation results, and
  result artifacts.
- The **preparer** is the optional setup stage. It creates the initial state the
  task requires before the AI agent starts, such as installed software,
  application data, or intentional configuration drift.
- The **evaluator** determines whether the resulting systems satisfy the task's
  requirements. It collects evidence by inspecting the live environment and
  running relevant probes or commands.
- The **verifier** is Harbor's evaluation component. It runs the task's
  evaluation process, coordinates evidence collection, and converts the
  evaluator's findings into scores and recorded results.

The process from an idea to complete data is:

1. An infrastructure scenario is turned into a task with candidate instructions,
   an environment definition, any required preparation, and evaluation checks.
2. Harbor uses `harbor-antrieb` to provision the task's disposable environment
   through Antrieb.
3. The AI agent receives the task and operates the systems through Harbor's
   managed execution interface.
4. The evaluator inspects the resulting systems, tests the required behavior,
   and records evidence, scores, and any limitations.
5. Harbor stores the complete execution data, including the agent trace,
   commands, outputs, evaluator evidence, and result artifacts.
6. The validated results are summarized and published in the
   [InfraSet dataset on Hugging Face](https://huggingface.co/datasets/infraset/infraset).

This table summarizes the recorded [jobs](https://github.com/open-sudo/infraset/tree/main/jobs). `Full passes` counts trials with complete evaluation coverage and successful functional behavior. `Evaluation coverage` and `Operational hygiene` are per-trial averages. `Best score` is the highest per-trial reward; `Provisioning time` and `Mean duration` are averages across recorded trials.

`Operational hygiene` measures whether the evaluator found executor-created residue, abandoned files, conflicting services, unsafe exposure, or other unwanted changes. `100%` means all applicable hygiene checks passed; `0%` means none passed.

| # | Task | Environment | Runs | Full passes | Best score | Evaluation coverage | Operational hygiene | Provisioning time | Mean duration |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | disk-full-recovery-centos-stream10 | centos-stream10 | 1 | 1/1 | 1.00 | 100% | 100% | 1.0 sec | 8.3 min |
| 2 | kernel-network-stack-migration | ubuntu16.04 + ubuntu24.04 | 2 | 2/2 | 1.00 | 100% | 100% | 0.8 sec | 14.9 min |
| 3 | loki-cascading-failure-ubuntu24 | ubuntu24.04 x4 | 2 | 1/2 | 1.00 | 100% | 100% | 1.0 sec | 8.6 min |
| 4 | mariadb-migration-ubuntu16-ubuntu24 | ubuntu16.04 + ubuntu24.04 | 1 | 1/1 | 1.00 | 100% | 100% | 1.0 sec | 15.8 min |
| 5 | nginx-tls-certificate-rotation-debian13 | debian13 x2 | 2 | 2/2 | 0.75 | 100% | 0% | 0.8 sec | 8.6 min |
| 6 | rhel9-drift-remediation | rhel9.8 x4 | 3 | 2/3 | 1.00 | 100% | 50% | 1.0 sec | 9.3 min |
| 7 | rhel9-ssh-hardening-jumpbox | rhel9.8 + almalinux9 x2 | 2 | 1/2 | 1.00 | 100% | 100% | 0.9 sec | 4.8 min |
| 8 | sudoers-rescue-alma9 | almalinux9 | 1 | 1/1 | 1.00 | 100% | 100% | 0.7 sec | 6.2 min |
| 9 | systemd-broken-execstart-alma9 | almalinux9 | 1 | 1/1 | 1.00 | 100% | 100% | 0.7 sec | 7.5 min |
| 10 | user-password-hash-migration | ubuntu16.04 + ubuntu24.04 | 1 | 1/1 | 1.00 | 100% | 100% | 0.9 sec | 16.8 min |
| 11 | bind-dnssec-alma9 | almalinux9 x4 | 1 | 1/1 | 1.00 | 100% | 100% | 1.3 sec | 14.3 min |
| 12 | etcd-mtls-centos-stream10 | centos-stream10 x4 | 2 | 0/2 | — | 50% | 100% | 1.5 sec | 22.3 min |
| 13 | haproxy-nodejs-ubuntu16 | ubuntu16.04 | 5 | 3/5 | 1.00 | 92% | 40% | 0.6 sec | 6.5 min |
| 14 | mariadb-galera-ubuntu16 | ubuntu16.04 x3 | 2 | 1/2 | 0.88 | 80% | 0% | 0.7 sec | 33.8 min |
| 15 | mariadb-galera-ubuntu24 | ubuntu24.04 x3 | 1 | 1/1 | 0.88 | 100% | 0% | 1.1 sec | 14.2 min |
| 16 | minio-distributed-ubuntu24 | ubuntu24.04 x4 | 1 | 1/1 | 0.75 | 100% | 0% | 1.0 sec | 19.6 min |
| 17 | nfs-ubuntu24 | ubuntu24.04 x3 | 2 | 1/2 | 1.00 | 73% | 100% | 1.1 sec | 14.4 min |
| 18 | nginx-alma-alpine | almalinux9 x2 + alpine x2 | 1 | 1/1 | 0.92 | 100% | 0% | 1.1 sec | 9.2 min |
| 19 | nginx-haproxy | ubuntu24.04 x4 | 1 | 1/1 | 1.00 | 100% | 100% | 1.0 sec | 9.3 min |
| 20 | nginx-rhel10-port-6700 | rhel10.0 | 1 | 1/1 | 1.00 | 100% | 100% | 0.9 sec | 7.0 min |
| 21 | nginx-rhel7-port-6700 | rhel7.9 | 3 | 1/3 | 0.90 | 100% | 0% | 0.7 sec | 3.1 min |
| 22 | nginx-rhel8-port-6700 | rhel8.8 | 1 | 1/1 | 1.00 | 100% | 100% | 0.7 sec | 7.7 min |
| 23 | nginx-rhel9-port-6500 | rhel9.8 | 1 | 1/1 | 0.90 | 100% | 0% | 0.7 sec | 5.6 min |
| 24 | nginx-ubuntu24-cluster | ubuntu24.04 x3 | 5 | 3/5 | 1.00 | 90% | 100% | 1.3 sec | 4.8 min |
| 25 | nodejs-rootless-podman-centos-stream10 | centos-stream10 | 1 | 1/1 | 1.00 | 100% | 100% | 0.9 sec | 10.9 min |
| 26 | opentelemetry-collector-routing | ubuntu24.04 x3 | 1 | 1/1 | 0.78 | 100% | 0% | 0.8 sec | 22.2 min |
| 27 | openwrt-guest-isolation | openwrt + ubuntu24.04 x3 | 1 | 1/1 | 0.78 | 100% | 0% | 1.2 sec | 12.4 min |
| 28 | opnsense-three-zone | opnsense + ubuntu24.04 x3 | 1 | 1/1 | 0.78 | 100% | 0% | 1.7 sec | 12.7 min |
| 29 | postgresql-ha-vyos-dual-lan | vyos + ubuntu24.04 x3 | 3 | 1/3 | 0.71 | 62% | 0% | 1.4 sec | 21.2 min |
| 30 | postgresql-replication-alma9 | almalinux9 x3 | 2 | 0/2 | — | 75% | 0% | 1.0 sec | 15.3 min |
| 31 | prometheus-node-exporter-ubuntu24 | ubuntu24.04 x4 | 3 | 1/3 | 1.00 | 77% | 50% | 0.9 sec | 14.6 min |
| 32 | prometheus-thanos-objectstorage | ubuntu24.04 x4 | 6 | 1/6 | 0.75 | 68% | 0% | 1.4 sec | 25.0 min |
| 33 | redis-sentinel-ubuntu24 | ubuntu24.04 x3 | 1 | 1/1 | 1.00 | 100% | 100% | 0.9 sec | 15.8 min |
| 34 | rhel8-offline-package-repository | rhel8.8 x2 | 1 | 1/1 | 1.00 | 100% | — | 0.7 sec | 15.8 min |
| 35 | rsyslog-rhel7-rhel10-tls | rhel7.9 + rhel8.8 + rhel9.8 + rhel10.0 | 3 | 0/3 | — | 52% | 0% | 1.0 sec | 20.7 min |
| 36 | samba-ad-debian13 | debian13 x4 | 1 | 0/1 | 0.32 | 100% | 0% | 1.1 sec | 23.8 min |
| 37 | sonic-frr-bgp-transit | sonic + ubuntu24.04 x2 | 1 | 1/1 | 0.73 | 100% | 0% | 2.5 sec | 22.3 min |
| 38 | ssh-auth-ubuntu24 | ubuntu24.04 x3 | 5 | 4/5 | 1.00 | 90% | 25% | 1.4 sec | 10.5 min |
| 39 | static-route-convergence-vyos | vyos + ubuntu24.04 x2 | 1 | 1/1 | 1.00 | 100% | 100% | 1.1 sec | 13.0 min |
| 40 | vault-raft-auto-unseal | ubuntu24.04 x4 | 3 | 1/3 | 0.75 | 50% | 0% | 1.1 sec | 18.5 min |
| 41 | vyos-dual-lan-kubernetes | vyos + ubuntu24.04 x3 | 2 | 2/2 | 1.00 | 100% | 100% | 1.1 sec | 20.5 min |
| 42 | wireguard-vyos-dual-lan | vyos x2 + ubuntu24.04 x2 | 2 | 0/2 | — | 86% | — | 1.3 sec | 11.8 min |
