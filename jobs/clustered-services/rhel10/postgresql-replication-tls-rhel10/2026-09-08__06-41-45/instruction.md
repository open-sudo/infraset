Configure PostgreSQL streaming replication across `node1`, `node2`, and
`node3` with `node1` as the writable primary.

Carry replication traffic over TLS using a certificate authority you create for
this cluster, and accept replication connections only from peers presenting a
certificate issued by that authority.
