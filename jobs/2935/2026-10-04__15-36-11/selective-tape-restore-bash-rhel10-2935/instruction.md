On node1, restore the missing invoices named in restore-request.txt from the
supplied tar archive into live/. The live directory also contains a newer
customer register that must retain its current contents. Recover the requested
invoice bytes and file modes without restoring unrelated archived files.
The archive and live data are under /srv/legacy2/selective-tape-restore.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
