Build a three-member etcd cluster across `node1`, `node2`, and `node3`. A key
written through any member must be readable from the others.

The cluster should keep serving reads and writes while one member is
unavailable, and bring that member back up to date when it returns.
