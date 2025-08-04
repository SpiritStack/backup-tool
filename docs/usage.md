# Backup Tool Usage Guide

## Basic Commands

**Interactive Mode:**
```bash
backup-tool -i
```

**Direct Backup:**
```bash
backup-tool --source /path/to/source --dest /path/to/backup
```

## Advanced Features

**Exclude Patterns:**
```bash
backup-tool --source src --dest backup --exclude "*.tmp" --exclude "temp/"
```

**Dry Run:**
```bash
backup-tool --source src --dest backup --dry-run
```

**Cleanup Old Backups:**
```bash
backup-tool --cleanup --dest /path/to/backup
```

## Configuration

The tool automatically creates a config file at:
- Linux/macOS: `~/.config/backup-tool/config.json`
- Windows: `%APPDATA%\backup-tool\config.json`

You can customize:
- Default exclude patterns
- History retention
- UI preferences