@echo off
TITLE Heb-Eng Converter Installer
CLS

ECHO ========================================================
ECHO    Hebrew-English Text Converter Installer
ECHO    Target: Windows 11 / Python 3.x
ECHO ========================================================
ECHO.

:: 1. Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] Python is not detected. 
    ECHO Please install Python from python.org or the Microsoft Store first.
    PAUSE
    EXIT /B
)

:: 2. Check if the source file exists
IF NOT EXIST "language_switcher.py" (
    ECHO [ERROR] language_switcher.py not found!
    ECHO Please make sure language_switcher.py is in the same folder as this script.
    PAUSE
    EXIT /B
)

ECHO [1/5] Python detected. Installing dependencies...
pip install pyperclip pynput pyinstaller --upgrade
IF %ERRORLEVEL% NEQ 0 (
    ECHO [WARNING] Pip install reported an issue. Trying to continue anyway...
)

ECHO.
ECHO [2/5] Building the standalone EXE file...
:: --noconsole: Runs silently (no black window)
:: --onefile: Packs everything into one .exe
:: We use "python -m PyInstaller" to avoid "command not found" errors if PATH is missing
python -m PyInstaller --noconsole --onefile --name "HebEngFixer" language_switcher.py

IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] PyInstaller failed to build the program.
    ECHO Details above.
    PAUSE
    EXIT /B
)

ECHO.
ECHO [3/5] Moving program to permanent location...
:: Create a hidden folder in Local AppData so it's safe from accidental deletion
SET "INSTALL_DIR=%LOCALAPPDATA%\HebEngFixer"
IF NOT EXIST "%INSTALL_DIR%" MKDIR "%INSTALL_DIR%"

:: Move the new EXE there
MOVE /Y "dist\HebEngFixer.exe" "%INSTALL_DIR%\" >nul

ECHO.
ECHO [4/5] Cleaning up build junk...
RMDIR /S /Q build
RMDIR /S /Q dist
RMDIR /S /Q __pycache__
DEL /F /Q HebEngFixer.spec

ECHO.
ECHO [5/5] Creating Startup Shortcut...
SET "TARGET_EXE=%INSTALL_DIR%\HebEngFixer.exe"
SET "STARTUP_LINK=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\HebEngFixer.lnk"

:: Use PowerShell to create the shortcut
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%STARTUP_LINK%');$s.TargetPath='%TARGET_EXE%';$s.Description='Hebrew-English Keyboard Fixer';$s.Save()"

ECHO.
ECHO ========================================================
ECHO    INSTALLATION SUCCESSFUL!
ECHO ========================================================
ECHO.
ECHO 1. The program is now running in the background.
ECHO 2. It will start AUTOMATICALLY every time you turn on Windows.
ECHO 3. You can now safely delete this installer and the python file.
ECHO.
ECHO Starting the program now...
START "" "%TARGET_EXE%"

PAUSE