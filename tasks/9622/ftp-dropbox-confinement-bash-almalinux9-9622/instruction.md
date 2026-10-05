A legacy scanner on node2 only supports passive FTP. Set up node1 as its upload
destination with the scanner account described in access.txt, confined to a
dedicated dropbox. It needs to upload and retrieve its files, including the
supplied sample scan, with host files outside that dropbox inaccessible.
Anonymous access should be unavailable. The handover and sample are staged in
/srv/legacy2/ftp-dropbox-confinement on both nodes.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
