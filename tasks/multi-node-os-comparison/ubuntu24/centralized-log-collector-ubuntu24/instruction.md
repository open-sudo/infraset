On `node2`, forward the `inventory` application's log messages to a centralized log
collector on `node1`. Persist the received messages on `node1` under
`/var/log/inventory/node2.log`, and keep the flow of logs working after either
system restarts.
