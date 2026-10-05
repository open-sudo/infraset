The node1 FIFO consumer exits when its first producer disconnects. Repair
consumer.py in /srv/legacy2/fifo-worker-reconnection so successive producers can
submit newline-delimited job IDs through jobs.fifo without restarting the
consumer. Record each complete line in received.txt, ignore empty lines, and
avoid a busy loop when no producer is connected. Retain the previous records
and provide a clean SIGTERM shutdown.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
