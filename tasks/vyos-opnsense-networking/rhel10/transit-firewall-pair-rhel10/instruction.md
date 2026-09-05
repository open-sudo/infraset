`node3` sits behind `node1` on `lan-a`, `node4` sits behind `node2` on
`lan-b`, and the two routers face each other across a transit network. Both
routers refuse forwarded traffic by default. Open a path for `node3` to
reach an HTTP service `node4` serves on TCP port 8080, leaving other traffic
between the two networks refused.
