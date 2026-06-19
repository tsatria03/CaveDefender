import sys
import shutil
import subprocess
from pathlib import Path

# Compile the CaveDefender CLIENT and assemble it into
# release/windows/CaveDefender/client. NVGT produces a bundle folder (cfc/) with
# the exe + its own runtime libs in lib/; we then copy our game assets from
# play/client into that bundle (merging lib/ so GameEngine64.dll + oggenc2.exe land
# beside the runtime libs, and adding sounds/ and docks/). The exe runs with its
# folder as cwd, so the in-code cwd-relative paths (lib/..., sounds/..., docks/...)
# resolve. Run in a console so output is visible; only the client side is touched.

NVGT = r"C:\nvgt2\nvgt.exe"
HERE = Path(__file__).resolve().parent            # src/client
ROOT = HERE.parent.parent                          # repo root
PLAY = ROOT / "play" / "client"                    # asset source
BUNDLE = HERE / "cfc"                              # the folder nvgt -c produces
DEST = ROOT / "release" / "windows" / "CaveDefender" / "client"

# Asset folders copied from play/client into the bundle (lib merges with NVGT's).
ASSETS = ["lib", "sounds", "docks"]


def pause_exit(code):
    input("Press Enter to exit...")
    sys.exit(code)


print("Compiling client...")
result = subprocess.run([NVGT, "-c", "cfc.nvgt"], cwd=str(HERE))
if result.returncode != 0:
    print("Client compilation failed; nothing was assembled.")
    pause_exit(1)

print("Copying assets from play/client...")
for name in ASSETS:
    src = PLAY / name
    if not src.is_dir():
        print("Missing asset folder: " + str(src))
        pause_exit(1)
    shutil.copytree(src, BUNDLE / name, dirs_exist_ok=True)

DEST.mkdir(parents=True, exist_ok=True)
target = DEST / "cfc"
if target.exists():
    shutil.rmtree(target)
shutil.move(str(BUNDLE), str(target))

print("Done. The client build is in release\\windows\\CaveDefender\\client\\cfc.")
pause_exit(0)
