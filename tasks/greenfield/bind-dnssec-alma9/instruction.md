Configure `node1` as the BIND primary and `node2` and `node3` as authoritative
secondaries for the DNSSEC-signed zone `infra.test` on AlmaLinux 9. Configure
`node4` to resolve the zone through both secondaries.

Publish `app.infra.test` as `10.63.0.50` and the TXT record
`status.infra.test` as `ready`. Permit authenticated dynamic updates from
`node1` using a root-only key at `/root/infra-update.key`. Zone transfers must be
available to the declared secondaries, and normal authoritative queries must be
available throughout the `10.63.0.0/24` DNS network.

Resolution must continue while any one authoritative server is unavailable.
Updates accepted by the primary must propagate automatically to both secondaries.

The signed zone, update authorization, transfers, client resolver configuration,
and service availability must remain operational after all four systems are
rebooted.
