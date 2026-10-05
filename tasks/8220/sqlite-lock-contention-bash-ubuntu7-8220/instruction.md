The local reservation utility on node1 fails or loses changes when two clients
reserve stock at once. Repair bin/reserve.py beneath
/srv/legacy2/sqlite-lock-contention. A request takes a unique request ID and
positive quantity; successful requests decrement remaining stock exactly once.
Repeating a successful ID should return its earlier result, insufficient stock
should be rejected, and competing requests must keep remaining stock nonnegative. Preserve existing
reservations and use bounded lock waits rather than hanging indefinitely.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
