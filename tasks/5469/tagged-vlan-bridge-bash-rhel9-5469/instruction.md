`node1`, `node2` and `node3` share one physical link. Carry two tagged
VLANs, 10 and 20, over that link: place `node2` in VLAN 10 and `node3` in
VLAN 20, each in its own subnet with `node1` as its router. Keep the two
VLANs isolated, so each host reaches `node1` on its own VLAN while traffic
between `node2` and `node3` is refused.
