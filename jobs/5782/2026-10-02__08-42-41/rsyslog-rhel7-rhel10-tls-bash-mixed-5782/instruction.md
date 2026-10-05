Configure `node1` (RHEL 7.9), `node2` (RHEL 8.8), and `node3` (RHEL 9.8) to
send `local0` messages over TLS to a central rsyslog service on the RHEL 10
system `node4` using TCP port 6514.

Store messages in source-identifiable application logs, exclude unrelated
facilities such as `user`, and provide no cleartext listener. Rotate the central
application logs daily, retain at least seven rotations, and compress rotated
logs.
