Repair the node1 status writer so SIGHUP reloads message.conf without terminating
the process or creating a second writer. It should continue appending the current
message to journal.txt, reject an empty configuration while retaining the last
valid message, and exit cleanly on SIGTERM. The application is worker.py beneath
/srv/legacy2/signal-driven-config-reload. Preserve the existing journal entries.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
