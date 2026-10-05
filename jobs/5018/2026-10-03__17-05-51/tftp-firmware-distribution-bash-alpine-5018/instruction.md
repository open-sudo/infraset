The boot controller on node2 needs to download boot.cfg and firmware.bin from
node1 using TFTP. Publish the staged boot tree as a read-only TFTP root, preserving
the firmware bytes. Upload attempts and requests outside the boot root should
be rejected. The approved files are in /srv/legacy2/tftp-firmware-distribution.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
