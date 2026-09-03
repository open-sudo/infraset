# OS comparison tasks

This matrix runs the same 50 single-node administration requests on 11
general-purpose Linux operating systems. The public instruction for a task family
is identical on every operating system; only the environment image changes. This
keeps the comparison focused on how the executor adapts to each distribution's
packages, service manager, paths, and native tools.

The task directory name includes the operating-system ID because InfraSet task and
job names are globally unique.

| Directory | Environment image |
|---|---|
| `almalinux9` | AlmaLinux 9 |
| `alpine` | Alpine Linux |
| `archlinux` | Arch Linux |
| `centos-stream10` | CentOS Stream 10 |
| `debian13` | Debian 13 |
| `rhel7` | RHEL 7.9 |
| `rhel8` | RHEL 8.8 |
| `rhel9` | RHEL 9.8 |
| `rhel10` | RHEL 10.0 |
| `ubuntu16` | Ubuntu 16.04 |
| `ubuntu24` | Ubuntu 24.04 |

Run all 50 tasks for one operating system from the repository root:

```bash
./run-task.sh ./tasks/os-comparison/ubuntu24
```

`catalog.toml` is the source of truth for the operating systems and task families.
Regenerate the concrete task directories after editing it:

```bash
uv run --no-project --with tomli python ./scripts/generate_os_comparison_tasks.py
```
