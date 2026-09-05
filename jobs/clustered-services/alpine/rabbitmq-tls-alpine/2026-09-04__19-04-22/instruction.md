Run a RabbitMQ cluster across `node1`, `node2`, and `node3` that serves AMQP
over TLS, using a certificate authority you create for this cluster.

Accept only client connections presenting a certificate issued by that
authority, and keep the management interface reachable only from within the
cluster.
