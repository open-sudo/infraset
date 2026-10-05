Bring up an LDAP directory on node1 for dc=branch,dc=test and import the staged
LDIF without changing the supplied identities or mail addresses. Node2 must be
able to search the people subtree and find both users. Directory updates require
an authenticated administrator; anonymous writes should fail. The directory
export is in /srv/legacy2/ldap-directory-import.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
