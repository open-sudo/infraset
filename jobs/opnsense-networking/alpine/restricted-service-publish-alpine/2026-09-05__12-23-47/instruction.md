`node2` runs an HTTP service on TCP port 8080 on the private network it
shares with `node1`. Publish it on TCP port 80 of `node1`'s management
address so that `node3` reaches it there, while the same published port
stays refused for every other source address.
