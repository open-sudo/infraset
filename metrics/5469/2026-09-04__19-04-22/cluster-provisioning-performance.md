# Cluster provisioning performance

Scope: `5469/2026-09-04__19-04-22`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **33 clusters**: median **1054 ms**, 95th percentile **1580 ms**, slowest **1792 ms**. 14 of 33 (42%) completed in under a second, and every one completed in under 1.8 seconds.

Provisioning accounts for a median of **0.20%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 30 | 1066 ms | 1462 ms | 1580 ms |
| 4 | 1 | 3 | 1034 ms | 1792 ms | 1792 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
