Connect `lan-a` and `lan-b` through a routed WireGuard tunnel between the two
VyOS systems. Configure `node1` as the `lan-a` gateway at `10.70.1.1`, `node2`
as the `lan-b` gateway at `10.70.2.1`, and use `10.70.255.1/30` and
`10.70.255.2/30` for their respective `wg01` tunnel addresses.

Configure Ubuntu `node3` as `10.70.1.10` and Ubuntu `node4` as `10.70.2.10` on
their private LANs. Provide an HTTP service on `node3` at TCP port 8080 whose
root response contains `lan-a application`. Permit `node4` to use that service
through the tunnel while keeping other new connections between the LANs outside
the declared application path.

The gateways must route without translating addresses. The tunnel and application
path must recover automatically after either gateway or application system
restarts.

The addressing, routes, firewall policy, WireGuard identities, and application
service must remain operational after all four systems are rebooted.
