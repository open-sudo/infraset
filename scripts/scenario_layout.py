"""Resolve collection-era task references through the recorded scenario migration."""
from __future__ import annotations

from functools import lru_cache
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@lru_cache(maxsize=None)
def manifest(root: Path = ROOT) -> dict:
    path = root / 'data/scenario-layout.json'
    return json.loads(path.read_text()) if path.exists() else {'scenarios': [], 'tasks': {}}


def collection_root(collection: str, root: Path = ROOT) -> Path:
    collection = manifest(root).get('scenario_aliases', {}).get(collection, collection)
    for scenario in manifest(root)['scenarios']:
        if collection in [scenario['collection'], *scenario.get('aliases', [])]:
            return root / 'tasks' / scenario['id']
    return root / 'tasks' / collection


def collection_tasks(collection: str, root: Path = ROOT) -> list[Path]:
    mapping = {**manifest(root)['tasks'], **manifest(root).get('task_aliases', {})}
    found = [root / 'tasks' / new for old, new in sorted(mapping.items())
             if old.startswith(collection + '/')]
    return found or sorted(p.parent for p in collection_root(collection, root).rglob('task.toml'))


def collection_asset(collection: str, relative: str, root: Path = ROOT) -> Path:
    folder = collection_root(collection, root)
    return folder / '_collection' / relative if folder.name.isdigit() else folder / relative


def resolve_task_path(path: Path, root: Path = ROOT) -> Path:
    """Resolve an old task or task file, also accepting pre-collection paths."""
    try:
        relative = path.relative_to(root / 'tasks')
    except ValueError:
        return path
    mapping = {**manifest(root)['tasks'], **manifest(root).get('task_aliases', {})}
    for prefix in ('', 'vanilla/'):
        parts = Path(prefix + relative.as_posix()).parts
        for length in range(len(parts), 0, -1):
            old = '/'.join(parts[:length])
            if old in mapping:
                return root / 'tasks' / mapping[old] / Path(*parts[length:])
    return path


@lru_cache(maxsize=None)
def reverse_paths(root: Path = ROOT) -> dict:
    return {new: old for old, new in manifest(root)['tasks'].items()}


def original_task_path(path: Path, root: Path = ROOT) -> Path:
    relative = path.relative_to(root / 'tasks').as_posix()
    return root / 'tasks' / reverse_paths(root).get(relative, relative)
