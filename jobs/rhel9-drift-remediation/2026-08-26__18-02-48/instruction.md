Remediate four RHEL 9 systems that have drifted from the site's standard
rsyslog configuration. The systems are `node1` through `node4`.

Converge all four systems on the image-provided distribution-supported rsyslog
package and a consistent service configuration. Rsyslog must be enabled and
active on every node, accept TCP syslog on port 5514, and persist `local0`
messages in `/var/log/infraset-app.log`. Keep SELinux enforcing and correct the
labeling and policy needed for the log destination rather than disabling or
bypassing SELinux. Keep firewalld enabled and permit only the required service
access.

The nodes intentionally have inconsistent package, service, configuration, and
SELinux state. Resolve the drift using native RHEL administration tools. Make
the configuration persistent and idempotent: repeating the remediation should
not create duplicate directives, conflicting units, or unnecessary changes.

Each node contains existing application data under
`/var/lib/infraset-app/data/records.db`. Preserve its contents, ownership, and
permissions while repairing the service. Do not replace the data directory with
a new empty directory.

After convergence, reboot all four nodes sequentially. Rsyslog, SELinux, the
firewall policy, the application response, and the existing data must remain
correct without manual repair.
