Configure an OpenTelemetry Collector gateway on `node1` to accept OTLP/HTTP over
HTTPS on port 4318 and route traces by the `service.namespace` resource
attribute. Send `payments` traces only to `node2` and `inventory` traces only to
`node3`, rejecting missing or unsupported namespaces.

Use mutual TLS between the collectors. Retain accepted traces in
`/var/lib/otel/payments.json` on `node2` and
`/var/lib/otel/inventory.json` on `node3`, and provide the client credentials
under `/root/otel-client` on `node1`. Avoid cross-routing and duplicate
delivery.
