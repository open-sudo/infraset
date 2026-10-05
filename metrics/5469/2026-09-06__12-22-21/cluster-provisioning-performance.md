# Cluster provisioning performance

Scope: `5469/2026-09-06__12-22-21`.

Every task in this dataset runs on a disposable cluster that [Antrieb](https://antrieb.sh/) provisions on demand. This page reports how long that takes, measured from the provider's own `provision_time_ms` for each cluster actually created during a recorded job.

Across **1 clusters**: median **1403 ms**, 95th percentile **1403 ms**, slowest **1403 ms**. 0 of 1 (0%) completed in under a second, and every one completed in under 1.4 seconds.

Provisioning accounts for a median of **0.08%** of a trial's total wall clock, so the completion times reported in the per-category metrics are effectively all executor work rather than environment setup.

## By cluster shape

Grouped by what was actually provisioned rather than by operating system: within a single image the spread is wider than the spread between images, so a per-OS breakdown would show host scheduling jitter rather than a property of the image.

| Nodes | Networks | Clusters | Median | 95th pct | Slowest |
|---:|---:|---:|---:|---:|---:|
| 4 | 4 | 1 | 1403 ms | 1403 ms | 1403 ms |

Provisioning stays broadly flat as clusters grow: adding nodes and additional isolated networks moves the median by a few hundred milliseconds rather than by orders of magnitude.
