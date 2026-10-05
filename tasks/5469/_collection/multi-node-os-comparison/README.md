# Multi-node OS comparison tasks

This matrix runs the same 10 multi-node administration requests on 8 general-purpose
Linux operating systems. Every node in a task's cluster runs the same operating
system; the public instruction for a task family is identical on every operating
system, so the comparison stays focused on how the executor coordinates the same
distribution across cooperating nodes (packages, service manager, paths, and native
tools).

The task directory name includes the operating-system ID because InfraSet task and
job names are globally unique.

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

Each task family provisions either two or three nodes of the same image (see
`nodes` in `catalog.toml`); none declare custom networks, so nodes reach each other
and the internet over the default cluster network.

Run all 10 tasks for one operating system from the repository root:

```bash
./run-task.sh ./tasks/multi-node-os-comparison/ubuntu24
```

`catalog.toml` is the source of truth for the operating systems and task families.
Regenerate the concrete task directories after editing it:

```bash
uv run --no-project --with tomli python ./scripts/generate_multi_node_os_comparison_tasks.py
```
