Deploy the supplied PostgreSQL stock schema as branch_stock on node1. The stock_app
role on node2 needs to read and update stock quantities but not change schema or
read supplier_costs. The auditor role needs read-only access to stock and
supplier_costs. Establish separate credentials for those roles and preserve the
supplied records in /srv/legacy2/database-reader-writer-roles.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
