Node2 needs an HTTP forward proxy on node1, TCP port 3128, for the legacy document
origin running on node2. Permit requests to that origin on TCP port 8081 and
reject other destination ports, including CONNECT tunnels. The staged origin
application in /srv/legacy2/forward-proxy-destination-policy serves the approved
handbook. Preserve it and make it reachable through the proxy from node2.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
