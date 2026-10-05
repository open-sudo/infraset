Restore the node1 mail-processing entry point bin/deliver beneath
/srv/legacy2/mail-filter-routing. It reads one RFC822 message from standard input.
Messages whose X-Department header is accounts belong in Maildir/accounts/new;
messages tagged support belong in Maildir/support/new; everything else belongs
in Maildir/general/new. Match header names without case sensitivity and leave
each delivered message byte-for-byte intact. Messages with repeated subjects must remain separate deliveries. Retain the staged samples.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
