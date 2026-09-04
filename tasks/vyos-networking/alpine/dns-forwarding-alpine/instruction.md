Make `node1` the DNS resolver for the private network it shares with `node2`
and `node3`. It should answer for `inventory.internal` with `node2`'s address
on that network and forward everything else upstream. Configure `node2` and
`node3` to resolve through it.
