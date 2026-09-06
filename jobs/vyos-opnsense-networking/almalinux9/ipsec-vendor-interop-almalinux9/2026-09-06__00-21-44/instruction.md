`node3` sits on `lan-a` behind `node1` and `node4` sits on `lan-b` behind
`node2`, with the two routers reachable to each other only across the
transit network. Establish an IPsec tunnel between `node1` and `node2` and
carry both private networks over it, so `node3` and `node4` reach each other
by their private addresses with that traffic encrypted in transit.
