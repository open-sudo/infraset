# bash-centos6

100 matched tasks for `antrieb:centos6.10:v1`: 70 single-node and 30 multi-node.
The task instructions, topology sizes and timeouts match `bash-centos5` and `bash-ubuntu7`.
64 tasks have static preparation and required baselines; 36 are greenfield.

Preparation uses POSIX shell, root-or-noninteractive-sudo execution, base64,
SHA256 checks, and GNU/BusyBox-compatible file tools. It requires no Python,
package installation, repository access, or changes to management networking.
Fixture bytes, permissions and timestamps are checked during setup. Existing
fixture paths and business requirements are preserved across operating systems.
The executor remains responsible for task-specific software and services.

```sh
./run-task.sh --namespace bash-centos6 --skip-existing ./tasks/bash-centos6
```

Regenerate with `scripts/generate_bash_os_tasks.py`; validate with
`scripts/check_bash_os_tasks.py`. See [matrix notes](../../scripts/bash_matrix/README.md)
for image coverage, compatibility limits, and the distinction between local
preparation checks and live-image validation.
