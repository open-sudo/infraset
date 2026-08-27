Configure `node1` as a curated offline DNF repository server for RHEL 8.8 and
`node2` as its client.

Publish the repository as `offline-rhel8` at
`http://node1:8080/offline-rhel8/`. It must contain the RHEL 8 `zsh` package and
all packages required to install or reinstall it, together with valid repository
metadata. Publish the repository's public signing key from the same HTTP service.

Sign the repository metadata with a dedicated GPG key. Preserve and verify the
Red Hat signatures on mirrored RPM packages. Configure `node2` to enforce both
repository-metadata and RPM-package signature verification for `offline-rhel8`.

Set `offline-rhel8` to DNF priority `10`. Every other enabled repository on
`node2` must have a numeric priority of `90` or greater. Install `zsh` on
`node2` from `offline-rhel8`; it must remain reinstallable using only that
repository while all other repositories are disabled.

Restrict the repository HTTP service to its required managed-network access on
TCP port `8080`, while keeping the standard RHEL host security controls
enforcing. The repository service, client configuration, priorities, signature
verification, and offline package consumption must remain operational after both
systems are rebooted.
