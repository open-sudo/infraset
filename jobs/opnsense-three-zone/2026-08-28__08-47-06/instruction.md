Configure `node1` as the OPNsense gateway for three zones:

- WAN: the WAN-facing interface of `node1` and Ubuntu 24.04 `node4`.
- LAN: the LAN-facing interface of `node1` and Ubuntu 24.04 `node3`.
- DMZ: the DMZ-facing interface of `node1` and Ubuntu 24.04 `node2`.

Provide an HTTP service on `node2` at TCP port 8080 whose root response contains
`infraset-dmz`. Publish only that service to the WAN at the WAN address of `node1`
on TCP 8443. LAN clients must also be able to reach `node2` directly on TCP 8080
through the DMZ network.

Permit stateful return traffic while preventing WAN access to the LAN or other DMZ
services and preventing DMZ systems from initiating connections into the LAN.

The addressing, routing, application, firewall policy, and port forwarding must
remain operational after all four systems are rebooted.
