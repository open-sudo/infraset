Restore the staged branch ledger on node1 as a MySQL database and establish node2
as a read-only application replica. Committed inserts on node1 should arrive on
node2. After a short replica disconnect, it must catch up without losing or
duplicating ledger rows. Use a replication-only account, retain the original
ledger IDs and amounts, and preserve the export in
/srv/legacy2/mysql-replication-catchup. Node1 remains the sole application writer.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
