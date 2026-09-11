# Findings calculations

These scripts reproduce the aggregate numbers used in `docs/findings.md` from
the canonical records under `jobs/`.

```bash
python3 scripts/findings/corpus_totals.py
python3 scripts/findings/command_fail_rates.py
python3 scripts/findings/network_outcomes.py
python3 scripts/findings/forceful_commands.py
python3 scripts/findings/repository_urls.py
```

- `corpus_totals.py` counts provisioning attempts, created VMs, LLM runs,
  command requests, pass/fail outcomes, category rates, and hygiene results.
- `command_fail_rates.py` calculates the Linux-release and network-OS rates
  used by the article chart. Its denominator is commands that returned an
  on-node result; reboot-related transport failures and unfinished requests
  are excluded.
- `network_outcomes.py` compares network-device command failures with final
  task outcomes.
- `forceful_commands.py` produces the command-class table in finding 5.
- `repository_urls.py` counts runs that attempted explicit external repository
  configuration and records configured hostnames that later failed DNS.

All scripts use Python's standard library. A run is identified by its canonical
`agent/executor-commands.jsonl`; a provisioning attempt is identified by its
job-level `result.json`. VM totals come from the `nodes` arrays returned in the
saved Antrieb provisioning responses.
