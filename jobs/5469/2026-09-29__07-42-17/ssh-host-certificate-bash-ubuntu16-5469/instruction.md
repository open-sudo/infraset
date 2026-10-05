On `node1`, create an SSH certificate authority and have the host present a
certificate signed by it, so a client that trusts the authority connects
without pinning the host key.
