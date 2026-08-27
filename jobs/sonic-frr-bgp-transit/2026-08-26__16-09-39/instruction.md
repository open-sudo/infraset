Configure routed BGP transit between two Ubuntu 24.04 systems through a SONiC
switch.

`node1` is the SONiC system and uses its existing FRR BGP instance in AS 65100.
`node2` is an FRR peer in AS 65101, and `node3` is an FRR peer in AS 65102. Use
the following data-plane addressing:

| Link | node1 | Ubuntu peer |
| --- | --- | --- |
| `peer-a` (`10.91.0.0/24`) | `10.91.0.254` | `node2`: `10.91.0.10` |
| `peer-b` (`10.92.0.0/24`) | `10.92.0.254` | `node3`: `10.92.0.10` |

Provide stable endpoint address `198.18.201.2/32` on `node2` and
`198.18.202.3/32` on `node3`. Establish one eBGP session on each data link.
`node2` must originate only `198.18.201.2/32`, and `node3` must originate only
`198.18.202.3/32`. SONiC must learn both routes and provide bidirectional transit
between the endpoint addresses while preserving their source addresses.

Limit BGP adjacency and route exchange to the declared data links and prefixes.
The management network remains outside the routed data plane. The FRR sessions,
addressing, routing policy, kernel forwarding state, endpoint reachability, and
host security state must return automatically after all three nodes are rebooted.
