On `node1`, mount `/tmp` and `/dev/shm` so that program execution, setuid bits,
and device nodes are all ignored there. The settings should survive a reboot.
