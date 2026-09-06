#!/usr/bin/env bash
# Re-run the ten cross-vendor cells lost to the executor's stop_sequence exit.
# One task at a time, each conditional on the previous one succeeding, so a
# repeat of the same failure stops the chain instead of burning the rest.
set -u
cd "$(dirname "$0")"

tasks=(
  tasks/vyos-opnsense-networking/ubuntu16/ipsec-vendor-interop-ubuntu16
  tasks/vyos-opnsense-networking/ubuntu16/wireguard-vendor-interop-ubuntu16
  tasks/vyos-opnsense-networking/ubuntu24/transit-firewall-pair-ubuntu24
  tasks/vyos-opnsense-networking/ubuntu24/published-service-two-hops-ubuntu24
  tasks/vyos-opnsense-networking/ubuntu24/split-dns-authority-ubuntu24
  tasks/vyos-opnsense-networking/ubuntu24/dhcp-per-segment-gateway-ubuntu24
  tasks/vyos-opnsense-networking/ubuntu24/ipsec-vendor-interop-ubuntu24
  tasks/vyos-opnsense-networking/ubuntu24/wireguard-vendor-interop-ubuntu24
  tasks/vyos-opnsense-networking/ubuntu24/redundant-path-failover-ubuntu24
  tasks/vyos-opnsense-networking/ubuntu24/policy-based-egress-ubuntu24
)

for t in "${tasks[@]}"; do
  printf '\n=== [%s] %s\n' "$(date '+%H:%M:%S')" "$(basename "$t")"
  if ! ./run-task.sh "$t"; then
    printf '\n!!! [%s] stopped: %s exited non-zero\n' "$(date '+%H:%M:%S')" "$(basename "$t")"
    exit 1
  fi
done

printf '\n=== [%s] all ten completed\n' "$(date '+%H:%M:%S')"
