On `node1`, export `/srv/nfs/shared` as an NFS share and mount it at `/mnt/shared` on
`node2`. Use the shared identity `dataops` with UID and GID 4500 on both systems, and
set the shared directory to `dataops:dataops` with mode 2770 so files created on
either system keep consistent ownership and permissions.
