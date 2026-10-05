# Cluster provisioning performance

Scope: `trentina/aggregate`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **842 clusters**: median **1041 ms**, 95th percentile **2912 ms**, slowest **5324 ms**. 401 of 842 (48%) completed in under a second, and every one completed in under 5.3 seconds.

Provisioning accounts for a median of **0.27%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 249 | 733 ms | 1084 ms | 1550 ms |
| 2 | 1 | 132 | 989 ms | 1644 ms | 2011 ms |
| 2 | 2 | 1 | 1457 ms | 1457 ms | 1457 ms |
| 3 | 1 | 113 | 965 ms | 1795 ms | 2180 ms |
| 3 | 2 | 128 | 1335 ms | 2578 ms | 3391 ms |
| 3 | 3 | 81 | 1902 ms | 2936 ms | 3868 ms |
| 3 | 4 | 1 | 1078 ms | 1078 ms | 1078 ms |
| 4 | 1 | 19 | 1221 ms | 2977 ms | 2977 ms |
| 4 | 2 | 9 | 2651 ms | 3944 ms | 3944 ms |
| 4 | 3 | 11 | 1479 ms | 2141 ms | 2141 ms |
| 4 | 4 | 82 | 2572 ms | 3483 ms | 5132 ms |
| 4 | 5 | 16 | 2589 ms | 5324 ms | 5324 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
