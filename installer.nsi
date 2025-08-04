!include "MUI2.nsh"

Name "Backup Tool"
OutFile "BackupTool-Installer.exe"
InstallDir "$PROGRAMFILES\BackupTool"

!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"

Section
  SetOutPath $INSTDIR
  File "dist\backup-tool-windows.exe"
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
  # Add to PATH
  EnVar::AddValue "PATH" "$INSTDIR"
  
  # Create shortcuts
  CreateDirectory "$SMPROGRAMS\BackupTool"
  CreateShortcut "$SMPROGRAMS\BackupTool\Backup Tool.lnk" "$INSTDIR\backup-tool-windows.exe"
SectionEnd

Section "Uninstall"
  Delete "$INSTDIR\backup-tool-windows.exe"
  Delete "$INSTDIR\uninstall.exe"
  RMDir "$INSTDIR"
  
  # Remove from PATH
  EnVar::DeleteValue "PATH" "$INSTDIR"
  
  # Remove shortcuts
  Delete "$SMPROGRAMS\BackupTool\Backup Tool.lnk"
  RMDir "$SMPROGRAMS\BackupTool"
SectionEnd