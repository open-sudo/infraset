`node1` is an AlmaLinux 9 server in single-user recovery because
`/etc/sudoers` is invalid. Repair sudo and return the server to normal
multi-user operation.

Preserve the existing `opsadmin` account and its non-interactive administrative
access, and leave `/srv/operations/keep.txt` unchanged.
