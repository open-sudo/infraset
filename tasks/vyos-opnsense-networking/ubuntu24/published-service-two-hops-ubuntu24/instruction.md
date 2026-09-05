`node4` runs an HTTP service on TCP port 8080 on `lan-b` behind `node2`.
Publish it on TCP port 80 of `node2`'s transit address, and give `node1` a
route to that address, so `node3` on `lan-a` reaches the service by asking
`node2` rather than by addressing `node4` itself.
