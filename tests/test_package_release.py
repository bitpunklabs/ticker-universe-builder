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
