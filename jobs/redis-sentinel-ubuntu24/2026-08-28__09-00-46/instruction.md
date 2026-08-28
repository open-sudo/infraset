Configure a Redis service on all three Ubuntu 24.04 systems. Start with `node1`
as the primary and `node2` and `node3` as replicas. Configure three Sentinels to
monitor the service under the name `infra-primary`, and store the key
`infra:proof` with the value `ready`.

Provide authenticated TLS client service on TCP port 6379 and authenticated TLS
Sentinel service on TCP port 26379. Use the node names as validated TLS identities
and confine Redis, replication, and Sentinel traffic to the dedicated cache
network. Provide sourceable administrative credentials on `node1` at
`/root/redis-admin.env` using the name `REDIS_PASSWORD`, and install the issuing
CA at `/etc/redis/pki/ca.crt`.

Sentinel must promote a replica when the primary becomes unavailable. Clients must
be able to discover and write to the promoted primary, and a recovered former
primary must return as a synchronized replica.

The data, replication, automatic failover, authentication, TLS trust, and service
configuration must remain operational after all three systems are rebooted.
