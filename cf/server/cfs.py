import os
import re
import sys
import shutil
import subprocess
from pathlib import Path

# Launch the CaveDefender server, supervised. We run downcheck (the supervisor), not the server
# directly: downcheck launches the server and relaunches it after any /restart, /fastrestart, or crash,
# so the server always comes back on its own. The .nvgt source lives in src/server, but the assets
# (data, docks, lib) live here in cf/server, so we run with cwd set to this folder -- and downcheck
# passes that same cwd to the server it spawns. Run as a .py (python.exe) so a console is present;
# subprocess.run blocks until downcheck exits, keeping the window open for the whole session. Close this
# window to stop the server for good. (To run the server once WITHOUT supervision, launch
# "C:\nvgt\nvgt.exe src/server/cfs.nvgt" from this folder by hand instead.)

NVGT = r"C:\nvgt\nvgt.exe"
HERE = Path(__file__).resolve().parent
SCRIPT = HERE.parent.parent / "src" / "server" / "downcheck.nvgt"
VERSION_TXT = HERE.parent.parent / "build" / "version.txt"
VERSION_NVGT = HERE.parent.parent / "src" / "server" / "includes" / "version.nvgt"
SERVER_DIR = HERE.parent.parent / "src" / "server"
SERVER_SCRIPT = SERVER_DIR / "cfs.nvgt"
# Where a compile-error report is written: the folder cfs.py was launched from, the same as the client launcher.
# Created only when the server fails to compile (a clean launch removes any stale copy first), so an absent
# errors.txt means "no errors".
ERRORS_PATH = os.path.join(os.getcwd(), "errors.txt")


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

def compile_check():
    # Compile the server once before handing it to downcheck. downcheck relaunches a server that exits, so a
    # script with compile errors would otherwise just fail over and over in the background with nothing to read.
    # "nvgt -c -q" only compiles (quiet unless something is wrong) and prints any errors; it writes a throwaway
    # build folder (src/server/cfs) that is removed again straight after. Returns True when it compiled.
    try:
        os.remove(ERRORS_PATH)  # clear a report left by an earlier failed launch
    except OSError:
        pass
    build_dir = SERVER_DIR / "cfs"
    existed = build_dir.exists()
    print("Checking the server script for errors...")
    try:
        result = subprocess.run([NVGT, "-c", "-q", SERVER_SCRIPT.name], cwd=str(SERVER_DIR), capture_output=True, timeout=300)
    except Exception as error:
        print("Could not run the compile check: %s" % error)
        return True  # the check itself failed to start; let downcheck try the normal launch
    finally:
        if not existed and build_dir.exists():
            shutil.rmtree(build_dir, ignore_errors=True)
    if result.returncode == 0:
        return True
    raw = (result.stdout + result.stderr).decode("utf-8", "replace")
    # Same tidy-up as cfc.py: drop the doubled carriage returns, collapse runs of blank lines to one blank between
    # records, and put the leading "Compilation error:" on its own line so every record starts with "file:".
    details = re.sub(r"\n{2,}", "\n\n", raw.replace("\r", ""))
    details = details.replace("Compilation error: ", "Compilation error:\n").strip()
    body = details if details else "(the server failed to compile with exit code %d but printed no output)" % result.returncode
    try:
        with open(ERRORS_PATH, "w", encoding="utf-8") as f:
            f.write(body + "\n\n")
    except OSError:
        pass
    print("The server failed to compile (exit code %d)." % result.returncode)
    print("Details written to: " + ERRORS_PATH)
    return False


sync_version()
if not compile_check():
    input("Press Enter to exit...")
    sys.exit(1)
print("Started CaveDefender server (supervised by downcheck)")
result = subprocess.run([NVGT, str(SCRIPT)], cwd=str(HERE))
if result.returncode != 0:
    print("Downcheck exited with an error (code %d)." % result.returncode)
    input("Press Enter to exit...")
