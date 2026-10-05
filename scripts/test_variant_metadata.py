"""Regression checks for the searchable metadata contract; no managed resources."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import variant_metadata as metadata


class VariantMetadataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.task = self.root / 'tasks/vanilla-ansible/networking/ubuntu24/log-collector-ubuntu24'
        (self.task / 'environment').mkdir(parents=True)
        (self.task / 'instruction.md').write_text('Keep logs searchable.\n\nImplement using Ansible.\n')
        (self.task / 'task.toml').write_text('[metadata]\ndifficulty = "hard"\n')
        (self.task / 'environment/harbor_antrieb.toml').write_text(
            'cluster = ["ubuntu24.04 x2", "vyos", "ansible-controller"]\n')
        with patch.object(metadata, 'ROOT', self.root):
            self.data = metadata.initial_metadata(self.task)
        target = self.root / 'tasks/4523/log-collector-ansible-ubuntu24-4523'
        target.parent.mkdir(parents=True)
        self.task.rename(target)
        self.task = target
        self.data['id'] = '4523'
        self.write()

    def write(self):
        (self.task / 'variant.toml').write_text(metadata.dumps(self.data))

    def test_target_os_preserved_with_appliance_and_controller(self):
        data = metadata.validate(self.task)
        self.assertEqual(data['usecase'], 'log-collector')
        self.assertEqual(data['language'], 'ansible')
        self.assertEqual(data['os'], 'ubuntu24')
        self.assertEqual(data['environment']['node_count'], 4)
        self.assertNotIn('run', data)

    def test_prompt_change_requires_metadata_update(self):
        (self.task / 'instruction.md').write_text('A different prompt.\n')
        with self.assertRaisesRegex(ValueError, 'stale'):
            metadata.validate(self.task)

    def test_mixed_os_usecase_retains_its_full_name(self):
        mixed = self.root / 'tasks/vanilla/mixed-os-scenarios/greenfield/nginx-alma-alpine'
        with patch.object(metadata, 'ROOT', self.root):
            data = metadata.initial_metadata(mixed, instruction='Serve HTTP.\n',
                environment='cluster = ["almalinux9 x2", "alpine x2"]\n',
                task_config='[metadata]\ndifficulty = "medium"\n')
        self.assertEqual(data['os'], 'mixed')
        self.assertEqual(data['usecase'], 'nginx-alma-alpine')

    def test_environment_change_is_detected(self):
        (self.task / 'environment/harbor_antrieb.toml').write_text('cluster = ["ubuntu7.10"]\n')
        with self.assertRaisesRegex(ValueError, 'environment metadata'):
            metadata.validate(self.task)

    def test_run_settings_rejected_in_task_descriptor(self):
        self.data['run'] = {'id': 'one', 'execution_mode': 'batch'}
        self.write()
        with self.assertRaisesRegex(ValueError, 'saved job snapshot'):
            metadata.validate(self.task)

    def test_editorial_fields_survive_initialization(self):
        self.data['title'] = 'Our curated title'
        self.write()
        before = (self.task / 'variant.toml').read_bytes()
        with patch('sys.argv', ['variant_metadata.py', 'init', str(self.task)]), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(metadata.main(), 0)
        self.assertEqual(before, (self.task / 'variant.toml').read_bytes())

    def test_failed_index_does_not_emit_partial_records(self):
        bad = self.task.parent / 'bad-task'
        bad.mkdir()
        (bad / 'task.toml').write_text('')
        output = io.StringIO()
        with patch('sys.argv', ['variant_metadata.py', 'index', str(self.root)]), contextlib.redirect_stdout(output), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(metadata.main(), 1)
        self.assertEqual(output.getvalue(), '')


if __name__ == '__main__':
    unittest.main()
