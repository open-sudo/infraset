#!/usr/bin/env python3
"""Validate all OS datasets and execute portable preparation in temporary directories.

No VM allocation or host service changes. --busybox checks Alpine's actual tool
implementations in addition to local GNU tools. This does not claim live-image QA.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import importlib.util
import json
import os
import stat
import subprocess
import tempfile
from pathlib import Path
from scenario_layout import collection_root, resolve_task_path
from variant_metadata import read

from generate_bash_os_tasks import REPO, SOURCE, PROFILES, FAMILIES, expected_files, seed_shell, tomllib
from generate_legacy2_tasks import seed_program, baseline, payloads
from check_legacy2_tasks import snapshot, semantics


def run(command, *, text=None, env=None):
    p = subprocess.run(command, input=text, text=True, errors='surrogateescape', capture_output=True, timeout=60, env=env)
    if p.returncode:
        raise AssertionError(f'{command}: rc={p.returncode}\n{p.stdout[-1500:]}\n{p.stderr[-2500:]}')
    return p.stdout


def check_layout():
    location = REPO / 'skills/infraset-task-builder/scripts/validate_example.py'
    spec = importlib.util.spec_from_file_location('task_validator', location)
    validator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validator)
    reference = {read(p.parent / 'variant.toml')['usecase']: p.parent for p in SOURCE.rglob('task.toml')}
    assert len(reference) == 100
    unique_commands = set()
    total = 0
    for profile in PROFILES:
        root = collection_root('bash-' + profile['id'])
        tasks = sorted(root.rglob('task.toml'))
        assert len(tasks) == 100, root
        if not profile['existing']:
            expected = expected_files(profile)
            actual = {p for config in tasks for p in config.parent.rglob('*') if p.is_file()}
            assert actual == set(expected), root
            for p, (content, mode) in expected.items():
                assert p.read_bytes() == content and stat.S_IMODE(p.stat().st_mode) == mode, p
        for config in tasks:
            task = config.parent
            errors, warnings = validator.validate(task)
            assert not errors, (task, errors)
            family = read(task / 'variant.toml')['usecase']
            source = reference[family]
            for relative in ('instruction.md', 'task.toml', 'tests/test.sh'):
                assert (task / relative).read_bytes() == (source / relative).read_bytes(), (task, relative)
            env = tomllib.loads((task / 'environment/harbor_antrieb.toml').read_text())
            original = tomllib.loads((source / 'environment/harbor_antrieb.toml').read_text())
            assert env['cluster'] == [x.replace('centos5.11', profile['image']) for x in original['cluster']]
            env['cluster'] = original['cluster']
            if profile['id'].startswith('rhel'):
                assert env.pop('initialize') == ['rhsm:30s'], task
            assert env == original, task
            for p in (task / 'prepare').glob('*.toml'):
                data = tomllib.loads(p.read_text())
                for item in data.get('steps', []) + data.get('observations', []):
                    unique_commands.add(item['command'])
            total += 1
        print(f'PASS {root.name}: 100 tasks, strict validation and instruction/topology parity', flush=True)
    for command in unique_commands:
        run(['sh', '-n'], text=command)
    print(f'PASS {total} tasks; {len(unique_commands)} distinct setup/baseline commands parse as POSIX shell', flush=True)


def verify_payloads(family, root):
    files, links, special = payloads(family)
    for encoded, payload, mode, epoch in files:
        path = root / os.fsdecode(base64.b64decode(encoded))
        assert path.read_bytes() == base64.b64decode(payload), path
        assert stat.S_IMODE(path.stat().st_mode) == mode and int(path.stat().st_mtime) == epoch, path
    for encoded, target in links:
        path = root / os.fsdecode(base64.b64decode(encoded))
        assert os.fsencode(os.readlink(path)) == base64.b64decode(target), path


def check_preparation(busybox=None):
    variants = [('GNU', ['sh', '-s'], None)]
    with tempfile.TemporaryDirectory(prefix='bash-matrix-tools-') as tools_dir:
        if busybox:
            busybox = Path(busybox).resolve()
            run([str(busybox), '--install', '-s', tools_dir])
            environment = dict(os.environ, PATH=tools_dir)
            variants.append(('BusyBox', [str(busybox), 'sh', '-s'], environment))
        for name, shell, environment in variants:
            for family in FAMILIES:
                with tempfile.TemporaryDirectory(prefix='bash-matrix-prep-') as directory:
                    root = Path(directory) / family['slug']
                    program = seed_shell(family).replace('/srv/legacy2/' + family['slug'], str(root))
                    run(shell, text=program, env=environment)
                    first = snapshot(root)
                    verify_payloads(family, root)
                    run(shell, text=program, env=environment)
                    assert first == snapshot(root), ('Non-idempotent preparation', family['slug'])
                    semantics(family, root)
                    command = tomllib.loads(baseline(family))['observations'][0]['command']
                    # Use the real baseline body, without privilege escalation or
                    # its fixed PATH, so this also exercises BusyBox find/stat/hash.
                    command = command.split("<<'LEGACY2_BASELINE_SH'\n", 1)[1].rsplit('LEGACY2_BASELINE_SH', 1)[0]
                    command = command.replace('/srv/legacy2/' + family['slug'], str(root))
                    before = snapshot(root)
                    output = run(shell, text=command, env=environment)
                    assert 'SHA256' in output and 'POSIX cksum' in output
                    assert before == snapshot(root), ('Baseline mutated state', family['slug'])
                    # The new shell implementation must preserve the old Python
                    # implementation's fixture bytes, modes, links and sizes.
                    import sys
                    reference = Path(directory) / 'python-reference'
                    seed = seed_program(family).replace(repr('/srv/legacy2/' + family['slug']), repr(str(reference)))
                    run([sys.executable, '-'], text=seed)
                    assert snapshot(reference) == first, ('Fixture parity', family['slug'])
            print(f'PASS {name}: all 60 fixture setups executed twice; semantics, byte parity, timestamps and read-only baselines passed', flush=True)
            check_original_preparation(name, shell, environment)


def check_original_preparation(name, shell, environment):
    """Exercise the four hand-authored setups under a temporary filesystem prefix.

    Only the destination prefix and root ownership/privilege wrapper are mapped
    to the current local user. Actual managed-image privilege checks require VMs.
    """
    import pwd
    import grp
    user = pwd.getpwuid(os.getuid()).pw_name
    group = grp.getgrgid(os.getgid()).gr_name
    root = REPO / 'tasks/bash-alpine/single-node-os-comparison'
    for slug in ('application-log-rotation', 'repair-application-permissions',
                 'scheduled-maintenance', 'unprivileged-service'):
        task = resolve_task_path(root / (slug + '-alpine'))
        with tempfile.TemporaryDirectory(prefix='bash-matrix-original-') as directory:
            prefix = Path(directory)

            def mapped(command):
                for path in ('/srv/inventory', '/var/log/inventory', '/usr/local/bin'):
                    command = command.replace(path, directory + path)
                command = command.replace('PATH=/usr/sbin:/usr/bin:/sbin:/bin\nexport PATH\n', '')
                command = command.replace('sudo -n "$@"', '"$@"')
                return command.replace('-o root -g root', f'-o {user} -g {group}').replace('root:root', user + ':' + group)

            setup = tomllib.loads((task / 'prepare/setup.toml').read_text())
            observation = tomllib.loads((task / 'prepare/baseline.toml').read_text())
            for repeat in range(2):
                for step in setup['steps']:
                    run(shell, text=mapped(step['command']), env=environment)
                state = snapshot(prefix)
                if repeat:
                    assert state == initial, slug
                else:
                    initial = state
            for item in observation['observations']:
                output = run(shell, text=mapped(item['command']), env=environment)
                assert output.strip(), slug
            assert snapshot(prefix) == initial, slug
            assert len(initial) == (2 if slug == 'repair-application-permissions' else 1), slug
    print(f'PASS {name}: four original setups repeated with local path/ownership mapping; read-only baselines passed', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--busybox', type=Path)
    args = parser.parse_args()
    check_layout()
    check_preparation(args.busybox)
