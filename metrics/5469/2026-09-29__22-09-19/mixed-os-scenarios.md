# mixed-os-scenarios: command execution summary

Scope: `5469/2026-09-29__22-09-19`.

Successful/failed executor commands per task per OS/image, from each task's latest recorded job run, split by which node(s) in that task's topology ran each image. Task names link to that run's analysis. Unlike the OS-comparison matrices, each mixed-os-scenarios task has its own bespoke topology, so most rows only populate the column(s) for the image(s) that task actually provisions; `—` means that image was not part of this task's topology.

| Task | Ubuntu 24.04 |
|---|---:|
| [ubuntu24/nfs-ubuntu24](../../../jobs/5469/2026-09-29__22-09-19/nfs-bash-ubuntu24-5469) | 25/1 |
