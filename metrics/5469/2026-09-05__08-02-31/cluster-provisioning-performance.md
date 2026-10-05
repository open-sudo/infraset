# Cluster provisioning performance

Scope: `5469/2026-09-05__08-02-31`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **80 clusters**: median **1092 ms**, 95th percentile **1780 ms**, slowest **1950 ms**. 32 of 80 (40%) completed in under a second, and every one completed in under 1.9 seconds.

Provisioning accounts for a median of **0.24%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 56 | 1080 ms | 1780 ms | 1823 ms |
| 3 | 3 | 16 | 1128 ms | 1751 ms | 1751 ms |
| 4 | 4 | 8 | 1126 ms | 1950 ms | 1950 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
