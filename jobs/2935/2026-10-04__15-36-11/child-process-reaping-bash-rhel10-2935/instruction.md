The node1 job supervisor leaves finished child processes behind. Repair
supervisor.py under /srv/legacy2/child-process-reaping so it starts the requested
number of short jobs, reaps every child, and records each job's exit status in
results.tsv. Jobs numbered with an even integer succeed; odd-numbered jobs exit
with status 3. Preserve the previous results and keep the supervisor available
until its children have finished.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
