Set up one distributed MinIO service across `node1` through `node4` using the
dedicated storage network. Provide authenticated TLS S3 access on port 9000 and
create the bucket `infra-data` with `proof.txt` containing
`distributed-storage-ready`.

Provide MinIO Client administration from `node1`. Objects should remain readable
and writable while one storage member is unavailable. When that member returns,
it should rejoin automatically with current data.
