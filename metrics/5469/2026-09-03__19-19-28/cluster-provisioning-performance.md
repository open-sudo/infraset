# Cluster provisioning performance

Scope: `5469/2026-09-03__19-19-28`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **40 clusters**: median **1190 ms**, 95th percentile **2006 ms**, slowest **2011 ms**. 1 of 40 (2%) completed in under a second, and every one completed in under 2.0 seconds.

Provisioning accounts for a median of **0.30%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 24 | 1151 ms | 2006 ms | 2011 ms |
| 3 | 3 | 8 | 1080 ms | 1931 ms | 1931 ms |
| 4 | 3 | 8 | 1446 ms | 1999 ms | 1999 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
