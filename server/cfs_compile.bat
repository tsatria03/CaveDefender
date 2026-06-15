@echo off
rem Compiles the CaveDefender server in release mode.
rem Run from this folder (double-click) so the script's relative data/ paths resolve.
cd /d "%~dp0"
"C:\nvgt\nvgt.exe" -c cfs.nvgt
pause
