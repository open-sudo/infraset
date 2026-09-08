Configure PostgreSQL streaming replication across `node1`, `node2`, and
`node3`, using `node1` as the writable primary and the other two systems as
read-only standbys.

Changes committed on the primary should be visible on both standbys.
