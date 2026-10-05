`node3` sits behind `node1` on `lan-a` and `node4` sits behind `node2` on
`lan-b`. The two routers share a transit network but the two private
networks have no route between them. Build an encrypted tunnel between
`node1` and `node2` over the transit network and route the private networks
across it, so `node3` and `node4` reach each other by their private
addresses and that traffic is encrypted in transit.
