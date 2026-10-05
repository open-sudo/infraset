#!/usr/bin/env python3
"""Expand the established 100-family benchmark across general-purpose Linux images.

The existing CentOS5/Ubuntu7 tasks and their historical jobs are never rewritten.
The image catalog is an explicit, reviewable MCP snapshot, not a guessed OS list.
"""
from __future__ import annotations

import base64
import datetime
import hashlib
import json
import shlex
import stat
from pathlib import Path
from scenario_layout import collection_root, resolve_task_path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from generate_legacy2_tasks import FAMILIES, PREAMBLE, payloads, baseline
from variant_metadata import dumps, environment_fields, read

REPO = Path(__file__).resolve().parents[1]
SOURCE = collection_root('bash-centos5')
PROFILES = json.loads((REPO / 'scripts/bash_matrix/images.json').read_text())['images']
EXTENSIONS = {f['slug']: f for f in FAMILIES}


def shell_bytes(encoded: str) -> str:
    """ASCII shell source preserving arbitrary filename bytes (including latin-1)."""
    raw = base64.b64decode(encoded)
    assert b'\x00' not in raw and b'\n' not in raw
    return '"$(printf ' + shlex.quote(''.join('\\%03o' % b for b in raw)) + ')"'


def seed_shell(family: dict) -> str:
    lines = []
    files, links, special = payloads(family)
    for encoded, payload, mode, epoch in files:
        digest = hashlib.sha256(base64.b64decode(payload)).hexdigest()
        stamp = datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc).strftime('%Y%m%d%H%M.%S')
        lines += [f'destination {shell_bytes(encoded)}', 'regular_destination',
                  'staging=$(mktemp "$(dirname "$path")/.seed-XXXXXX")',
                  f"base64 -d > \"$staging\" <<'BASH_MATRIX_FILE'\n{payload}\nBASH_MATRIX_FILE",
                  f'chmod {mode:o} "$staging"', f'touch -t {stamp} "$staging"',
                  'mv -f "$staging" "$path"', 'staging=',
                  f'verify_regular {digest} {mode:o} {epoch}']
    for encoded, target in links:
        lines += [f'destination {shell_bytes(encoded)}', f'link={shell_bytes(target)}',
                  'if [ -L "$path" ]; then',
                  '  if [ "$(readlink "$path")" != "$link" ]; then rm "$path"; ln -s "$link" "$path"; fi',
                  'else', '  [ ! -e "$path" ] || exit 1', '  ln -s "$link" "$path"', 'fi',
                  '[ "$(readlink "$path")" = "$link" ] || exit 1']
    for kind, encoded in special:
        lines += [f'destination {shell_bytes(encoded)}']
        if kind == 'fifo':
            lines += ['[ ! -L "$path" ] || exit 1',
                      'if [ ! -e "$path" ]; then mkfifo -m 0600 "$path"; fi',
                      '[ -p "$path" ] || exit 1', '[ "$(stat -c %a "$path")" = 600 ] || exit 1']
        elif kind == 'sparse':
            lines += ['regular_destination', 'staging=$(mktemp "$(dirname "$path")/.seed-XXXXXX")',
                      "printf 'BRANCH-IMAGE\\n' > \"$staging\"",
                      "printf 'END\\n' | dd of=\"$staging\" bs=1 seek=67108860 conv=notrunc 2>/dev/null",
                      'chmod 0644 "$staging"', 'touch -t 202311142213.20 "$staging"',
                      'mv -f "$staging" "$path"', 'staging=',
                      '[ "$(stat -c %s "$path")" = 67108864 ] || exit 1',
                      '[ "$(stat -c %b "$path")" -lt 4096 ] || exit 1']
        else:
            raise ValueError(kind)
    template = (REPO / 'scripts/bash_matrix/seed.sh.template').read_text()
    return template.replace('__ROOT__', shlex.quote('/srv/legacy2/' + family['slug'])).replace('__BODY__', '\n'.join(lines))


