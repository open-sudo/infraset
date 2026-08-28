Configure `node1` as an NFSv4 server and `node2` and `node3` as its clients. The
storage network, and NFS access must be restricted to that network rather than
the management network.

Export `/srv/nfs/shared` from `node1` and mount it at `/mnt/shared` on both
clients. Use a shared system identity named `sharedops` with UID and GID `4200`
on all three nodes. The exported directory must be owned by
`sharedops:sharedops` with mode `2770`.

Files created through either client must be immediately visible through the
other client while retaining their numeric ownership and permissions. The NFS
service, exports, client mounts, access controls, and shared data must remain
fully operational after all three nodes are rebooted.
