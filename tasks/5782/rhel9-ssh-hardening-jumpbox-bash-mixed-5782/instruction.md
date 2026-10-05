Harden OpenSSH on the RHEL 9.8 system `node1`, using `node2` as the authorized
jump box and `node3` as an untrusted client. The prepared `opsadmin` account
must have pinned, non-interactive key access from `sshprobe` on `node2`.

Allow SSH only for members of `ssh-access` using public-key authentication.
Deny direct root access, password-based authentication, the prepared
`contractor` account, and network access from `node3`. Use the dedicated
`ssh-admin` firewalld zone for the jump-box boundary and preserve the prepared
accounts, keys, and data.
