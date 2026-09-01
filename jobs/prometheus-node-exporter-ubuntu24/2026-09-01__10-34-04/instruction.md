Configure `node1` as the Prometheus server monitoring `node2`, `node3`, and
`node4` through node_exporter on port 9100. Identify targets by node name and
make current host metrics from all three systems queryable on `node1`.

Keep the Prometheus interface on port 9090 local to `node1`, and limit each
node_exporter endpoint to collection by `node1`.
