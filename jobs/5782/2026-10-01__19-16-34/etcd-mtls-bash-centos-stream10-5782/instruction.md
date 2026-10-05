Build a three-member etcd cluster on `node1`, `node2`, and `node3`, with
`node4` available for administration and backups. Protect client and peer
traffic with mutual TLS.

Store `/infraset/restore-proof=ready` and leave a current recovery snapshot on
`node4`. The cluster should continue serving consistent reads and writes when
one member is unavailable and bring that member back with current data when it
returns.
