# Cluster provisioning performance

Scope: `8220/2026-10-03__01-23-07`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **60 clusters**: median **568 ms**, 95th percentile **656 ms**, slowest **725 ms**. 60 of 60 (100%) completed in under a second, and every one completed in under 0.7 seconds.

Provisioning accounts for a median of **0.23%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 40 | 561 ms | 626 ms | 629 ms |
| 2 | 1 | 20 | 580 ms | 725 ms | 725 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
