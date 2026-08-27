Migrate the prepared MariaDB database from `node1` (Ubuntu 16.04) to
`node2` (Ubuntu 24.04).

Install and configure a supported MariaDB server on `node2`, migrate the
complete `legacy_shop` database including its schema and all rows, and leave
the destination service enabled and ready for use after reboot. The source on
`node1` is the authoritative legacy system: preserve its database and service
while completing the migration.

The migration must preserve table definitions, primary keys, indexes,
constraints, row values, ordering keys, and the relationships between
customers, orders, order items, and audit events. Transfer the discovered
source state completely rather than using an approximation or recreating rows
from this instruction. Use the managed nodes' available connectivity.

Keep credentials, package caches, dump archives, temporary transfer services,
and migration scripts out of persistent system locations. Remove
migration-only artifacts when finished. The evaluator will inspect the live
systems and reboot the nodes to verify persistence.

The evaluator uses the local MariaDB client and privileged read-only checks;
an evaluator account is unnecessary.
