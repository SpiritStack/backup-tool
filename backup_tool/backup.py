import subprocess
import json
from pathlib import Path
from datetime import datetime
from send2trash import send2trash
from .utils import format_size, format_time

class BackupManager:
    def __init__(self):
        self.stats = {
            'files_processed': 0,
            'bytes_processed': 0,
            'total_files': 0,
            'total_size': 0
        }

    def run_backup(self, source, destination, progress_callback=None):
        """Run the backup operation"""
        self._estimate_size(source, destination)
        
        cmd = [
            'rsync', '-rltD', '--update', '--info=progress2',
            '--out-format=%n', f"{source}/", destination
        ]
        
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        
        for line in process.stderr:
            if progress_callback:
                progress_callback(self._parse_line(line))
        
        return process.wait() == 0

    def _estimate_size(self, source, destination):
        """Estimate total backup size"""
        cmd = ['rsync', '-n', '-r', '--stats', f"{source}/", destination]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        for line in result.stderr.splitlines():
            if 'Total file size' in line:
                self.stats['total_size'] = int(line.split(':')[1].strip().split()[0])
            elif 'Number of files' in line:
                self.stats['total_files'] = int(line.split(':')[1].strip().split()[0])

    def _parse_line(self, line):
        """Parse rsync output line"""
        if line.startswith('>f+++++++++'):
            self.stats['files_processed'] += 1
        return self.stats