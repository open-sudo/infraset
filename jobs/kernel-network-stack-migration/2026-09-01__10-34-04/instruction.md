Migrate `legacy-netapp` from the Ubuntu 16.04 server on `node1` to the Ubuntu
24.04 server on `node2`. Keep the endpoint `legacy-netapp.service.lan` on TCP
port 4180 and preserve its health, identity, and two-worker `SO_REUSEPORT`
behavior.

Expose the migrated service only on `node2`'s application LAN and retain the
legacy stateful, rate-limited firewall policy. Retire the listener and its
application-specific firewall policy from `node1`, while preserving the source
application files and unrelated configuration on both systems.
