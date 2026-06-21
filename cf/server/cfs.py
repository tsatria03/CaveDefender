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
VERSION_TXT = HERE.parent.parent / "build" / "version.txt"
VERSION_NVGT = HERE.parent.parent / "src" / "server" / "includes" / "version.nvgt"


def sync_version():
    # build/version.txt is the single source of truth for the version number; mirror it into the server's
    # version.nvgt before launching so interpreted runs (and the window title) always reflect it without
    # hand-editing version.nvgt. Silent no-op if version.txt is missing or already matches.
    try:
        with open(VERSION_TXT, "r", encoding="utf-8", newline="") as f:
            value = f.read().strip()
    except OSError:
        return
    if not value:
        return
    line = 'const string version="%s";\r\n' % value
    try:
        with open(VERSION_NVGT, "r", encoding="utf-8", newline="") as f:
            if f.read() == line:
                return
    except OSError:
        pass
    try:
        with open(VERSION_NVGT, "w", encoding="utf-8", newline="") as f:
            f.write(line)
    except OSError:
        pass


if not Path(NVGT).is_file():
    print("Could not find the NVGT runtime at:\n" + NVGT)
    input("Press Enter to exit...")
    sys.exit(1)
if not SCRIPT.is_file():
    print("Could not find the server script at:\n" + str(SCRIPT))
    input("Press Enter to exit...")
    sys.exit(1)

sync_version()
print("Started CaveDefender server")
result = subprocess.run([NVGT, str(SCRIPT)], cwd=str(HERE))
if result.returncode != 0:
    print("The server exited with an error (code %d)." % result.returncode)
    input("Press Enter to exit...")
