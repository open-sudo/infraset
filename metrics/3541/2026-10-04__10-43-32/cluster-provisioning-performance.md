# Cluster provisioning performance

Scope: `3541/2026-10-04__10-43-32`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **100 clusters**: median **732 ms**, 95th percentile **1117 ms**, slowest **1213 ms**. 90 of 100 (90%) completed in under a second, and every one completed in under 1.2 seconds.

Provisioning accounts for a median of **0.27%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 70 | 692 ms | 1003 ms | 1119 ms |
| 2 | 1 | 28 | 780 ms | 1186 ms | 1213 ms |
| 3 | 1 | 2 | 838 ms | 895 ms | 895 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
