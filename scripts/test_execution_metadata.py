import json
from pathlib import Path
import tempfile
import unittest

from execution_metadata import prepare, reusable, task_revision


class ExecutionMetadataTests(unittest.TestCase):
    def test_reuse_requires_settings_revision_and_completed_attempts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            task = root / 'tasks/5782/example-bash-ubuntu7-5782'
            task.mkdir(parents=True)
            (task / 'instruction.md').write_text('Install nginx')
            jobs = root / 'jobs'
            settings = {'transport': 'direct', 'model': 'example', 'execution_mode': 'interactive', 'n_attempts': 1}
            self.assertEqual(prepare(jobs, 'first', [task], settings), [task])
            job = jobs / '5782/first' / task.name
            job.mkdir()
            (job / 'result.json').write_text(json.dumps({'n_total_trials': 1, 'stats': {'n_completed_trials': 1}}))
            self.assertTrue(reusable(jobs, task, settings, task_revision(task)))
            self.assertEqual(prepare(jobs, 'second', [task], settings, True), [])
            for field, value in [('transport', 'trentina'), ('model', 'different'), ('execution_mode', 'batch'), ('n_attempts', 2)]:
                self.assertFalse(reusable(jobs, task, {**settings, field: value}, task_revision(task)))
            (task.parent / 'prompt').write_text('Additional guidance')
            self.assertEqual(prepare(jobs, 'prompted', [task], settings, True), [task])
            self.assertEqual((jobs / '5782/prompted/prompt').read_text(), 'Additional guidance')
            prompted_job = jobs / '5782/prompted' / task.name
            prompted_job.mkdir()
            (prompted_job / 'result.json').write_text((job / 'result.json').read_text())
            self.assertEqual(prepare(jobs, 'same-prompt', [task], settings, True), [])
            (task.parent / 'prompt').write_text('Changed guidance')
            self.assertEqual(prepare(jobs, 'changed-prompt', [task], settings, True), [task])
            (task / 'prepare.sh').write_text('echo changed')
            self.assertFalse(reusable(jobs, task, settings, task_revision(task)))
            with self.assertRaises(ValueError):
                prepare(jobs, 'first', [task], settings)
            other = task.with_name('other-bash-ubuntu7-5782')
            other.mkdir()
            with self.assertRaises(ValueError):
                prepare(jobs, 'first', [other], {**settings, 'transport': 'trentina'})
            self.assertFalse((jobs / '5782/first' / other.name).exists())


if __name__ == '__main__':
    unittest.main()
