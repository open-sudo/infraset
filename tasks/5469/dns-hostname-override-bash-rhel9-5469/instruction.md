`node2` runs an HTTP service on TCP port 8080, reachable over the private
network shared with `node1` and `node3`. Make `node1` answer DNS for that
network so `node3` can reach the service by the name `app.internal` without
any local hosts-file entry.
