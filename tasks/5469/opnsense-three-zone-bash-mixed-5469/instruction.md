Configure the OPNsense system `node1` as the gateway between the WAN with
`node4`, the LAN with `node3`, and the DMZ with `node2`.

Serve `infraset-dmz` from `node2` on port 8080. Publish only that service to the
WAN through `node1` on port 8443, and allow LAN clients to reach it directly on
port 8080. Keep the LAN protected from WAN and DMZ-initiated connections.
