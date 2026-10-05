The inventory status endpoint on node1 is intentionally bound only to loopback
on TCP port 9081. Give node2 a persistent SSH tunnel exposing that endpoint on
node2's loopback port 9082. Other cluster hosts should not gain direct access to
either application listener. Preserve the supplied status document and application
under /srv/legacy2/ssh-local-service-tunnel. The tunnel should recover after a
brief SSH connection interruption without manual recreation.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
