Run PostgreSQL streaming replication across `node1`, `node2`, and `node3` with
`node1` as the writable primary and the other two systems as standbys.

When the primary is lost, a standby has to take over as the writable primary
without losing committed data, and the recovered former primary has to come
back as a standby of whichever system is primary at that point.
