# Single-node OS comparison tasks

Thirty single-node administration requests issued against the same eight
general-purpose Linux operating systems. The rule that makes the matrix
comparable: one node, the public instruction for a task family is identical on
every operating system, and only the environment image changes. Anything a task
needs that differs per distribution has to be worked out by the executor.

The set was built in two generations. The first ten cover accounts,
permissions, scheduling, and services; four of them prepare existing state
before the executor starts. The remaining twenty cover ground the first set
does not — mandatory access control, boot and kernel configuration, storage
management, package pinning, and service confinement — and are all greenfield.

| Task | Difficulty | Setup |
|---|---|---|
| `account-resource-limits` | medium | greenfield |
| `application-log-rotation` | medium | brownfield |
| `custom-ca-trust` | medium | greenfield |
| `host-firewall-baseline` | medium | greenfield |
| `kernel-network-hardening` | medium | greenfield |
| `repair-application-permissions` | medium | brownfield |
| `scheduled-maintenance` | easy | brownfield |
| `ssh-key-only` | medium | greenfield |
| `sticky-drop-directory` | easy | greenfield |
| `unprivileged-service` | medium | brownfield |
| `mandatory-access-control-port` | medium | greenfield |
| `kernel-module-blacklist` | medium | greenfield |
| `boot-kernel-parameter` | medium | greenfield |
| `mount-option-hardening` | medium | greenfield |
| `service-sandboxing` | hard | greenfield |
| `password-complexity-policy` | medium | greenfield |
| `sudo-command-logging` | medium | greenfield |
| `cron-access-control` | easy | greenfield |
| `ssh-host-certificate` | hard | greenfield |
| `disk-quota` | hard | greenfield |
| `encrypted-volume` | hard | greenfield |
| `lvm-extend` | medium | greenfield |
| `filesystem-snapshot-rollback` | hard | greenfield |
| `zram-swap` | medium | greenfield |
| `package-version-hold` | medium | greenfield |
| `local-package-repository` | hard | greenfield |
| `oom-protection` | hard | greenfield |
| `rootless-container-service` | hard | greenfield |
| `certificate-rotation` | hard | greenfield |
| `file-integrity-baseline` | medium | greenfield |

Roughly half of the second generation are strong operating-system
discriminators: mandatory access control, boot configuration, module
blacklisting, PAM, package pinning, and rootless containers all diverge sharply
between the RPM family, the Debian family, and Alpine. Five are behavioral
rather than configuration-only (`filesystem-snapshot-rollback`,
`oom-protection`, `certificate-rotation`, `file-integrity-baseline`, and
`lvm-extend`): the requirement is that something survives, recovers, or is
detected, which has to be demonstrated rather than asserted from a
configuration file.

The images ship a single disk, so the storage tasks (`disk-quota`,
`encrypted-volume`, `lvm-extend`, `filesystem-snapshot-rollback`) are expected
to be satisfied with loopback-backed volumes rather than a second block device.
The instructions state the outcome and leave that choice open.

| Directory | Environment image |
|---|---|
| `almalinux9` | AlmaLinux 9 |
| `alpine` | Alpine Linux |
| `centos-stream10` | CentOS Stream 10 |
| `rhel7` | RHEL 7.9 |
| `rhel9` | RHEL 9.8 |
| `rhel10` | RHEL 10.0 |
| `ubuntu16` | Ubuntu 16.04 |
| `ubuntu24` | Ubuntu 24.04 |

Run all 30 tasks for one operating system from the repository root:

```bash
./run-task.sh ./tasks/single-node-os-comparison/ubuntu24
```

`catalog.toml` is the source of truth. Each family declares its own difficulty,
agent and verifier timeouts, and whether it prepares existing state. The
`prepare/` setup and baseline files of the four brownfield families are
maintained by hand and are not rewritten by the generator. Regenerate the
concrete task directories after editing the catalog:

```bash
uv run --no-project --with tomli python ./scripts/generate_single_node_os_comparison_tasks.py
```

Results for this category are summarized in
[metrics/single-node-os-comparison.md](../../metrics/single-node-os-comparison.md).
