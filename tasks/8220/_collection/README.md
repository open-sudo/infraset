# bash-ubuntu7

100 tasks for Ubuntu 7.10: 70 single-node and 30 multi-node.
The matching families in `../bash-centos5` have identical task contents except the OS image.

Run this OS dataset:

```sh
./run-task.sh --namespace bash-ubuntu7 --skip-existing ./tasks/bash-ubuntu7
```

Results: [dataset.json](../../jobs/bash-ubuntu7/dataset.json) and [dataset.csv](../../jobs/bash-ubuntu7/dataset.csv).

Regenerate both OS datasets and verify parity:

```sh
uv run --no-project --with tomli python scripts/generate_legacy_tasks.py
uv run --no-project --with tomli python scripts/check_legacy_os_parity.py
```

Original family catalogs are in `scripts/legacy2/catalogs`; the 60 extension families are in `scripts/legacy2/catalog.py`.
Preparation, guest fixture paths, task IDs, and historical execution evidence are preserved.
