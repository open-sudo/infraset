# Cluster provisioning performance

Scope: `2935/2026-10-04__17-37-12`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **100 clusters**: median **805 ms**, 95th percentile **1260 ms**, slowest **1353 ms**. 74 of 100 (74%) completed in under a second, and every one completed in under 1.4 seconds.

Provisioning accounts for a median of **0.22%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 70 | 776 ms | 1174 ms | 1353 ms |
| 2 | 1 | 28 | 846 ms | 1260 ms | 1328 ms |
| 3 | 1 | 2 | 1300 ms | 1343 ms | 1343 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
