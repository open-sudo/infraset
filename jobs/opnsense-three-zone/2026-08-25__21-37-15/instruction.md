Configure `node1` as the OPNsense gateway for three zones:

- WAN: `10.80.3.0/24`, with `node1` at `10.80.3.1` and Ubuntu 24.04
  `node4` at `10.80.3.10`.
- LAN: `10.80.1.0/24`, with `node1` at `10.80.1.1` and Ubuntu 24.04
  `node3` at `10.80.1.10`.
- DMZ: `10.80.2.0/24`, with `node1` at `10.80.2.1` and Ubuntu 24.04
  `node2` at `10.80.2.10`.

Provide an HTTP service on `node2` at TCP port 8080 whose root response contains
`infraset-dmz`. Publish only that service to the WAN as
`10.80.3.1:8443`. LAN clients must also be able to reach the service directly at
`10.80.2.10:8080`.

Permit stateful return traffic while preventing WAN access to the LAN or other DMZ
services and preventing DMZ systems from initiating connections into the LAN.

The addressing, routing, application, firewall policy, and port forwarding must
remain operational after all four systems are rebooted.
