import sys
import shutil
import subprocess
from pathlib import Path

# Compile the CaveDefender SERVER and assemble it into
# release/windows/CaveDefender/server. NVGT produces a bundle folder (cfs/) with the
# exe + its own runtime libs in lib/; we then copy our server assets from play/server
# (data/ and docks/) into that bundle. The server uses no custom DLL, so NVGT's
# auto-copied lib/ is enough. The exe runs with its folder as cwd, so the in-code
# cwd-relative paths (data/..., docks/...) resolve. Run in a console so output is
# visible; only the server side is touched.

NVGT = r"C:\nvgt2\nvgt.exe"
HERE = Path(__file__).resolve().parent            # src/server
ROOT = HERE.parent.parent                          # repo root
PLAY = ROOT / "play" / "server"                    # asset source
BUNDLE = HERE / "cfs"                              # the folder nvgt -c produces
DEST = ROOT / "release" / "windows" / "CaveDefender" / "server"

# Asset folders copied from play/server into the bundle (NVGT supplies lib/ itself).
ASSETS = ["data", "docks"]


def pause_exit(code):
    input("Press Enter to exit...")
    sys.exit(code)


print("Compiling server...")
result = subprocess.run([NVGT, "-c", "cfs.nvgt"], cwd=str(HERE))
if result.returncode != 0:
    print("Server compilation failed; nothing was assembled.")
    pause_exit(1)

print("Copying assets from play/server...")
for name in ASSETS:
    src = PLAY / name
    if not src.is_dir():
        print("Missing asset folder: " + str(src))
        pause_exit(1)
    shutil.copytree(src, BUNDLE / name, dirs_exist_ok=True)

DEST.mkdir(parents=True, exist_ok=True)
target = DEST / "cfs"
if target.exists():
    shutil.rmtree(target)
shutil.move(str(BUNDLE), str(target))

print("Done. The server build is in release\\windows\\CaveDefender\\server\\cfs.")
pause_exit(0)
