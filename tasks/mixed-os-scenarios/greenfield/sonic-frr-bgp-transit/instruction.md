Set up BGP transit through the SONiC system `node1` in AS 65100 between the
Ubuntu FRR peers `node2` in AS 65101 and `node3` in AS 65102. Use the dedicated
`peer-a` and `peer-b` links and keep the management network outside the data
plane.

Give each Ubuntu peer a stable endpoint prefix and have it originate only that
prefix. `node1` should learn both routes and provide bidirectional transit while
preserving the endpoint source addresses.
