#!/usr/bin/env python3
"""Move each complete task collection into its own persistent scenario ID."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import secrets

from variant_metadata import ROOT, dumps, read


def task_files(task: Path) -> dict:
    return {str(p.relative_to(task)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in task.rglob('*') if p.is_file() and p.name != 'variant.toml'}


def migrate(root: Path, write: bool = False) -> dict:
    tasks = root / 'tasks'
    plan_path = root / 'data/scenario-layout.json'
    if plan_path.exists():
        plan = json.loads(plan_path.read_text())
    else:
        collections = sorted(p for p in tasks.iterdir() if p.is_dir() and not p.name.isdigit())
        used, scenarios, mapping = set(), [], {}
        for collection in collections:
            scenario_id = str(1000 + secrets.randbelow(9000))
            while scenario_id in used or (tasks / scenario_id).exists():
                scenario_id = str(1000 + secrets.randbelow(9000))
            used.add(scenario_id)
            scenarios.append({'id': scenario_id, 'collection': collection.name})
            for config in sorted(collection.rglob('task.toml')):
                data = read(config.parent / 'variant.toml')
                name = '-'.join(data[k] for k in ('usecase', 'language', 'os')) + '-' + scenario_id
                mapping[str(config.parent.relative_to(tasks))] = f'{scenario_id}/{name}'
        if len(set(mapping.values())) != len(mapping):
            raise ValueError('Duplicate target task names; no migration performed')
        plan = {'schema_version': 1, 'scenarios': scenarios, 'tasks': mapping}
    for old, new in plan['tasks'].items():
        source, target = tasks / old, tasks / new
        if source.exists() and target.exists():
            raise ValueError(f'Both source and target exist: {old}, {new}')
        if not source.exists() and not target.exists():
            raise ValueError(f'Missing source and target: {old}, {new}')
    if write:
        if not plan_path.exists():
            plan_path.write_text(json.dumps(plan, indent=2) + '\n')
        for scenario in plan['scenarios']:
            destination = tasks / scenario['id']
            destination.mkdir(exist_ok=True)
            (destination / 'scenario.toml').write_text(dumps({
                'schema_version': 1, 'id': scenario['id'], 'name': scenario['collection']}))
        for old, new in plan['tasks'].items():
            source, target = tasks / old, tasks / new
            if source.exists():
                before = task_files(source)
                source.rename(target)
                if task_files(target) != before:
                    raise ValueError(f'Task contents changed while moving {old}')
            data = read(target / 'variant.toml')
            data['id'] = target.parent.name
            (target / 'variant.toml').write_text(dumps(data))
        for scenario in plan['scenarios']:
            source = tasks / scenario['collection']
            if not source.exists():
                continue
            # Preserve catalogs and collection notes separately from direct task children.
            for file in sorted(source.rglob('*')):
                if file.is_file():
                    target = tasks / scenario['id'] / '_collection' / file.relative_to(source)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    file.rename(target)
            for directory in sorted(source.rglob('*'), key=lambda p: len(p.parts), reverse=True):
                if directory.is_dir():
                    directory.rmdir()
            source.rmdir()
    return {'tasks': len(plan['tasks']), 'scenarios': len(plan['scenarios']),
            'collections': {s['collection']: s['id'] for s in plan['scenarios']}, 'written': write}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    print(json.dumps(migrate(ROOT, args.write), indent=2))
