# Cluster provisioning performance

Scope: `8220/2026-10-02__23-55-49`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **40 clusters**: median **572 ms**, 95th percentile **720 ms**, slowest **806 ms**. 40 of 40 (100%) completed in under a second, and every one completed in under 0.8 seconds.

Provisioning accounts for a median of **0.26%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 30 | 557 ms | 644 ms | 660 ms |
| 2 | 1 | 8 | 627 ms | 806 ms | 806 ms |
| 3 | 1 | 2 | 698 ms | 720 ms | 720 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
