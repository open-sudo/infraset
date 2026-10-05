The branch worker on node1 refuses to start after an unclean stop because it
trusts a leftover PID file. Repair bin/control in
/srv/legacy2/stale-pidfile-startup. Its start, stop, and status actions should
distinguish a live worker, a stale PID, and a PID belonging to another process.
Repeated starts should retain a single worker, and stopping it should leave
unrelated processes running. Preserve the worker's existing journal.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
