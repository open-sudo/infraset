# Cluster provisioning performance

Scope: `5469/2026-09-04__20-11-34`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **80 clusters**: median **1176 ms**, 95th percentile **2022 ms**, slowest **2395 ms**. 25 of 80 (31%) completed in under a second, and every one completed in under 2.4 seconds.

Provisioning accounts for a median of **0.16%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 72 | 1166 ms | 2022 ms | 2395 ms |
| 4 | 1 | 8 | 1301 ms | 1882 ms | 1882 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
