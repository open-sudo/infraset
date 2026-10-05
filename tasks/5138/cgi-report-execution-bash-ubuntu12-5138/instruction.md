The report bundle staged on node1 was retired after its endpoint exposed the script instead of running it.
Configure a legacy-compatible web service on TCP port 8080 so /cgi-bin/report
executes the supplied report and returns its text output. Static files in public/
should remain available at /; application source and private/ must stay outside
the published content. Use the assets in /srv/legacy2/cgi-report-execution and
preserve the report's business output.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
