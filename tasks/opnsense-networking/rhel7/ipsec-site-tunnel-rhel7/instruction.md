`node3` sits behind `node1` on `lan-a` and `node4` sits behind `node2` on
`lan-b`. The two firewalls share a transit network, while the private
networks have no path between them. Build an IPsec tunnel between `node1`
and `node2` and carry the private networks over it, so `node3` and `node4`
reach each other by their private addresses with that traffic encrypted in
transit.
