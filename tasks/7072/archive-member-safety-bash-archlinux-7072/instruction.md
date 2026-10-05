Repair bin/unpack on node1 so supplier tar packages can be unpacked into incoming/
without writing outside that directory. Ordinary nested files should be accepted;
packages with absolute paths, parent traversal, or symlink-based escapes should
be rejected before any members are installed. The packages under
/srv/legacy2/archive-member-safety include normal and malformed deliveries.
Preserve those source packages and the sibling protected/ files.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
