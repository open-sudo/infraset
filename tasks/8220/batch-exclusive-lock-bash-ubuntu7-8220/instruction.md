The reconciliation job on node1 sometimes processes the same batch twice when
two operators start it together. Repair bin/reconcile under
/srv/legacy2/batch-exclusive-lock so only one invocation processes pending.tsv
at a time, each batch ID reaches ledger.tsv once, and an interrupted invocation
does not permanently block later work. Preserve existing ledger entries and
leave a clear result when another invocation already owns the job.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
