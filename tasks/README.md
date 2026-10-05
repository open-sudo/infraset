# Scenarios

Each task collection has a persistent scenario ID. Tasks are stored as
`<id>/<usecase>-<language>-<os>-<id>/`. Scenario 5782 shares one task set across
direct and Trentina executions; former scenario 7292 is consolidated into it.

| ID | Original collection | Tasks |
| --- | --- | ---: |
| [9622](9622/) | bash-almalinux9 | 100 |
| [5018](5018/) | bash-alpine | 100 |
| [7072](7072/) | bash-archlinux | 100 |
| [4543](4543/) | bash-centos-stream10 | 100 |
| [8799](8799/) | bash-centos5 | 100 |
| [5364](5364/) | bash-centos6 | 100 |
| [4480](4480/) | bash-debian13 | 100 |
| [3922](3922/) | bash-rhel10 | 100 |
| [9038](9038/) | bash-rhel10-admin-prompt | 100 |
| [2935](2935/) | bash-rhel10-admin-prompt-v2 | 100 |
| [8350](8350/) | bash-rhel7 | 100 |
| [4330](4330/) | bash-rhel8 | 100 |
| [6324](6324/) | bash-rhel9 | 100 |
| [5138](5138/) | bash-ubuntu12 | 100 |
| [3541](3541/) | bash-ubuntu16 | 100 |
| [7403](7403/) | bash-ubuntu24 | 100 |
| [8220](8220/) | bash-ubuntu7 | 100 |
| [5469](5469/) | vanilla | 842 |
| [7778](7778/) | vanilla-ansible | 842 |
| [5782](5782/) | vanilla / trentina | 362 |

Run a scenario with `./run-task.sh tasks/<id>`. The runner inherits its ID.
See [metadata documentation](../docs/variant-metadata.md) for the task schema.
