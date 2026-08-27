Configure resilient static routing between two Ubuntu 24.04 systems.

`node1` is the VyOS router. `node2` and `node3` are the Ubuntu endpoints. Use the
following data-plane addressing; the management network remains available for
system management and software acquisition.

| Network | Role | node1 | node2 | node3 |
| --- | --- | --- | --- | --- |
| `primary-transit` (`10.84.0.0/24`) | preferred direct path | — | `10.84.0.2` | `10.84.0.3` |
| `lan-a` (`10.84.1.0/24`) | routed standby, side A | `10.84.1.254` | `10.84.1.10` | — |
| `lan-b` (`10.84.2.0/24`) | routed standby, side B | `10.84.2.254` | — | `10.84.2.10` |

Provide stable endpoint addresses `10.84.10.2/32` on `node2` and
`10.84.10.3/32` on `node3`. Under normal conditions, bidirectional traffic
between these addresses must use `primary-transit`. If the complete
`primary-transit` path becomes unavailable, traffic must resume through `node1`
within 10 seconds. When the path returns, it must automatically become preferred
again.

Use static routing and preserve the endpoint source addresses across both paths.
Keep the management network outside the routed data plane. The addressing,
routing preference, saved VyOS configuration, endpoint reachability, and host
security state must remain operational after all three nodes are rebooted.
