`node3` sits behind `node1` and `node4` sits behind `node2`, each on its own
private network, and the two switches share a transit link. Have `node1` and
`node2` learn each other's private network through a routing protocol rather
than from routes entered by hand, so `node3` and `node4` reach each other.
