Run a three-member MariaDB Galera cluster on `node1`, `node2`, and `node3`
holding application data.

Capacity is growing, so add `node4` as a fourth member. It should carry the
data that already exists and accept writes like the other members.
