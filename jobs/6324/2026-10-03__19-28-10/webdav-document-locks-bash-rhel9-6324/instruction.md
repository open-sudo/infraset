Provide a WebDAV workspace at /documents/ on node1, TCP port 8080, using the
supplied project documents. The editor account in access.txt should be able to
create, read, replace, and delete documents. Honor exclusive document locks so
an update without the lock token cannot overwrite a locked document. Anonymous
clients may not access the workspace. Preserve the initial project documents
in /srv/legacy2/webdav-document-locks.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
