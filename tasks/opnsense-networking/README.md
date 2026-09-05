# OPNsense networking tasks

Ten firewall and edge-services scenarios built around an OPNsense appliance,
each issued against eight general-purpose Linux operating systems. The
appliance is fixed; only the operating system of the hosts behind it changes.

OPNsense is FreeBSD with `pf`, and it is built to be configured through its web
UI. Automating it from a shell means editing `/conf/config.xml` and triggering
the apply pipeline with `configctl`, which is deliberately less comfortable
than the other appliances in this dataset — the tool is not optimised for the
approach. FreeBSD tooling applies throughout: `ifconfig`, `netstat -rn` and
`pfctl` rather than `ip` and `ss`.

Three properties of the image shape most of the work. The firewall ships
**default-deny**, so any forwarded flow needs an explicit pass rule. Outbound
NAT is **automatic** by default, so the common egress case needs no rule at all
and writing one is usually a mistake. And several files, `authorized_keys`
among them, are regenerated from `config.xml` on every apply, so changes made
directly to them are discarded.

| Task | Difficulty | Topology | Nodes | What it exercises |
|---|---|---|---|---|
| `default-deny-baseline` | medium | dual-lan | 1 + 2 | One explicit pass rule through a deny-by-default firewall |
| `alias-based-policy` | medium | dual-lan | 1 + 2 | A named object holding a port set, referenced from one rule |
| `restricted-service-publish` | medium | gateway-client | 1 + 2 | A port forward reachable from one source address only |
| `hairpin-nat-reflection` | hard | single-lan | 1 + 2 | Reaching a published service from the network it lives on |
| `outbound-nat-mapping` | hard | dual-lan | 1 + 2 | Source translation observable at the far end, one direction only |
| `dns-domain-blocking` | medium | single-lan | 1 + 2 | Resolver serving a network with one domain withheld |
| `logged-block-policy` | medium | dual-lan | 1 + 2 | Refused traffic recorded and the log entry produced |
| `additional-zone-interface` | medium | dual-lan | 1 + 2 | An unconfigured interface brought up as its own zone |
| `haproxy-service-frontend` | hard | frontend-backends | 1 + 3 | One entry point spreading requests across two backends |
| `ipsec-site-tunnel` | hard | dual-site | 2 + 2 | IPsec joining two private networks across a transit link |

The nodes column is appliances plus Linux hosts. Appliances are allocated
first, so `node1` is OPNsense in every task and `node1`/`node2` are both
OPNsense in `ipsec-site-tunnel`.

Two families are behavioral rather than configuration-only.
`logged-block-policy` has to produce an actual log entry from an actual refused
attempt, and `haproxy-service-frontend` has to show answers arriving from both
backends. `hairpin-nat-reflection` is close to behavioral as well: the
distinguishing evidence is a request that leaves the network and returns to it.

`ipsec-site-tunnel` deliberately uses IPsec rather than WireGuard, which the
VyOS and OpenWrt categories already cover, so the three tunnel families across
the dataset exercise three different mechanisms.

## Topologies

Every node carries an always-on `mgmt` network with egress, declared first so
it is the first interface on the node. The task-specific networks carry no
egress and no platform DHCP, so addressing on them is the executor's to
arrange.

| Topology | Networks | Shape |
|---|---|---|
| `single-lan` | mgmt, lan | Firewall and both hosts on one private network |
| `dual-lan` | mgmt, lan-a, lan-b | Firewall between two private networks, one host on each |
| `gateway-client` | mgmt, lan | Firewall and one host on a private network, second host outside it |
| `frontend-backends` | mgmt, lan | Two backends behind the firewall, one client outside |
| `dual-site` | mgmt, transit, lan-a, lan-b | Two firewalls on a transit link, each with its own network and host |

The `mgmt` network carries the exec path, and OPNsense's transport is SSH. A
`configctl filter reload` that applies a ruleset without a pass rule for the
management side cuts the connection and leaves the appliance unreachable for
the rest of the lease. The baseline image ships that rule; the OPNsense
reference in `base_runbooks` documents preserving it across any rewrite of the
filter section.

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
./run-task.sh ./tasks/opnsense-networking/ubuntu24
```

`catalog.toml` is the source of truth. Regenerate the concrete task
directories after editing it:

```bash
uv run --no-project --with tomli python ./scripts/generate_opnsense_networking_tasks.py
```
