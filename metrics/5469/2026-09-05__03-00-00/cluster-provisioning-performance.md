# Cluster provisioning performance

Scope: `5469/2026-09-05__03-00-00`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **72 clusters**: median **2226 ms**, 95th percentile **3441 ms**, slowest **5080 ms**. 0 of 72 (0%) completed in under a second, and every one completed in under 5.1 seconds.

Provisioning accounts for a median of **0.43%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 8 | 1893 ms | 5080 ms | 5080 ms |
| 3 | 3 | 48 | 2278 ms | 3322 ms | 4992 ms |
| 4 | 4 | 8 | 2130 ms | 3379 ms | 3379 ms |
| 4 | 5 | 8 | 2646 ms | 3441 ms | 3441 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
