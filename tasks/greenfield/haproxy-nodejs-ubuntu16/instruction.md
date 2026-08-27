Configure `node1` as an HTTP reverse proxy using the distribution-supported HAProxy
and Node.js software.

HAProxy must accept HTTP requests on TCP port `80`. Requests for `/` must be
forwarded to a Node.js application on the same node that listens only on the
loopback interface on TCP port `3000`. A successful request to `/` must return HTTP
status `200` with the response body `infraset-nodejs`.

Run both components as persistent system services. The complete configuration and
HTTP service must remain operational after `node1` is rebooted.
