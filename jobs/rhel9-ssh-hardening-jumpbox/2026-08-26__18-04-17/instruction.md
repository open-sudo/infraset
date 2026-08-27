Harden the OpenSSH service on the RHEL 9.8 system `node1`. Use `node2` as the
authorized jump box and treat `node3` as an untrusted client.

The prepared `opsadmin` account on `node1` is a member of `ssh-access` and must
have non-interactive key-based access from the prepared `sshprobe` account on
`node2` using the stable name `node1` and pinned host-key verification.

OpenSSH on `node1` must accept user authentication only by public key. Direct
root login, password authentication, and keyboard-interactive authentication
must be disabled. Membership in `ssh-access` must be required for SSH login.
The prepared `contractor` account is outside that group and must be denied even
though it retains a valid prepared key and local password.

On `node1`, create a persistent firewalld zone named `ssh-admin`. The zone must
permit the SSH service only from `node2`'s managed address. Other active zones
must keep SSH closed, confining its exposure to `ssh-admin`. `node3`, which has
the same valid probe key as the jump box, must be unable to establish TCP port
22 access to `node1`.

Preserve the prepared users, group memberships, local password state,
authorized keys, client probe identities, pinned host keys, and home-directory
marker files. Keep SELinux enforcing and the required services enabled.

The allowed jump-box access, authentication restrictions, group policy,
firewall-zone boundary, prepared state, and host-key verification must remain
effective after all three systems are rebooted.
