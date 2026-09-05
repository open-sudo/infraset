# Cluster provisioning performance

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **759 clusters**: median **1088 ms**, 95th percentile **2774 ms**, slowest **5080 ms**. 321 of 759 (42%) completed in under a second, and every one completed in under 5.1 seconds.

Provisioning accounts for a median of **0.33%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 244 | 779 ms | 1337 ms | 2403 ms |
| 2 | 1 | 64 | 816 ms | 1665 ms | 1893 ms |
| 3 | 1 | 118 | 1090 ms | 1883 ms | 2395 ms |
| 3 | 2 | 146 | 1386 ms | 2852 ms | 5080 ms |
| 3 | 3 | 128 | 1968 ms | 3333 ms | 4992 ms |
| 4 | 1 | 11 | 1210 ms | 1882 ms | 1882 ms |
| 4 | 2 | 8 | 2820 ms | 3428 ms | 3428 ms |
| 4 | 3 | 8 | 1446 ms | 1999 ms | 1999 ms |
| 4 | 4 | 24 | 2101 ms | 3074 ms | 3379 ms |
| 4 | 5 | 8 | 2646 ms | 3441 ms | 3441 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
