Build the Samba Active Directory domain `CORP.EXAMPLE` (`CORP`) with replicated
controllers on `node1` and `node2`, a member file server on `node3`, and a joined
client on `node4`. Use the dedicated identity network for directory, DNS,
Kerberos, and SMB traffic.

Create the `engineering` group and its member `infrasetuser`. Publish
`/srv/corp/engineering` from `node3` as the `engineering` share with
`welcome.txt` containing `infraset-samba`; engineering members should have write
access. Place `SAMBA_USER=infrasetuser` and its `SAMBA_PASSWORD` in
`/root/corp-user.env` on `node4`, and keep authentication, DNS, and share access
available if either controller is down.
