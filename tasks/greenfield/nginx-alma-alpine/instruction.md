Configure the distribution-supported Nginx service on all four managed nodes:

- `node1` and `node2` run AlmaLinux 9.
- `node3` and `node4` run Alpine Linux.

Each node must provide a successful HTTP response at `/` over TCP port `6700`. The
Nginx configuration and service must remain operational after every node is
rebooted.
