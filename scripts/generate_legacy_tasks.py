#!/usr/bin/env python3
"""Regenerate all 100 paired families in the merged legacy task suite."""
from pathlib import Path
import subprocess
import sys

SCRIPTS = Path(__file__).resolve().parent

if __name__ == '__main__':
    for name in ('generate_single_node_os_comparison_tasks.py',
                 'generate_multi_node_os_comparison_tasks.py',
                 'generate_legacy2_tasks.py',
                 'check_legacy_os_parity.py'):
        subprocess.run([sys.executable, str(SCRIPTS / name)], check=True)
