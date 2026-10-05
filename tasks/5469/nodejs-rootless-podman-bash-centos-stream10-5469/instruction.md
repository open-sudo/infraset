Run a Node.js hello-world application in a rootless Podman container on the
CentOS Stream 10 system `node1`. Use `nodeapp` as the service account and
`node-hello` as the container and service name.

The application should return exactly `Hello, world!` from `/` on TCP port
8080 without requiring an interactive login to start.
