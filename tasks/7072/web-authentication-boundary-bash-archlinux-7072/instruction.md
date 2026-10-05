On node1, publish the staged public and staff trees under /public/ and /staff/
on TCP port 8080. Public pages are anonymous; staff pages require HTTP Basic
authentication as reader using the demonstration password in access.txt.
Failed authentication must leave staff content inaccessible, and neither the
password file nor directory listings should be served. Keep the supplied pages
under /srv/legacy2/web-authentication-boundary intact.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
