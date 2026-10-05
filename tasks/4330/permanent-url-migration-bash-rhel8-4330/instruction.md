The help site on node1 has moved from /manual/ to /help/. Serve the staged help
tree on TCP port 8080 and permanently redirect old manual URLs to the corresponding
help URL, retaining the remaining path and query string. Existing /status.txt
requests must still return the supplied status document without a redirect.
Source content is in /srv/legacy2/permanent-url-migration.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
