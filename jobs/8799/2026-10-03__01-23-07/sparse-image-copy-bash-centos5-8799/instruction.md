The node1 disk-image transfer utility bin/copy-image consumes the full logical
size of sparse files. Repair it so copying source.img to a chosen destination
retains the logical length and bytes while preserving holes: the supplied
64 MiB image should occupy less than 2 MiB of allocated space at the destination.
Keep source.img intact and make repeated copying safe. The utility and image
are in /srv/legacy2/sparse-image-copy.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
