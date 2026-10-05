#!/usr/bin/env python3
"""Initialize, validate, and export searchable task variant metadata (Python 3.11+)."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from scenario_layout import original_task_path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
IMAGE_IDS = {
    'ubuntu7.10': 'ubuntu7', 'ubuntu12.10': 'ubuntu12',
    'ubuntu16.04': 'ubuntu16', 'ubuntu24.04': 'ubuntu24',
    'centos5.11': 'centos5', 'centos6.10': 'centos6',
    'rhel7.9': 'rhel7', 'rhel8.8': 'rhel8',
    'rhel9.8': 'rhel9', 'rhel10.0': 'rhel10',
}


def read(path: Path) -> dict:
    return tomllib.loads(path.read_text(encoding='utf-8'))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def environment_path(task: Path) -> Path:
    for name in ('harbor_antrieb.toml', 'infraset.toml'):
        path = task / 'environment' / name
        if path.is_file():
            return path
    raise ValueError(f'{task}: missing environment definition')


def environment_fields(config: dict) -> dict:
    images, node_count = [], 0
    cluster = config.get('cluster')
    if not isinstance(cluster, list) or not cluster:
        raise ValueError('cluster must be a nonempty array')
    for item in cluster:
        if not isinstance(item, str):
            raise ValueError('Metadata schema v1 currently requires string cluster entries')
        match = re.fullmatch(r'(.+?)(?:\s+x([1-9][0-9]*))?', item)
        if match is None:
            raise ValueError('cluster image selectors must not be empty')
        image, count = match.groups()
        if image not in images:
            images.append(image)
        node_count += int(count or 1)
    return {
        'images': images,
        'node_count': node_count,
        'initial_state': 'brownfield' if config.get('prepare', {}).get('enabled', False) else 'greenfield',
    }


def initial_metadata(task: Path, *, instruction: str | None = None,
                     environment: str | None = None, task_config: str | None = None) -> dict:
    """Bootstrap descriptive fields from authored files; never infer a run mode/model."""
    instruction = instruction if instruction is not None else (task / 'instruction.md').read_text()
    environment = environment if environment is not None else environment_path(task).read_text()
    config = tomllib.loads(task_config) if task_config is not None else read(task / 'task.toml')
    env = environment_fields(tomllib.loads(environment))
    original = original_task_path(task, ROOT)
    parts = original.relative_to(ROOT / 'tasks').parts
    collection = parts[0]
    if len(parts) < 3 or not (collection.startswith('bash-') or collection in (
            'vanilla', 'vanilla-ansible', 'vanilla-luna', 'trentina')):
        raise ValueError('Unrecognized collection layout; author variant.toml explicitly')
    language = 'ansible' if collection == 'vanilla-ansible' else 'bash'
    category = parts[1]
    images = [image for image in env['images'] if image != 'ansible-controller']
    os_ids = [IMAGE_IDS.get(image, image) for image in images]
    if collection.startswith('bash-'):
        os_id = collection.removeprefix('bash-')
    elif original.parent.name in os_ids:
        os_id = original.parent.name
    else:
        os_id = os_ids[0] if len(set(os_ids)) == 1 else 'mixed'
    usecase = original.name
    # Strip only a known OS suffix, longest first (centos-stream10 contains '-').
    suffixes = set(os_ids + ['alma9']) if os_id != 'mixed' else set()
    for suffix in sorted(suffixes, key=len, reverse=True):
        if usecase.endswith('-' + suffix):
            usecase = usecase[:-(len(suffix) + 1)]
            break
    paragraphs = re.split(r'\n\s*\n', instruction.strip())
    summary = next((p for p in paragraphs if not p.lstrip().startswith('#')), paragraphs[0])
    data = {
        'schema_version': 1,
        'usecase': usecase,
        'title': usecase.replace('-', ' ').capitalize(),
        'description': ' '.join(summary.replace('`', '').split()),
        'category': category,
        'tags': [category],
        'language': language,
        'os': os_id,
        'difficulty': config['metadata']['difficulty'],
        'prompt': {'path': 'instruction.md', 'sha256': hashlib.sha256(instruction.encode()).hexdigest()},
        'environment': env,
    }
    if re.fullmatch(r'[1-9][0-9]{3}', task.parent.name):
        data['id'] = task.parent.name
    return data


def dumps(data: dict) -> str:
    """Emit the schema's strings, integers, arrays, and one-level tables as TOML."""
    lines = []
    for key, value in data.items():
        if not isinstance(value, dict):
            lines.append(f'{key} = {json.dumps(value, ensure_ascii=False)}')
    for key, value in data.items():
        if isinstance(value, dict):
            lines.extend(['', f'[{key}]'])
            lines.extend(f'{name} = {json.dumps(item, ensure_ascii=False)}' for name, item in value.items())
    return '\n'.join(lines) + '\n'


