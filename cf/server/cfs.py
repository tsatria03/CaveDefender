import sys
import subprocess
from pathlib import Path

# Launch the CaveDefender server, supervised. We run downcheck (the supervisor), not the server
# directly: downcheck launches the server and relaunches it after any /restart, /fastrestart, or crash,
# so the server always comes back on its own. The .nvgt source lives in src/server, but the assets
# (data, docks, lib) live here in cf/server, so we run with cwd set to this folder -- and downcheck
# passes that same cwd to the server it spawns. Run as a .py (python.exe) so a console is present;
# subprocess.run blocks until downcheck exits, keeping the window open for the whole session. Close this
# window to stop the server for good. (To run the server once WITHOUT supervision, launch
# "C:\nvgt2\nvgt.exe src/server/cfs.nvgt" from this folder by hand instead.)

NVGT = r"C:\nvgt2\nvgt.exe"
HERE = Path(__file__).resolve().parent
SCRIPT = HERE.parent.parent / "src" / "server" / "downcheck.nvgt"
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
    print("Could not find the supervisor script (downcheck.nvgt) at:\n" + str(SCRIPT))
    input("Press Enter to exit...")
    sys.exit(1)

sync_version()
print("Started CaveDefender server (supervised by downcheck)")
result = subprocess.run([NVGT, str(SCRIPT)], cwd=str(HERE))
if result.returncode != 0:
    print("Downcheck exited with an error (code %d)." % result.returncode)
    input("Press Enter to exit...")
