`node2` and `node3` each serve HTTP on TCP port 8080 on the private network
they share with `node1`, and each returns content identifying which host
answered. Have `node1` present one entry point on TCP port 80 of its
management address that spreads requests across both hosts, and show `node4`
receiving answers from each of them through that entry point.
