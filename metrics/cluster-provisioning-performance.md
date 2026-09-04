# Cluster provisioning performance

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **246 clusters**: median **965 ms**, 95th percentile **1912 ms**, slowest **2403 ms**. 127 of 246 (52%) completed in under a second, and every one completed in under 2.4 seconds.

Provisioning accounts for a median of **0.36%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 84 | 766 ms | 1517 ms | 2403 ms |
| 2 | 1 | 64 | 816 ms | 1665 ms | 1893 ms |
| 3 | 1 | 16 | 922 ms | 1998 ms | 1998 ms |
| 3 | 2 | 50 | 1354 ms | 1992 ms | 2011 ms |
| 3 | 3 | 24 | 1268 ms | 1931 ms | 1960 ms |
| 4 | 3 | 8 | 1446 ms | 1999 ms | 1999 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
