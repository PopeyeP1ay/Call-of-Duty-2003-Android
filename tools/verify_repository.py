"""Reject common proprietary game assets and signing keys from this public repo.

This is a guardrail rather than a legal or security audit. Run from the repo root.
"""
from __future__ import annotations

import pathlib
import subprocess
import sys

FORBIDDEN_EXTENSIONS = {
    ".apk", ".aab", ".apks", ".codpack", ".pk3", ".pak",
    ".exe", ".dll", ".so", ".keystore", ".jks", ".p12", ".pfx",
    ".pem", ".key", ".ico",
}
FORBIDDEN_NAMES = {"cod_icon.png", "english-unsigned.apk"}
PRIVATE_DIRECTORY_PARTS = {
    "game", "originals", "recomp_out", "callofrecomp-allinone-build",
    "callofrecomp-english-build", "private", "local-build",
}

def main() -> int:
    try:
        output = subprocess.check_output(["git", "ls-files", "-z"])
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"Could not read tracked Git files: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    for filename in output.decode("utf-8", errors="replace").split("\0"):
        if not filename:
            continue
        path = pathlib.PurePosixPath(filename)
        if path.suffix.lower() in FORBIDDEN_EXTENSIONS:
            errors.append(f"Game asset / executable / key must not be tracked: {filename}")
        elif path.name.lower() in FORBIDDEN_NAMES:
            errors.append(f"Local icon/private artifact must not be tracked: {filename}")
        elif any(part.lower() in PRIVATE_DIRECTORY_PARTS for part in path.parts[:-1]):
            errors.append(f"Private build directory must not be tracked: {filename}")
        elif pathlib.Path(filename).is_file() and pathlib.Path(filename).stat().st_size > 25 * 1024 * 1024:
            errors.append(f"Unexpectedly large tracked file; inspect before publishing: {filename}")

    if errors:
        print("Public repository verification FAILED:")
        print("\n".join("- " + message for message in errors))
        return 1
    print("Public repo verification passed: no known private game assets, APKs, or signing keys tracked.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
