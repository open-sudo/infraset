Build a load-balanced HTTP service with Nginx backends on `node1`, `node2`, and
`node3` and HAProxy on `node4`. Each backend should serve its node identifier
from `/` on port 5660, while HAProxy serves port 80 and distributes requests
across healthy backends.

Keep the service available when any one backend fails.
