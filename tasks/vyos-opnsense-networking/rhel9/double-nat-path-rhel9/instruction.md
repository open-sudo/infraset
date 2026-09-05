`node3` on `lan-a` opens connections to an HTTP service `node4` serves on
TCP port 8080 on `lan-b`. Translate the source address twice along the way,
once on `node1` as traffic enters the transit network and once on `node2` as
it enters `lan-b`, so `node4` records the connection as arriving from
`node2` rather than from `node3` or from `node1`.
