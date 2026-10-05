The custom `telemetry-heartbeat.service` on the AlmaLinux 9 system `node1`
stopped working after a unit-file change. Repair the service so it runs the
installed heartbeat program as the existing `svc-heartbeat` identity and
refreshes `/run/telemetry-heartbeat/heartbeat` at least every five seconds.

Preserve the program, service identity, and existing service security
restrictions.