def preparation(family: dict) -> str:
    command = PREAMBLE + "as_root sh -s <<'BASH_MATRIX_SEED'\n" + seed_shell(family) + 'BASH_MATRIX_SEED\n'
    text = 'timeout_sec = 180\n'
    for index in range(1, family['nodes'] + 1):
        text += f'\n[[steps]]\nid = "seed-node{index}"\nstage = 10\nnode = "node{index}"\ncommand = {json.dumps(command)}\n'
    return text


def expected_files(profile: dict) -> dict[Path, tuple[bytes, int]]:
    result = {}
    for config in sorted(SOURCE.rglob('task.toml')):
        source = config.parent
        slug = read(source / 'variant.toml')['usecase']
        category = read(source / 'variant.toml')['category']
        target = resolve_task_path(REPO / 'tasks' / ('bash-' + profile['id']) / category / (slug + '-' + profile['id']))
        for path in sorted(source.rglob('*')):
            if not path.is_file():
                continue
            relative = path.relative_to(source)
            if relative == Path('variant.toml'):
                continue
            content = path.read_bytes()
            if relative == Path('environment/harbor_antrieb.toml'):
                content = content.decode().replace('centos5.11', profile['image']).encode()
                if profile['id'].startswith('rhel'):
                    content = b'initialize = ["rhsm:30s"]\n' + content
            if slug in EXTENSIONS and relative == Path('prepare/setup.toml'):
                content = preparation(EXTENSIONS[slug]).encode()
            # These baseline commands use only tools common to GNU and BusyBox.
            if slug in EXTENSIONS and relative == Path('prepare/baseline.toml'):
                content = baseline(EXTENSIONS[slug]).encode()
            if relative == Path('prepare/setup.toml') and slug in ('scheduled-maintenance', 'unprivileged-service'):
                content = content.replace(b"cat <<'SCRIPT'", b"as_root install -d -o root -g root -m 0755 /usr/local/bin\ncat <<'SCRIPT'")
            result[target / relative] = content, stat.S_IMODE(path.stat().st_mode)
        metadata = read(source / 'variant.toml')
        metadata['os'] = profile['id']
        metadata['id'] = target.parent.name
        metadata['environment'] = environment_fields(tomllib.loads(
            result[target / 'environment/harbor_antrieb.toml'][0].decode()))
        result[target / 'variant.toml'] = dumps(metadata).encode(), 0o644
    return result


def generate() -> None:
    for profile in PROFILES:
        if profile['existing']:
            continue
        outputs = expected_files(profile)
        for path, (content, mode) in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
            path.chmod(mode)
        root = collection_root('bash-' + profile['id'])
        (root / '_collection' / 'README.md').write_text(f'''# bash-{profile['id']}

100 matched tasks for `{profile['ani']}`: 70 single-node and 30 multi-node.
The task instructions, topology sizes and timeouts match `bash-centos5` and `bash-ubuntu7`.
64 tasks have static preparation and required baselines; 36 are greenfield.

Preparation uses POSIX shell, root-or-noninteractive-sudo execution, base64,
SHA256 checks, and GNU/BusyBox-compatible file tools. It requires no Python,
package installation, repository access, or changes to management networking.
Fixture bytes, permissions and timestamps are checked during setup. Existing
fixture paths and business requirements are preserved across operating systems.
The executor remains responsible for task-specific software and services.

```sh
./run-task.sh --skip-existing ./tasks/{root.name}
```

Regenerate with `scripts/generate_bash_os_tasks.py`; validate with
`scripts/check_bash_os_tasks.py`. See [matrix notes](../../scripts/bash_matrix/README.md)
for image coverage, compatibility limits, and the distinction between local
preparation checks and live-image validation.
''')
        print(f'Generated {root.relative_to(REPO)}: 100 tasks')


if __name__ == '__main__':
    generate()
