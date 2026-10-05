"""Historical job backfill must use saved facts and preserve existing descriptors."""
import json
from pathlib import Path
import tempfile
import unittest

from backfill_job_variants import backfill
from variant_metadata import digest, dumps, read


class BackfillTests(unittest.TestCase):
    def test_snapshots_missing_settings_and_idempotency(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tasks, jobs = root / 'tasks', root / 'jobs'
            source = tasks / 'vanilla/group/ubuntu7/example-ubuntu7'
            source.mkdir(parents=True)
            (source / 'variant.toml').write_text(dumps({
                'schema_version': 1, 'id': '4523', 'usecase': 'example', 'title': 'Example',
                'description': 'Current prompt, not the historical prompt.',
                'category': 'group', 'tags': ['group'], 'language': 'bash',
                'os': 'ubuntu7', 'difficulty': 'hard',
                'prompt': {'path': 'instruction.md', 'sha256': 'current'},
                'environment': {'images': ['ubuntu24.04'], 'node_count': 99, 'initial_state': 'brownfield'},
            }))
            job = jobs / 'vanilla/group/2026-01-01__00-00-00/ubuntu7/example-ubuntu7'
            job.mkdir(parents=True)
            (job / 'instruction.md').write_bytes(b'Historical request.\r\n')
            (job / 'environment.toml').write_text('cluster = ["ubuntu7.10 x2"]\n')
            before = {p: p.read_bytes() for p in root.rglob('*') if p.is_file()}
            self.assertEqual(backfill(jobs, tasks)['would_create'], 1)
            self.assertFalse((job / 'variant.toml').exists())
            self.assertEqual(backfill(jobs, tasks, write=True)['created'], 1)
            data = read(job / 'variant.toml')
            self.assertEqual(data['description'], 'Historical request.')
            self.assertEqual(data['prompt']['sha256'], digest(job / 'instruction.md'))
            self.assertEqual(data['environment']['node_count'], 2)
            self.assertEqual(data['run']['id'], '4523')
            self.assertEqual(data['backfill']['unrecorded_run_fields'], ['execution_mode', 'transport'])
            saved = (job / 'variant.toml').read_bytes()
            self.assertEqual(backfill(jobs, tasks, write=True)['created'], 0)
            self.assertEqual((job / 'variant.toml').read_bytes(), saved)
            for path, content in before.items():
                self.assertEqual(path.read_bytes(), content)
            newer = jobs / 'vanilla-batch/vanilla/group/ubuntu7/example-ubuntu7/2026-01-02__00-00-00'
            newer.mkdir(parents=True)
            for name in ('instruction.md', 'environment.toml'):
                (newer / name).write_bytes((job / name).read_bytes())
            (newer / 'config.json').write_text(json.dumps({
                'tasks': [{'path': '/old/workspace/tasks/group/ubuntu7/example-ubuntu7'}],
                'agents': [{'kwargs': {'execution_mode': 'batch'}}],
            }))
            self.assertEqual(backfill(jobs, tasks, write=True)['created'], 1)
            self.assertEqual(read(newer / 'variant.toml')['run']['execution_mode'], 'batch')
            legacy = read(newer / 'variant.toml')
            del legacy['run']['id']
            legacy['backfill']['unrecorded_run_fields'].append('id')
            (newer / 'variant.toml').write_text(dumps(legacy))
            self.assertEqual(backfill(jobs, tasks, write=True)['updated'], 1)
            repaired = read(newer / 'variant.toml')
            self.assertEqual(repaired['run']['id'], '4523')
            self.assertEqual(repaired['run']['execution_mode'], 'batch')
            self.assertNotIn('id', repaired['backfill']['unrecorded_run_fields'])
            self.assertEqual(backfill(jobs, tasks, write=True)['updated'], 0)


if __name__ == '__main__':
    unittest.main()