def validate(task: Path) -> dict:
    data = read(task / 'variant.toml')
    scenario_id = data.get('id')
    if not isinstance(scenario_id, str) or not re.fullmatch(r'[1-9][0-9]{3}', scenario_id):
        raise ValueError('id must be the four-digit scenario ID')
    if task.parent.name != scenario_id:
        raise ValueError('id must match the task parent scenario folder')
    if type(data.get('schema_version')) is not int or data['schema_version'] != 1:
        raise ValueError('unsupported schema_version (expected 1)')
    for field in ('usecase', 'language', 'os', 'category'):
        if not isinstance(data.get(field), str) or not SLUG.fullmatch(data[field]):
            raise ValueError(f'{field} must be a lowercase hyphen-separated slug')
    expected_name = '-'.join(data[key] for key in ('usecase', 'language', 'os', 'id'))
    if task.name != expected_name:
        raise ValueError(f'task folder must be named {expected_name}')
    for field in ('title', 'description'):
        if not isinstance(data.get(field), str) or not data[field].strip():
            raise ValueError(f'{field} must be a nonempty string')
    if data.get('difficulty') not in ('easy', 'medium', 'hard', 'expert'):
        raise ValueError('difficulty must be easy, medium, hard, or expert')
    tags = data.get('tags')
    if not isinstance(tags, list) or not tags or any(not isinstance(x, str) or not SLUG.fullmatch(x) for x in tags) or len(tags) != len(set(tags)):
        raise ValueError('tags must be a nonempty array of unique slugs')
    prompt = data.get('prompt')
    if not isinstance(prompt, dict) or prompt.get('path') != 'instruction.md':
        raise ValueError('prompt.path must be instruction.md')
    if prompt.get('sha256') != digest(task / 'instruction.md'):
        raise ValueError('prompt.sha256 is stale; update it after reviewing the prompt change')
    expected = environment_fields(read(environment_path(task)))
    if data.get('environment') != expected:
        raise ValueError('environment metadata does not match the environment definition')
    if data.get('difficulty') != read(task / 'task.toml')['metadata']['difficulty']:
        raise ValueError('difficulty does not match task.toml')
    if 'run' in data:
        raise ValueError('[run] belongs only in a saved job snapshot')
    return data


def tasks_under(root: Path) -> list[Path]:
    if (root / 'task.toml').is_file():
        return [root]
    tasks = sorted(path.parent for path in root.rglob('task.toml'))
    if not tasks:
        raise ValueError(f'no tasks found under {root}')
    return tasks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('init', 'check', 'index'))
    parser.add_argument('root', type=Path, nargs='?', default=ROOT / 'tasks')
    args = parser.parse_args()
    try:
        tasks = tasks_under(args.root.resolve())
    except ValueError as exc:
        parser.error(str(exc))
    records, errors, created = [], [], 0
    for task in tasks:
        try:
            path = task / 'variant.toml'
            if args.command == 'init' and not path.exists():
                path.write_text(dumps(initial_metadata(task)), encoding='utf-8')
                created += 1
            data = validate(task)
            records.append({'task_path': str(task.relative_to(args.root.resolve())) if task != args.root.resolve() else '.', **data})
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f'{task}: {exc}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    if args.command == 'index':
        for record in records:
            print(json.dumps(record, ensure_ascii=False))
    else:
        print(f'Validated {len(records)} variant files; created {created}.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
