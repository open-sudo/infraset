Build a four-node HTTP service using the managed Ubuntu nodes:

- `node1`, `node2`, and `node3` are Nginx backend servers.
- `node4` is the HAProxy load balancer.

Each backend must provide HTTP on TCP port `5660`, with `/` returning its stable node
identifier: `node1`, `node2`, or `node3`. The load balancer must provide HTTP on TCP
port `80` and distribute requests across every healthy backend.

The service must remain available if any one backend fails. The complete
configuration and service must remain operational after all four nodes are rebooted.
