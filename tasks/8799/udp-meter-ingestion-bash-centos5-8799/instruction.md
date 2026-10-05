Branch meters on node2 send UDP datagrams to node1 port 9098 in the format
meter_id,sequence,reading. Repair and run collector.py so valid datagrams append
to readings.csv, duplicate meter/sequence pairs are ignored, and malformed
datagrams are recorded separately without terminating collection. Sequence and
reading are nonnegative decimal integers. Preserve the previously recorded
reading under /srv/legacy2/udp-meter-ingestion, including across collector restarts.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
