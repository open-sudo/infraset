#!/usr/bin/env python3
"""Rebuild metrics for each recorded scenario/batch without combining executions."""
from pathlib import Path
import os
import tomllib

from generate_category_summary import (
    ROOT, completed_jobs, build_matrix_category, build_mixed_os_scenarios,
)
from generate_provisioning_metrics import build as build_provisioning, samples
from scenario_layout import collection_asset


def rebuild() -> None:
    indexes = {}
    reports = 0
    for scenario in sorted((ROOT / 'jobs').iterdir()):
        if not scenario.is_dir() or not (len(scenario.name) == 4 and scenario.name.isdigit()):
            continue
        for batch in sorted(scenario.iterdir()):
            if not batch.is_dir():
                continue
            jobs = sorted(p for p in batch.iterdir() if (p / 'variant.toml').is_file())
            if not jobs:
                continue
            out = ROOT / 'metrics' / scenario.name / batch.name
            out.mkdir(parents=True, exist_ok=True)
            scope = f'{scenario.name}/{batch.name}'
            categories = sorted({tomllib.loads((job / 'variant.toml').read_text())['category'] for job in jobs})
            pages = []
            for category in categories:
                selected = completed_jobs([batch], category)
                if not selected:
                    continue
                if collection_asset('vanilla', f'{category}/catalog.toml').is_file():
                    content = build_matrix_category(category, selected, out, batch, scope)
                elif category == 'mixed-os-scenarios':
                    content = build_mixed_os_scenarios(selected, out, scope)
                else:
                    continue
                name = category + '.md'
                (out / name).write_text(content)
                pages.append(name)
            if samples(batch):
                name = 'cluster-provisioning-performance.md'
                (out / name).write_text(build_provisioning(batch, scope))
                pages.append(name)
            lines = [f'# Execution metrics: {scope}', '',
                     f'Jobs: {len(jobs)}. Reports cover recorded observations in this batch only.', '']
            execution = batch / 'execution.toml'
            if execution.is_file():
                parameters = tomllib.loads(execution.read_text()).get('parameters', {})
                lines += [f"Transport: `{parameters.get('transport', 'unrecorded')}`. "
                          f"[Execution settings]({os.path.relpath(execution, out)}).", '']
            lines += [f'- [{name[:-3]}]({name})' for name in pages]
            if not pages:
                lines += ['No category or provisioning metrics are available from the recorded observations in this batch.', '']
            lines += ['', '## Jobs', '']
            lines += [f'- [{job.name}]({os.path.relpath(job, out)}/)' for job in jobs]
            (out / 'README.md').write_text('\n'.join(lines) + '\n')
            indexes.setdefault(scenario.name, []).append(batch.name)
            reports += len(pages)
    for scenario, batches in indexes.items():
        out = ROOT / 'metrics' / scenario
        lines = [f'# Scenario {scenario} metrics', '', 'Each timestamp identifies a separate execution batch.', '']
        lines += [f'- [{batch}]({batch}/)' for batch in batches]
        comparisons = sorted(out.glob('*report.md'))
        if comparisons:
            lines += ['', '## Comparisons', ''] + [f'- [{p.stem}]({p.name})' for p in comparisons]
        (out / 'README.md').write_text('\n'.join(lines) + '\n')
    print(f'Generated {reports} reports across {sum(map(len, indexes.values()))} batches and {len(indexes)} scenarios.')


if __name__ == '__main__':
    rebuild()
