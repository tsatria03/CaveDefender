@echo off
rem Compiles the CaveDefender client in release mode.
rem Run from this folder (double-click) so the script's relative paths resolve.
cd /d "%~dp0"
"C:\nvgt\nvgt.exe" -c ../cfc.nvgt
pause
