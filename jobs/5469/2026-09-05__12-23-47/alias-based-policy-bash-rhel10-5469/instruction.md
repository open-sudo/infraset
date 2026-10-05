`node1` routes between `lan-a` and `lan-b`. Permit `node2` to reach `node3`
on TCP ports 8080, 8443 and 9000, expressing that set of ports as a single
named object on `node1` and referring to the object from the rule instead of
writing one rule for each port.
