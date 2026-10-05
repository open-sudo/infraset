Repair the release publisher on node1 under /srv/legacy2/atomic-release-publication.
bin/publish takes a release directory and updates current to expose that complete
release. Concurrent readers must see either the complete previous release or the
complete new one, with the current path continuously present and complete. Refuse a release missing
MANIFEST and retain the previous current target on rejection. Preserve both
staged releases and keep rollback to either release possible.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
