Set up authoritative DNS for the DNSSEC-signed zone `infra.test`. Use `node1`
as the primary, `node2` and `node3` as secondaries, and configure `node4` to
resolve through both secondaries.

Publish `app.infra.test` as `node1`'s service address and
`status.infra.test` as the TXT value `ready`. Support authenticated updates
from `node1`, propagate changes to both secondaries, and keep resolution
available if one authoritative server is unavailable.
