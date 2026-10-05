Build a Redis service across `node1`, `node2`, and `node3`, starting with
`node1` as primary and the other systems as replicas. Configure three Sentinels
to monitor it as `infra-primary`, and store `infra:proof=ready`.

Provide authenticated TLS for Redis on port 6379 and Sentinel on port 26379 over
the cache network, with administrative credentials in
`/root/redis-admin.env` on `node1`. Automatically promote a replica when the
primary is unavailable and return the recovered former primary as a synchronized
replica.
