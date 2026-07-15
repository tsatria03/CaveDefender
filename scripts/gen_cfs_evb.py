"""Regenerate src/server/cfs.evb — the Enigma Virtual Box project for the server.

The .evb embeds, into cfs.exe: the 4 audio DLLs (bass, bassmix, bass_fx, phonon) plus the ENTIRE docks/
folder (the read-only /help and /rules pages). No opus (voice is client-only) and no sounds folder.
Screen-reader DLLs stay real files in lib/. Enigma has no wildcard support, so every embedded file needs
its own explicit entry; this script walks the real asset folder (cf/server) and writes them all out. With
docks embedded, no external docks folder ships beside cfs.exe -- the server reads them virtually.

Note: the .evb lives in src/server, but the assets it references stay in cf/server — an .evb's location is
independent of the source paths inside it.

This is the server mirror of gencfcevb.py. Run it whenever the server docks folder changes:
    python scripts/gencfsevb.py
It reads build/tools.ini for the game name/password, so the release input/output paths stay correct even
if the password changes. Paths are derived from this file's location, so it works as long as it lives in a
folder directly under the repo root (e.g. scripts/).
"""

import os
import configparser

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR   = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

_cfg = configparser.ConfigParser()
_cfg.read(os.path.join(REPO_DIR, "build", "tools.ini"))
GAME       = _cfg["game"]["name"]
PASSWORD   = _cfg["game"]["password"]
SERVER_OUT = os.path.splitext(_cfg["game"]["server_file"])[0]   # cfs

# Assets the .evb reads from live in cf/server; the .evb itself is written to src/server. The release build
# is the GUI input/output (tools.py overrides these at run time).
SERVER_ASSETS = os.path.join(REPO_DIR, "cf", "server")
SERVER_SRC    = os.path.join(REPO_DIR, "src", "server")
SERVER_FOLDER = f"{GAME}Server_password_is_{PASSWORD}"
REL           = os.path.join(REPO_DIR, "release", "windows", SERVER_FOLDER, SERVER_OUT)
OUT           = os.path.join(SERVER_SRC, f"{SERVER_OUT}.evb")

# Only these DLLs get embedded; screen readers stay real files in lib/. No opus (voice is client-only).
LIB_DLLS = ["bass.dll", "bassmix.dll", "bass_fx.dll", "phonon.dll"]
# Whole asset folders to embed (walked recursively). Server ships no sounds, only docks.
EMBED_FOLDERS = ["docks"]

# The DLL list is fixed (not discovered), so verify each one exists in lib/ before writing -- otherwise the
# .evb would reference a file Enigma can't find and boxing would fail later. Abort with the missing names.
_missing = [dll for dll in LIB_DLLS if not os.path.isfile(os.path.join(SERVER_ASSETS, "lib", dll))]
if _missing:
    print(f"ERROR: {len(_missing)} required DLL(s) missing from {os.path.join(SERVER_ASSETS, 'lib')}:")
    for _dll in _missing:
        print(f"  {_dll}")
    print("Add them to lib/ and re-run. Nothing was written.")
    raise SystemExit(1)

def ind(n):
    return " " * n

def file_entry(name, src, depth):
    p, q = ind(depth), ind(depth + 2)
    return (
        f"{p}<File>\n"
        f"{q}<Type>2</Type>\n"
        f"{q}<Name>{name}</Name>\n"
        f"{q}<File>{src}</File>\n"
        f"{q}<ActiveX>False</ActiveX>\n"
        f"{q}<ActiveXInstall>False</ActiveXInstall>\n"
        f"{q}<Action>0</Action>\n"
        f"{q}<OverwriteDateTime>False</OverwriteDateTime>\n"
        f"{q}<OverwriteAttributes>False</OverwriteAttributes>\n"
        f"{q}<PassCommandLine>False</PassCommandLine>\n"
        f"{q}<HideFromDialogs>0</HideFromDialogs>\n"
        f"{p}</File>\n"
    )

def folder_entry(name, children_xml, depth):
    p, q = ind(depth), ind(depth + 2)
    return (
        f"{p}<File>\n"
        f"{q}<Type>3</Type>\n"
        f"{q}<Name>{name}</Name>\n"
        f"{q}<Action>0</Action>\n"
        f"{q}<OverwriteDateTime>False</OverwriteDateTime>\n"
        f"{q}<OverwriteAttributes>False</OverwriteAttributes>\n"
        f"{q}<HideFromDialogs>0</HideFromDialogs>\n"
        f"{q}<Files>\n"
        f"{children_xml}"
        f"{q}</Files>\n"
        f"{p}</File>\n"
    )

