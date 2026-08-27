Configure a routed Kubernetes environment across two isolated LANs:

- `node1` is the VyOS router between `lan-a` (`10.10.1.0/24`) and `lan-b`
  (`10.10.2.0/24`). Its LAN addresses are `10.10.1.254` and `10.10.2.254`.
- `node2` is an Ubuntu 24.04 Kubernetes control-plane node on `lan-a`.
- `node3` and `node4` are Ubuntu 24.04 Kubernetes worker nodes on `lan-b`.

All three Ubuntu nodes must be Ready members of one Kubernetes cluster. Their
Kubernetes node addresses, control-plane communication, and pod data paths must use
the two LANs, with cross-LAN traffic routed by `node1`. Pod-to-pod communication,
cluster DNS, and ClusterIP services must work across the two LANs.

A separate management network is available for software and container-image
acquisition. The Kubernetes control and data paths belong to `lan-a` and `lan-b`.

The VyOS configuration, host routing, Kubernetes services, cluster state, and
cross-LAN workload networking must remain operational after all four nodes are
rebooted.
