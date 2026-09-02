Set up `node1` as an NFSv4 server for `node2` and `node3` over the dedicated
storage network. Export `/srv/nfs/shared` and mount it at `/mnt/shared` on both
clients.

Use the shared identity `sharedops` with UID and GID 4200 on all three systems,
and set the shared directory to `sharedops:sharedops` with mode 2770. Files
created from either client should be immediately available from the other while
retaining their ownership and permissions.
