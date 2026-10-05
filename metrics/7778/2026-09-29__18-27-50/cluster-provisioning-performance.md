# Cluster provisioning performance

Scope: `7778/2026-09-29__18-27-50`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **10 clusters**: median **1268 ms**, 95th percentile **2000 ms**, slowest **2000 ms**. 2 of 10 (20%) completed in under a second, and every one completed in under 2.0 seconds.

Provisioning accounts for a median of **0.20%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 8 | 1308 ms | 2000 ms | 2000 ms |
| 4 | 1 | 2 | 1094 ms | 1227 ms | 1227 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
