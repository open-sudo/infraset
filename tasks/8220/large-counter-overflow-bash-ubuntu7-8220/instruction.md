The node1 billing accumulator produces negative totals when a byte counter exceeds
the signed 32-bit range. Repair bin/total.py in
/srv/legacy2/large-counter-overflow to sum nonnegative decimal counters exactly,
including totals larger than 4 GiB, and reject invalid or negative records without
publishing a partial total. Keep the counters and the integer-decimal output
interface intact. The same program must work on the installed system architecture.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
