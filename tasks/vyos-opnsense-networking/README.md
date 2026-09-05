# VyOS and OPNsense cross-vendor networking tasks

Ten scenarios in which two different network appliances face each other and
have to be made to agree. VyOS is `node1` and OPNsense is `node2` in every
task; the Linux nodes behind them carry the workload, and only their operating
system varies across the matrix. What the matrix measures is how the same
cross-vendor outcome is reached with different hosts behind the routers.

The two platforms disagree about almost everything an operator touches. VyOS
takes a unified configuration CLI inside a `configure`/`commit`/`save`
envelope, applies its own nftables ruleset, and refuses direct `iptables` use.
OPNsense keeps everything in `/conf/config.xml`, expects the web UI, and is
driven from a shell only by editing that file and running `configctl`. Both
default to refusing forwarded traffic, so every path across the pair has to be
opened twice, in two different languages.

| Task | Difficulty | Topology | What it exercises |
|---|---|---|---|
| `transit-firewall-pair` | medium | dual-site | One flow permitted through two default-deny firewalls |
| `published-service-two-hops` | medium | dual-site | A port forward on one router reached through a route on the other |
| `double-nat-path` | hard | dual-site | Source translation applied once on each router |
| `ipsec-vendor-interop` | hard | dual-site | An IPsec tunnel negotiated between the two platforms |
| `wireguard-vendor-interop` | hard | dual-site | A WireGuard tunnel joining the two private networks |
| `split-dns-authority` | medium | dual-site | One name resolving differently on each side |
| `dhcp-per-segment-gateway` | medium | dual-site | Each router addressing its own segment and offering itself as the route |
| `firewall-log-correlation` | medium | dual-site | One attempt recorded as permitted on one router and refused on the other |
| `redundant-path-failover` | hard | dual-path | Connectivity surviving either transit network going away |
| `policy-based-egress` | hard | dual-path | Two flows steered across two different transit networks |

Every task provisions two appliances and two workload nodes. Appliances are
allocated first, so `node1` is always VyOS and `node2` always OPNsense, and an
instruction naming a node names the same platform on every operating system in
the matrix.

Three families are behavioral rather than configuration-only.
`redundant-path-failover` has to keep two hosts talking across a transit
network being taken out of service, `firewall-log-correlation` has to produce
the actual pair of log entries from one attempt, and `policy-based-egress` has
to show which transit network carried each flow. Each is demonstrated by a
single bounded, reversible state change.

## Why this pairing

The two appliances differ on the axis that decides what a mistake costs. VyOS
reaches its exec channel over vsock and cannot be locked out by its own
configuration. OPNsense reaches it over SSH and can be, the moment a
`configctl filter reload` applies a ruleset with no pass rule for the
management path — after which the appliance is unreachable for the rest of the
lease.

Pairing one of each means half the topology stays reachable while the other
half is mid-mistake. Pairing two SSH-transport appliances would double the
exposure instead, which is why OpenWrt and OPNsense are not combined.

## Topologies

Every node carries an always-on `mgmt` network with egress, declared first so
it lands on the first interface and the OPNsense management path survives a
filter reload. The task-specific networks carry no egress and no platform
DHCP, so addressing on them is the executor's to arrange.

| Topology | Networks | Shape |
|---|---|---|
| `dual-site` | mgmt, transit, lan-a, lan-b | The routers meet on one transit network, one workload behind each |
| `dual-path` | mgmt, transit-a, transit-b, lan-a, lan-b | The same pair joined by two independent transit networks |

Two platform constraints apply throughout. The bridge owns `.1` on any
DHCP-enabled network, so a router taking that address causes flip-flop ARP —
`.254` is the convention. And a private network declared without platform DHCP
forwards frames but assigns no addresses, so hosts that have not been addressed
will not reach anything.

| Directory | Workload node image |
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
./run-task.sh ./tasks/vyos-opnsense-networking/ubuntu24
```

`catalog.toml` is the source of truth. Regenerate the concrete task
directories after editing it:

```bash
uv run --no-project --with tomli python ./scripts/generate_vyos_opnsense_networking_tasks.py
```
