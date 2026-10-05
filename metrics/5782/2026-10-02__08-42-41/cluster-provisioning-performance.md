# Cluster provisioning performance

Scope: `5782/2026-10-02__08-42-41`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **362 clusters**: median **912 ms**, 95th percentile **1836 ms**, slowest **3534 ms**. 227 of 362 (63%) completed in under a second, and every one completed in under 3.5 seconds.

Provisioning accounts for a median of **0.38%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 249 | 836 ms | 1337 ms | 1992 ms |
| 2 | 1 | 68 | 992 ms | 1884 ms | 2108 ms |
| 2 | 2 | 1 | 1419 ms | 1419 ms | 1419 ms |
| 3 | 1 | 25 | 1235 ms | 2156 ms | 3293 ms |
| 3 | 3 | 1 | 2644 ms | 2644 ms | 2644 ms |
| 3 | 4 | 1 | 1674 ms | 1674 ms | 1674 ms |
| 4 | 1 | 11 | 2441 ms | 3534 ms | 3534 ms |
| 4 | 2 | 1 | 2915 ms | 2915 ms | 2915 ms |
| 4 | 3 | 3 | 2342 ms | 2404 ms | 2404 ms |
| 4 | 4 | 2 | 1606 ms | 2305 ms | 2305 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
