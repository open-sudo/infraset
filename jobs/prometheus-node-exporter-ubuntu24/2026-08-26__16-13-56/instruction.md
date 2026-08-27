Configure `node1` as the Prometheus monitoring server for `node2`, `node3`, and
`node4`. Run node_exporter on each of the three Ubuntu 24.04 target systems and
collect their host metrics over its standard TCP port 9100.

Prometheus must identify each target by its node name. All three targets must appear
healthy in the Prometheus targets interface and API, and current node_exporter host
metrics from every target must be queryable on `node1`.

The Prometheus interface on TCP port 9090 is an administrative endpoint local to
`node1`. Limit each node_exporter endpoint to collection by `node1`.

The complete monitoring configuration, target identity, service availability, and
host security controls must remain operational after all four systems are rebooted
sequentially.
