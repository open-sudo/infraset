Resolve incident `INC-042`, which has taken down a three-tier service:
`catalog-api` on `node2:18081`, `orders-api` on `node3:18082`, and
`checkout-api` on `node4:18083`. Use the existing Grafana and Loki services on
`node1` to identify and correct the originating fault, then restore every tier
and the complete request path from `node1`.

Record the originating node, earliest relevant Loki timestamp, and initiating
error in `/root/INC-042-report.txt` on `node1`. Preserve the incident history,
catalog data, and unrelated service configuration.
