Configure PostgreSQL streaming replication across three AlmaLinux 9 nodes.

`node1` must be the writable primary. `node2` and `node3` must be read-only
streaming standbys. Committed database changes on `node1` must become available
on both standbys.

The database network is `10.40.0.0/24`. Any PostgreSQL network access, including
replication traffic, must be confined to that network.

The complete PostgreSQL configuration, replicated data, access controls, and
services must remain operational after each of the three nodes is rebooted.
