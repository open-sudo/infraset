Bring the drifted RHEL 9 systems `node1` through `node4` back to the site's
standard rsyslog configuration. Each system should accept TCP syslog on port
5514 and write `local0` messages to `/var/log/infraset-app.log`.

Preserve the existing application data at
`/var/lib/infraset-app/data/records.db` on every node while correcting the
package, service, configuration, and security drift.
