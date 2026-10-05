Recover the branch's staged print jobs on node1 into a working CUPS queue named
archive. This is an electronic archive printer: completed raw job payloads belong
in /srv/legacy2/print-spool-recovery/printed, one file per job. Process each job
listed in spool/jobs.tsv exactly once, retaining its bytes and the original
spool files. New raw jobs submitted to the queue should follow the same path;
no physical printer is available.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