def build_tree(src_dir, depth):
    """Mirror a real folder as nested evb folder/file entries."""
    out = ""
    entries = sorted(os.listdir(src_dir), key=str.lower)
    for e in [x for x in entries if os.path.isdir(os.path.join(src_dir, x))]:
        out += folder_entry(e, build_tree(os.path.join(src_dir, e), depth + 4), depth)
    for e in [x for x in entries if os.path.isfile(os.path.join(src_dir, x))]:
        out += file_entry(e, os.path.join(src_dir, e), depth)
    return out

# Children of %DEFAULT FOLDER% sit at this indent.
DEPTH = 14

lib_folder = folder_entry("lib", "".join(
    file_entry(dll, os.path.join(SERVER_ASSETS, "lib", dll), DEPTH + 4) for dll in LIB_DLLS), DEPTH)
asset_folders = "".join(
    folder_entry(f, build_tree(os.path.join(SERVER_ASSETS, f), DEPTH + 4), DEPTH) for f in EMBED_FOLDERS)
default_children = lib_folder + asset_folders

evb = f"""<?xml version="1.0" encoding="windows-1252"?>
<>
  <InputFile>{os.path.join(REL, f"{SERVER_OUT}.exe")}</InputFile>
  <OutputFile>{os.path.join(REL, f"{SERVER_OUT}_boxed.exe")}</OutputFile>
  <Files>
    <Enabled>True</Enabled>
    <DeleteExtractedOnExit>False</DeleteExtractedOnExit>
    <CompressFiles>True</CompressFiles>
    <Files>
      <File>
        <Type>3</Type>
        <Name>%DEFAULT FOLDER%</Name>
        <Action>0</Action>
        <OverwriteDateTime>False</OverwriteDateTime>
        <OverwriteAttributes>False</OverwriteAttributes>
        <HideFromDialogs>0</HideFromDialogs>
        <Files>
{default_children}        </Files>
      </File>
    </Files>
  </Files>
  <Registries>
    <Enabled>False</Enabled>
    <Registries>
      <Registry>
        <Type>1</Type>
        <Virtual>True</Virtual>
        <Name>Classes</Name>
        <ValueType>0</ValueType>
        <Value/>
        <Registries/>
      </Registry>
      <Registry>
        <Type>1</Type>
        <Virtual>True</Virtual>
        <Name>User</Name>
        <ValueType>0</ValueType>
        <Value/>
        <Registries/>
      </Registry>
      <Registry>
        <Type>1</Type>
        <Virtual>True</Virtual>
        <Name>Machine</Name>
        <ValueType>0</ValueType>
        <Value/>
        <Registries/>
      </Registry>
      <Registry>
        <Type>1</Type>
        <Virtual>True</Virtual>
        <Name>Users</Name>
        <ValueType>0</ValueType>
        <Value/>
        <Registries/>
      </Registry>
      <Registry>
        <Type>1</Type>
        <Virtual>True</Virtual>
        <Name>Config</Name>
        <ValueType>0</ValueType>
        <Value/>
        <Registries/>
      </Registry>
    </Registries>
  </Registries>
  <Packaging>
    <Enabled>False</Enabled>
  </Packaging>
  <Options>
    <ShareVirtualSystem>False</ShareVirtualSystem>
    <MapExecutableWithTemporaryFile>True</MapExecutableWithTemporaryFile>
    <TemporaryFileMask/>
    <AllowRunningOfVirtualExeFiles>True</AllowRunningOfVirtualExeFiles>
    <ProcessesOfAnyPlatforms>False</ProcessesOfAnyPlatforms>
  </Options>
  <Storage>
    <Files>
      <Enabled>False</Enabled>
      <Folder>%DEFAULT FOLDER%\\</Folder>
      <RandomFileNames>False</RandomFileNames>
      <EncryptContent>False</EncryptContent>
    </Files>
  </Storage>
</>
"""

with open(OUT, "w", encoding="windows-1252") as f:
    f.write(evb)

counts = {f: sum(len(files) for _, _, files in os.walk(os.path.join(SERVER_ASSETS, f))) for f in EMBED_FOLDERS}
print(f"Wrote {OUT}")
print(f"  lib DLLs embedded: {len(LIB_DLLS)}")
for f, n in counts.items():
    print(f"  {f} files embedded: {n}")
