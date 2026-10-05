The SQLite catalog application on node1 needs a schema upgrade from v1 to v2.
Repair bin/upgrade.py to retain the existing IDs and descriptions, add a
nonnegative price_cents field initialized to zero, and advance schema_version
only after the whole upgrade succeeds. It must be safe to repeat and leave the
v1 database usable if an upgrade fails. The v1 database and faulty migration
are under /srv/legacy2/transactional-schema-upgrade.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
