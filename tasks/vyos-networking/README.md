# VyOS networking tasks

This matrix runs the same 5 network-appliance requests on 8 general-purpose
Linux operating systems, with a single VyOS router (`node1`) fixed in every
task. Only the operating system of the two Linux nodes behind it (`node2`
and `node3`) varies across the matrix, so the comparison stays focused on
how the executor's approach to the same VyOS configuration changes with the
Linux distribution it has to interoperate with.

Every node also carries an always-on `mgmt` network (DHCP, egress) purely
for control-plane reachability; it is out of scope for the tested behavior.
The task-specific topology (`lan`, or `lan-a`/`lan-b`) is where the request
is actually satisfied.

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

Run all 5 tasks for one operating system from the repository root:

```bash
./run-task.sh ./tasks/vyos-networking/ubuntu24
```

`catalog.toml` is the source of truth for the operating systems, task
families, and their network topology. Regenerate the concrete task
directories after editing it:

```bash
uv run --no-project --with tomli python ./scripts/generate_vyos_networking_tasks.py
```
