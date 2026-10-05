A restored mail spool on node1 contains duplicate queue entries. Repair bin/replay
under /srv/legacy2/mail-spool-deduplication so it recovers the pending messages
into delivered/, once per Message-ID, without losing distinct messages that have
the same subject. Re-running recovery must skip messages already recorded in delivered/index.tsv. Preserve the original spool and the already-delivered
message; malformed messages belong in quarantine with an explanation.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
