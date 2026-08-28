Configure routed BGP transit between two Ubuntu 24.04 systems through a SONiC
switch.

`node1` is the SONiC system and uses its existing FRR BGP instance in AS 65100.
`node2` is an FRR peer in AS 65101, and `node3` is an FRR peer in AS 65102. Use
the dedicated `peer-a` and `peer-b` data links for BGP and transit, and keep the
management network outside the routed data plane.

Address both data links and give `node2` and `node3` distinct stable endpoint
prefixes. Establish one eBGP session on each data link. Each Ubuntu peer must
originate only its own endpoint prefix. SONiC must learn both routes and provide
bidirectional transit between the endpoints while preserving their source
addresses.

Limit BGP adjacency and route exchange to the declared data links and prefixes.
The management network remains outside the routed data plane. The FRR sessions,
addressing, routing policy, kernel forwarding state, endpoint reachability, and
host security state must return automatically after all three nodes are rebooted.
