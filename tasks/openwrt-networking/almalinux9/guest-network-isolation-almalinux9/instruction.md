`lan-a` carries trusted hosts and `lan-b` is for guests; `node2` is on the
first and `node3` on the second, with `node1` between them. Guests must be
able to reach services `node1` itself offers them, such as DNS, but no host
on `lan-b` may open a connection to any host on `lan-a`. Trusted hosts keep
full access in the other direction.
