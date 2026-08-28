Configure resilient static routing between two Ubuntu 24.04 systems.

`node1` is the VyOS router. `node2` and `node3` are the Ubuntu endpoints. Use the
dedicated `primary-transit`, `lan-a`, and `lan-b` data networks supplied by the
environment. Keep the management network available for system management and
software acquisition, but outside the routed data plane.

Address the data interfaces and give `node2` and `node3` distinct stable private
endpoint addresses. Under normal conditions, bidirectional traffic between those
endpoints must use `primary-transit`. If the complete `primary-transit` path
becomes unavailable, traffic must resume through `node1` within 10 seconds. When
the path returns, it must automatically become preferred again.

Use static routing and preserve the endpoint source addresses across both paths.
Keep the management network outside the routed data plane. The addressing,
routing preference, saved VyOS configuration, endpoint reachability, and host
security state must remain operational after all three nodes are rebooted.
