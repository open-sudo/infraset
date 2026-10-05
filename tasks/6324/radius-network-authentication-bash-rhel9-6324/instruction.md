A legacy access concentrator on node2 needs RADIUS authentication from node1.
Configure a dedicated client secret and the demonstration user in access.txt.
Correct credentials should receive Access-Accept, wrong credentials Access-Reject,
and requests with the wrong client secret should not be accepted. Keep the
handover in /srv/legacy2/radius-network-authentication intact.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
