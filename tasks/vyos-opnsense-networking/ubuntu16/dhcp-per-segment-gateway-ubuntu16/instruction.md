`node1` serves addresses on `lan-a` and `node2` serves addresses on `lan-b`.
Have each router hand its own host an address from its own pool along with
itself as that host's default route, so `node3` and `node4` each obtain
their addressing from the router in front of them rather than from static
configuration.
