# Cluster provisioning performance

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **519 clusters**: median **925 ms**, 95th percentile **1811 ms**, slowest **2403 ms**. 289 of 519 (56%) completed in under a second, and every one completed in under 2.4 seconds.

Provisioning accounts for a median of **0.34%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 244 | 779 ms | 1337 ms | 2403 ms |
| 2 | 1 | 64 | 816 ms | 1665 ms | 1893 ms |
| 3 | 1 | 118 | 1090 ms | 1883 ms | 2395 ms |
| 3 | 2 | 50 | 1354 ms | 1992 ms | 2011 ms |
| 3 | 3 | 24 | 1268 ms | 1931 ms | 1960 ms |
| 4 | 1 | 11 | 1210 ms | 1882 ms | 1882 ms |
| 4 | 3 | 8 | 1446 ms | 1999 ms | 1999 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
