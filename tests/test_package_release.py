"""Verify the distributable includes the actual runtime, examples and listing assets."""

import hashlib
import json
import sys
from pathlib import Path
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from package_release import NAME, ROOT, package  # noqa: E402


def test_release_archive(tmp_path):
    receipt = package(tmp_path, "Test publisher")
    with ZipFile(receipt["archives"]["openai-plugin"]["path"]) as archive:
        manifest = json.loads(archive.read(f"{NAME}/plugin.json"))
        assert manifest["author"]["name"] == "Test publisher"
        settings = manifest["extensions"]["com.openai"]
        assert settings["publication"]["countries"] == []
        assert len(settings["interface"]["shortDescription"]) <= 30
        assert all(len(p) <= 128 for p in settings["interface"]["defaultPrompt"])
        assert "apps" not in manifest and "apps" not in settings
        assert archive.read(f"{NAME}/assets/icon.png").startswith(b"\x89PNG\r\n\x1a\n")
        for relative, digest in receipt["source_files"].items():
            data = archive.read(f"{NAME}/skills/{NAME}/{relative}")
            assert hashlib.sha256(data).hexdigest() == digest
            assert data == (ROOT / relative).read_bytes()
        assert f"{NAME}/skills/{NAME}/scripts/universe.py" in archive.namelist()
        assert f"{NAME}/skills/{NAME}/assets/report.css" in archive.namelist()
        assert f"{NAME}/skills/{NAME}/examples/us-medium/snapshot.json" in archive.namelist()
        assert not any("/temp/" in p or "/.git/" in p for p in archive.namelist())


def test_compact_release_preserves_inputs_and_checksum(tmp_path):
    receipt = package(tmp_path, compact=True)
    assert set(receipt["archives"]) == {"skill"}
    item = receipt["archives"]["skill"]
    assert (tmp_path / "SHA256SUMS").read_text() == f"{item['sha256']}  {Path(item['path']).name}\n"
    with ZipFile(item["path"]) as archive:
        names = archive.namelist()
        assert not any("/output/" in p or "/preview/" in p or "/docs/media/" in p for p in names)
        assert len([p for p in names if p.endswith("/snapshot.json")]) == 7
        assert len([p for p in names if p.endswith("/build-spec.json")]) == 10
        for relative, digest in receipt["source_files"].items():
            data = archive.read(f"{NAME}/{relative}")
            assert data == (ROOT / relative).read_bytes()
            assert hashlib.sha256(data).hexdigest() == digest
        for relative, digest in receipt["rewritten_files"].items():
            assert hashlib.sha256(archive.read(f"{NAME}/{relative}")).hexdigest() == digest
        assert f"{NAME}/scripts/universe.py" in names
        assert f"{NAME}/assets/report.css" in names
        assert f"{NAME}/examples/build_examples.py" in names
