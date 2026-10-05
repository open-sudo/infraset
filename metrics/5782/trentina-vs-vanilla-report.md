Scope: scenario `5782`; Trentina `2026-10-02__08-42-41` versus direct `2026-10-01__19-16-34`.

**Trentina performed better:** 347 perfect rewards versus 340, with 5 recorded errors versus 9.

Both directories contain **362 completed trials covering the same tasks**, with matching task checksums. Counts below use trial-level results, excluding duplicate job summaries.

| Reward / outcome | Trentina | Vanilla |
|---|---:|---:|
| **1.0** | **347 (95.9%)** | **340 (93.9%)** |
| 0.9 ≤ reward < 1.0 | 0 | 2 |
| 0.8 ≤ reward < 0.9 | 1 | 1 |
| 0.7 ≤ reward < 0.8 | 2 | 1 |
| 0.6 ≤ reward < 0.7 | 0 | 1 |
| 0.5 ≤ reward < 0.6 | 1 | 1 |
| 0 < reward < 0.5 | 1 | 0 |
| Zero reward | 0 | 2 |
| **No reward recorded** | **10** | **14** |
| **Total** | **362** | **362** |

For **exact scores**, 0.9 occurs **0 / 1** times and 0.8 occurs **0 / 0** times. The 0.8-band results are both 0.8333; vanilla’s other 0.9-band result is 0.9167.

**Execution time**

| Agent execution time | Trentina | Vanilla |
|---|---:|---:|
| Median | 195.41 seconds (3.26 minutes) | 163.89 seconds (2.73 minutes) |
| Average | 268.40 seconds (4.47 minutes) | 276.73 seconds (4.61 minutes) |

Calculated from `agent_execution.finished_at - agent_execution.started_at` for the 360 trials in each set with both timestamps, including timeouts. Two trials in each set have no agent execution timestamps and are excluded. These durations exclude environment setup and verification.

**Errors and incomplete evaluations**

| Error category | Trentina | Vanilla |
|---|---:|---:|
| Agent execution timeout | 3 | 7 |
| RHSM initialization: provider DNS unavailable | 1 | 1 |
| Required Antrieb runbook could not be read | 0 | 1 |
| HTTP transport `ReadError` | 1 | 0 |
| **Total recorded exceptions** | **5** | **9** |
| No reward, but no recorded exception | 5 | 6 |

Errors overlap the reward table: all five trentina errors have no reward; vanilla has eight errors without rewards and one with reward 0.

- **Trentina timeouts:** `disk-quota-almalinux9`, `kernel-module-blacklist-rhel7`, and `boot-kernel-parameter-ubuntu16`, all after 40 minutes. Evidence reports backend access failures, missing observations, and/or expired cluster leases.
- **Trentina infrastructure errors:** `zram-swap-rhel10` failed RHSM initialization because provider DNS was unavailable; `application-log-rotation-ubuntu16` encountered an HTTP read failure.
- **Vanilla timeouts:** password-hash migration, SSH key-only on RHEL10, local package repository on RHEL7, encrypted volume and SSH host certificate on RHEL9, certificate rotation on Ubuntu16, and file integrity on Ubuntu24. Six timed out after 40 minutes; password migration after 30 minutes. Their verifier reports describe expired cluster leases and unavailable node access.
- **Vanilla setup errors:** `config-sync-rhel10` could not read `antrieb/primer`; `cron-access-control-rhel10` failed RHSM initialization because provider DNS was unavailable.

The additional unscored trials mostly reflect **cluster expiration or failed node access**. Trentina also includes an SSH host-certificate task where the node became unreachable after reloading SSH. These are incomplete outcomes, not confirmed zero-reward implementations.

**What caused the lower scores**

| Trentina task | Reward | Verifier finding |
|---|---:|---|
| SSH authentication, Ubuntu24 | 0.8333 | Required documentation contents were not captured |
| Configuration sync, RHEL9 | 0.75 | Manual sync demonstrated; automatic pickup not demonstrated |
| OOM protection, RHEL10 | 0.75 | Tested cgroup-local OOM, not system-wide OOM |
| Network hardening, Ubuntu16 | 0.5 | Loopback hardening incomplete after reboot |
| Password complexity, CentOS Stream10 | 0.25 | Tested password-setting paths bypassed minimum length |

Vanilla’s partial scores involved automatic MinIO healing (0.9), incomplete Thanos outage testing (0.9167), automatic configuration sync (0.75), broken/incomplete SSH controller access (0.625), firewall scope (0.8333), and unverified sudo logging behavior (0.5). Both zero-reward trials involved cluster expiration.

Trentina improved the perfect-score rate by **1.9 percentage points**, with **four fewer exceptions** and **four fewer unscored trials**. **Both sets used `gpt-5.6-sol` as the configured executor model**. This compares Trentina and vanilla execution, not different models.

Sources: [trentina results](../../jobs/5782/2026-10-02__08-42-41), [vanilla results](../../jobs/5782/2026-10-01__19-16-34), using each trial’s `result.json` and `verifier/reward-details.json`.
