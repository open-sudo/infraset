#!/usr/bin/env python3
"""Capture batch execution settings and match completed runs by configuration and revision."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import subprocess
import importlib.metadata

from variant_metadata import dumps, read


def fingerprint(value: dict) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def runtime_revision(directory: str, package: str) -> str:
    if directory:
        commit = subprocess.run(['git', '-C', directory, 'rev-parse', 'HEAD'], capture_output=True, text=True)
        diff = subprocess.run(['git', '-C', directory, 'diff', '--binary', 'HEAD'], capture_output=True)
        if commit.returncode == diff.returncode == 0:
            return commit.stdout.strip() + ':' + hashlib.sha256(diff.stdout).hexdigest()
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return 'unavailable'


def task_revision(task: Path) -> str:
    """Hash all task inputs, including permissions, independently of scenario ID."""
    files = {}
    for path in sorted(task.rglob('*')):
        if path.is_file() and path.name != 'variant.toml':
            files[str(path.relative_to(task))] = [hashlib.sha256(path.read_bytes()).hexdigest(), path.stat().st_mode & 0o777]
    return fingerprint(files)


def completed(job: Path, attempts: int) -> bool:
    try:
        result = json.loads((job / 'result.json').read_text())
        stats = result.get('stats', {})
        return (result.get('n_total_trials') == attempts
                and stats.get('n_completed_trials') == attempts
                and not any(stats.get(key, 0) for key in (
                    'n_errored_trials', 'n_running_trials', 'n_pending_trials', 'n_cancelled_trials')))
    except (OSError, ValueError, AttributeError):
        return False


def reusable(jobs: Path, task: Path, parameters: dict, revision: str) -> bool:
    for manifest in (jobs / task.parent.name).glob('*/execution.toml'):
        try:
            data = read(manifest)
        except (OSError, ValueError):
            continue
        if (data.get('parameters') == parameters
                and data.get('tasks', {}).get(task.name) == revision
                and completed(manifest.parent / task.name, parameters['n_attempts'])):
            return True
    return False


def prepare(jobs: Path, batch_name: str, tasks: list[Path], parameters: dict,
            skip_existing: bool = False) -> list[Path]:
    active, revisions, task_parameters, prompts = [], {}, {}, {}
    for task in tasks:
        revision = task_revision(task)
        prompt_path = task.parent / 'prompt'
        prompt = prompt_path.read_text() if prompt_path.is_file() else ''
        if '\0' in prompt:
            raise ValueError(f'Prompt contains NUL, which cannot be passed through the environment: {prompt_path}')
        effective = dict(parameters)
        if prompt:
            effective['prompt_sha256'] = hashlib.sha256(prompt.encode()).hexdigest()
        task_parameters[task] = effective
        prompts[task] = prompt
        if skip_existing and reusable(jobs, task, effective, revision):
            print(f'[{task.name}] Skipping: matching execution configuration and task revision completed.', file=sys.stderr)
        else:
            active.append(task)
            revisions[task] = revision
    manifests = {}
    for task in active:
        parameters = task_parameters[task]
        batch = jobs / task.parent.name / batch_name
        if (batch / task.name).exists():
            raise ValueError(f'Job already exists: {batch / task.name}; choose a new batch timestamp or use --skip-existing')
        if batch not in manifests:
            path = batch / 'execution.toml'
            data = read(path) if path.exists() else {
                'schema_version': 1, 'scenario_id': task.parent.name,
                'configuration_fingerprint': fingerprint(parameters),
                'parameters': parameters, 'tasks': {},
            }
            if data.get('parameters') != parameters or data.get('scenario_id') != task.parent.name:
                raise ValueError(f'Batch has different execution settings: {batch}; choose a new timestamp')
            manifests[batch] = data
        manifests[batch]['tasks'][task.name] = revisions[task]
    # Preflight every destination before creating any files.
    for batch, data in manifests.items():
        prompt = next(prompts[task] for task in active if jobs / task.parent.name / batch_name == batch)
        data['task_set_revision'] = fingerprint(data['tasks'])
        batch.mkdir(parents=True, exist_ok=True)
        (batch / 'execution.toml').write_text(dumps(data))
        if prompt:
            (batch / 'prompt').write_text(prompt)
    return active


def historical_parameters(config: dict, transport: str, attempts: int) -> dict:
    agents = config.get('agents', [])
    if len(agents) != 1:
        raise ValueError('Expected one recorded agent per historical job')
    agent = agents[0]
    kwargs = agent.get('kwargs', {})
    verifier = config.get('verifier', {}).get('kwargs', {})
    fields = {
        'transport': transport, 'execution_mode': kwargs.get('execution_mode'),
        'agent_name': kwargs.get('agent_name'), 'model': agent.get('model_name'),
        'reasoning_effort': kwargs.get('reasoning_effort'),
        'service_tier': kwargs.get('service_tier', '') if kwargs.get('agent_name') == 'codex' else '',
        'evaluator_model': verifier.get('model'),
        'evaluator_reasoning_effort': verifier.get('reasoning_effort'),
        'agent_timeout_sec': kwargs.get('timeout_sec'), 'n_attempts': attempts,
    }
    return {key: value for key, value in fields.items() if value is not None}


def historical_manifest(batch: Path, transport: str) -> dict:
    parameters = None
    digests = {}
    for job in sorted(p for p in batch.iterdir() if (p / 'variant.toml').is_file()):
        lock = json.loads((job / 'lock.json').read_text())
        trials = lock.get('trials', [])
        settings = historical_parameters(json.loads((job / 'config.json').read_text()), transport, len(trials))
        if parameters is not None and parameters != settings:
            raise ValueError(f'Mixed historical execution settings in {batch}')
        parameters = settings
        values = {trial['task']['digest'] for trial in trials}
        if len(values) == 1:
            digests[job.name] = values.pop()
    if parameters is None:
        raise ValueError(f'No historical jobs in {batch}')
    return {
        'schema_version': 1, 'scenario_id': batch.parent.name,
        'configuration_fingerprint': fingerprint(parameters),
        'revision_status': 'historical-harbor-digests',
        'parameters': parameters,
        'recorded_task_digests': digests,
        'provenance': {'transport_source': 'user-confirmed', 'settings_source': 'saved-job-configs'},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--jobs-root', required=True, type=Path)
    parser.add_argument('--batch', required=True)
    parser.add_argument('--skip-existing', action='store_true')
    parser.add_argument('--parameter', action='append', default=[])
    parser.add_argument('--harbor-dir', default='')
    parser.add_argument('--provider-dir', default='')
    parser.add_argument('tasks', nargs='+', type=Path)
    args = parser.parse_args()
    parameters = dict(value.split('=', 1) for value in args.parameter)
    for field in ('agent_timeout_sec', 'n_attempts', 'parallel_limit'):
        parameters[field] = int(parameters[field])
    parameters['harbor_revision'] = runtime_revision(args.harbor_dir, 'harbor')
    parameters['provider_revision'] = runtime_revision(args.provider_dir, 'harbor-antrieb')
    try:
        active = prepare(args.jobs_root, args.batch, args.tasks, parameters, args.skip_existing)
    except (OSError, ValueError) as exc:
        parser.exit(2, f'{exc}\n')
    if not active:
        print(f'Skipped {len(args.tasks)} existing task(s); nothing to run.', file=sys.stderr)
    for task in active:
        print(task)


if __name__ == '__main__':
    main()
