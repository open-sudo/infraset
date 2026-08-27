Configure `node1` as a production HashiCorp Vault service and `node2` as a
PostgreSQL service. Vault must provide a hostname-validating HTTPS API at
`https://node1:8200`, and PostgreSQL must accept TLS-authenticated connections from
the Vault system and its local application client.

Create PostgreSQL database `infraset` with table `public.credential_probe`. Enable
Vault's database secrets engine at `database/`, configure PostgreSQL connection
`pg-main`, and publish dynamic role `infraset-app`. Each credential request through
`database/creds/infraset-app` must create a unique PostgreSQL login with only the
permissions needed to select, insert, update, and delete rows in
`public.credential_probe`. Use a default lease of 30 seconds and a maximum lease of
60 seconds. Revoking a returned lease must invalidate its login immediately, and an
expired lease must cease authenticating without operator intervention.

Place sourceable client variables in `/root/infraset-client.env` on `node1`. Include
`VAULT_ADDR`, `VAULT_CACERT`, `VAULT_TOKEN`, `PGHOST`, `PGPORT`, `PGDATABASE`,
`PGSSLMODE`, and `PGSSLROOTCERT`. The Vault token must have only the capabilities
needed to inspect the declared dynamic role, request its credentials, and revoke
returned leases. Protect this file for root-only access.

The Vault configuration and storage, database secrets-engine configuration,
PostgreSQL data, TLS trust, credential lifecycle, authentication, and host security
controls must remain operational after both systems are rebooted sequentially.
