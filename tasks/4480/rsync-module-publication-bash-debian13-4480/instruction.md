Publish the release tree on node1 as a read-only rsync daemon module named
releases. Node2 needs to retrieve the full tree with file modes and symlinks
intact. Writes through the module and access outside its tree must be denied.
Preserve the approved release under /srv/legacy2/rsync-module-publication.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
