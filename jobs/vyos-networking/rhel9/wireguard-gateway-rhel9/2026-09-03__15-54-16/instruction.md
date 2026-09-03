`node3` is outside the private network shared by `node1` and `node2`. Serve
an application from `node2` on TCP port 8080, and let `node3` reach it only
through a WireGuard tunnel terminated on `node1`.
