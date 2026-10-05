#!/usr/bin/env python3
"""Generate the 60 extension families within the merged legacy suite."""
from __future__ import annotations

import base64
import io
import json
import sqlite3
import tarfile
import tempfile
from pathlib import Path
from scenario_layout import resolve_task_path

from legacy2.catalog import FAMILIES

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / 'tasks'
SYSTEMS = {'centos5': 'centos5.11', 'ubuntu7': 'ubuntu7.10'}
EPOCH = 1700000000
SENTINEL = '#!/bin/sh\necho "InfraSet requires the configured Harbor-Antrieb verifier." >&2\nexit 1\n'
TASK = '''schema_version = "1.4"

[metadata]
author_name = "InfraSet"
difficulty = "hard"
category = "infrastructure"

[agent]
timeout_sec = 2400

[verifier]
timeout_sec = 1200
environment_mode = "shared"

[environment]
network_mode = "public"
'''
PREAMBLE = '''set -eu
PATH=/usr/sbin:/usr/bin:/sbin:/bin
export PATH
LC_ALL=C
export LC_ALL
as_root() {
  if [ "$(id -u)" -eq 0 ]; then
    "$@"
  else
    sudo -n "$@"
  fi
}
'''


def b64(value: bytes) -> str:
    return base64.b64encode(value).decode('ascii')


def tar_bytes(members: dict) -> bytes:
    result = io.BytesIO()
    with tarfile.open(fileobj=result, mode='w', format=tarfile.USTAR_FORMAT) as archive:
        # Preserve author order: the intentionally unsafe packages include a safe
        # member first to exercise rejection before partial extraction.
        for name, content in members.items():
            info = tarfile.TarInfo(name)
            info.uid = info.gid = 0
            info.uname = info.gname = 'root'
            info.mode = 0o644
            info.mtime = EPOCH
            if isinstance(content, dict):
                info.type = tarfile.SYMTYPE
                info.linkname = content['symlink']
                archive.addfile(info)
            else:
                data = content.encode('utf-8')
                info.size = len(data)
                archive.addfile(info, io.BytesIO(data))
    return result.getvalue()


def sqlite_bytes(schema: str) -> bytes:
    with tempfile.TemporaryDirectory(prefix='legacy2-sqlite-') as directory:
        path = Path(directory) / 'fixture.db'
        connection = sqlite3.connect(path)
        try:
            connection.execute('PRAGMA page_size=1024')
            connection.execute('PRAGMA journal_mode=DELETE')
            connection.executescript(schema)
            connection.commit()
            assert connection.execute('PRAGMA integrity_check').fetchone() == ('ok',)
        finally:
            connection.close()
        data = path.read_bytes()
        # The writer-library version stamp is not schema/data. Normalize it so
        # different authoring-host SQLite versions emit identical legacy fixtures.
        return data[:96] + bytes(4) + data[100:]


def payloads(family: dict) -> tuple[list, list, list]:
    slug = family['slug']
    files = []
    for name, text in sorted(family['files'].items()):
        # These two cases deliberately model old filename/content encodings.
        name_encoding = 'utf-8'
        content_encoding = 'utf-8'
        if slug == 'filename-encoding-migration' and name.startswith('imported/'):
            name_encoding = 'latin-1'
        if slug == 'text-export-normalization' and name.endswith('western.txt'):
            content_encoding = 'latin-1'
        data = text.encode(content_encoding)
        if slug == 'text-export-normalization' and name.endswith('invalid.txt'):
            data = b'invalid UTF-8: \xff\n'
        if name.endswith('.py') and not text.startswith('#!'):
            data = b'#!/usr/bin/python\n' + data
        mode = 0o644
        if data.startswith(b'#!') or name.startswith('libexec/'):
            mode = 0o755
        if name == 'access.txt' or name.startswith('private/') or name.endswith('private.dat'):
            mode = 0o600
        epoch = EPOCH
        if slug == 'inode-cache-retention' and name == 'cache/keep-new.thumb':
            epoch = 1800000000
        files.append((b64(name.encode(name_encoding)), b64(data), mode, epoch))
    for name, members in sorted(family['archives'].items()):
        files.append((b64(name.encode()), b64(tar_bytes(members)), 0o644, EPOCH))
    if slug in ('transactional-schema-upgrade', 'sqlite-lock-contention'):
        name = 'catalog.db' if slug == 'transactional-schema-upgrade' else 'stock.db'
        files.append((b64(name.encode()), b64(sqlite_bytes(family['files']['schema.sql'])), 0o644, EPOCH))
    if slug == 'inode-cache-retention':
        for index in range(256):
            files.append((b64(f'cache/obsolete-{index:04d}.thumb'.encode()), b64(f'obsolete {index}\n'.encode()), 0o644, EPOCH))
    links = [(b64(name.encode()), b64(target.encode())) for name, target in sorted(family['links'].items())]
    special = []
    if slug == 'sparse-image-copy':
        special.append(('sparse', b64(b'source.img')))
    if slug == 'fifo-worker-reconnection':
        special.append(('fifo', b64(b'jobs.fifo')))
    return files, links, special


