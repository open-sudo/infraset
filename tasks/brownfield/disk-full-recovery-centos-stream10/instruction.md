`node1` is a CentOS Stream 10 server whose archive-ingestion filesystem has
reached 100% utilization. Writes to `/srv/archive/incoming` are failing. Diagnose
the unexpected space consumer and restore normal write capacity while keeping the
current boot online.

At completion, `/srv/archive` must remain the existing persistent filesystem, its
utilization must be below 80%, and the existing `archiveapp` identity must be able
to write to the incoming directory. Preserve existing archive data, filesystem
mount protections, and host security state.

The recovered capacity, persistent mount, application access, protected state, and
existing data must remain intact after `node1` is subsequently rebooted.
