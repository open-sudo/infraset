# VyOS networking tasks

This matrix runs the same 10 network-appliance requests on 8 general-purpose
Linux operating systems, with VyOS fixed as the appliance in every task. Only
the operating system of the Linux nodes behind it varies, so the comparison
stays focused on how the executor's approach to the same VyOS configuration
changes with the Linux distribution it has to interoperate with.

| Task | Topology | Nodes |
|---|---|---|
| `nat-egress` | one private LAN | 1 VyOS + 2 Linux |
| `cross-lan-firewall` | two private LANs | 1 VyOS + 2 Linux |
| `lan-to-lan-routing` | two private LANs | 1 VyOS + 2 Linux |
| `wireguard-gateway` | private LAN plus an outside client | 1 VyOS + 2 Linux |
| `dhcp-server` | one private LAN | 1 VyOS + 2 Linux |
| `port-forward` | private LAN plus an outside client | 1 VyOS + 2 Linux |
| `dns-forwarding` | one private LAN | 1 VyOS + 2 Linux |
| `vlan-segmentation` | one shared trunk link | 1 VyOS + 2 Linux |
| `vrrp-failover` | two LANs joined by two routers | 2 VyOS + 2 Linux |
| `traffic-shaping` | two private LANs | 1 VyOS + 2 Linux |

`vrrp-failover` is the only task that provisions two appliances, because
router redundancy cannot be demonstrated with a single router. It is also the
only behavioral task in the set: the requirement is that the gateway survives
a router going down, which the executor has to demonstrate rather than assert
from configuration.

Every node also carries an always-on `mgmt` network (DHCP, egress) purely for
control-plane reachability; it is out of scope for the tested behavior. The
task-specific networks (`lan`, `lan-a`/`lan-b`, or `trunk`) carry no egress
and are where each request is actually satisfied.

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

Run all 10 tasks for one operating system from the repository root:

```bash
./run-task.sh ./tasks/vyos-networking/ubuntu24
```

`catalog.toml` is the source of truth for the operating systems, task
families, and their network topology. Regenerate the concrete task
directories after editing it:

```bash
uv run --no-project --with tomli python ./scripts/generate_vyos_networking_tasks.py
```
