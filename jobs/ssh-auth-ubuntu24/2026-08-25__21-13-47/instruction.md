Configure key-based, non-interactive SSH access for the non-root user `clusterops`
across `node1`, `node2`, and `node3`.

From each node, `clusterops` must be able to connect non-interactively to each of the
other two nodes using the stable names `node1`, `node2`, and `node3`. Access must be
limited to the managed cluster peers.

The SSH configuration and complete six-path mesh must remain operational after every
node is rebooted.

Create `/usr/local/share/doc/ssh-cluster/OPERATIONS.md` describing the topology and
the operator procedures for verifying all six connections, confirming reboot
persistence, and recovering from an interrupted SSH service.
