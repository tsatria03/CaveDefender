import subprocess
import os
import sys
import shutil
import configparser

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

_cfg = configparser.ConfigParser()
_cfg.read(os.path.join(SCRIPT_DIR, "tools.ini"))

_tools = configparser.ConfigParser()
_tools.read(os.path.join(os.path.expanduser("~"), ".game_tools", "tools.ini"))

GAME         = _cfg["game"]["name"]
PASSWORD     = _cfg["game"]["password"]
# CaveDefender is two-sided: a client (players) and a server (hosts), each its own .nvgt entry.
CLIENT_FILE  = _cfg["game"]["client_file"]            # cfc.nvgt
SERVER_FILE  = _cfg["game"]["server_file"]            # cfs.nvgt
CLIENT_OUT   = os.path.splitext(CLIENT_FILE)[0]       # cfc
SERVER_OUT   = os.path.splitext(SERVER_FILE)[0]       # cfs

# Source lives in src/<side>; assets in cf/<side> (the split layout). nvgt -c run from src/<side> produces
# the bundle folder there, then we copy that side's assets in (client merges lib/ with NVGT's runtime DLLs;
# server uses NVGT's auto-copied lib/).
SRC_CLIENT    = os.path.join(REPO_DIR, "src", "client")
SRC_SERVER    = os.path.join(REPO_DIR, "src", "server")
ASSETS_CLIENT = os.path.join(REPO_DIR, "cf", "client")
ASSETS_SERVER = os.path.join(REPO_DIR, "cf", "server")
CLIENT_ASSETS = ["lib", "sounds", "docks"]
SERVER_ASSETS = ["data", "docks"]
CLIENT_BUNDLE = os.path.join(SRC_CLIENT, CLIENT_OUT)
SERVER_BUNDLE = os.path.join(SRC_SERVER, SERVER_OUT)

# The single source of truth for the version is build/version.txt; it's mirrored into both sides' version.nvgt on compile.
CLIENT_VERSION_NVGT = os.path.join(SRC_CLIENT, "includes", "version.nvgt")
SERVER_VERSION_NVGT = os.path.join(SRC_SERVER, "includes", "version.nvgt")

SITE_HTML    = _cfg["site"]["html"]
SITE_REPO    = _cfg["site"]["repo"]
SITE_PATH    = _cfg["site"]["path"]

NVGT    = _tools["tools"]["nvgt"]  # shared across all the legacy-engine games; set to the legacy build in ~/.game_tools/tools.ini
SEVENZIP = _tools["tools"]["sevenzip"]
GH      = _tools["tools"]["gh"]

# Each side assembles into its own password-named folder under release/windows (release/ singular), e.g.
# release/windows/CaveDefenderClient_password_is_WallSmasher/cfc and .../CaveDefenderServer_..._/cfs.
CLIENT_FOLDER = f"{GAME}Client_password_is_{PASSWORD}"
SERVER_FOLDER = f"{GAME}Server_password_is_{PASSWORD}"
CLIENT_DEST   = os.path.join(REPO_DIR, "release", "windows", CLIENT_FOLDER)
SERVER_DEST   = os.path.join(REPO_DIR, "release", "windows", SERVER_FOLDER)
CLIENT_BUILD  = os.path.join(CLIENT_DEST, CLIENT_OUT)   # the finished client bundle (cfc)
SERVER_BUILD  = os.path.join(SERVER_DEST, SERVER_OUT)   # the finished server bundle (cfs)

# Two separate portable archives: client for players, server for hosts (named to match their folders).
ARCHIVE_DIR    = os.path.join(REPO_DIR, "release", "archives")
CLIENT_ARCHIVE = os.path.join(ARCHIVE_DIR, f"{CLIENT_FOLDER}.7z")
SERVER_ARCHIVE = os.path.join(ARCHIVE_DIR, f"{SERVER_FOLDER}.7z")

SKIP = 0
DO = 1
SILENT_SKIP = 2

def ask(prompt):
    return input(f"{prompt} (Y/N): ").strip().upper() == "Y"

def run(args, capture=False):
    return subprocess.run(args, cwd=REPO_DIR, capture_output=capture, text=True)

def run_out(args):
    return run(args, capture=True).stdout.strip()

def run_cmd(args, cwd=None):
    return subprocess.run(args, cwd=cwd).returncode == 0

def clip(text):
    subprocess.run("clip", input=text.strip(), text=True)

def get_version():
    with open(os.path.join(SCRIPT_DIR, "version.txt"), "r") as f:
        return f.read().strip()

