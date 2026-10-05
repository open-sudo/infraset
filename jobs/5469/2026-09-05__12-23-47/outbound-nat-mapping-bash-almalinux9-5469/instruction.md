`node1` routes between `lan-a` and `lan-b`. When `node2` on `lan-a` opens a
connection to `node3` on `lan-b`, have `node3` observe it as arriving from
an address of your choosing on `node1` rather than from `node2`'s own
address, while connections in the other direction keep their original
source.
