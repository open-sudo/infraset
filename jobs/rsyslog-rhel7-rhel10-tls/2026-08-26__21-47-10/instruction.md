Configure centralized rsyslog logging across these four systems:

- `node1` is a RHEL 7.9 client.
- `node2` is a RHEL 8.8 client.
- `node3` is a RHEL 9.8 client.
- `node4` is a RHEL 10.0 central logging server.

Install and configure rsyslog on every system. The three clients must forward
the designated application stream (`local0`) to `node4` over TCP with TLS.
The collector must accept TLS syslog traffic on TCP port 6514, authenticate the
collector with a private certificate authority trusted by the clients, and
write records from each client to persistent, source-identifiable central log
files. The central listener should expose no cleartext alternative.

Only the designated `local0` stream is to be centralized. Messages from an
unrelated facility such as `user` should be excluded from the central
application log files. Configure persistent rotation and retention for the
central application logs so that at least seven days of logs are retained and
rotated logs are compressed where the platform supports it.

The services, TLS trust, forwarding, filtering, log destinations, rotation,
and retention policy must all persist after node1 through node4 are rebooted
sequentially. Leave all systems healthy and operational when finished.
