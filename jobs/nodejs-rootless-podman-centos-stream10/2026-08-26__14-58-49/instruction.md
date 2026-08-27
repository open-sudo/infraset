Configure `node1`, a CentOS Stream 10 system, to provide a Node.js hello-world application
in a rootless Podman container.

Use `nodeapp` as the application service account and `node-hello` as the
container and service name. The application must return exactly `Hello, world!`
from `/` over TCP port `8080` on the node.

The container must be managed as an enabled service, start without an
interactive user login, and remain fully operational after `node1` is rebooted.
