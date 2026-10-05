# Cluster provisioning performance

Scope: `2935/2026-10-04__15-36-11`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **100 clusters**: median **788 ms**, 95th percentile **1196 ms**, slowest **1417 ms**. 76 of 100 (76%) completed in under a second, and every one completed in under 1.4 seconds.

Provisioning accounts for a median of **0.25%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 70 | 765 ms | 1169 ms | 1196 ms |
| 2 | 1 | 28 | 871 ms | 1234 ms | 1417 ms |
| 3 | 1 | 2 | 1222 ms | 1262 ms | 1262 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
