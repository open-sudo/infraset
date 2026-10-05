The node1 audit writer can hold disk space after its output file has been removed.
Repair writer.py under /srv/legacy2/deleted-open-file-recovery so it can reopen
audit.log on SIGHUP, release its old file descriptor, and continue writing to
the current path without restarting the process. Preserve the existing archive
records. The writer must also close its log and exit cleanly on SIGTERM.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
