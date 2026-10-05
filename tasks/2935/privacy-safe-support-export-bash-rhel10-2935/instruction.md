Repair the support-bundle exporter on node1. Its output should retain timestamps,
event types, and ticket IDs while replacing every email address and auth_token
value with [REDACTED]. Include logs in nested directories and reject symlinks
that lead outside logs/. Source logs and the private sibling file under
/srv/legacy2/privacy-safe-support-export must remain unchanged. The entry point
bin/export takes the output directory as its argument.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
