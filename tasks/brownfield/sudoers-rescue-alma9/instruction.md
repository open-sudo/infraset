`node1` is an AlmaLinux 9 server currently in single-user recovery after
`/etc/sudoers` became syntactically invalid. Restore secure administrative
operation and return the server to its normal multi-user operating state.

The existing `opsadmin` account and its current sudo authorization are required
system state. Preserve that account and authorization, and preserve
`/srv/operations/keep.txt` unchanged. The account must retain non-interactive
administrative access through sudo after recovery. SELinux and the host firewall
must be active in the recovered system.

The server must boot into normal multi-user operation, remain manageable, and
retain the repaired sudo configuration, administrative access, protected host
state, and existing operations data after an additional reboot.
