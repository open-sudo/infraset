Configure `node1` and `node2` as replicated 389 Directory Server suppliers on
AlmaLinux 9. Use the naming context `dc=infra,dc=test` and make directory
updates converge in both directions.

Provide LDAPS service on TCP port 636 using `node1` and `node2` as validated
TLS identities. Directory and replication traffic must be confined to the
`10.60.0.0/24` directory network. Anonymous access is limited to inspection of
the LDAP root DSE; entries in the naming context require authentication.

Create the POSIX group `infra-admins` with GID `20001` and the POSIX user
`opsuser` with UID and primary GID `20001`, home directory `/home/opsuser`, and
login shell `/bin/bash`. Make `opsuser` a member of `infra-admins`. Permit the
user to update its own `description` attribute while keeping numeric identity
and group membership under administrative control. Store its generated bind
password on `node3` at `/root/opsuser.bindpw` for root-only use, and install the
issuing CA certificate at `/etc/openldap/certs/infra-ca.crt`.

Integrate `node3` with both directory suppliers through SSSD so the directory
user and group resolve through the system identity interfaces. Directory
lookups and authenticated binds from `node3` must continue while either
supplier is unavailable, and a recovered supplier must rejoin with current
directory data.

The directory data, replication, client integration, access controls, and TLS
trust must remain operational after all three systems are rebooted.
