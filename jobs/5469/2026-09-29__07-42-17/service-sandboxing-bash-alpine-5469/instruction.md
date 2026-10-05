On `node1`, run a long-running background worker as a managed service named
`inventory-worker`, confined so it writes only inside `/var/lib/inventory` and
gains no new privileges.
