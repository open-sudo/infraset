Incident `INC-042` has left a three-tier service unavailable. `catalog-api` runs on
`node2` at TCP port 18081, `orders-api` on `node3` at TCP port 18082 depends on it,
and `checkout-api` on `node4` at TCP port 18083 depends on `orders-api`. The complete
request path is consumed from `node1` through `node4`.

Existing Grafana and Loki observability services run on `node1` and are part of
the incident state that must be preserved. Loki contains the incident events emitted
by all three service nodes. Correlate their node labels and timestamps to determine
the originating failure, correct that fault, and restore successful health responses
at every tier and through the complete request path.

Record the originating node, earliest relevant Loki timestamp, and initiating error
in `/root/INC-042-report.txt` on `node1`. Preserve the centralized incident history,
existing catalog data, unrelated service configuration, and the established access
boundaries.

The repaired services, complete request path, incident evidence, report, and host
security controls must remain operational after all four systems are rebooted
sequentially.
