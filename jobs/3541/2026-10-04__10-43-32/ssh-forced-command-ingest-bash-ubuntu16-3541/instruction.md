Give the uploader on node2 an SSH key that can submit a newline-delimited batch
to node1's ingest account but cannot run arbitrary commands, obtain a shell, or
establish forwarding. Submitted bytes should be stored as separate files under
/srv/legacy2/ssh-forced-command-ingest/received on node1. Preserve existing receipts
and the sample batch. This restricted application identity is separate from
administrative access.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
