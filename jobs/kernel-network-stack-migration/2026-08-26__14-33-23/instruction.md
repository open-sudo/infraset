`node1` is an Ubuntu 16.04 legacy server that provides `legacy-netapp` over
TCP port 4180 on its application-facing LAN. Migrate the application and its
network policy to the Ubuntu 24.04 server on `node2`.

Preserve the existing health, identity, and worker endpoint behavior. The
application must continue to use two concurrent, unprivileged workers sharing
the same listener with `SO_REUSEPORT`. Clients must use
`legacy-netapp.service.lan` for the migrated endpoint.

Bind the migrated service only to `node2`'s application-facing address. Permit
TCP port 4180 from the application LAN and reject it through the client LAN,
while preserving the stateful and rate-limited logging behavior of the legacy
firewall policy. Keep Ubuntu 24.04's standard predictable interface naming and
nftables-backed iptables selection.

Retire the active listener and application-specific firewall policy on
`node1`; it will remain available as a client of the migrated service. Preserve
the legacy application files and unrelated configuration on both systems.

The migrated service, endpoint name, firewall behavior, worker model, and
source retirement must remain correct after both systems are rebooted.
