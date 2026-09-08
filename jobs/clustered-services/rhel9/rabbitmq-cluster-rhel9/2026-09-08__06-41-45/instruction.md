Join `node1`, `node2`, and `node3` into a single RabbitMQ cluster with a
`payments` virtual host and an application account that can publish and consume
there.

Messages published to a durable queue must survive the loss of any one node and
stay consumable from the remaining nodes.
