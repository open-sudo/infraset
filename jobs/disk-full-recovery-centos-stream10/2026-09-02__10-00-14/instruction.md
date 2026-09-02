`node1` is a CentOS Stream 10 server whose archive filesystem is full, causing
writes to `/srv/archive/incoming` to fail. Find the unexpected space consumer and
restore write capacity without taking the server offline.

Bring `/srv/archive` below 80% utilization and ensure the existing `archiveapp`
identity can write to the incoming directory. Preserve the filesystem and its
existing archive data.
