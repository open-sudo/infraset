`node1` is the router for the private network shared by `node2` and `node3`.
Have `node1` hand out addresses on that network, and make sure `node2`
always receives the same address across repeated leases while `node3` is
addressed from the general pool.
