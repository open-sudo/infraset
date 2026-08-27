Configure a three-node OpenTelemetry Collector service on Ubuntu 24.04. `node1`
must accept OTLP traces over HTTPS on TCP port 4318 and route them according to the
resource attribute `service.namespace` using the Collector's current routing
mechanism.

Route the value `payments` exclusively to the Collector on `node2`, and route the
value `inventory` exclusively to the Collector on `node3`. Reject telemetry with a
missing or unsupported namespace. Forwarding between Collectors must be mutually
authenticated and encrypted. Retain accepted traces on their selected backend in
`/var/lib/otel/payments.json` on `node2` and `/var/lib/otel/inventory.json` on
`node3` so routing can be audited after a service restart.

Install the client CA, certificate, and private key required to submit evaluation
traffic as `/root/otel-client/ca.crt`, `/root/otel-client/client.crt`, and
`/root/otel-client/client.key` on `node1`, with private material readable only by
root. The services must start automatically and recover buffered work without
cross-routing or duplicate delivery.

Routing behavior, retained telemetry, mutual trust, and security controls must remain
operational after all three systems are rebooted.
