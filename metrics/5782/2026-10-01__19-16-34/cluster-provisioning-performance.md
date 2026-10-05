# Cluster provisioning performance

Scope: `5782/2026-10-01__19-16-34`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **361 clusters**: median **848 ms**, 95th percentile **1658 ms**, slowest **3320 ms**. 244 of 361 (68%) completed in under a second, and every one completed in under 3.3 seconds.

Provisioning accounts for a median of **0.42%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 249 | 776 ms | 1329 ms | 1886 ms |
| 2 | 1 | 67 | 962 ms | 1515 ms | 1665 ms |
| 2 | 2 | 1 | 782 ms | 782 ms | 782 ms |
| 3 | 1 | 25 | 1272 ms | 1802 ms | 2485 ms |
| 3 | 3 | 1 | 2106 ms | 2106 ms | 2106 ms |
| 3 | 4 | 1 | 1714 ms | 1714 ms | 1714 ms |
| 4 | 1 | 11 | 1454 ms | 2272 ms | 2272 ms |
| 4 | 2 | 1 | 1358 ms | 1358 ms | 1358 ms |
| 4 | 3 | 3 | 1766 ms | 2134 ms | 2134 ms |
| 4 | 4 | 2 | 2116 ms | 3320 ms | 3320 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
