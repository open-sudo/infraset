Configure `node1`, `node2`, and `node3` as a three-member MariaDB Galera
cluster. Writes through any member should be available from the other members.

Keep the database available when one member is unavailable, and resynchronize
that member automatically when it returns.
