Repair the node1 settlement utility bin/reconcile.py in
/srv/legacy2/cross-file-accounting-reconciliation. Join payments.csv to invoices.csv
by invoice ID, account for multiple payments and credit amounts exactly in cents,
and publish balances.csv with invoice_id and outstanding_cents. Unknown invoice
IDs and malformed amounts belong in rejected.csv with a reason. Preserve the
source files and avoid counting a duplicate payment_id twice.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
