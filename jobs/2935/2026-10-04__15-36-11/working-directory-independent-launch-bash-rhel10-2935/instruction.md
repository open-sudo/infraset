Repair bin/start-report on node1 so the report application loads its own
config/report.conf regardless of the caller's working directory. A caller's
unrelated file with the same relative name should have no effect on the application
configuration. Preserve the existing configuration and business output in
/srv/legacy2/working-directory-independent-launch. The launcher should propagate
application errors to its caller rather than reporting success.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
