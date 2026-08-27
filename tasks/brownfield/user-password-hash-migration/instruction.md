`node1` is an Ubuntu 16.04 legacy system containing the local users `mira`,
`niko`, and `sana`. Migrate these accounts to the Ubuntu 24.04 system on
`node2`.

Preserve each account's UID, primary group, supplementary group membership,
login shell, password hash, and password-aging state. Users must be able to
authenticate on `node2` with their original passwords without being required to
reset them.

Migrate each complete home directory. Preserve its regular and hidden files,
directory structure, file contents, ownership, group ownership, permissions,
and symbolic links. The original accounts and home directories on `node1` must
remain unchanged.

The source state and the migrated identities, authentication, and home-directory
data must remain intact and usable after both systems are rebooted.
