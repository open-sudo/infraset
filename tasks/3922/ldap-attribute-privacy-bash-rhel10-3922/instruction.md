The HR directory needs field-level privacy. Load the supplied LDIF into LDAP on
node1. The directory-reader identity must be able to search employee names and
mail addresses from node2, but only the HR administrator may read or change the
employeeNumber attribute. Anonymous users should see no employee records.
Retain the supplied records in /srv/legacy2/ldap-attribute-privacy; provision
dedicated demonstration credentials for the reader and administrator.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
