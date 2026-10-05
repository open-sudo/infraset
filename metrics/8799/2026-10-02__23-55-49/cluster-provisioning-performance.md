# Cluster provisioning performance

Scope: `8799/2026-10-02__23-55-49`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **40 clusters**: median **734 ms**, 95th percentile **1205 ms**, slowest **1267 ms**. 33 of 40 (82%) completed in under a second, and every one completed in under 1.3 seconds.

Provisioning accounts for a median of **0.22%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 30 | 671 ms | 840 ms | 850 ms |
| 2 | 1 | 8 | 1045 ms | 1267 ms | 1267 ms |
| 3 | 1 | 2 | 1186 ms | 1188 ms | 1188 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
