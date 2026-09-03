Build a Kubernetes cluster across two LANs routed by the VyOS system `node1`.
Use `node2` on `lan-a` as the control plane and `node3` and `node4` on `lan-b` as
workers.

All three Ubuntu systems should be Ready members using the private LANs for
Kubernetes control and data traffic. Provide working cross-LAN pod networking,
cluster DNS, and ClusterIP services, while keeping the management network out of
the Kubernetes data plane.
