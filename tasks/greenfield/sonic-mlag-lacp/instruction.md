Build a redundant Layer 2 fabric with SONiC `node1` and `node2` as the switches and
Ubuntu 24.04 `node3` and `node4` as dual-attached hosts.

Use both inter-switch links for the peer connection. Attach each Ubuntu host to both
switches using LACP, and provide one multi-chassis link aggregation domain named
`infraset-fabric`. Carry VLAN 100 across the fabric. Configure `node3` as
`192.168.100.10/24` and `node4` as `192.168.100.20/24` on their bonded VLAN 100
interfaces.

The two Ubuntu systems must communicate without routing or address translation.
Connectivity must continue while any one host member link, inter-switch member
link, or SONiC switch is unavailable, and restored components must return to active
service automatically.

The switching configuration, peer state, LACP bonds, VLAN membership, addressing,
and failure tolerance must remain operational after all four systems are rebooted.
