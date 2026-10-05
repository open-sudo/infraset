# Cluster provisioning performance

Scope: `6324/2026-10-03__19-28-10`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **99 clusters**: median **790 ms**, 95th percentile **1524 ms**, slowest **1725 ms**. 72 of 99 (73%) completed in under a second, and every one completed in under 1.7 seconds.

Provisioning accounts for a median of **0.34%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 69 | 740 ms | 1098 ms | 1160 ms |
| 2 | 1 | 28 | 1172 ms | 1572 ms | 1725 ms |
| 3 | 1 | 2 | 922 ms | 975 ms | 975 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
