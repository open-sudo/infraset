Connect `lan-a` and `lan-b` through a routed WireGuard tunnel between the VyOS
gateways `node1` and `node2`, using `wg01` on both systems. Keep the routed
traffic free of address translation.

Serve `lan-a application` from `node3` on TCP port 8080 and allow `node4` to
reach it through the tunnel. Limit new cross-LAN connections to this application
path.
