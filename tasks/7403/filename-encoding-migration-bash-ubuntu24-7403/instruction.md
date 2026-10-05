Convert the staged Latin-1 filenames in imported/ on node1 into UTF-8 filenames
under converted/, retaining their directory structure and file contents. The
export and its filename inventory are under /srv/legacy2/filename-encoding-migration.
Preserve the imported tree. A collision with an existing UTF-8 destination must
be reported without overwriting that destination or silently dropping a source.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
