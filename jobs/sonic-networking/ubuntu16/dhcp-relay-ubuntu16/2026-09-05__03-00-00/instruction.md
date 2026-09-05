`node2` runs an address-assignment service for the subnet `node3` belongs
to, but the two hosts sit on different segments of `node1`, so the service's
broadcast traffic stays on `node2`'s segment. Arrange for `node3` to obtain
its address from the service running on `node2`.
