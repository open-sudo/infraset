Establish the BRANCH.TEST Kerberos realm on node1 for a legacy application on
node2. Create the user principal analyst and the service principal
reports/node2.branch.test, with a keytab for the application on node2. An analyst
should be able to obtain a ticket for that service; the application keytab must
validate the service ticket. Keep the principal ownership notes under
/srv/legacy2/kerberos-service-identity intact.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
