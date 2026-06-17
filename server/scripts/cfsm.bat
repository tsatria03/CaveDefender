@echo off
rem Compiles the CaveDefender server in release mode, then moves the bundled folder
rem (NVGT drops it at ..\cfs, next to cfs.nvgt) into this scripts folder.
rem Run from this folder (double-click) so the relative paths resolve.
cd /d "%~dp0"
"C:\nvgt\nvgt.exe" -c ../cfs.nvgt
if errorlevel 1 (
echo Compilation failed; the build was not moved.
pause
exit /b 1
)
if exist "cfs" rmdir /s /q "cfs"
move "..\cfs" "cfs"
pause
