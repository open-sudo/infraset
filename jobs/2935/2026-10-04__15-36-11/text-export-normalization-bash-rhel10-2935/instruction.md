The node1 records pipeline needs UTF-8 text with LF line endings. Convert the
files in incoming/ according to encodings.tsv, writing matching filenames into
normalized/. Preserve accented characters, empty records, and the final newline
state. Report undecodable input without silently replacing characters or
publishing a partial output. Keep all source files in
/srv/legacy2/text-export-normalization intact.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
