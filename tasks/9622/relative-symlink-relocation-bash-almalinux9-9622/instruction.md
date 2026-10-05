The report bundle on node1 was copied from a retired server and its absolute
symlinks still refer to /opt/retired-reports. Repair the links in bundle/ under
/srv/legacy2/relative-symlink-relocation so the bundle works in its current
location and when copied to another directory. Preserve the regular files and
the intended targets recorded in links.tsv; links must remain links.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
