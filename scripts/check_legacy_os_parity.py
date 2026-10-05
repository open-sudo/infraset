#!/usr/bin/env python3
"""Check that the legacy OS comparison changes only the selected image."""

from pathlib import Path
from scenario_layout import collection_tasks, resolve_task_path
from legacy2.catalog import FAMILIES
try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and earlier
    import tomli as tomllib


ROOT = Path(__file__).resolve().parents[1] / "tasks"
SYSTEMS = {"centos5": "centos5.11", "ubuntu7": "ubuntu7.10"}


def check() -> int:
    pairs = 0
    expected_tasks = set()
    for group, count in (("single-node-os-comparison", 30), ("multi-node-os-comparison", 10)):
        matrix = ROOT.parent / "scripts" / "legacy2" / "catalogs"
        catalog = tomllib.loads((matrix / (group + ".toml")).read_text())
        actual = {item["id"]: item["image"] for item in catalog["operating_systems"]}
        if actual != SYSTEMS or len(catalog["tasks"]) != count:
            raise ValueError(f"{group}: unexpected systems or family count")
        extensions = [f for f in FAMILIES if (f['nodes'] == 1) == (group == 'single-node-os-comparison')]
        families = catalog['tasks'] + extensions
        if len({f['slug'] for f in families}) != len(families):
            raise ValueError(f'{group}: duplicate family')
        for family in families:
            paths = [resolve_task_path(ROOT / ("bash-" + os) / group / f'{family["slug"]}-{os}') for os in SYSTEMS]
            expected_tasks.update(p / "task.toml" for p in paths)
            files = [{p.relative_to(task) for p in task.rglob("*") if p.is_file()} for task in paths]
            if files[0] != files[1]:
                raise ValueError(f"{family['slug']}: different task files")
            for relative in files[0]:
                contents = [(task / relative).read_bytes() for task in paths]
                if relative == Path("environment/harbor_antrieb.toml"):
                    environments = [tomllib.loads(content.decode()) for content in contents]
                    for environment, image in zip(environments, SYSTEMS.values()):
                        normalized = []
                        for entry in environment["cluster"]:
                            tokens = entry.split()
                            if tokens[0] != image:
                                raise ValueError(f"{family['slug']}: unexpected image {tokens[0]}")
                            normalized.append(" ".join(["OS_IMAGE", *tokens[1:]]))
                        environment["cluster"] = normalized
                    if environments[0] != environments[1]:
                        raise ValueError(f"{family['slug']}: topology, resources, or preparation differ")
                elif relative == Path('variant.toml'):
                    from variant_metadata import validate
                    metadata = [validate(task) for task in paths]
                    for item in metadata:
                        item['id'] = 'ID'
                        item['os'] = 'OS'
                        item['environment']['images'] = ['OS_IMAGE']
                    if metadata[0] != metadata[1]:
                        raise ValueError(f"{family['slug']}: variant metadata differs beyond OS")
                elif contents[0] != contents[1]:
                    raise ValueError(f"{family['slug']}: {relative} differs between OSes")
            pairs += 1
    unexpected = {task / "task.toml" for os in SYSTEMS for task in collection_tasks("bash-" + os)} - expected_tasks
    missing = expected_tasks - {task / "task.toml" for os in SYSTEMS for task in collection_tasks("bash-" + os)}
    if unexpected or missing:
        raise ValueError(f"Unpaired or missing tasks: {sorted(unexpected | missing)}")
    if pairs != 100:
        raise ValueError(f'Expected 100 paired families, found {pairs}')
    print(f"PASS: {pairs} paired families / {pairs * 2} tasks; only the OS image differs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(check())
