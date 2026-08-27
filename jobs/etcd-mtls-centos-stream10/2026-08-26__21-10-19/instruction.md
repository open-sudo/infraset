Configure `node1`, `node2`, and `node3` as a three-member etcd cluster on
CentOS Stream 10. Keep `node4` available as a replacement system outside the
initial membership.

Protect all client and peer communication with mutually authenticated TLS and
provide administrative client access from `node1` and `node4`. Store
`/infraset/restore-proof` with the value `ready` and maintain a current
recovery snapshot at `/var/backups/etcd/snapshot.db` on `node4`.

The cluster must continue accepting consistent reads and writes while any one
member is unavailable, and recovered members must return to service with
current data. The snapshot must support recovery of the committed cluster
state as a healthy three-member service on `node1`, `node2`, and `node4` when
`node3` is permanently unavailable.

The service, data, access controls, and recovery assets must remain operational
after all four systems are rebooted.
