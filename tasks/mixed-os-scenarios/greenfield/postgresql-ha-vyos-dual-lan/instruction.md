Build a highly available PostgreSQL service across two routed LANs. Use the VyOS
system `node1` to route between `lan-a` and `lan-b`, with the initial primary on
`node2` and streaming replicas on `node3` and `node4`.

Create and replicate the `appdb` database over the private LANs. Keep exactly
one writable primary, remain writable when one database node is unavailable,
and automatically return recovered nodes to service.
