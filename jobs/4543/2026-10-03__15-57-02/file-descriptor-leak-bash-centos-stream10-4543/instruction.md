The node1 document reader exhausts file descriptors during large batches. Repair
bin/read-documents.py beneath /srv/legacy2/file-descriptor-leak so it can process
at least 500 successive reads with a soft open-file limit of 64, returning the
same document length for every read and closing resources on failed opens too.
Keep the supplied document unchanged and retain the command's count argument.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
