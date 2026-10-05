Reclaim duplicate payload storage in the release-cache/ tree on node1 beneath
/srv/legacy2/hardlink-aware-deduplication. Identical immutable payload files with
matching ownership and mode may share an inode. Preserve every pathname, byte,
and mode, keep files with different permissions independent, and leave mutable/
files independently writable. A later cache pass should make no further changes.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
