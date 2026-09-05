Run a three-member etcd cluster across `node1`, `node2`, and `node3` holding
application keys.

The member on `node3` is permanently lost and its data cannot be recovered.
Replace it with a working member on that same system so the cluster is back to
three healthy members with the existing keys intact.
