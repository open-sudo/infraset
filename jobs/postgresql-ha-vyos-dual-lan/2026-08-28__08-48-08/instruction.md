Configure a highly available PostgreSQL service across two routed LANs.

`node1` is the VyOS router between `lan-a` and `lan-b`. Configure its interfaces
on both private LANs and keep the management network separate.
`node2` is the initial writable PostgreSQL primary on `lan-a`. `node3` and
`node4` are streaming replicas on `lan-b`.

Create a database named `appdb` and replicate its committed data to the other
database nodes. Database replication and HA coordination must use the routed
LANs. Restrict cross-LAN access to traffic required by the HA service; the
management network is for software acquisition.

The service must remain writable when any one database node is unavailable,
maintain exactly one writable primary, and automatically return recovered nodes
to service. The saved router configuration, host routes, data, HA behavior, and
access controls must remain operational after all four nodes are rebooted.
