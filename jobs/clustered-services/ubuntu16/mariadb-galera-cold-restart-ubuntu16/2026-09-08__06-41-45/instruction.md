Run a three-member MariaDB Galera cluster across `node1`, `node2`, and `node3`
holding application data.

The cluster has to come down completely for a maintenance window. Bring it
back afterwards with every committed write still present and all three members
serving again.
