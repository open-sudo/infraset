Configure `node1` as an OpenWrt gateway for a trusted network and an isolated guest
network:

- Trusted: the trusted interface of `node1`, Ubuntu 24.04 `node2`, and Ubuntu
  24.04 `node4`.
- Guest: the guest interface of `node1` and Ubuntu 24.04 `node3`.

Provide DHCP and DNS service for both networks. Publish `app.home.test` as
the trusted address of `node2`. On `node2`, provide an HTTP service at TCP port 8080 whose root
response contains `infraset-trusted`.

Trusted clients must reach the application and use internet services through
`node1`. Guest clients must receive working DNS and internet access through
`node1` while remaining isolated from the trusted network.

The addressing, reservations, name resolution, application, routing, NAT, and
isolation policy must remain operational after all four systems are rebooted.
