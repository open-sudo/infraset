import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from generate_job_index import generate, render, status


class JobIndexTests(unittest.TestCase):
    def test_historical_fallback_partial_results_and_concurrent_updates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            jobs = []
            for name in ('one', 'two'):
                job = root / '5782/2026-10-01__10-00-00' / f'{name}-bash-ubuntu7-5782'
                job.mkdir(parents=True)
                (job / 'variant.toml').write_text('id="5782"\nos="ubuntu7"\nlanguage="bash"\n[run]\ntransport="direct"\n')
                (job / 'config.json').write_text(json.dumps({'agents': [{'model_name': 'model-x', 'kwargs': {'execution_mode': 'batch', 'agent_name': 'codex'}}]}))
                jobs.append(job)
            (jobs[0] / 'result.json').write_text('{')
            generate(root)
            text = (root / 'INDEX.md').read_text()
            self.assertIn('GENERATED', text)
            self.assertIn('2 jobs', text)
            self.assertIn('| OS | Language |', text)
            self.assertIn('| ubuntu7 | bash |', text)
            self.assertIn('codex / model-x', text)
            self.assertIn('direct / batch', text)
            self.assertIn('pending / no result', text)
            processes = [subprocess.Popen([sys.executable, str(Path(__file__).with_name('generate_job_index.py')), '--jobs-root', str(root), '--job', str(job), '--status', state]) for job, state in zip(jobs, ('failed', 'interrupted'))]
            for process in processes:
                self.assertEqual(process.wait(), 0)
            text = (root / 'INDEX.md').read_text()
            self.assertIn('| failed |', text)
            self.assertIn('| interrupted |', text)
            for job in jobs:
                self.assertEqual(text.count('[' + job.name + ']'), 1)
            (root / '5782/2026-10-01__10-00-00/execution.toml').write_text('[parameters]\ntransport="trentina"\nmodel="model-y"\n')
            self.assertIn('trentina / batch', render(root))
            self.assertIn('model-y', render(root))

    def test_completion_is_not_inferred_from_runner_exit(self):
        self.assertEqual(status({}, {'status': 'finished'}), 'finished; no complete result')
        self.assertEqual(status({'n_total_trials': 1, 'stats': {'n_completed_trials': 1}}, {}), 'completed')
        self.assertEqual(status({'stats': {'n_errored_trials': 1}}, {}), 'errors')


if __name__ == '__main__':
    unittest.main()
