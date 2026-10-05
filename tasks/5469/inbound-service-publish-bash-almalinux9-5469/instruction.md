`node2` runs an HTTP service on TCP port 8080 on the private network it
shares with `node1`. `node3` is not on that network. Publish the service
through `node1` so that `node3` can reach it on TCP port 80 of `node1`'s
management address, with the service itself staying on the private network.
