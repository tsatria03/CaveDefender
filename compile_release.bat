@echo off
cd /d "%~dp0"

echo Compiling client...
"C:\nvgt\nvgt.exe" -c client\cfc.nvgt
if errorlevel 1 (
echo Client compilation failed; nothing was assembled.
pause
exit /b 1
)

echo Compiling server...
"C:\nvgt\nvgt.exe" -c server\cfs.nvgt
if errorlevel 1 (
echo Server compilation failed; nothing was assembled.
pause
exit /b 1
)

if exist "releases\windows\CaveDefender" rmdir /s /q "releases\windows\CaveDefender"
mkdir "releases\windows\CaveDefender\client"
mkdir "releases\windows\CaveDefender\server"

move "client\cfc" "releases\windows\CaveDefender\client\cfc"
move "server\cfs" "releases\windows\CaveDefender\server\cfs"

echo Done. The build is in releases\windows\CaveDefender (client\cfc and server\cfs).
pause
