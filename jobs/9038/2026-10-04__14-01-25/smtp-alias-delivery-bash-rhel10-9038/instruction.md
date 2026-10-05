Restore local mail delivery for branch.test on node1. Mail sent from node2 to
helpdesk@branch.test should reach both the alice and bob local mailboxes;
accounts@branch.test should reach bob only. Unknown recipients should be rejected,
and relaying for unrelated domains should be rejected. Preserve the
sample messages and routing handover in /srv/legacy2/smtp-alias-delivery.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
