`node2` sits on `lan-a` and `node3` on `lan-b`, with `node1` between them
refusing forwarded traffic by default. Open exactly one path through it: let
`node2` reach `node3` on TCP port 8080, leaving every other flow between the
two networks refused as it already is.
