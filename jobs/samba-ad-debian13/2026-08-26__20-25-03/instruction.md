Configure Debian 13 `node1` and `node2` as replicated Samba Active Directory
domain controllers for the realm `CORP.EXAMPLE` and NetBIOS domain `CORP`.
Configure Debian 13 `node3` as a domain member file server and Debian 13 `node4`
as a joined client. Use the `10.83.0.0/24` identity network for directory, DNS,
Kerberos, and SMB traffic.

Create the group `engineering` and user `infrasetuser`, with `infrasetuser` as a member of
that group. On `node3`, publish an SMB share named `engineering` backed by
`/srv/corp/engineering`. The file `welcome.txt` must contain
`infraset-samba`. Members of `engineering` must be able to create and modify
files while other ordinary domain users have no write access.

Provide sourceable credentials on `node4` at `/root/corp-user.env` using the names
`SAMBA_USER` and `SAMBA_PASSWORD`. The client must obtain Kerberos credentials,
resolve the domain through both controllers, and access the share using the domain
identity.

Authentication, DNS, and share access must continue while either domain controller
is unavailable. A recovered controller must return with current directory and DNS
state.

The domain, replication, identities, DNS, Kerberos, share data, permissions, client
membership, and access controls must remain operational after all four systems are
rebooted.