def sync_version_files(version):
    # Mirror version.txt into both sides' version.nvgt so client and server always match (CRLF, like the repo).
    line = f'const string version="{version}";\r\n'
    for path in (CLIENT_VERSION_NVGT, SERVER_VERSION_NVGT):
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(line)
    print(f"Synced version {version} into client and server version.nvgt.\n")

def compile_side(label, nvgt_file, src_dir, bundle, assets_dir, asset_folders, dest, out_name):
    # Compile one side from src/<side> (so the bundle lands there), copy its assets in, and move it into
    # the release folder. Mirrors the old cfcm.py / cfsm.py, now unified here.
    print(f"Compiling {label}...")
    if not run_cmd([NVGT, "-c", "-Q", nvgt_file], cwd=src_dir):
        print(f"ERROR: {label} compilation failed.")
        return False
    print(f"Copying {label} assets...")
    for folder in asset_folders:
        asset_src = os.path.join(assets_dir, folder)
        if not os.path.isdir(asset_src):
            print(f"ERROR: missing asset folder: {asset_src}")
            return False
        shutil.copytree(asset_src, os.path.join(bundle, folder), dirs_exist_ok=True)
    os.makedirs(dest, exist_ok=True)
    target = os.path.join(dest, out_name)
    if os.path.exists(target):
        shutil.rmtree(target)
    shutil.move(bundle, target)
    print(f"{label} build assembled in {target}.\n")
    return True

# ── Commit ────────────────────────────────────────────────────────────────────

def unpushed_count():
    out = run_out(["git", "log", "origin/HEAD..HEAD", "--oneline"])
    return len([l for l in out.splitlines() if l.strip()])

def do_commit():
    status = run_out(["git", "status", "--short"])
    changes = len([l for l in status.splitlines() if l.strip()])
    print(f"Changes: {changes}")
    print()
    if changes == 0:
        print("No changes to commit.")
        return
    print(status)
    print()
    if not ask("Do you want to commit?"):
        print("Cancelled.")
        return
    print()
    summary = input("Commit summary: ").strip()
    if not summary:
        print("Summary cannot be empty.")
        return
    print()
    print("Commit description (enter lines one by one, blank line to finish):")
    desc_lines = []
    while True:
        line = input(f"Line {len(desc_lines) + 1}: ")
        if not line.strip():
            break
        desc_lines.append(line)
    description = "\n".join(desc_lines)
    print()
    print(f"Summary:     {summary}")
    if description:
        print(f"Description: {description}")
    print()
    if not ask("Is this correct?"):
        print("Cancelled.")
        return
    print()
    run(["git", "add", "-A"])
    args = ["git", "commit", "-m", summary]
    if description:
        args += ["-m", description]
    result = run(args)
    if result.returncode != 0:
        print("ERROR: Commit failed.")
        return
    print()
    print(f"Committed {changes} file(s).")
    print()
    if not ask("Do you want to push?"):
        print("Changes committed but not pushed.")
        return
    print()
    result = run(["git", "push"])
    if result.returncode != 0:
        print("ERROR: Push failed.")
    else:
        print("Push complete.")

def do_undo(unpushed):
    if unpushed == 0:
        print("Nothing to undo. All commits have been pushed.")
        return
    last_msg = run_out(["git", "log", "-1", "--format=%s"])
    print(f"Last commit: {last_msg}")
    print()
    if not ask("Undo this commit? Your changes will remain staged."):
        print("Cancelled.")
        return
    result = run(["git", "reset", "--soft", "HEAD~1"])
    if result.returncode != 0:
        print("ERROR: Undo failed.")
    else:
        print("Commit undone. Your changes are still staged.")

def do_push(unpushed):
    if unpushed == 0:
        print("Nothing to push. All commits are already on the remote.")
        return
    log = run_out(["git", "log", "origin/HEAD..HEAD", "--oneline"])
    print(f"Unpushed commits ({unpushed}):")
    print()
    print(log)
    print()
    if not ask("Push these commits to the remote?"):
        print("Cancelled.")
        return
    result = run(["git", "push"])
    if result.returncode != 0:
        print("ERROR: Push failed.")
    else:
        print("Push complete.")

