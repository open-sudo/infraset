Build a highly available metrics service on four Ubuntu 24.04 systems. Run
independent Prometheus servers on `node1` and `node2`, with unique replica labels,
and collect host metrics from all four systems. Integrate both servers with Thanos.

Use `node3` to provide one Thanos query endpoint on TCP port 10902 and the store and
compaction services needed for long-term queries. Use `node4` to provide an
S3-compatible HTTPS object store on TCP port 9000 containing the bucket
`thanos-metrics`, with its data under `/srv/thanos-objectstore`. Object-store access
must be authenticated and encrypted. Place `S3_ENDPOINT`, `S3_ACCESS_KEY`,
`S3_SECRET_KEY`, and `S3_CA_CERT` in `/root/thanos-objectstore.env` on `node3`,
readable only by root.

Queries through `node3` must deduplicate the two Prometheus replicas, include current
host metrics from every system, and continue returning historical samples from
object storage when either Prometheus server is unavailable. A recovered server must
return to service automatically without creating duplicate series in query results.

The complete service, retained metrics, authentication, trust, and host security
controls must remain operational after all four systems are rebooted.
