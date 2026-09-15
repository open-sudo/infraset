# Findings calculations

These scripts reproduce the aggregate numbers used in `docs/findings.md` from
the canonical records under `jobs/`.

```bash
python3 scripts/findings/corpus_totals.py
python3 scripts/findings/cluster_vm_totals.py
python3 scripts/findings/pre_command_failures.py
python3 scripts/findings/llm_command_totals.py
python3 scripts/findings/command_fail_rates.py
python3 scripts/findings/network_outcomes.py
python3 scripts/findings/forceful_commands.py
python3 scripts/findings/repository_urls.py
python3 scripts/findings/residue_classification.py
```

- `corpus_totals.py` counts provisioning attempts, created VMs, LLM runs,
  command requests, pass/fail outcomes, category rates, and hygiene results.
- `cluster_vm_totals.py` counts every created cluster and the virtual machines
  listed in its saved provisioning response.
- `pre_command_failures.py` counts provisioned clusters with no recorded LLM
  command request. Use `--list` to print the affected jobs and cluster IDs.
- `llm_command_totals.py` counts every recorded command request issued by the
  LLM and rejects missing or duplicate command IDs.
- `command_fail_rates.py` calculates the Linux-release and network-OS rates
  used by the article chart. Its denominator is commands that returned an
  on-node result; reboot-related transport failures and unfinished requests
  are excluded.
- `network_outcomes.py` compares network-device command failures with final
  task outcomes.
- `forceful_commands.py` produces the command-class table in finding 5.
- `repository_urls.py` counts runs that attempted explicit external repository
  configuration and records configured hostnames that later failed DNS.
- `residue_classification.py` classifies retained executor state as confirmed
  residue, confirmed clean, or indeterminate and counts affected runs by
  residue type. It excludes artifacts created by the mandatory restart-evidence
  protocol. Use `--format tsv` to inspect every decision and its source report.

All scripts use Python's standard library. A run is identified by its canonical
`agent/executor-commands.jsonl`; a provisioning attempt is identified by its
job-level `result.json`. VM totals come from the `nodes` arrays returned in the
saved Antrieb provisioning responses.
