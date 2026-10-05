The branch report installer was written for Bash but is invoked through the
system /bin/sh on node1. Make bin/install-report work under POSIX sh, including
when the destination path contains spaces. It should install both supplied
templates with their contents intact, make the launcher executable, and report
failure when the destination cannot be populated. Repeating installation should
be safe. The bundle is in /srv/legacy2/posix-shell-installer.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
