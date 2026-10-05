#!/usr/bin/env python3
"""Check parity, non-overlap, generated files, and actual preparation locally.

No managed clusters are created. --python may name an additional legacy Python
interpreter for preparation execution. All writes stay in temporary directories.
"""
from __future__ import annotations
import argparse
import collections
import hashlib
import io
import json
import os
import sqlite3
import stat
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path
from scenario_layout import resolve_task_path
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib
from generate_legacy2_tasks import FAMILIES, ROOT, REPO, SYSTEMS, expected_files, seed_program, task_dir


def snapshot(root):
    result = {}
    for p in root.rglob('*'):
        s = p.lstat()
        if stat.S_ISDIR(s.st_mode):
            continue
        value = None
        if p.is_symlink():
            value = os.readlink(p)
        elif p.is_file():
            value = hashlib.sha256(p.read_bytes()).hexdigest()
        result[str(p.relative_to(root))] = (stat.S_IFMT(s.st_mode), stat.S_IMODE(s.st_mode), s.st_size, value)
    return result


def run(args, **kwargs):
    result = subprocess.run(args, capture_output=True, timeout=30, **kwargs)
    if result.returncode:
        raise AssertionError(f'{args}: {result.stderr!r}')
    return result


def check_layout():
    expected = expected_files()
    actual = {p for f in FAMILIES for system in SYSTEMS
              for p in task_dir(f, system).rglob('*') if p.is_file()}
    assert actual == set(expected), ('Missing or unexpected files', actual ^ set(expected))
    for p, (content, mode) in expected.items():
        assert p.read_text() == content, f'Generated file drift: {p}'
        assert stat.S_IMODE(p.stat().st_mode) == mode, f'Mode drift: {p}'
    old_slugs = set()
    old_instructions = set()
    for catalog_path in (REPO / 'scripts/legacy2/catalogs').glob('*.toml'):
        for family in tomllib.loads(catalog_path.read_text())['tasks']:
            old_slugs.add(family['slug'])
            p = resolve_task_path(ROOT / 'bash-centos5' / catalog_path.stem / (family['slug'] + '-centos5'))
            old_instructions.add((p / 'instruction.md').read_text())
    instructions = set()
    for f in FAMILIES:
        assert f['slug'] not in old_slugs, f'Overlapping family: {f["slug"]}'
        assert len(f['distinction']) > 30, 'Missing scope review'
        dirs = [task_dir(f, system) for system in SYSTEMS]
        text = (dirs[0] / 'instruction.md').read_text()
        assert text not in old_instructions and text not in instructions, f'Duplicate request: {f["slug"]}'
        instructions.add(text)
        for relative in [p.relative_to(dirs[0]) for p in dirs[0].rglob('*') if p.is_file()]:
            texts = [(d / relative).read_text() for d in dirs]
            if relative == Path('environment/harbor_antrieb.toml'):
                envs = [tomllib.loads(t) for t in texts]
                for env, image in zip(envs, SYSTEMS.values()):
                    assert env['cluster'] == [image + (f' x{f["nodes"]}' if f['nodes'] > 1 else '')]
                    env['cluster'] = ['IMAGE']
                assert envs[0] == envs[1], f'Environment parity: {f["slug"]}'
            elif relative == Path('variant.toml'):
                from variant_metadata import validate
                metadata = [validate(d) for d in dirs]
                for item in metadata:
                    item['id'] = 'ID'
                    item['os'] = 'OS'
                    item['environment']['images'] = ['OS_IMAGE']
                assert metadata[0] == metadata[1], f'Variant parity: {f["slug"]}'
            else:
                assert texts[0] == texts[1], f'Pair differs: {f["slug"]}/{relative}'
            if relative.suffix == '.toml':
                parsed = tomllib.loads(texts[0])
                for key in ('steps', 'observations'):
                    for entry in parsed.get(key, []):
                        run(['sh', '-n'], input=entry['command'].encode())
        # Only the installer fixture intentionally contains an unsupported shell
        # dialect. The preparation shell itself must always pass sh -n above.
        for name, body in f['files'].items():
            if name.endswith('.py'):
                compile(body, f'{f["slug"]}/{name}', 'exec')
            if body.startswith('#!/bin/sh') and f['slug'] != 'posix-shell-installer':
                run(['sh', '-n'], input=body.encode())
    assert len(instructions) == 60
    print('PASS: 120 tasks, 60 unique families, exact OS parity, no legacy slug/request duplicates')


