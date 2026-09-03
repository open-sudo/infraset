Configure `node1` as an offline DNF repository for the RHEL 8.8 client
`node2`. Publish `offline-rhel8` over HTTP on TCP port 8080 with `zsh`, its
dependencies, repository metadata, and the public signing key.

Sign the metadata and enforce repository and RPM signature verification on
`node2`. Give `offline-rhel8` priority 10 and other enabled repositories
priority 90 or lower preference. Install `zsh` from the offline repository and
keep it reinstallable with every other repository disabled.
