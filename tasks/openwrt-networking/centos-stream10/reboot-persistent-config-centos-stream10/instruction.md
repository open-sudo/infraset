`node1` routes the private network shared with `node2` and `node3`. Give
`node1` a fixed address of its own on that network, a DHCP service for the
other two, and a rule refusing TCP port 23 from that network, then show that
every one of those settings is still in place and serving traffic after
`node1` has been restarted.
