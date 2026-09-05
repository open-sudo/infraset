`node2` sits on `lan-a` and `node3` sits on `lan-b`, with `node1` routing
between them. Permit `node2` to reach `node3` on TCP port 5432 and refuse
every other connection between the two networks, in both directions.
