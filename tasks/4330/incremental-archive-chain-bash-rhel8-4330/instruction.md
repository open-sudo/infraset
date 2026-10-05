Reconstruct the shipping workspace on node1 from the base archive and ordered
change archives under /srv/legacy2/incremental-archive-chain. Each change archive
contains replacement files; its deletions.txt records paths removed at that stage.
The recovered/ tree must represent the end of day 3, including deletions and the
latest version of changed files. Preserve all recovery media and the order
documented in chain.txt.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
