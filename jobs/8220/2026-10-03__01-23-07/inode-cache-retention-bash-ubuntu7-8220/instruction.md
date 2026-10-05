The node1 thumbnail cache contains hundreds of obsolete tiny files. Repair
bin/prune so it removes only cache entries absent from active.txt and older than
the cutoff epoch supplied as its argument. Keep active entries, newer inactive
entries, non-cache files, and the source media unchanged; symbolic links should
be handled as links rather than followed. The fixture and timestamp policy are
in /srv/legacy2/inode-cache-retention.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
