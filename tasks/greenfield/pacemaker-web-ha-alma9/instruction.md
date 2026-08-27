Configure `node1`, `node2`, and `node3` as a Pacemaker and Corosync cluster named
`infraset-ha` on AlmaLinux 9. Use `node1` and `node2` as the service nodes and
`node3` as a quorum member that does not host the application resources.

Provide an Apache HTTP service on TCP port 8080 through the floating address
`10.62.0.50`. A request to `/` must return content containing
`infraset-ha`. Keep the web content under `/srv/ha-web` on storage replicated
between the two service nodes and mounted only where the application is active.

Use watchdog-based self-fencing on every cluster member. Confine cluster
communication, storage replication, and application access to the
`10.62.0.0/24` HA network.

The application and its current content must remain available when either service
node becomes unavailable. A recovered service node must rejoin the cluster with
current storage before it is eligible to host the application again.

The cluster, quorum, fencing, replicated storage, floating address, application,
access controls, and service availability must remain operational after all three
systems are rebooted.
