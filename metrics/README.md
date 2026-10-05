# InfraSet metrics

Metrics mirror the job execution folders:

```text
jobs/<scenario-id>/<timestamp>/<task-name>/
metrics/<scenario-id>/<timestamp>/
```

Each timestamp folder contains batch category reports and provisioning metrics.
Task-specific metrics, when present, belong under the matching task name.
Cross-batch comparisons live directly in `metrics/<scenario-id>/`.
Transport and model belong to the execution; different batches remain separate.

## Scenarios

- [2935](2935/)
- [3541](3541/)
- [3922](3922/)
- [4543](4543/)
- [5018](5018/)
- [5469](5469/)
- [5782](5782/)
- [6324](6324/)
- [7403](7403/)
- [7778](7778/)
- [8220](8220/)
- [8350](8350/)
- [8799](8799/)
- [9038](9038/)
- [9622](9622/)

## Generate reports

```bash
python3.11 scripts/rebuild_metrics.py
python3.11 scripts/generate_category_summary.py --scenario 5782 --run 2026-10-02__08-42-41 single-node-os-comparison
python3.11 scripts/generate_provisioning_metrics.py --scenario 5782 --run 2026-10-02__08-42-41
```

Omitting `--run` selects the latest batch. `--runner` is a compatibility alias
for `--scenario`. Explicit `--aggregate` reports are written at scenario level
with an `aggregate-` filename prefix; category aggregates select the latest job
per task, while provisioning aggregates include all observations. These scopes
can mix execution settings and must not be read as one execution.

Historical collection-level aggregates are archived unchanged under
`data/metrics-archives/`; their old links and labels are historical.
The migration record is `data/metrics-layout.json`.
