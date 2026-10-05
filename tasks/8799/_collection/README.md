# bash-centos5

100 tasks for CentOS 5.11: 70 single-node and 30 multi-node.
The matching families in `../bash-ubuntu7` have identical task contents except the OS image.

Run this OS dataset:

```sh
./run-task.sh --namespace bash-centos5 --skip-existing ./tasks/bash-centos5
```

Results: [dataset.json](../../jobs/bash-centos5/dataset.json) and [dataset.csv](../../jobs/bash-centos5/dataset.csv).

Regenerate both OS datasets and verify parity:

```sh
uv run --no-project --with tomli python scripts/generate_legacy_tasks.py
uv run --no-project --with tomli python scripts/check_legacy_os_parity.py
```

Original family catalogs are in `scripts/legacy2/catalogs`; the 60 extension families are in `scripts/legacy2/catalog.py`.
Preparation, guest fixture paths, task IDs, and historical execution evidence are preserved.
