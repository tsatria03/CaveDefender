import os
import sys
import subprocess
import ctypes

# Launch the CaveDefender client. The .nvgt source lives in src/client, but the
# assets (lib, sounds, docks) live here in cf/client, so we run with cwd set to
# this folder: every cwd-relative path in the game (lib/GameEngine64.dll,
# sounds/..., lib/oggenc2.exe, docks/...) then resolves against cf/client.
# CREATE_NO_WINDOW gives nvgt no console; the launcher spawns and exits, so its
# own console only flashes. The client opens its own NVGT game window.

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.normpath(os.path.join(HERE, "..", "..", "src", "client", "cfc.nvgt"))
NVGT = r"C:\nvgt2\nvgt.exe"
VERSION_TXT = os.path.normpath(os.path.join(HERE, "..", "..", "build", "version.txt"))
VERSION_NVGT = os.path.normpath(os.path.join(HERE, "..", "..", "src", "client", "includes", "version.nvgt"))


def fail(message):
    ctypes.windll.user32.MessageBoxW(0, message, "CaveDefender launcher", 0x10)
    sys.exit(1)


def sync_version():
    # build/version.txt is the single source of truth for the version number; mirror it into the client's
    # version.nvgt before launching so interpreted runs (and the window title) always show the current
    # version without hand-editing version.nvgt. Silent no-op if version.txt is missing or already matches.
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


if not os.path.isfile(NVGT):
    fail("Could not find the NVGT runtime at:\n" + NVGT)
if not os.path.isfile(SCRIPT):
    fail("Could not find the client script at:\n" + SCRIPT)

sync_version()

try:
    subprocess.Popen(
        [NVGT, SCRIPT],
        cwd=HERE,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
except Exception as error:
    fail("Failed to start the client:\n" + str(error))
