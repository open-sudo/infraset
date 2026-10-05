On `node1`, create a certificate authority named `Fleet Internal CA`. Issue it a TLS
certificate for `node2` and configure `node2` to serve HTTPS on port 8443 with that
certificate. Install the CA as a trusted system certificate authority on both
`node1` and `node2`.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
