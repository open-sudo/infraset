"""Exercise scenario inheritance through the runner with a fake Harbor process."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RunnerScenarioTests(unittest.TestCase):
    def test_multiple_scenarios_and_removed_id_option(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            credentials = root / 'credentials.env'
            credentials.write_text('ANTRIEB_TOKEN=test-only\n')
            credentials.chmod(0o600)
            uv = root / 'uv'
            uv.write_text('''#!/usr/bin/env python3
import json, sys, subprocess, os
from pathlib import Path
args = sys.argv[1:]
if 'python' in args and any(Path(a).name in ('execution_metadata.py', 'generate_job_index.py') for a in args):
    sys.exit(subprocess.call(['python3.11', *args[args.index('python') + 1:]]))
if 'harbor' not in args:
    sys.exit(0)
job = Path(args[args.index('--jobs-dir') + 1]) / args[args.index('--job-name') + 1]
(job / 'received-prompt').write_text(os.environ.get('INFRASET_EXECUTOR_PROMPT', 'missing'))
(job / 'result.json').write_text(json.dumps({'n_total_trials': 1, 'stats': {'n_completed_trials': 1}}))
''')
            uv.chmod(0o755)
            env = {**os.environ, 'PATH': str(root) + ':' + os.environ['PATH'],
                   'CREDENTIALS_FILE': str(credentials), 'INFRASET_JOBS_DIR': str(root / 'jobs'),
                   'INFRASET_JOB_NAME': 'check', 'INFRASET_ID': '9999'}
            paths = []
            for scenario, usecase in (('4523', 'nginx'), ('4523', 'dns'), ('7812', 'nginx')):
                task = root / 'tasks' / scenario / f'{usecase}-bash-ubuntu7-{scenario}'
                (task / 'environment').mkdir(parents=True)
                (task / 'task.toml').write_text('')
                (task / 'instruction.md').write_text('Serve HTTP.\n')
                (task / 'variant.toml').write_text(f'id = "{scenario}"\n')
                (task / 'environment/harbor_antrieb.toml').write_text('')
                paths.append(task)
            extra_prompt = 'Protect credentials.\nStop before unsafe workarounds.\n'
            (root / 'tasks/4523/prompt').write_text(extra_prompt)
            env['INFRASET_EXECUTOR_PROMPT'] = 'must not leak from parent'
            def run(*args, code=0):
                result = subprocess.run(['bash', str(ROOT / 'run-task.sh'), *map(str, args)],
                                        env=env, text=True, capture_output=True)
                self.assertEqual(result.returncode, code, result.stdout + result.stderr)
                return result.stdout + result.stderr
            run('--transport', 'direct', '--mode', 'batch', *paths)
            for task in paths:
                snapshot = tomllib.loads((root / 'jobs' / task.parent.name / 'check' / task.name / 'variant.toml').read_text())
                received = root / 'jobs' / task.parent.name / 'check' / task.name / 'received-prompt'
                self.assertEqual(received.read_text(), extra_prompt if task.parent.name == '4523' else '')
                self.assertEqual(snapshot['id'], task.parent.name)
                self.assertEqual(snapshot['run'], {'id': task.parent.name, 'execution_mode': 'batch', 'transport': 'direct'})
            index = (root / 'jobs/INDEX.md').read_text()
            self.assertIn('GENERATED', index)
            self.assertIn('3 jobs', index)
            self.assertIn('direct / batch', index)
            self.assertIn('completed', index)
            self.assertIn('Skipped 3 existing task(s)', run('--skip-existing', '--transport', 'direct', '--mode', 'batch', *paths))
            env['INFRASET_JOB_NAME'] = 'trentina-check'
            run('--skip-existing', '--transport', 'trentina', '--mode', 'batch', *paths)
            for task in paths:
                manifest = tomllib.loads((root / 'jobs' / task.parent.name / 'trentina-check/execution.toml').read_text())
                self.assertEqual(manifest['parameters']['transport'], 'trentina')
                self.assertTrue((root / 'jobs' / task.parent.name / 'trentina-check' / task.name / 'result.json').exists())
            self.assertIn('Unknown option: --id', run('--id', '9999', paths[0], code=2))
            self.assertNotIn('--id', run('--help'))
            wrong = paths[0].with_name('nginx-bash-ubuntu7-9999')
            paths[0].rename(wrong)
            self.assertIn('must end with its scenario ID', run(wrong, code=2))


if __name__ == '__main__':
    unittest.main()
