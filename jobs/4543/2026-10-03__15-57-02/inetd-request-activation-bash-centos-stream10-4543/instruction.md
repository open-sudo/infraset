A legacy client on node2 expects a one-request-per-connection service on node1,
TCP port 9097. Deploy the supplied stdio handler through inetd or xinetd so each
connection gets its own handler process. PING followed by a newline should
return PONG; other lines should return ERROR. Multiple sequential and concurrent
clients must finish without leaving handler processes behind. Preserve the
protocol notes in /srv/legacy2/inetd-request-activation.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
