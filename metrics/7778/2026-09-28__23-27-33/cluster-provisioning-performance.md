# Cluster provisioning performance

Scope: `7778/2026-09-28__23-27-33`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **80 clusters**: median **1916 ms**, 95th percentile **3426 ms**, slowest **3598 ms**. 0 of 80 (0%) completed in under a second, and every one completed in under 3.6 seconds.

Provisioning accounts for a median of **0.19%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 48 | 1854 ms | 3369 ms | 3598 ms |
| 4 | 3 | 24 | 1840 ms | 3536 ms | 3583 ms |
| 5 | 3 | 8 | 2134 ms | 3347 ms | 3347 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
