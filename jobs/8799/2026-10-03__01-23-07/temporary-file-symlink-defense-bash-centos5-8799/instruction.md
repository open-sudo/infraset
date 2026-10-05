Repair the invoice export utility bin/export on node1 so concurrent exports use
private temporary files and a pre-existing symlink cannot redirect its writes.
The utility takes an output pathname and exports the supplied invoices.csv.
Successful exports must retain all invoice rows, failures should leave the prior
destination intact, and temporary files should be removed when the utility exits.
The utility and a protected sentinel are under
/srv/legacy2/temporary-file-symlink-defense; preserve the sentinel and source data.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
