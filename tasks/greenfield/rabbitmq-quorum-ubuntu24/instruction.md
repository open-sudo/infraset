Configure `node1`, `node2`, and `node3` as a RabbitMQ cluster named
`infra-rabbit` on Ubuntu 24.04. Provide the virtual host `/infra` and the durable
quorum queue `infra.jobs`.

Provide authenticated TLS access to AMQP on TCP port 5671 and to the management
API on TCP port 15671. Use the node names as validated TLS identities and confine
messaging and cluster traffic to the `10.61.0.0/24` messaging network. Provide
sourceable operator credentials on `node1` at `/root/rabbitmq-operator.env` using
the names `RABBITMQ_USER` and `RABBITMQ_PASSWORD`, and install the issuing CA at
`/etc/rabbitmq/pki/ca.crt`.

Publishers and consumers must continue using `infra.jobs` while any one broker is
unavailable. A recovered broker must return to the cluster with the current queue
state.

The cluster, queue, access controls, TLS trust, and operator access must remain
operational after all three systems are rebooted.
