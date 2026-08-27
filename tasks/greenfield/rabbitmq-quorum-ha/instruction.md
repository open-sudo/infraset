Configure `node1`, `node2`, and `node3` as one three-member RabbitMQ cluster.
Provide a durable quorum queue named `infraset.events` in the virtual host
`/infraset`, replicated across all three brokers.

Configure `node4` as an AMQP client system. Create a dedicated account named
`infraset-client` with only the permissions needed to publish to and consume from the
declared queue. Place the client endpoints, virtual host, queue name, username, and
generated password in `/root/rabbitmq-client.env` on `node4` as sourceable variables,
with the file readable only by root.

From `node4`, applications must be able to publish persistent messages with
publisher confirmation and consume them through any broker. Confirmed messages and
queue operations must remain available while any one broker is unavailable, and a
recovered broker must return to the cluster and synchronize automatically.

Cluster membership, queue replication, client access, retained messages, and host
security controls must remain operational after all four systems are rebooted
sequentially.
