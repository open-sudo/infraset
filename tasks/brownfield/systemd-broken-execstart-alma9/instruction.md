`node1` is an AlmaLinux 9 server with an enabled custom service named
`telemetry-heartbeat.service`. The service fails to start following a service
definition change. Restore the existing service to the `active (running)` state by
repairing its unit so that it launches the installed heartbeat program under the
existing `svc-heartbeat` service identity.

While running, the service must refresh
`/run/telemetry-heartbeat/heartbeat` at least once every five seconds. Preserve the
installed program and service identity, and retain the service's existing security
restrictions.

The repaired unit must remain enabled, start automatically, reach `active (running)`,
and continue producing fresh heartbeats after `node1` is rebooted.
