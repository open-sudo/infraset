"""Scenario path compatibility and flat job discovery."""
import json
from pathlib import Path
import tempfile
import unittest

from job_layout import job_location
from scenario_layout import collection_asset, resolve_task_path, original_task_path


class ScenarioLayoutTests(unittest.TestCase):
    def test_historical_paths_and_flat_job(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'data').mkdir()
            old = 'vanilla/services/rhel7/nginx-rhel7'
            new = '4523/nginx-bash-rhel7-4523'
            (root / 'data/scenario-layout.json').write_text(json.dumps({
                'scenarios': [{'id': '4523', 'collection': 'vanilla'}],
                'tasks': {old: new},
            }))
            self.assertEqual(resolve_task_path(root / 'tasks' / old, root), root / 'tasks' / new)
            self.assertEqual(resolve_task_path(root / 'tasks/services/rhel7/nginx-rhel7/instruction.md', root), root / 'tasks' / new / 'instruction.md')
            self.assertEqual(original_task_path(root / 'tasks' / new, root), root / 'tasks' / old)
            self.assertEqual(collection_asset('vanilla', 'services/catalog.toml', root), root / 'tasks/4523/_collection/services/catalog.toml')
            job = root / 'jobs/nginx-bash-rhel7-4523/2026-10-04__12-00-00'
            job.mkdir(parents=True)
            (job / 'variant.toml').write_text('id = "4523"\ncategory = "services"\nos = "rhel7"\n')
            location = job_location(job, root / 'jobs')
            self.assertEqual(location.runner, '4523')
            self.assertEqual(location.category, 'services')
            self.assertEqual(location.task_name, 'nginx-bash-rhel7-4523')
            grouped = root / 'jobs/4523/2026-10-04__12-00-00/nginx-bash-rhel7-4523'
            grouped.parent.mkdir(parents=True)
            job.rename(grouped)
            for scope in (root / 'jobs', grouped.parent.parent, grouped.parent):
                location = job_location(grouped, scope)
                self.assertEqual(location.runner, '4523')
                self.assertEqual(location.category, 'services')
                self.assertEqual(location.run_name, '2026-10-04__12-00-00')
                self.assertEqual(location.task_name, grouped.name)



if __name__ == '__main__':
    unittest.main()
