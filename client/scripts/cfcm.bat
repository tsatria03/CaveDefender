@echo off
rem Compiles the CaveDefender client in release mode, then moves the bundled folder
rem (NVGT drops it at ..\cfc, next to cfc.nvgt) into this scripts folder.
rem Run from this folder (double-click) so the relative paths resolve.
cd /d "%~dp0"
"C:\nvgt\nvgt.exe" -c ../cfc.nvgt
if errorlevel 1 (
echo Compilation failed; the build was not moved.
pause
exit /b 1
)
if exist "cfc" rmdir /s /q "cfc"
move "..\cfc" "cfc"
pause
