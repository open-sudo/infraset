Configure `node1`, `node2`, and `node3` as a three-member MariaDB Galera
cluster.

All three members must form one Primary component, accept database writes, and
make committed data available through either of the other members. The database
and Galera replication interfaces must be accessible only to the three cluster
members, and the database installation must be secured for production use.

The database must remain available while any one member is unavailable, and a
recovered member must synchronize and return to service automatically. The
complete cluster configuration and service must remain operational after each
node is rebooted.