def do_history():
    raw = run_out(["git", "log", "-50", "--decorate-refs=refs/tags", "--format=%h~%ar~%s%d"])
    commits = []
    print()
    print("Last 50 commits:")
    print()
    for i, line in enumerate(raw.splitlines(), 1):
        parts = line.split("~", 2)
        if len(parts) < 3:
            continue
        sha, date, msg = parts
        commits.append((sha, msg))
        print(f"  {i}. {sha}  {msg}  (Time: {date})")
    print()
    pick = input("Select a commit number (or 0 to go back): ").strip()
    if pick == "0" or pick == "":
        return
    try:
        index = int(pick) - 1
        if index < 0 or index >= len(commits):
            raise ValueError
    except ValueError:
        print("Invalid selection.")
        return
    sha, msg = commits[index]
    print()
    print(f"Selected: {sha} {msg}")
    commit_menu(sha, msg)

def commit_menu(sha, msg):
    while True:
        print()
        print("========================")
        print(" Commit Options")
        print("========================")
        print(" 1. Show description")
        print(" 2. Copy SHA")
        print(" 3. Create tag")
        print(" 4. Copy tag")
        print(" 5. Reset to this commit")
        print(" 6. Go back")
        print("========================")
        choice = input("Choose an option: ").strip()
        print()
        if choice == "1":
            show_desc(sha)
        elif choice == "2":
            copy_sha(sha)
        elif choice == "3":
            create_tag(sha)
        elif choice == "4":
            copy_tag(sha)
        elif choice == "5":
            if do_reset(sha):
                return
        elif choice == "6":
            do_history()
            return
        else:
            print("Invalid choice.")

def show_desc(sha):
    desc = run_out(["git", "log", "-1", "--format=%B", sha])
    print(desc if desc else "(No description)")
    print()

def copy_sha(sha):
    full = run_out(["git", "rev-parse", sha])
    clip(full)
    print(f"SHA copied to clipboard: {full}")

def create_tag(sha):
    tag_name = input("Enter tag name: ").strip()
    if not tag_name:
        print("Tag name cannot be empty.")
        return
    result = run(["git", "tag", tag_name, sha])
    if result.returncode != 0:
        print("ERROR: Failed to create tag.")
        return
    print(f'Tag "{tag_name}" created.')
    if ask("Push tag to remote?"):
        run(["git", "push", "origin", tag_name])
        print("Tag pushed.")

def copy_tag(sha):
    tag = run_out(["git", "tag", "--points-at", sha])
    if not tag:
        print("No tag found on this commit.")
    else:
        clip(tag)
        print(f"Tag copied to clipboard: {tag}")

def do_create_tag():
    raw = input("Commit to tag (press Enter for HEAD): ").strip()
    target = raw if raw else "HEAD"
    sha = run_out(["git", "rev-parse", "--verify", target])
    if not sha:
        print(f"ERROR: Could not resolve commit '{target}'.")
        return
    short = sha[:7]
    msg = run_out(["git", "log", "--format=%s", "-1", sha])
    print(f"{target} is at: {short} {msg}")
    if not ask(f"Tag this commit?"):
        print("Cancelled.")
        return
    create_tag(sha)

def do_reset(sha):
    print("WARNING: Resetting will move HEAD to this commit.")
    print()
    print(" 1. Soft (keeps changes staged)")
    print(" 2. Hard (discards all changes permanently)")
    print(" 3. Cancel")
    print()
    choice = input("Choose reset type: ").strip()
    if choice == "3" or choice == "":
        print("Cancelled.")
        return False
    if choice == "1":
        flag = "--soft"
    elif choice == "2":
        flag = "--hard"
        print()
        print("WARNING: Hard reset will permanently discard all uncommitted changes.")
    else:
        print("Invalid choice.")
        return False
    print()
    if not ask(f"Reset to {sha}?"):
        print("Cancelled.")
        return False
    result = run(["git", "reset", flag, sha])
    if result.returncode != 0:
        print("ERROR: Reset failed.")
        return False
    print("Reset complete.")
    return True

# ── Release ───────────────────────────────────────────────────────────────────

