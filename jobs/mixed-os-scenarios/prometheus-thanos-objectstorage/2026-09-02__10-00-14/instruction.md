Build a highly available Prometheus and Thanos service across `node1` through
`node4`. Run independent Prometheus replicas on `node1` and `node2`, collect host
metrics from all four systems, and provide the Thanos query, store, and compaction
services on `node3`.

Use an authenticated HTTPS object store on `node4:9000` with the bucket
`thanos-metrics` and data under `/srv/thanos-objectstore`; place its access
variables in `/root/thanos-objectstore.env` on `node3`. Queries on `node3:10902`
should deduplicate replicas and retain historical results when either Prometheus
server is unavailable.
