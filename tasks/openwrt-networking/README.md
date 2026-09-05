# OpenWrt networking tasks

Ten routed and firewalled network scenarios built around an OpenWrt appliance,
each issued against eight general-purpose Linux operating systems. The
appliance is fixed; only the operating system of the Linux nodes behind it
changes, so the matrix measures how the same network outcome is reached with
different hosts on the other side of the router.

OpenWrt is configured through UCI rather than by editing files, its root shell
is BusyBox `ash`, and current releases use `apk` in place of `opkg`. Staged
changes need an explicit commit and a service reload to take effect, which is
why one family is specifically about what survives a restart.

| Task | Difficulty | Topology | Nodes | What it exercises |
|---|---|---|---|---|
| `static-lease-reservation` | easy | single-lan | 1 + 2 | DHCP service with a reservation pinned by host |
| `dns-hostname-override` | easy | single-lan | 1 + 2 | Local DNS answering for a private name |
| `inbound-service-publish` | medium | gateway-client | 1 + 2 | Destination NAT from the management side into a private network |
| `interzone-port-policy` | medium | dual-lan | 1 + 2 | One permitted port between two networks, everything else refused |
| `guest-network-isolation` | medium | dual-lan | 1 + 2 | Asymmetric zone policy: guests reach the router, not the trusted network |
| `tagged-vlan-bridge` | hard | trunk | 1 + 2 | Two tagged VLANs over one link, isolated from each other |
| `bandwidth-limit` | hard | gateway-client | 1 + 2 | Shaping a client to a measured rate in both directions |
| `reboot-persistent-config` | medium | single-lan | 1 + 2 | Addressing, DHCP and a firewall rule surviving a restart |
| `site-to-site-tunnel` | hard | dual-site | 2 + 2 | Encrypted tunnel between two routers joining two private networks |
| `gateway-failover` | hard | redundant-gateway | 2 + 1 | A shared address moving between routers without the client losing it |

The nodes column is appliances plus Linux hosts. Appliances are always
allocated first, so `node1` is OpenWrt in every task and `node1`/`node2` are
both OpenWrt in the two-appliance families.

Three of the families are behavioral rather than configuration-only.
`bandwidth-limit` has to show a measured transfer, `reboot-persistent-config`
has to survive a restart, and `gateway-failover` has to keep serving across one
transition. In each the outcome is demonstrated by a single bounded, reversible
state change rather than asserted from a config file.

## Topologies

Every node carries an always-on `mgmt` network with egress, declared first so
it lands on `eth0`. The task-specific networks carry no egress and no platform
DHCP, so addressing on them is the executor's to arrange.

| Topology | Networks | Shape |
|---|---|---|
| `single-lan` | mgmt, lan | Router and two hosts on one private network |
| `dual-lan` | mgmt, lan-a, lan-b | Router between two private networks, one host on each |
| `gateway-client` | mgmt, lan | Router and one host on a private network, second host outside it |
| `trunk` | mgmt, trunk | Three nodes sharing one link for tagged VLANs |
| `dual-site` | mgmt, transit, lan-a, lan-b | Two routers meeting on a transit link, each with its own private network and host |
| `redundant-gateway` | mgmt, lan | Two routers and one host on a single private network |

The `mgmt` network matters more here than for a console-managed appliance:
OpenWrt's exec transport is SSH, so a firewall reload that moves the management
interface into a restrictive zone costs access to the appliance mid-task. The
OpenWrt reference carried in `base_runbooks` documents the rule to stage before
the first reload.

| Directory | Linux node image |
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
./run-task.sh ./tasks/openwrt-networking/ubuntu24
```

`catalog.toml` is the source of truth. Regenerate the concrete task
directories after editing it:

```bash
uv run --no-project --with tomli python ./scripts/generate_openwrt_networking_tasks.py
```
