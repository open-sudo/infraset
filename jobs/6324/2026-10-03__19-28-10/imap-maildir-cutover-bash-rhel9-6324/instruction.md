Move the staged archive mailbox into a working IMAP service on node1 for the
archive account. Node2 should be able to authenticate and retrieve both messages,
preserving their Message-ID values, bodies, and the read/unread state described
in mailbox.tsv. The supplied mailbox under /srv/legacy2/imap-maildir-cutover is
the only copy and must remain intact. Use a dedicated demonstration password.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
