bin/render on node1 works in the developer's login shell but fails in the batch
environment. Repair it so it can run with an empty environment except for
PATH=/usr/bin:/bin, from any working directory. It should find the supplied
branch-format helper and templates, write the requested output file, and retain
the report contents. The application lives under
/srv/legacy2/minimal-environment-job; preserve its source template.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
