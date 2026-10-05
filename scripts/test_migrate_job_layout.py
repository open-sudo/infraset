"""Moving historical jobs must preserve artifacts and reject destination collisions."""
import tempfile
from pathlib import Path
import unittest

from migrate_job_layout import migrate


class JobMigrationTests(unittest.TestCase):
    def job(self, root, path):
        job = root / 'jobs' / path
        job.mkdir(parents=True)
        (job / 'instruction.md').write_bytes(b'Original prompt\r\n')
        (job / 'variant.toml').write_text('id = "4523"\nusecase = "nginx"\nlanguage = "bash"\nos = "ubuntu7"\n[run]\nid = "4523"\n')
        (job / 'trial').mkdir()
        (job / 'trial/log.txt').write_bytes(b'\x00historical log\xff')
        return job

    def test_preserves_contents_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            old = self.job(root, 'old/category/nginx-ubuntu7/2026-01-01__00-00-00')
            contents = {p.relative_to(old): p.read_bytes() for p in old.rglob('*') if p.is_file()}
            self.assertEqual(migrate(root)['would_move'], 1)
            self.assertTrue(old.exists())
            self.assertEqual(migrate(root, write=True)['moved'], 1)
            new = root / 'jobs/4523/2026-01-01__00-00-00/nginx-bash-ubuntu7-4523'
            for relative, content in contents.items():
                self.assertEqual((new / relative).read_bytes(), content)
            self.assertFalse(old.exists())
            self.assertEqual(migrate(root, write=True)['moved'], 0)

    def test_collision_does_not_move_any_jobs(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            one = self.job(root, 'one/2026-01-01__00-00-00/nginx')
            two = self.job(root, 'two/2026-01-01__00-00-00/nginx')
            with self.assertRaisesRegex(ValueError, 'collision'):
                migrate(root, write=True)
            self.assertTrue(one.is_dir() and two.is_dir())
            self.assertFalse((root / 'data/job-layout.json').exists())


if __name__ == '__main__':
    unittest.main()
