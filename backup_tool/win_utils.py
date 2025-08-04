import os
import sys
import ctypes
from pathlib import Path

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def setup_windows_path():
    """Add to PATH if running as admin"""
    if not is_admin():
        return False
        
    install_dir = Path(os.environ['PROGRAMDATA']) / 'BackupTool'
    install_dir.mkdir(exist_ok=True)
    
    # Add to system PATH
    import winreg
    with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
        with winreg.OpenKey(hkey, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 0, winreg.KEY_ALL_ACCESS) as sub_key:
            path = winreg.QueryValueEx(sub_key, 'Path')[0]
            if str(install_dir) not in path:
                winreg.SetValueEx(sub_key, 'Path', 0, winreg.REG_EXPAND_SZ, path + f';{install_dir}')
    
    return True