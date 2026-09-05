# SONiC networking tasks

Nine switching and fabric scenarios built around a SONiC appliance, each issued
against eight general-purpose Linux operating systems. The appliance is fixed;
only the operating system of the hosts attached to it changes.

SONiC-VS on this platform does not drive an ASIC through SAI. The data plane is
the ordinary Linux kernel — bridge FDB for layer 2, FIB for layer 3 — and the
`Ethernet*` front-panel abstractions in configdb are unbound from the virtio
NICs, so `eth0..ethN` are the real data-plane interfaces. That places these
families on switching ground rather than the perimeter-filtering ground the
VyOS and OpenWrt categories cover: layer-2 domains, VLAN membership, dynamic
routing, and link redundancy.

Three properties of the image shape most of the work. A `docker0` bridge boots
holding an RFC-reserved class-E address that the kernel will otherwise pick as
the source for outbound traffic on the data-plane NICs. An
`interfaces-config.service` reconciler rewrites interface state at boot and
clobbers addresses assigned by hand. And per-interface forwarding defaults off
after bridge operations, so enabling it globally is not enough.

| Task | Difficulty | Topology | Nodes | What it exercises |
|---|---|---|---|---|
| `transparent-l2-bridge` | medium | two-segment | 1 + 2 | Two segments joined into one layer-2 domain, switch not a routed hop |
| `port-isolation` | medium | single-segment | 1 + 2 | Two hosts on one segment kept apart while both reach the switch |
| `vlan-access-segmentation` | hard | two-segment | 1 + 2 | Untagged access ports placing each host in its own VLAN |
| `inter-vlan-routing` | medium | two-segment | 1 + 2 | A routed interface inside each VLAN, forwarding across the boundary |
| `transit-traffic-acl` | medium | two-segment | 1 + 2 | Filtering one port out of traffic passing through the switch |
| `dhcp-relay` | hard | two-segment | 1 + 2 | Address assignment reaching a host on the far segment |
| `configdb-persistence` | medium | two-segment | 1 + 2 | Routed configuration returning by itself after a restart |
| `dynamic-route-exchange` | hard | dual-site | 2 + 2 | Two switches learning each other's network through a protocol |
| `redundant-uplinks` | hard | dual-transit | 2 + 2 | Two parallel links, connectivity surviving either one going away |

The nodes column is appliances plus Linux hosts. Appliances are allocated
first, so `node1` is SONiC in every task and `node1`/`node2` are both SONiC in
the two-appliance families.

Two families are behavioral rather than configuration-only.
`configdb-persistence` has to survive a restart, and `redundant-uplinks` has to
keep two hosts talking across one link being taken out of service. Each is
demonstrated by a single bounded, reversible state change.

A tenth family, `jumbo-frame-path`, was removed after its first campaign. It
asked for an 8000-byte payload to cross the switch unfragmented, and it failed
on all eight operating systems: across those runs no do-not-fragment ping above
2000 bytes ever drew a reply, even where the executor had set an MTU of 9000 on
every interface in the path. The virtual fabric caps the path MTU regardless of
what a guest configures, so the task was unachievable as written and measured
only that ceiling.

`dynamic-route-exchange` carries a constraint worth knowing about: SONiC boots
with FRR already running as AS 65100 with a full Clos template of placeholder
neighbors, and FRR refuses a second autonomous system on the same instance. The
existing instance has to be extended rather than replaced.

## Topologies

Every node carries an always-on `mgmt` network with egress, declared first so
it lands on `eth0`. The task-specific networks carry no egress and no platform
DHCP, so addressing on them is the executor's to arrange.

| Topology | Networks | Shape |
|---|---|---|
| `single-segment` | mgmt, seg | Switch and both hosts on one shared segment |
| `two-segment` | mgmt, seg-a, seg-b | Segments meeting only at the switch, one host on each |
| `dual-site` | mgmt, transit, lan-a, lan-b | Two switches on a transit link, each with its own network and host |
| `dual-transit` | mgmt, transit-a, transit-b, lan-a, lan-b | The same pair joined by two independent links |

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

Run all 9 tasks for one operating system from the repository root:

```bash
./run-task.sh ./tasks/sonic-networking/ubuntu24
```

`catalog.toml` is the source of truth. Regenerate the concrete task
directories after editing it:

```bash
uv run --no-project --with tomli python ./scripts/generate_sonic_networking_tasks.py
```
