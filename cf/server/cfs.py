import sys
import subprocess
from pathlib import Path

# Launch the CaveDefender server. The .nvgt source lives in src/server, but the
# assets (data, docks, lib) live here in cf/server, so we run with cwd set to
# this folder so every cwd-relative path resolves against cf/server. Run as a
# .py (python.exe) so a console is present; subprocess.run blocks until the server
# exits, keeping that window open for the whole session (it's the server's UI).

NVGT = r"C:\nvgt2\nvgt.exe"
HERE = Path(__file__).resolve().parent
SCRIPT = HERE.parent.parent / "src" / "server" / "cfs.nvgt"

if not Path(NVGT).is_file():
    print("Could not find the NVGT runtime at:\n" + NVGT)
    input("Press Enter to exit...")
    sys.exit(1)
if not SCRIPT.is_file():
    print("Could not find the server script at:\n" + str(SCRIPT))
    input("Press Enter to exit...")
    sys.exit(1)

print("Started CaveDefender server")
result = subprocess.run([NVGT, str(SCRIPT)], cwd=str(HERE))
if result.returncode != 0:
    print("The server exited with an error (code %d)." % result.returncode)
    input("Press Enter to exit...")
