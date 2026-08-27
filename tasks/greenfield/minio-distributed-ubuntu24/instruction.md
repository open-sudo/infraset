Configure `node1` through `node4` as one distributed MinIO service on Ubuntu
24.04, using `/srv/minio` on every node. Provide the bucket `infra-data` and the
object `proof.txt` containing `distributed-storage-ready`.

Provide authenticated TLS S3 service on TCP port 9000 using each node name as a
validated TLS identity. Confine storage traffic to the `10.64.0.0/24` storage
network. Provide administrative MinIO Client access from `node1`, with sourceable
credentials at `/root/minio-admin.env` using `MINIO_USER` and `MINIO_PASSWORD`,
and install the issuing CA at `/etc/minio/pki/ca.crt`.

Objects must remain readable and new objects must remain writable while any one
storage node is unavailable. A recovered node must return to the distributed
service automatically with current data.

The service, objects, administrative access, TLS trust, and security controls must
remain operational after all four systems are rebooted.
