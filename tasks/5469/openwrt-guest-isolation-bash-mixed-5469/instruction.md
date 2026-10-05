Configure the OpenWrt system `node1` as the gateway for a trusted network
containing `node2` and `node4`, and an isolated guest network containing
`node3`. Provide DHCP, DNS, and internet access to both networks.

On `node2`, serve `infraset-trusted` over HTTP on port 8080 and publish it as
`app.home.test`. Trusted clients should reach the application, while guest
clients remain isolated from the trusted network.
