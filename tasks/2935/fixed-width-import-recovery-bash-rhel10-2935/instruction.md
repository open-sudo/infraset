The node1 warehouse importer drops records with leading-zero IDs and treats
padded names incorrectly. Repair bin/import.py to convert the staged fixed-width
records into CSV with id, name, and quantity columns. The layout is documented
in layout.txt; preserve ID strings, trim only right-hand name padding, and reject
wrong-length or nonnumeric quantity records into rejects.txt with their line
number. Preserve the original input in /srv/legacy2/fixed-width-import-recovery.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