def seed_program(family: dict) -> str:
    files, links, special = payloads(family)
    template = (REPO / 'scripts/legacy2/seed.py.template').read_text()
    return (template.replace('__ROOT__', repr('/srv/legacy2/' + family['slug']))
            .replace('__FILES__', repr(files)).replace('__LINKS__', repr(links))
            .replace('__SPECIAL__', repr(special)))


def setup(family: dict) -> str:
    command = PREAMBLE + "as_root python - <<'LEGACY2_SEED_PY'\n" + seed_program(family) + 'LEGACY2_SEED_PY\n'
    result = 'timeout_sec = 180\n'
    for index in range(1, family['nodes'] + 1):
        result += f'''\n[[steps]]
id = "seed-node{index}"
stage = 10
node = "node{index}"
command = {json.dumps(command)}
'''
    return result


def baseline(family: dict) -> str:
    root = '/srv/legacy2/' + family['slug']
    # No timestamps from the current clock, no symlink following, no FIFO reads.
    # Both hashes address the differing native tools the agents choose on old OSes.
    command = PREAMBLE + "as_root sh -s <<'LEGACY2_BASELINE_SH'\nset -eu\n"
    command += f"cd '{root}'\n"
    command += "printf '%s\\n' 'SHA256 (regular files only)'\nfind . -type f -exec sha256sum {} \\;\n"
    command += "printf '%s\\n' 'POSIX cksum (regular files only)'\nfind . -type f -exec cksum {} \\;\n"
    command += "printf '%s\\n' 'Type, permissions, owner, group, length, mtime, allocated blocks and link targets'\nfind . -exec stat -c '%F|%a|%U|%G|%s|%Y|%b|%N' {} \\;\n"
    command += "LEGACY2_BASELINE_SH\n"
    result = 'timeout_sec = 180\n'
    for index in range(1, family['nodes'] + 1):
        result += f'''\n[[observations]]
id = "seeded-state-node{index}"
stage = 10
node = "node{index}"
required = true
command = {json.dumps(command)}
'''
    return result


def task_dir(family: dict, system: str) -> Path:
    category = 'single-node-os-comparison' if family['nodes'] == 1 else 'multi-node-os-comparison'
    return resolve_task_path(ROOT / ('bash-' + system) / category / (family['slug'] + '-' + system))


def expected_files() -> dict[Path, tuple[str, int]]:
    from variant_metadata import dumps, initial_metadata

    outputs = {}
    for family in FAMILIES:
        preparation = setup(family)
        observations = baseline(family)
        instruction = family['instruction'] + '\nKeep the installed operating-system release and kernel; use software compatible with this legacy platform.\n'
        for system, image in SYSTEMS.items():
            directory = task_dir(family, system)
            cluster = image + (f" x{family['nodes']}" if family['nodes'] > 1 else '')
            environment = f'''cluster = [{json.dumps(cluster)}]
base_runbooks = ["antrieb/primer", "antrieb/networking-primer"]
control_node = "node1"
endpoint = "https://antrieb.sh/mcp"

[prepare]
enabled = true
mode = "static"
setup = "prepare/setup.toml"
baseline = "prepare/baseline.toml"
timeout_sec = 180
'''
            for relative, content in [('instruction.md', instruction), ('task.toml', TASK),
                    ('environment/harbor_antrieb.toml', environment), ('prepare/setup.toml', preparation),
                    ('prepare/baseline.toml', observations), ('tests/test.sh', SENTINEL)]:
                outputs[directory / relative] = (content, 0o755 if relative == 'tests/test.sh' else 0o644)
            outputs[directory / 'variant.toml'] = (dumps(initial_metadata(
                directory, instruction=instruction, environment=environment,
                task_config=TASK)), 0o644)
    return outputs


def main() -> None:
    assert len(FAMILIES) == len({f['slug'] for f in FAMILIES}) == 60
    for path, (content, mode) in expected_files().items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        path.chmod(mode)
    print('Generated 120 tasks: 60 paired families, 40 single-node and 20 two-node.')


if __name__ == '__main__':
    main()
