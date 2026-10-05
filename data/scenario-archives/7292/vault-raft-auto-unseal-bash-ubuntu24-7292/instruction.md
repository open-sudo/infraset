Build a Vault Transit seal provider on `node1` and a three-member Vault cluster
using integrated Raft storage on `node2`, `node3`, and `node4`. Use validated TLS
and the Transit service to automatically unseal the Raft members after restart.

Enable versioned KV at `secret/`, store `proof=raft-auto-unseal` at
`secret/infraset`, and place administrative access variables in
`/root/vault-admin.env` on each Raft member. Keep the service available when one
Raft member is down and return recovered members to the voter set.
