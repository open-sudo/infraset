Build a Vault deployment on four Ubuntu 24.04 systems. Configure `node1` as an
independent Vault Transit seal provider. Configure `node2`, `node3`, and `node4` as a
three-member highly available Vault cluster using integrated Raft storage and the
Transit service for automatic unsealing.

Provide validated TLS for every Vault API and cluster identity, with the issuing CA
available as `/etc/vault/pki/ca.crt` on every system. Limit the Transit
token to the encrypt and decrypt operations required by the seal key, and keep all
tokens, recovery material, and private keys readable only by their intended service
or by root. Treat the Transit provider's Shamir material as operator-held; automatic
unsealing is required for the Raft members.

Enable a versioned KV service at `secret/` and store `proof=raft-auto-unseal` at
`secret/infraset`. Place sourceable administrative access variables in
`/root/vault-admin.env` on each Raft member, readable only by root. The Raft service
must remain available when any one Raft member is unavailable, elect a replacement
leader when required, and return a recovered member to the voter set automatically.

Configuration and data on the Transit provider must be durable. The Raft cluster,
stored secret, automatic unsealing, authentication, trust, and host security controls
must remain operational after `node2`, `node3`, and `node4` are rebooted sequentially
while the Transit provider is available.
