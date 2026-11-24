@echo off
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
    "%LOCALAPPDATA%\Programs\Python\Launcher\py.exe" -3.12 tools.py
) else (
    py -3.12 tools.py
)
pause
