import sys
import shutil
import subprocess
from pathlib import Path

# Compile the CaveDefender SERVER and assemble it into
# release/windows/CaveDefender/server. This script lives in cf/server (beside the
# assets); the .nvgt source is in src/server. We run nvgt -c from src/server (so the
# bundle folder cfs/ lands there), then copy our server assets from cf/server (data/
# and docks/) into the bundle. The server uses no custom DLL, so NVGT's auto-copied
# lib/ is enough. The exe runs with its folder as cwd, so the in-code cwd-relative
# paths (data/..., docks/...) resolve. Run in a console so output is visible; only the
# server side is touched.

NVGT = r"C:\nvgt2\nvgt.exe"
HERE = Path(__file__).resolve().parent            # cf/server (assets + this script)
ROOT = HERE.parent.parent                          # repo root
SRC = ROOT / "src" / "server"                      # the .nvgt source
BUNDLE = SRC / "cfs"                               # the folder nvgt -c produces (in cwd=SRC)
DEST = ROOT / "release" / "windows" / "CaveDefender" / "server"

# Asset folders copied from cf/server (HERE) into the bundle (NVGT supplies lib/ itself).
ASSETS = ["data", "docks"]


def pause_exit(code):
    input("Press Enter to exit...")
    sys.exit(code)


print("Compiling server...")
result = subprocess.run([NVGT, "-c", "cfs.nvgt"], cwd=str(SRC))
if result.returncode != 0:
    print("Server compilation failed; nothing was assembled.")
    pause_exit(1)

print("Copying assets from cf/server...")
for name in ASSETS:
    src = HERE / name
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
