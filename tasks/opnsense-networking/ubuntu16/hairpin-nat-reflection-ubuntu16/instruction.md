`node2` runs an HTTP service on TCP port 8080 on the private network shared
with `node1` and `node3`. Publish that service on TCP port 80 of `node1`'s
outward-facing address, and arrange for `node3`, which sits on the same
private network as the service, to reach it through that outward-facing
address rather than by contacting `node2` directly.
