Set up `node1`, `node2`, and `node3` as a three-member MariaDB Galera cluster.
Writes made through any member should be available from the other members.

The database should remain readable and writable while one member is unavailable.
When that member returns, it should rejoin automatically with all data written
during its absence.
