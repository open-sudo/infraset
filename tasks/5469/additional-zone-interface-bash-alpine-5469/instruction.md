`node1` has an interface facing `lan-b` that carries no configuration yet,
and `node3` sits on that network. Bring the interface into service as its
own zone with an address on `lan-b`, so `node3` reaches `node1` there and
reaches `node2` on `lan-a` through it.
