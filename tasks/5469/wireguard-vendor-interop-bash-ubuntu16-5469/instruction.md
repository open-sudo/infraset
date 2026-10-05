`node1` and `node2` face each other across the transit network, each serving
a private network with one host on it, `node3` and `node4`. Join the two
private networks with a WireGuard tunnel between the routers, so the hosts
reach each other by their private addresses and the traffic between the
routers travels inside the tunnel.
