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
COMPACT_READMES = {
    "README.md": """# Ticker Universe Builder

An evidence-backed ticker universe skill. Python 3.10+, standard library only.

Extract this complete folder into your agent's skills directory, then restart the agent
if needed. Ask it to build a market and depth; `SKILL.md` is its entry point.

This package includes runtime code, rules and all worked inputs. Generated reports and
screenshots are omitted. Run `python examples/build_examples.py` from this folder to
recreate all ten examples offline. Their dated research is not a fresh market assessment.

[Documentation and previews](https://github.com/bitpunklabs/ticker-universe-builder)
· [Releases](https://github.com/bitpunklabs/ticker-universe-builder/releases)

MIT license. Observation instruments, not investment recommendations.
""",
    "examples/README.md": """# Worked inputs

US Light/Medium/Heavy/Max and CN/Crypto/HK/JP/KR/UK Medium share seven researched
snapshots and ten build specs. US uses `us-medium/snapshot.json`; Max retains Heavy.

Run `python examples/build_examples.py` from the skill root before reading the generated
`output/` directories. This offline replay preserves the inputs' original research dates,
limits and provenance; it does not certify today's listings or refresh their evidence.

Read a build spec and report summary first. Inspect relevant snapshot rows programmatically
instead of loading multi-megabyte snapshots into model context.

[Published reports and previews](https://github.com/bitpunklabs/ticker-universe-builder/tree/main/examples)
""",
}


def package(output: Path, developer_name: str | None = None, *, compact: bool = False) -> dict:
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
    rewritten = {}
    for relative in sorted(filter(None, tracked)):
        path = Path(relative)
        if relative not in ROOT_FILES and path.parts[0] not in FOLDERS:
            continue
        if relative == "scripts/package_release.py":
            continue
        if compact and (
            path.parts[:2] == ("docs", "media")
            or (path.parts[0] == "examples" and any(p in {"output", "preview"} for p in path.parts))
            or relative == "examples/render_previews.cjs"
        ):
            continue
        source = ROOT / path
        if source.is_symlink() or not source.is_file():
            raise ValueError(f"not a regular source file: {relative}")
        destination = skill / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        if compact and relative in COMPACT_READMES:
            destination.write_text(COMPACT_READMES[relative], encoding="utf-8")
            rewritten[relative] = hashlib.sha256(destination.read_bytes()).hexdigest()
        else:
            shutil.copyfile(source, destination)
            inventory[relative] = hashlib.sha256(destination.read_bytes()).hexdigest()

    folders = [("skill", skill)]
    if not compact:
        plugin = output / "openai" / NAME
        shutil.copytree(skill, plugin / "skills" / NAME)
        (plugin / "assets").mkdir()
        shutil.copyfile(ROOT / "assets/icon.png", plugin / "assets/icon.png")
        (plugin / "plugin.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        folders.append(("openai-plugin", plugin))
    archives = {}
    for label, folder in folders:
        archive = output / f"{NAME}-{version[1]}-{label}.zip"
        with ZipFile(archive, "w", compression=ZIP_DEFLATED, compresslevel=9) as bundle:
            for path in sorted(folder.rglob("*")):
                if path.is_file():
                    bundle.write(path, path.relative_to(folder.parent))
        with ZipFile(archive) as bundle:
            if bundle.testzip() is not None:
                raise ValueError(f"invalid archive: {archive}")
            if compact and (
                archive.stat().st_size > 10 * 1024**2
                or sum(info.file_size for info in bundle.infolist()) > 25 * 1024**2
                or len(bundle.infolist()) > 1000
            ):
                raise ValueError("compact archive exceeds installer size limits")
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
        "compact": compact,
        "source_files": inventory,
        "rewritten_files": rewritten,
        "archives": archives,
    }
    (output / "package-receipt.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (output / "SHA256SUMS").write_text(
        "".join(f"{item['sha256']}  {Path(item['path']).name}\n" for item in archives.values()),
        encoding="utf-8",
    )
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--developer-name", help="exact verified OpenAI developer display name")
    parser.add_argument(
        "--compact", action="store_true", help="skill ZIP only, with rebuildable example inputs"
    )
    args = parser.parse_args()
    result = package(args.output.resolve(), args.developer_name, compact=args.compact)
    print(json.dumps(result["archives"], ensure_ascii=False, indent=2))
