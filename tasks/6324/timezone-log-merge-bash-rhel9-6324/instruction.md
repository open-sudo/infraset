The node1 incident timeline merges branch logs from different time zones and gets
the event order wrong. Repair bin/timeline.py beneath /srv/legacy2/timezone-log-merge
to write timeline.tsv in UTC chronological order from the supplied timestamped
events. Honor each record's explicit numeric UTC offset, retain event IDs and
messages, and use event ID as the tie-breaker. Preserve all source logs and put
invalid timestamps in rejected.tsv instead of guessing their time zone.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