def do_website_update(version, tag, skip_website):
    do_website = False
    if skip_website == DO:
        do_website = True
    elif skip_website == SKIP:
        do_website = ask("Do you want to update the game's website?")

    if not do_website:
        if skip_website == SKIP:
            print("Skipping website update.\n")
        return

    print("Updating website...")
    ps1 = os.path.join(SCRIPT_DIR, "site_updater.ps1")
    if not run_cmd(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", ps1, "-HtmlFile", SITE_HTML, "-Version", version, "-Tag", tag]):
        print("ERROR: Failed to update website HTML.")
        return
    print("Website updated.\n")

    version_txt = os.path.join(os.path.dirname(SITE_HTML), "version.txt")
    version_txt_relpath = os.path.dirname(SITE_PATH).replace("\\", "/") + "/version.txt"
    version_txt_updated = False
    if os.path.exists(version_txt):
        with open(version_txt, "w", encoding="utf-8") as f:
            f.write(version)
        print(f"Updated {version_txt} to {version}.\n")
        version_txt_updated = True

    print("Committing website changes...")
    log = subprocess.run(["git", "log", "--oneline"], cwd=SITE_REPO, capture_output=True, text=True).stdout
    if f"Updated {GAME} to version {version}." in log:
        print("WARNING: Commit already exists. Skipping commit.\n")
        return

    add_targets = [SITE_PATH]
    if version_txt_updated:
        add_targets.append(version_txt_relpath)
    run_cmd(["git", "add"] + add_targets, cwd=SITE_REPO)
    if not run_cmd(["git", "commit", "-m", f"Updated {GAME} to version {version}."], cwd=SITE_REPO):
        print("ERROR: Failed to commit website changes.")
        return
    if not run_cmd(["git", "push"], cwd=SITE_REPO):
        print("ERROR: Failed to push website changes.")
        return
    print("Website committed and pushed.\n")

def run_release(skip_compile, skip_package, skip_release, skip_website, skip_empty_release, interactive=True):
    version = get_version()
    if not version:
        print("ERROR: Could not read version from version.txt.")
        return

    title = f"{GAME} V{version}"
    tag = f"V{version}0"

    print(f"\nVersion: {version}")
    print(f"Tag:     {tag}")
    print(f"Title:   {title}\n")

    if skip_release != SILENT_SKIP:
        head_sha = run_out(["git", "rev-parse", "--verify", "HEAD"])
        existing_tag_sha = run_out(["git", "rev-parse", "--verify", "--quiet", f"refs/tags/{tag}"])
        existing_release = subprocess.run([GH, "release", "view", tag], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=REPO_DIR).returncode == 0
        if existing_tag_sha or existing_release:
            print(f"WARNING: {tag} already exists.")
            if existing_tag_sha:
                short = existing_tag_sha[:7]
                msg = run_out(["git", "log", "--format=%s", "-1", existing_tag_sha])
                if existing_tag_sha != head_sha:
                    head_short = head_sha[:7] if head_sha else "?"
                    head_msg = run_out(["git", "log", "--format=%s", "-1", "HEAD"])
                    print(f"  Tag points to {short} {msg}")
                    print(f"  This release will MOVE the tag to HEAD ({head_short} {head_msg}).")
                else:
                    print(f"  Tag already points to HEAD, so it will not move.")
            if existing_release:
                print(f"  GitHub release {tag} will be deleted and recreated with new assets.")
            print()
            if interactive:
                if not ask("Continue with the release?"):
                    print("Release cancelled.")
                    return
            else:
                print("ERROR: Refusing to overwrite an existing tag or release in non-interactive mode.")
                print("       Delete the tag and release manually first, or run tools.py interactively.")
                return

    # Compile
    do_compile = False
    if skip_compile == DO:
        do_compile = True
    elif skip_compile == SKIP:
        do_compile = ask("Do you want to compile this project?")

    if do_compile:
        # Keep both sides' version.nvgt in lockstep with version.txt before compiling.
        sync_version_files(version)
        if not compile_side("client", CLIENT_FILE, SRC_CLIENT, CLIENT_BUNDLE, ASSETS_CLIENT, CLIENT_ASSETS, CLIENT_DEST, CLIENT_OUT):
            return
        if not compile_side("server", SERVER_FILE, SRC_SERVER, SERVER_BUNDLE, ASSETS_SERVER, SERVER_ASSETS, SERVER_DEST, SERVER_OUT):
            return
        print("Both sides compiled and assembled.\n")
    elif skip_compile == SKIP:
        print("Skipping compilation.\n")

    # Package
    do_package = False
    if skip_package == DO:
        do_package = True
    elif skip_package == SKIP:
        do_package = ask("Do you want to package this project?")

    if do_package:
        os.makedirs(ARCHIVE_DIR, exist_ok=True)
        for label, build_dir, archive in (("client", CLIENT_BUILD, CLIENT_ARCHIVE), ("server", SERVER_BUILD, SERVER_ARCHIVE)):
            if not os.path.exists(build_dir):
                print(f"ERROR: {label} build folder not found. Please compile first.")
                return
            print(f"Building {label} portable 7z archive...")
            if os.path.exists(archive):
                os.remove(archive)
            if not run_cmd([SEVENZIP, "a", "-t7z", archive, build_dir, "-mx=9", "-m0=LZMA2", "-md=64m", "-mfb=64", "-ms=on", "-mmt=12", f"-p{PASSWORD}", "-mhe=on"]):
                print(f"ERROR: {label} 7z archive build failed.")
                return
        print("Archives built successfully.\n")
    elif skip_package == SKIP:
        print("Skipping packaging.\n")

    # Release
    do_rel = False
    if skip_release == DO:
        do_rel = True
    elif skip_release == SKIP:
        do_rel = ask("Do you want to release this project?")

    if not do_rel:
        if skip_release == SKIP:
            print("Skipping release.\n")
        do_website_update(version, tag, skip_website)
        return

    assets = []
    for archive in (CLIENT_ARCHIVE, SERVER_ARCHIVE):
        if os.path.exists(archive):
            assets.append(archive)

    if not assets:
        print("WARNING: No assets found.\n")
        proceed = False
        if skip_empty_release == DO:
            proceed = True
        elif skip_empty_release == SKIP:
            proceed = ask("Do you still want to create an empty release?")
        if not proceed:
            print("Release cancelled.\n")
            return

    print(f"Tagging latest commit as {tag}...")
    run_cmd(["git", "tag", "-f", tag], cwd=REPO_DIR)
    run_cmd(["git", "push", "origin", "-f", tag], cwd=REPO_DIR)

    print("\nDeleting existing release if it exists...")
    subprocess.run([GH, "release", "delete", tag, "--yes"], cwd=REPO_DIR, stderr=subprocess.DEVNULL)

    print(f"\nCreating GitHub release {title} with tag {tag}...\n")
    cmd = [GH, "release", "create", tag] + assets + ["--title", title, "--notes", ""]
    if not run_cmd(cmd, cwd=REPO_DIR):
        print("ERROR: GitHub release creation failed.")
        return

    print("\nRelease complete.\n")

    if not assets:
        print("WARNING: No assets were released. Skipping website update.\n")
        return

    do_website_update(version, tag, skip_website)

# ── Main menu ─────────────────────────────────────────────────────────────────

def menu():
    while True:
        unpushed = unpushed_count()
        print()
        print("========================")
        print(f"  {GAME} Tools")
        print("========================")
        print(" --- Commit ---")
        print(" 1. Make a commit")
        print(f" 2. Undo last commit (unpushed: {unpushed})")
        print(f" 3. Push commits (unpushed: {unpushed})")
        print(" 4. Show commit history")
        print(" 5. Create tag manually")
        print(" --- Release ---")
        print(" 6. Full release")
        print(" 7. Compile only")
        print(" 8. Package only")
        print(" 9. Release only")
        print(" 10. Website only")
        print(" ---")
        print(" 11. Exit")
        print("========================")
        choice = input("Choose an option: ").strip()
        print()
        if choice == "1":
            do_commit()
        elif choice == "2":
            do_undo(unpushed)
        elif choice == "3":
            do_push(unpushed)
        elif choice == "4":
            do_history()
        elif choice == "5":
            do_create_tag()
        elif choice == "6":
            run_release(SKIP, SKIP, SKIP, SKIP, SKIP)
        elif choice == "7":
            run_release(DO, SILENT_SKIP, SILENT_SKIP, SILENT_SKIP, SILENT_SKIP)
        elif choice == "8":
            run_release(SILENT_SKIP, DO, SILENT_SKIP, SILENT_SKIP, SILENT_SKIP)
        elif choice == "9":
            run_release(SILENT_SKIP, SILENT_SKIP, DO, SILENT_SKIP, DO)
        elif choice == "10":
            run_release(SILENT_SKIP, SILENT_SKIP, SILENT_SKIP, DO, SILENT_SKIP)
        elif choice == "11":
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1-11.")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        menu()
    else:
        usage = (
            "Usage: tools.py <skip_compile> <skip_package> <skip_release> "
            "<skip_website> <skip_empty_release>\n"
            f"  Each flag must be {SKIP} (ask), {DO} (force run), or {SILENT_SKIP} (skip silently)."
        )
        if len(args) != 5:
            print(f"Error: expected 5 args, got {len(args)}.\n{usage}")
            sys.exit(2)
        try:
            flags = [int(a) for a in args]
        except ValueError:
            print(f"Error: all args must be integers.\n{usage}")
            sys.exit(2)
        if any(f not in (SKIP, DO, SILENT_SKIP) for f in flags):
            print(f"Error: each flag must be {SKIP}, {DO}, or {SILENT_SKIP}.\n{usage}")
            sys.exit(2)
        run_release(*flags, interactive=False)
