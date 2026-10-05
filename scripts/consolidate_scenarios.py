#!/usr/bin/env python3
"""Consolidate the verified 7292/5782 task sets while preserving execution history."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from execution_metadata import historical_manifest
from variant_metadata import ROOT, dumps, read

SOURCE, TARGET = '7292', '5782'


def consolidate(root: Path, write: bool = False) -> dict:
    source, target = root / 'tasks' / SOURCE, root / 'tasks' / TARGET
    archive = root / 'data/scenario-archives' / SOURCE
    if not source.exists():
        if archive.is_dir():
            return {'already_consolidated': True, 'scenario_id': TARGET}
        raise ValueError(f'Missing source scenario: {SOURCE}')
    mapping = {}
    for config in sorted(source.glob('*/task.toml')):
        old = config.parent
        new = target / (old.name.removesuffix('-' + SOURCE) + '-' + TARGET)
        old_files = {p.relative_to(old): p for p in old.rglob('*') if p.is_file()}
        new_files = {p.relative_to(new): p for p in new.rglob('*') if p.is_file()}
        if old_files.keys() != new_files.keys():
            raise ValueError(f'Different task file sets: {old}')
        for relative, path in old_files.items():
            other = new_files[relative]
            if relative.as_posix() == 'variant.toml':
                a, b = read(path), read(other)
                a.pop('id'); b.pop('id')
                same = a == b
            else:
                same = path.read_bytes() == other.read_bytes()
            if not same or (path.stat().st_mode & 0o777) != (other.stat().st_mode & 0o777):
                raise ValueError(f'Different task contents or permissions: {path}')
        mapping[str(old.relative_to(root / 'tasks'))] = str(new.relative_to(root / 'tasks'))
    if len(mapping) != len(list(target.glob('*/task.toml'))):
        raise ValueError('Scenario task sets differ')
    manifests, moves = {}, {}
    for scenario, transport in ((TARGET, 'direct'), (SOURCE, 'trentina')):
        for batch in sorted((root / 'jobs' / scenario).iterdir()):
            if not batch.is_dir():
                continue
            data = historical_manifest(batch, transport)
            destination = root / 'jobs' / TARGET / batch.name
            if scenario == SOURCE and destination.exists():
                raise ValueError(f'Batch timestamp collision: {destination}')
            data['scenario_id'] = TARGET
            data['recorded_task_digests'] = {
                name.removesuffix('-' + scenario) + '-' + TARGET: digest
                for name, digest in data['recorded_task_digests'].items()
            }
            data['provenance']['original_scenario_id'] = scenario
            manifests[batch] = data
            for job in sorted(p for p in batch.iterdir() if (p / 'variant.toml').is_file()):
                new_name = job.name.removesuffix('-' + scenario) + '-' + TARGET
                moves[str(job.relative_to(root / 'jobs'))] = str((destination / new_name).relative_to(root / 'jobs'))
    if archive.exists():
        raise ValueError(f'Archive already exists: {archive}')
    if write:
        # Retain the former task definitions as an archive, outside the active task catalog.
        archive.parent.mkdir(parents=True, exist_ok=True)
        source.rename(archive)
        for batch, manifest in manifests.items():
            scenario = batch.parent.name
            destination = root / 'jobs' / TARGET / batch.name
            if scenario == SOURCE:
                batch.rename(destination)
                for job in list(destination.iterdir()):
                    if job.is_dir() and (job / 'variant.toml').is_file():
                        job.rename(job.with_name(job.name.removesuffix('-' + SOURCE) + '-' + TARGET))
            for job in destination.iterdir():
                if not (job / 'variant.toml').is_file():
                    continue
                data = read(job / 'variant.toml')
                data['id'] = TARGET
                data['run']['id'] = TARGET
                data['run']['transport'] = manifest['parameters']['transport']
                backfill = data.setdefault('backfill', {})
                backfill['original_scenario_id'] = scenario
                backfill['source_task'] = TARGET + '/' + job.name
                backfill['transport_source'] = 'user-confirmed-scenario-consolidation'
                backfill['unrecorded_run_fields'] = [key for key in backfill.get('unrecorded_run_fields', []) if key != 'transport']
                (job / 'variant.toml').write_text(dumps(data))
            (destination / 'execution.toml').write_text(dumps(manifest))
        (root / 'jobs' / SOURCE).rmdir()
        path = root / 'data/scenario-layout.json'
        layout = json.loads(path.read_text())
        layout['scenarios'] = [s for s in layout['scenarios'] if s['id'] != SOURCE]
        for scenario in layout['scenarios']:
            if scenario['id'] == TARGET:
                scenario['aliases'] = sorted(set(scenario.get('aliases', []) + ['trentina']))
        layout.setdefault('scenario_aliases', {})[SOURCE] = TARGET
        layout.setdefault('task_aliases', {}).update(mapping)
        layout['tasks'] = {old: mapping.get(new, new) for old, new in layout['tasks'].items()}
        path.write_text(json.dumps(layout, indent=2) + '\n')
        path = root / 'data/job-layout.json'
        layout = json.loads(path.read_text())
        layout['jobs'] = {old: moves.get(new, new) for old, new in layout['jobs'].items()}
        layout['jobs'].update({old: new for old, new in moves.items() if old != new})
        path.write_text(json.dumps(layout, indent=2) + '\n')
        scenario = read(target / 'scenario.toml')
        scenario['aliases'] = ['trentina']
        scenario['consolidated_from'] = [SOURCE]
        (target / 'scenario.toml').write_text(dumps(scenario))
        (root / 'data/scenario-consolidation.json').write_text(json.dumps({
            'source_id': SOURCE, 'target_id': TARGET, 'tasks': mapping, 'jobs': moves,
            'archived_tasks': str(archive.relative_to(root)),
        }, indent=2) + '\n')
    return {'scenario_id': TARGET, 'shared_tasks': len(mapping), 'historical_jobs': len(moves),
            'execution_batches': len(manifests), 'written': write}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    print(json.dumps(consolidate(ROOT, args.write), indent=2))
