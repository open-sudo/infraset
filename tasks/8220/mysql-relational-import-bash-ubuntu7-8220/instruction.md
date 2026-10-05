Restore the branch orders database on node1 from the supplied MySQL SQL export
under /srv/legacy2/mysql-relational-import. Keep customer/order relationships,
exact monetary values, and the supplied primary keys. Provide a reporting account
that can read the orders and customers from node2 but cannot change them; the
database administrator should retain write access. Preserve the export.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
