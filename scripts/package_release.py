#!/usr/bin/env python3
"""Package the committed skill and a skills-only OpenAI plugin; no runtime dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
NAME = "ticker-universe-builder"
ROOT_FILES = {"SKILL.md", "AGENTS.md", "README.md", "LICENSE", "CHANGELOG.md"}
FOLDERS = {"agents", "assets", "references", "scripts", "examples", "docs"}


def package(output: Path, developer_name: str | None = None) -> dict:
    if output.exists() and any(output.iterdir()):
        raise ValueError("output must be a new or empty directory")
    output.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((ROOT / "distribution/plugin.json").read_text())
    version = re.search(r"^  version: (\S+)$", (ROOT / "SKILL.md").read_text(), re.M)
    if version is None or version[1] != manifest["version"]:
        raise ValueError("plugin and skill versions must match")
    if developer_name:
        if not developer_name.strip() or len(developer_name) > 80:
            raise ValueError("developer name must contain 1-80 characters")
        manifest["author"] = {"name": developer_name}
        manifest["extensions"]["com.openai"]["interface"]["developerName"] = developer_name

    skill = output / "skill" / NAME
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    inventory = {}
    for relative in sorted(filter(None, tracked)):
        path = Path(relative)
        if relative not in ROOT_FILES and path.parts[0] not in FOLDERS:
            continue
        if relative == "scripts/package_release.py":
            continue
        source = ROOT / path
        if source.is_symlink() or not source.is_file():
            raise ValueError(f"not a regular source file: {relative}")
        destination = skill / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        inventory[relative] = hashlib.sha256(destination.read_bytes()).hexdigest()

    plugin = output / "openai" / NAME
    shutil.copytree(skill, plugin / "skills" / NAME)
    (plugin / "assets").mkdir()
    shutil.copyfile(ROOT / "assets/icon.png", plugin / "assets/icon.png")
    (plugin / "plugin.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    archives = {}
    for label, folder in (("skill", skill), ("openai-plugin", plugin)):
        archive = output / f"{NAME}-{version[1]}-{label}.zip"
        with ZipFile(archive, "w", compression=ZIP_DEFLATED, compresslevel=9) as bundle:
            for path in sorted(folder.rglob("*")):
                if path.is_file():
                    bundle.write(path, path.relative_to(folder.parent))
        with ZipFile(archive) as bundle:
            if bundle.testzip() is not None:
                raise ValueError(f"invalid archive: {archive}")
        archives[label] = {
            "path": str(archive), "bytes": archive.stat().st_size,
            "sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
        }
    receipt = {
        "version": version[1],
        "source_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "source_dirty": bool(subprocess.check_output(
            ["git", "status", "--porcelain"], cwd=ROOT, text=True
        ).strip()),
        "developer_identity_supplied": bool(developer_name),
        "source_files": inventory,
        "archives": archives,
    }
    (output / "package-receipt.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--developer-name", help="exact verified OpenAI developer display name")
    args = parser.parse_args()
    result = package(args.output.resolve(), args.developer_name)
    print(json.dumps(result["archives"], ensure_ascii=False, indent=2))
