#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from .backup import BackupManager
from .config import load_config, save_config
from .progress import LiveProgress
import questionary
from questionary import Style

# Executable support
if getattr(sys, 'frozen', False):
    # Running as compiled executable
    import os
    os.environ['BACKUP_TOOL_MODE'] = 'executable'
    
    # Windows-specific setup
    if sys.platform == 'win32':
        from .win_utils import setup_windows_path
        if not setup_windows_path():
            print("Run as administrator to add to system PATH")

custom_style = Style([
    ('qmark', 'fg:#34eb9b bold'),
    ('question', 'bold fg:#ffffff'),
    ('answer', 'fg:#34ebde bold'),
    ('pointer', 'fg:#eb34b4 bold'),
    ('selected', 'fg:#ebd534'),
])

class BackupCLI:
    def __init__(self):
        self.config = load_config()
        self.manager = BackupManager()
        self.progress = LiveProgress()

    def interactive_mode(self):
        """Run in interactive mode"""
        try:
            while True:
                action = self._main_menu()
                if action == 'exit':
                    break
        except KeyboardInterrupt:
            print("\nOperation cancelled.")

    def _main_menu(self):
        action = questionary.select(
            "Backup Tool - Main Menu",
            choices=[
                {'name': 'Run Backup', 'value': 'backup'},
                {'name': 'Cleanup Old Files', 'value': 'cleanup'},
                {'name': 'View Statistics', 'value': 'stats'},
                {'name': 'Configure Settings', 'value': 'config'},
                {'name': 'Exit', 'value': 'exit'}
            ],
            style=custom_style
        ).ask()
        
        if action == 'backup':
            self._run_backup()
        elif action == 'cleanup':
            self._run_cleanup()
        elif action == 'stats':
            self._show_stats()
        
        return action

    def _run_backup(self):
        source = questionary.path(
            "Source directory:",
            default=self.config.get('last_source', ''),
            style=custom_style
        ).ask()
        
        dest = questionary.path(
            "Destination directory:",
            default=self.config.get('last_destination', ''),
            style=custom_style
        ).ask()
        
        self.progress.start()
        try:
            success = self.manager.run_backup(source, dest, self.progress.update)
            if success:
                self.config['last_source'] = source
                self.config['last_destination'] = dest
                save_config(self.config)
        finally:
            self.progress.stop()

def main():
    parser = argparse.ArgumentParser(description="Generic Backup Tool")
    parser.add_argument('-i', '--interactive', action='store_true', help="Interactive mode")
    args = parser.parse_args()
    
    if args.interactive:
        BackupCLI().interactive_mode()
    else:
        print("Use -i for interactive mode or see --help")

if __name__ == "__main__":
    main()