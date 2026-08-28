Connect `lan-a` and `lan-b` through a routed WireGuard tunnel between the two
VyOS systems. Configure `node1` as the `lan-a` gateway and `node2` as the
`lan-b` gateway. Assign unique addresses from a private tunnel subnet to their
respective `wg01` interfaces.

Configure Ubuntu `node3` and `node4` on their respective private LANs. Provide
an HTTP service on `node3` at TCP port 8080 whose
root response contains `lan-a application`. Permit `node4` to use that service
through the tunnel while keeping other new connections between the LANs outside
the declared application path.

The gateways must route without translating addresses. The tunnel and application
path must recover automatically after either gateway or application system
restarts.

The addressing, routes, firewall policy, WireGuard identities, and application
service must remain operational after all four systems are rebooted.
