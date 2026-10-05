Configure PostgreSQL streaming replication across the AlmaLinux 9 systems
`node1`, `node2`, and `node3`. Use `node1` as the writable primary and the other
two systems as read-only standbys.

Replicate committed changes to both standbys over the dedicated database
network and keep PostgreSQL traffic off the management network.
