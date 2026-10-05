The branch ticket export on node1 restores explicit IDs but leaves its PostgreSQL
sequence behind, causing subsequent inserts to collide. Restore the supplied
tickets.sql into a PostgreSQL database named helpdesk and repair ID allocation.
Existing tickets must keep their IDs and text; new tickets without an explicit
ID must receive unique IDs greater than the imported maximum. Preserve the source
export under /srv/legacy2/postgresql-sequence-repair.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
