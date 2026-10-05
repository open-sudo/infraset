Configure HAProxy on `node1` to serve HTTP on port 80 and forward `/` to a
Node.js application listening only on loopback port 3000. The endpoint should
return HTTP 200 with the body `infraset-nodejs`.

Manage the application as `infraset-nodejs.service`.
