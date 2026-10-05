#!/usr/bin/env python3
"""Move saved jobs to <scenario-id>/<timestamp>/<task-name>-<scenario-id>."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

from variant_metadata import ROOT, read

TIMESTAMP = re.compile(r'\d{4}-\d{2}-\d{2}__\d{2}-\d{2}-\d{2}\Z')


def migrate(root: Path, *, write: bool = False) -> dict:
    jobs = root / 'jobs'
    mapping = {}
    for instruction in sorted(jobs.rglob('instruction.md')):
        job = instruction.parent
        metadata = read(job / 'variant.toml')
        scenario = metadata['id']
        if not re.fullmatch(r'[1-9][0-9]{3}', scenario) or metadata['run']['id'] != scenario:
            raise ValueError(f'{job}: invalid scenario ID')
        stamps = [part for part in job.relative_to(jobs).parts if TIMESTAMP.fullmatch(part)]
        if len(stamps) != 1:
            raise ValueError(f'{job}: expected exactly one saved timestamp')
        name = '-'.join(metadata[key] for key in ('usecase', 'language', 'os', 'id'))
        mapping[str(job.relative_to(jobs))] = f'{scenario}/{stamps[0]}/{name}'
    if not mapping:
        raise ValueError('No saved jobs found')
    if len(set(mapping.values())) != len(mapping):
        raise ValueError('Destination collision; no jobs moved')
    moves = {old: new for old, new in mapping.items() if old != new}
    for old, new in moves.items():
        if (jobs / new).exists():
            raise ValueError(f'Destination already exists: {new}')
    if write and moves:
        manifest_path = root / 'data/job-layout.json'
        previous = json.loads(manifest_path.read_text()) if manifest_path.exists() else {'schema_version': 1, 'jobs': {}}
        previous['jobs'].update(moves)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(previous, indent=2) + '\n')
        for old, new in moves.items():
            source, target = jobs / old, jobs / new
            before = source.stat()
            target.parent.mkdir(parents=True, exist_ok=True)
            source.rename(target)
            after = target.stat()
            if (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
                raise ValueError(f'Directory identity changed moving {old}')
            # Remove empty old ancestors only; retain any reports or other artifacts.
            parent = source.parent
            while parent != jobs:
                try:
                    parent.rmdir()
                except OSError:
                    break
                parent = parent.parent
    return {'jobs': len(mapping), 'moved' if write else 'would_move': len(moves),
            'scenarios': len({new.split('/')[0] for new in mapping.values()}),
            'batches': len({tuple(new.split('/')[:2]) for new in mapping.values()})}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    print(json.dumps(migrate(ROOT, write=args.write), indent=2))
