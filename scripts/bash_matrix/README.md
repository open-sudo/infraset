# Bash OS comparison matrix

The matrix contains 100 matching task families on each of 15 general-purpose Linux
images: **1,500 tasks**, with 70 single-node and 30 multi-node tasks per OS.
The catalog was retrieved from Antrieb MCP on 2026-10-03; exact image identities
and descriptions are recorded in [images.json](images.json).

| Task folder | Image |
|---|---|
| `tasks/bash-almalinux9` | `almalinux9` |
| `tasks/bash-alpine` | `alpine` (3.23) |
| `tasks/bash-archlinux` | `archlinux` |
| `tasks/bash-centos-stream10` | `centos-stream10` |
| `tasks/bash-centos5` | `centos5.11` |
| `tasks/bash-centos6` | `centos6.10` |
| `tasks/bash-debian13` | `debian13` |
| `tasks/bash-rhel7` | `rhel7.9` |
| `tasks/bash-rhel8` | `rhel8.8` |
| `tasks/bash-rhel9` | `rhel9.8` |
| `tasks/bash-rhel10` | `rhel10.0` |
| `tasks/bash-ubuntu7` | `ubuntu7.10` |
| `tasks/bash-ubuntu12` | `ubuntu12.10` |
| `tasks/bash-ubuntu16` | `ubuntu16.04` |
| `tasks/bash-ubuntu24` | `ubuntu24.04` |

OpenWrt, OPNsense, SONiC, and VyOS are excluded by the requested general-Linux-only
scope. Podman is an application stack on Ubuntu, not an additional OS.

## Comparison and regeneration

`bash-centos5` supplies the established 100-family definitions. The existing
CentOS5/Ubuntu7 datasets and historical jobs are not rewritten. Their existing
generators remain available through `scripts/generate_legacy_tasks.py`.

```sh
uv run --no-project --with tomli python scripts/generate_bash_os_tasks.py
```

The new generator copies exact instructions, task timeouts, and node counts. It
changes the image and strictly necessary initialization. Guest fixture paths retain
their historical `/srv/legacy2` prefix. The wording about retaining the installed
release/kernel is preserved for task parity. Each OS has its own task suffix and
matching job namespace, for example:

```sh
./run-task.sh --namespace bash-debian13 --skip-existing ./tasks/bash-debian13
```

The task runner creates job folders when tasks execute. Generation does not create
results or mark tasks successful.

## Preparation portability

Each OS has 64 brownfield tasks with required baselines and 36 greenfield tasks.
The 60 extension fixtures in the 13 new folders use a POSIX shell implementation
instead of the legacy Python seeder. It uses tools supplied by coreutils or BusyBox:
`base64`, `sha256sum`, `stat`, `touch`, `mktemp`, `dd`, and ordinary file commands.
It does not install packages or depend on a `python`/`python3` executable.

The shell seeder preserves the Python seeder's exact contents, modes, timestamps,
Latin-1 filenames, symbolic links, FIFO, sparse image and SQLite/archive payloads.
It checks file readback and metadata, stages writes in the destination directory,
and refuses symlink directories or unexpected destination types. Setup is safely
repeatable. Baselines hash regular files only and never read FIFOs.

The four original preparations use their existing portable shell commands, with
explicit creation of `/usr/local/bin` before placing the two worker scripts.
Privilege handling checks the execution UID first and uses noninteractive sudo only
when needed. Existing Ubuntu7 tasks retain their root-aware preparation because
their native sudo lacks `-n`.

## Validation and limits

```sh
/home/antrieb-studio/harbor-antrieb/.venv/bin/python scripts/check_bash_os_tasks.py
# Also exercise Alpine tools using a trusted BusyBox binary:
/home/antrieb-studio/harbor-antrieb/.venv/bin/python scripts/check_bash_os_tasks.py --busybox /path/to/busybox
```

Validated on 2026-10-03:

- All 1,500 tasks passed the strict public task validator and instruction/topology parity checks.
- All distinct setup and baseline commands passed shell syntax validation.
- All 60 extension setups executed twice under GNU tools and Alpine 3.23's
  BusyBox 1.37.0-r30, with fixture semantics and read-only baselines checked.
- Shell-generated fixture contents and metadata matched the legacy Python seeder.
- The four original shell setups executed twice under both toolsets using temporary
  paths and the local user's ownership; their baselines were read-only.

These are local preparation compatibility checks, **not live-image execution**.
No managed VMs or executor jobs were launched. Root/sudo access, installed tool
inventory, kernel capabilities and package availability on each deployed image have
not been smoke-tested in this change. Task-specific applications are installed or
repaired by the executor; preparation only stages their initial state. In particular,
RHEL package access may require registration, legacy repositories may be unavailable,
and security/storage tasks depend on the image's kernel facilities. The Antrieb
image descriptions remain the source for platform-specific constraints.

Source discovery used `antrieb/primer`, `antrieb/networking-primer`, the live image
catalog, and the local managed-image baseline builders, including Alpine's builder
which does not install Python. No task-specific verifier artifacts were added.
