# Cluster provisioning performance

Scope: `5018/2026-10-03__17-05-51`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **100 clusters**: median **712 ms**, 95th percentile **1073 ms**, slowest **1369 ms**. 93 of 100 (93%) completed in under a second, and every one completed in under 1.4 seconds.

Provisioning accounts for a median of **0.31%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 70 | 655 ms | 821 ms | 866 ms |
| 2 | 1 | 28 | 873 ms | 1289 ms | 1369 ms |
| 3 | 1 | 2 | 980 ms | 1027 ms | 1027 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
