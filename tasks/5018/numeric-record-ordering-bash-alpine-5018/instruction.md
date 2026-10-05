Repair bin/merge on node1 to merge the staged transaction exports into merged.csv.
Order records by the numeric transaction_id, retain quoted fields containing
commas, and emit one header. Duplicate IDs with identical data should collapse
to one row; conflicting duplicate IDs must stop publication and explain the
conflict. Keep the existing output intact on a failed merge. The handover is
under /srv/legacy2/numeric-record-ordering.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
