The local status service on node1 should be available only to its service owner
statusd and members of status-readers. Repair and operate server.py using the
Unix-domain socket run/status.sock under /srv/legacy2/unix-socket-access-boundary.
A client sending STATUS followed by a newline should receive the supplied status
document; other requests should receive an error. Provision status-reader and
outsider accounts to reflect those access roles. Preserve the status document.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
