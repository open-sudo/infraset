`node2` serves an application on TCP port 8080 on the private network it
shares with `node1`. `node3` is outside that network. Publish the application
through `node1` so `node3` can reach it on port 8080, without opening the rest
of the private network to `node3`.
