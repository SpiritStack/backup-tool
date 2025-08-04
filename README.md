# Generic Backup Tool

![Backup Tool Demo](docs/demo.gif)

A cross-platform backup solution with:
- Real-time progress tracking
- Safe file handling (moves to trash instead of delete)
- Interactive and scriptable modes
- Performance statistics

## Features

- ✅ **Incremental Backups** - Only copies changed files
- 📊 **Live Progress** - ETA, transfer speed, and progress bar
- 🗑️ **Safe Cleanup** - Files moved to trash instead of permanent deletion
- 📝 **Comprehensive Logging** - Detailed operation statistics
- 🖥️ **Cross-Platform** - Works on Windows, macOS, and Linux

## Installation

```bash
pip install backup-tool
```

Or from source:

```bash
git clone https://github.com/yourusername/backup-tool.git
cd backup-tool
pip install .
```

## Usage

**Interactive Mode:**
```bash
backup-tool -i
```

**Command Line:**
```bash
backup-tool --source /path/to/source --dest /path/to/backup
```

## Documentation

See [docs/usage.md](docs/usage.md) for complete documentation.

## Installation Instructions

For Linux/macOS:
bash
# Install dependencies
sudo apt-get install rsync  # On Debian/Ubuntu
brew install rsync         # On macOS

# Install Python package
pip3 install backup-tool --user

# Run it
backup-tool -i
For Windows:
Install Git for Windows (includes rsync)

Install Python 3.8+ from python.org

Run in Command Prompt:

cmd
pip install backup-tool
backup-tool -i

## License

MIT - See [LICENSE](LICENSE)