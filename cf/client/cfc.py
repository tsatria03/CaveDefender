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


def fail(message):
    ctypes.windll.user32.MessageBoxW(0, message, "CaveDefender launcher", 0x10)
    sys.exit(1)


if not os.path.isfile(NVGT):
    fail("Could not find the NVGT runtime at:\n" + NVGT)
if not os.path.isfile(SCRIPT):
    fail("Could not find the client script at:\n" + SCRIPT)

try:
    subprocess.Popen(
        [NVGT, SCRIPT],
        cwd=HERE,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
except Exception as error:
    fail("Failed to start the client:\n" + str(error))
