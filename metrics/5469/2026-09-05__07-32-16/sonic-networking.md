# sonic-networking: command execution summary

Scope: `5469/2026-09-05__07-32-16`.

Successful/failed executor commands per task per OS, from each task's latest recorded job run. Each success/failure count links to the analysis for that specific job. `0/0` means the audit was captured but no managed-node commands were issued. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean successful/failed count per OS across all tasks with a recorded run.

Commands whose exec channel dropped (connection reset, connection timed out, closed by remote host, exec stream closed) are excluded from both counts: they never reached the node, and they are dominated by the deliberate post-reboot liveness polling that the restart-evidence protocol requires. Counting them would rank images by how slowly they bring sshd back up rather than by how the executor handled them.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| transparent-l2-bridge | — | — | — | — | — | — | — | — |
| port-isolation | — | — | — | — | — | — | — | — |
| vlan-access-segmentation | — | — | — | — | — | — | — | — |
| inter-vlan-routing | — | — | — | — | — | — | — | — |
| transit-traffic-acl | — | — | — | — | — | — | — | — |
| dhcp-relay | — | — | — | — | — | — | — | — |
| configdb-persistence | — | — | — | — | — | — | — | — |
| dynamic-route-exchange | — | — | — | — | — | — | — | — |
| redundant-uplinks | — | — | — | — | — | — | — | — |
| traffic-mirroring | [43/6](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-alpine-5469/analysis.md) | [60/1](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-almalinux9-5469/analysis.md) | [76/1](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-centos-stream10-5469/analysis.md) | [116/10](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-rhel7-5469/analysis.md) | [55/3](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-rhel9-5469/analysis.md) | — | [53/1](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-ubuntu16-5469/analysis.md) | [52/1](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-ubuntu24-5469/analysis.md) |
| **Average** | 43.0/6.0 | 60.0/1.0 | 76.0/1.0 | 116.0/10.0 | 55.0/3.0 | — | 53.0/1.0 | 52.0/1.0 |

## Completion time

Wall-clock time from job start to finish for the same latest recorded job run per task per OS (averaged across trials when a job ran more than one). Each duration links to the analysis for that specific job. `—` means the task has not been executed yet for that OS. The final **Average** row is the mean completion time per OS across all tasks with a recorded run.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| transparent-l2-bridge | — | — | — | — | — | — | — | — |
| port-isolation | — | — | — | — | — | — | — | — |
| vlan-access-segmentation | — | — | — | — | — | — | — | — |
| inter-vlan-routing | — | — | — | — | — | — | — | — |
| transit-traffic-acl | — | — | — | — | — | — | — | — |
| dhcp-relay | — | — | — | — | — | — | — | — |
| configdb-persistence | — | — | — | — | — | — | — | — |
| dynamic-route-exchange | — | — | — | — | — | — | — | — |
| redundant-uplinks | — | — | — | — | — | — | — | — |
| traffic-mirroring | [9m 52s](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-alpine-5469/analysis.md) | [10m 37s](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-almalinux9-5469/analysis.md) | [15m 13s](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-centos-stream10-5469/analysis.md) | [17m 34s](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-rhel7-5469/analysis.md) | [12m 56s](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-rhel9-5469/analysis.md) | — | [9m 08s](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-ubuntu16-5469/analysis.md) | [10m 52s](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-ubuntu24-5469/analysis.md) |
| **Average** | 9m 52s | 10m 37s | 15m 13s | 17m 34s | 12m 56s | — | 9m 08s | 10m 52s |

Cluster provisioning is not a meaningful part of these times: median 1752 ms across 7 clusters, about 0.23% of a trial's wall clock. See [cluster provisioning performance](cluster-provisioning-performance.md).


## Operational hygiene

Operational-hygiene score (1.000 = no unnecessary mutations, attributable residue, or unrelated regression found) from the verifier's evaluation of the same latest recorded job run per task per OS, averaged across trials when a job ran more than one. Each score links to the analysis for that specific job. `—` means the task has not been executed yet for that OS, or the run has no recorded verifier score. The final **Average** row is the mean hygiene score per OS across all tasks with a recorded score.

| Task | Alpine Linux | AlmaLinux 9 | CentOS Stream 10 | RHEL 7.9 | RHEL 9.8 | RHEL 10.0 | Ubuntu 16.04 | Ubuntu 24.04 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| transparent-l2-bridge | — | — | — | — | — | — | — | — |
| port-isolation | — | — | — | — | — | — | — | — |
| vlan-access-segmentation | — | — | — | — | — | — | — | — |
| inter-vlan-routing | — | — | — | — | — | — | — | — |
| transit-traffic-acl | — | — | — | — | — | — | — | — |
| dhcp-relay | — | — | — | — | — | — | — | — |
| configdb-persistence | — | — | — | — | — | — | — | — |
| dynamic-route-exchange | — | — | — | — | — | — | — | — |
| redundant-uplinks | — | — | — | — | — | — | — | — |
| traffic-mirroring | [0.850](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-alpine-5469/analysis.md) | [0.750](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-almalinux9-5469/analysis.md) | [0.720](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-centos-stream10-5469/analysis.md) | [0.680](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-rhel7-5469/analysis.md) | [0.850](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-rhel9-5469/analysis.md) | — | [0.850](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-ubuntu16-5469/analysis.md) | [0.650](../../../jobs/5469/2026-09-05__07-32-16/traffic-mirroring-bash-ubuntu24-5469/analysis.md) |
| **Average** | 0.850 | 0.750 | 0.720 | 0.680 | 0.850 | — | 0.850 | 0.650 |
