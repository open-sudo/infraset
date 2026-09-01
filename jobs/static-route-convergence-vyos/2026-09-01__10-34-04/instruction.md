Configure resilient static routing between the Ubuntu endpoints `node2` and
`node3`, using the direct `primary-transit` network as the preferred path and the
VyOS system `node1` between `lan-a` and `lan-b` as the fallback.

If the direct path fails, restore traffic through `node1` within 10 seconds and
prefer the direct path again when it returns. Preserve endpoint source addresses
and keep the management network outside the routed data plane.
