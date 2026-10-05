# Cluster provisioning performance

Scope: `3922/2026-10-03__22-34-06`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **100 clusters**: median **846 ms**, 95th percentile **1425 ms**, slowest **1802 ms**. 59 of 100 (59%) completed in under a second, and every one completed in under 1.8 seconds.

Provisioning accounts for a median of **0.37%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 70 | 768 ms | 1210 ms | 1405 ms |
| 2 | 1 | 28 | 1190 ms | 1523 ms | 1802 ms |
| 3 | 1 | 2 | 1522 ms | 1723 ms | 1723 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
