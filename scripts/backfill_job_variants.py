#!/usr/bin/env python3
"""Backfill job variant descriptors from saved snapshots without inventing run settings."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
from scenario_layout import resolve_task_path

from variant_metadata import ROOT, digest, dumps, environment_fields, read, tomllib

TIMESTAMP = re.compile(r'\d{4}-\d{2}-\d{2}__\d{2}-\d{2}-\d{2}\Z')
COLLECTIONS = {
    'vanilla-batch': 'vanilla',
    'vanilla-token': 'vanilla',
    'vanilla-ansible-token': 'vanilla-ansible',
}


def source_task(job: Path, config: dict, jobs_root: Path, tasks_root: Path) -> Path:
    candidates = []
    tasks = config.get('tasks', [])
    if len(tasks) > 1:
        raise ValueError(f'{job}: multiple configured tasks; cannot assign one descriptor')
    for task in tasks:
        raw = str(task.get('path', ''))
        relative = raw.split('/tasks/', 1)[-1]
        # Older configs predate the vanilla collection directory.
        candidates.extend((tasks_root / relative, tasks_root / 'vanilla' / relative))
    parts = [part for part in job.relative_to(jobs_root).parts if not TIMESTAMP.fullmatch(part)]
    parts[0] = COLLECTIONS.get(parts[0], parts[0])
    if len(parts) > 1 and parts[0] == parts[1]:
        parts.pop(0)
    candidates.append(tasks_root.joinpath(*parts))
    for candidate in candidates:
        candidate = resolve_task_path(candidate, tasks_root.parent)
        if (candidate / 'variant.toml').is_file():
            return candidate
    raise ValueError(f'{job}: no matching task descriptor')


def descriptor(job: Path, jobs_root: Path, tasks_root: Path) -> dict:
    config_path = job / 'config.json'
    config = json.loads(config_path.read_text()) if config_path.exists() else {}
    source = source_task(job, config, jobs_root, tasks_root)
    data = read(source / 'variant.toml')
    # The source supplies catalog labels, while job snapshots supply historical facts.
    instruction = (job / 'instruction.md').read_text(encoding='utf-8')
    paragraphs = re.split(r'\n\s*\n', instruction.strip())
    summary = next((p for p in paragraphs if not p.lstrip().startswith('#')), paragraphs[0])
    data['description'] = ' '.join(summary.replace('`', '').split())
    data['prompt'] = {'path': 'instruction.md', 'sha256': digest(job / 'instruction.md')}
    data['environment'] = environment_fields(read(job / 'environment.toml'))
    # A collection name is not evidence of the actual transport or mode.
    data['run'] = {}
    agents = config.get('agents', [])
    modes = [agent.get('kwargs', {}).get('execution_mode') for agent in agents]
    if modes and all(mode == modes[0] for mode in modes) and modes[0] in ('interactive', 'batch'):
        data['run']['execution_mode'] = modes[0]
    data['backfill'] = {
        'method': 'saved-snapshots-and-task-catalog',
        'source_task': str(source.relative_to(tasks_root)),
        'catalog_fields': ['usecase', 'title', 'category', 'tags', 'language', 'os', 'difficulty'],
        'description_source': 'instruction.md',
        'environment_source': 'environment.toml',
        'run_settings_source': 'config.json' if config_path.exists() else 'unavailable',
        'unrecorded_run_fields': [field for field in ('id', 'execution_mode', 'transport') if field not in data['run']],
    }
    return data


def assign_scenario_id(data: dict, source: Path, tasks_root: Path) -> None:
    scenario_id = read(source / 'variant.toml')['id']
    previous = data.setdefault('run', {}).get('id')
    data['id'] = scenario_id
    data['run']['id'] = scenario_id
    if 'backfill' in data:
        if previous and previous != scenario_id:
            data['backfill'].setdefault('previous_run_id', previous)
        data['backfill']['id_source'] = 'scenario-folder'
        data['backfill']['source_task'] = str(source.relative_to(tasks_root))
        data['backfill']['unrecorded_run_fields'] = [
            field for field in data['backfill'].get('unrecorded_run_fields', [])
            if field != 'id'
        ]


def backfill(jobs_root: Path, tasks_root: Path, *, write: bool = False) -> dict:
    jobs = sorted(path.parent for path in jobs_root.rglob('instruction.md'))
    if not jobs:
        raise ValueError(f'No saved job instructions under {jobs_root}')
    pending, existing, updated, modes = [], 0, 0, Counter()
    # Prepare and parse every descriptor before writing anything.
    for job in jobs:
        destination = job / 'variant.toml'
        if destination.exists():
            data = read(destination)
            old_source = data.get('backfill', {}).get('source_task')
            source = resolve_task_path(tasks_root / old_source, tasks_root.parent) if old_source else None
            if source is None or not (source / 'variant.toml').is_file():
                config_path = job / 'config.json'
                config = json.loads(config_path.read_text()) if config_path.exists() else {}
                source = source_task(job, config, jobs_root, tasks_root)
            scenario_id = read(source / 'variant.toml')['id']
            if data.get('run', {}).get('id') == scenario_id and data.get('id') == scenario_id:
                existing += 1
                continue
            updated += 1
            open_mode = 'w'
        else:
            data = descriptor(job, jobs_root, tasks_root)
            source = tasks_root / data['backfill']['source_task']
            open_mode = 'x'
        assign_scenario_id(data, source, tasks_root)
        content = dumps(data)
        if tomllib.loads(content) != data:
            raise ValueError(f'{job}: metadata did not round-trip as TOML')
        pending.append((destination, content, open_mode))
        modes[data['run'].get('execution_mode', 'unrecorded')] += 1
    if write:
        for path, content, open_mode in pending:
            with path.open(open_mode, encoding='utf-8') as handle:
                handle.write(content)
    return {'jobs': len(jobs), 'existing': existing,
            'created' if write else 'would_create': len(pending) - updated,
            'updated' if write else 'would_update': updated,
            'execution_modes': dict(modes)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--jobs-root', type=Path, default=ROOT / 'jobs')
    parser.add_argument('--tasks-root', type=Path, default=ROOT / 'tasks')
    parser.add_argument('--write', action='store_true', help='Create descriptors and align IDs with task scenarios; default is a dry run')
    args = parser.parse_args()
    print(json.dumps(backfill(args.jobs_root.resolve(), args.tasks_root.resolve(), write=args.write), indent=2))


if __name__ == '__main__':
    main()