def semantics(f, root):
    slug = f['slug']
    for name, members in f['archives'].items():
        with tarfile.open(root / name) as archive:
            assert archive.getnames() == list(members)
            for member, expected in members.items():
                info = archive.getmember(member)
                if isinstance(expected, dict):
                    assert info.issym() and info.linkname == expected['symlink']
                else:
                    assert archive.extractfile(info).read() == expected.encode()
    if slug in ('transactional-schema-upgrade', 'sqlite-lock-contention'):
        dbname = 'catalog.db' if slug == 'transactional-schema-upgrade' else 'stock.db'
        with sqlite3.connect(root / dbname) as db:
            assert db.execute('PRAGMA integrity_check').fetchone() == ('ok',)
            if slug == 'transactional-schema-upgrade':
                assert db.execute('SELECT version FROM schema_version').fetchone() == (1,)
                assert db.execute('SELECT * FROM products ORDER BY id').fetchall() == [(1, 'Paper'), (2, 'Tape')]
            else:
                assert db.execute('SELECT remaining FROM stock').fetchone() == (5,)
                assert db.execute('SELECT * FROM reservations').fetchall() == [('previous-request', 2)]
    if slug == 'sparse-image-copy':
        p = root / 'source.img'
        assert p.stat().st_size == 64 * 1024 * 1024 and p.stat().st_blocks * 512 < 2 * 1024 * 1024
        with p.open('rb') as stream:
            assert stream.read(14) == b'BRANCH-IMAGE\n\x00'
            stream.seek(-4, 2)
            assert stream.read() == b'END\n'
    if slug == 'filename-encoding-migration':
        assert b'caf\xe9.txt' in os.listdir(os.fsencode(root / 'imported'))
        assert (root / 'converted/plain.txt').read_text().startswith('Existing destination')
    if slug == 'text-export-normalization':
        assert (root / 'incoming/western.txt').read_bytes() == b'caf\xe9\r\n\r\nr\xe9sum\xe9\r\n'
        assert (root / 'incoming/utf8.txt').read_bytes().endswith(b'last record')
        assert b'\xff' in (root / 'incoming/invalid.txt').read_bytes()
    if slug == 'hardlink-aware-deduplication':
        a, b = root/'release-cache/r1/payload.dat', root/'release-cache/r2/payload.dat'
        assert a.read_bytes() == b.read_bytes() and a.stat().st_ino != b.stat().st_ino
        assert stat.S_IMODE((root/'release-cache/private.dat').stat().st_mode) == 0o600
    if slug == 'inode-cache-retention':
        assert len(list((root/'cache').glob('obsolete-*.thumb'))) == 256
        assert (root/'cache/keep-active.thumb').stat().st_mtime == 1700000000
        assert (root/'cache/keep-new.thumb').stat().st_mtime == 1800000000
    if slug == 'fifo-worker-reconnection':
        assert stat.S_ISFIFO((root/'jobs.fifo').stat().st_mode)
    if slug == 'large-counter-overflow':
        result = run([sys.executable, str(root/'bin/total.py'), str(root/'counters.txt')])
        assert result.stdout.strip() == b'7', 'Fixture must exhibit overflow (correct answer is 4294967303)'
    if slug == 'cgi-report-execution':
        result = run(['sh', str(root/'cgi-bin/report')])
        assert b'Content-Type: text/plain\r\n\r\n' in result.stdout and b'open_orders=7' in result.stdout
    if slug == 'posix-shell-installer':
        destination = root / 'installed reports'
        result = subprocess.run(['sh', str(root/'bin/install-report'), str(destination)],
                                cwd=root, capture_output=True, timeout=5)
        # On hosts where sh is Bash, arrays parse but the unquoted destination
        # still exposes the real failure. On dash the syntax itself fails.
        assert result.returncode != 0 or not (destination/'run-report').exists(), 'Installer fault is missing'
    if slug == 'stale-pidfile-startup':
        result = subprocess.run(['sh', str(root/'bin/control'), 'start'], capture_output=True, timeout=5)
        assert result.returncode != 0, 'Stale PID fault is missing'
    if slug == 'inetd-request-activation':
        for request, response in [(b'PING\n', b'PONG\n'), (b'OTHER\n', b'ERROR\n')]:
            assert run([sys.executable, str(root/'handler.py')], input=request).stdout == response


def check_preparation(interpreters):
    total = 0
    for interpreter in interpreters:
        for f in FAMILIES:
            with tempfile.TemporaryDirectory(prefix='legacy2-prep-') as directory:
                root = Path(directory) / f['slug']
                program = seed_program(f).replace(repr('/srv/legacy2/' + f['slug']), repr(str(root)))
                run([interpreter, '-'], input=program.encode())
                first = snapshot(root)
                run([interpreter, '-'], input=program.encode())
                assert first == snapshot(root), f'Non-idempotent preparation: {f["slug"]}'
                semantics(f, root)
                baseline = task_dir(f, 'centos5') / 'prepare/baseline.toml'
                command = tomllib.loads(baseline.read_text())['observations'][0]['command']
                command = command.replace('/srv/legacy2/' + f['slug'], str(root)).replace('as_root sh -s', 'sh -s')
                before_baseline = snapshot(root)
                output = run(['sh', '-s'], input=command.encode()).stdout
                assert b'SHA256' in output and b'POSIX cksum' in output
                assert snapshot(root) == before_baseline, 'Baseline changed fixture state'
                total += 1
        print(f'PASS: all 60 preparations executed twice with {interpreter}; fixtures and read-only baselines checked')
    print(f'PASS: {total} fixture builds; no VM provisioning or host-service changes')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--python', action='append', default=[])
    args = parser.parse_args()
    check_layout()
    check_preparation([sys.executable] + args.python)


if __name__ == '__main__':
    main()
