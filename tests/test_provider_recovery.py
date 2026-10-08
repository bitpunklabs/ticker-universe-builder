"""Transport recovery must retain identity, verified TLS and honest partial results."""

import gzip
import http.client
import json
import ssl
import subprocess
import sys
import urllib.error
from datetime import datetime, timezone
from itertools import cycle
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import provider_core as p  # noqa: E402


@pytest.fixture(autouse=True)
def no_real_fallback(monkeypatch):
    monkeypatch.setattr(p.shutil, "which", lambda _: None)


def response(body=b'{"data": []}', encoding="identity", length=None):
    result = MagicMock()
    result.__enter__.return_value = result
    result.read1.side_effect = cycle([body, b""])
    result.headers = {"Content-Encoding": encoding, "Content-Length": str(
        len(body) if length is None else length)}
    return result


@pytest.mark.parametrize("failure", [
    http.client.IncompleteRead(b"partial", 100),
    http.client.RemoteDisconnected("connection closed"),
    response(b"<html>JavaScript shell</html>"),
    response(b'{"data": []}', length=100),
])
def test_transient_or_invalid_body_recovers_without_caching_failure(tmp_path, failure):
    cache = tmp_path / "receipt.json"
    with patch.object(p.urllib.request, "urlopen", side_effect=[failure, response()]) as call, \
            patch.object(p.time, "sleep"):
        assert p.request_json("https://example.org/data", cache) == {"data": []}
    assert call.call_count == 2
    assert not cache.with_suffix(".json.error.json").exists()
    assert json.loads(cache.read_text())["response"] == {"data": []}


def test_exhausted_retries_keep_diagnostics_not_a_fresh_response(tmp_path):
    cache = tmp_path / "receipt.json"
    with patch.object(p.urllib.request, "urlopen", return_value=response(b'null')) as call, \
            patch.object(p.time, "sleep"), pytest.raises(p.ProviderError):
        p.request_json("https://example.org/data", cache)
    assert call.call_count == 3 and not cache.exists()
    error = json.loads(cache.with_suffix(".json.error.json").read_text())
    assert len(error["attempts"]) == 3


def test_gzip_response_is_decoded_with_wire_hash_retained(tmp_path):
    raw = gzip.compress(b'{"data": []}')
    cache = tmp_path / "receipt.json"
    with patch.object(p.urllib.request, "urlopen", return_value=response(raw, "gzip")):
        assert p.request_json("https://example.org/data", cache) == {"data": []}
    assert json.loads(cache.read_text())["sha256"] == p.hashlib.sha256(raw).hexdigest()


def test_http_403_is_not_blindly_retried(tmp_path):
    error = urllib.error.HTTPError("https://example.org/data", 403, "blocked", {}, None)
    with patch.object(p.urllib.request, "urlopen", side_effect=error) as call, \
            pytest.raises(p.ProviderError):
        p.request_json(error.url, tmp_path / "receipt.json")
    assert call.call_count == 1


def test_macos_fallback_still_verifies_tls(tmp_path, monkeypatch):
    monkeypatch.delenv("SSL_CERT_FILE", raising=False)
    monkeypatch.delenv("SSL_CERT_DIR", raising=False)
    error = urllib.error.URLError(ssl.SSLCertVerificationError("untrusted default CA"))
    context = ssl.create_default_context()
    with patch.object(p.sys, "platform", "darwin"), \
            patch.object(p.Path, "is_file", return_value=True), \
            patch.object(p.ssl, "create_default_context", return_value=context) as trust, \
            patch.object(p.urllib.request, "urlopen", side_effect=[error, response()]) as call:
        p.request_json("https://example.org/data", tmp_path / "receipt.json")
    trust.assert_called_once_with(cafile="/etc/ssl/cert.pem")
    assert call.call_args.kwargs["context"].verify_mode == ssl.CERT_REQUIRED


def test_explicit_trust_store_is_not_overridden(tmp_path, monkeypatch):
    monkeypatch.setenv("SSL_CERT_FILE", "/explicit/ca.pem")
    error = urllib.error.URLError(ssl.SSLCertVerificationError("wrong CA"))
    with patch.object(p.sys, "platform", "darwin"), \
            patch.object(p.urllib.request, "urlopen", side_effect=error) as call, \
            pytest.raises(p.ProviderError, match="SSL_CERT_FILE"):
        p.request_json("https://example.org/data", tmp_path / "receipt.json")
    assert call.call_count == 1


def yahoo_payload():
    start = int(datetime(2026, 8, 1, tzinfo=timezone.utc).timestamp())
    return {"chart": {"result": [{
        "meta": {"symbol": "BRK-B", "currency": "USD"},
        "timestamp": [start + i * 86400 for i in range(35)],
        "indicators": {"quote": [{"close": list(range(100, 135)), "volume": [100] * 35}],
                       "adjclose": [{"adjclose": list(range(100, 135))}]},
    }]}}


@pytest.mark.parametrize("field,value", [("symbol", "BRK-A"), ("currency", "CNY")])
def test_wrong_identity_or_currency_is_rejected(field, value):
    payload = yahoo_payload()
    payload["chart"]["result"][0]["meta"][field] = value
    with pytest.raises(p.ProviderError):
        p.parse_yahoo(payload, "NYSE:BRK.B", "2026-09-04",
                      expected_symbol="BRK-B", currencies={"USD"})


def test_misaligned_history_does_not_silently_truncate():
    payload = yahoo_payload()
    payload["chart"]["result"][0]["indicators"]["quote"][0]["volume"].pop()
    with pytest.raises(p.ProviderError, match="misaligned"):
        p.parse_yahoo(payload, "NYSE:BRK.B", "2026-09-04")


def test_alternate_yahoo_host_records_actual_source_and_share_class(tmp_path):
    calls = []

    def request(url, cache):
        calls.append((url, cache.name))
        if "query1" in url:
            raise p.ProviderError("unavailable")
        p.write_json(cache, {"response": yahoo_payload()})
        return yahoo_payload()

    with patch.object(p, "request_json", side_effect=request):
        bars, receipt = p.fetch_equity_bars({"ticker": "NYSE:BRK.B"}, "us", tmp_path,
                                           "2026-09-04")
    assert len(bars) == 35 and "query2" in receipt["source"]
    assert calls[1][1] == "bars-query2-BRK-B.json" and receipt["fallback_notes"]


def test_inventory_failure_preserves_previous_bars_and_cutoff(tmp_path):
    before = p.write_fetch_result(tmp_path, "us", "2026-09-01",
                                 [("2026-09-01", "NYSE:TEST", 100, 1000)],
                                 {"requested": 1, "received": 1, "receipts": [], "failures": []})
    raw = (tmp_path / "prices.csv").read_bytes()
    with patch.object(p, "scan_equities", side_effect=p.ProviderError("listing unavailable")):
        result = p.fetch(market="us", output=tmp_path, cutoff="2026-09-02", limit=1, workers=1)
    assert not result["complete"] and result["prices_until"] == before["prices_until"]
    assert (tmp_path / "prices.csv").read_bytes() == raw
    assert result["requested_prices_until"] == "2026-09-02"


def test_first_inventory_failure_is_a_partial_manifest(tmp_path):
    with patch.object(p, "scan_equities", side_effect=p.ProviderError("listing unavailable")):
        result = p.fetch(market="us", output=tmp_path, cutoff="2026-09-02", limit=1, workers=1)
    assert not result["complete"] and result["received"] == 0
    assert (tmp_path / "manifest.json").is_file()


def test_optional_curl_recovers_in_the_same_attempt_budget(tmp_path, monkeypatch):
    monkeypatch.setattr(p.shutil, "which", lambda _: "/usr/bin/curl")
    monkeypatch.setenv("SSL_CERT_FILE", "/verified/ca.pem")
    result = subprocess.CompletedProcess([], 0, stdout=b'{"data": []}', stderr=b"")
    cache = tmp_path / "receipt.json"
    with patch.object(p.urllib.request, "urlopen", side_effect=http.client.IncompleteRead(b"")), \
            patch.object(p.subprocess, "run", return_value=result) as call, \
            patch.object(p.time, "sleep"):
        assert p.request_json("https://example.org/data", cache, {}) == {"data": []}
    args = call.call_args.args[0]
    assert "--cacert" in args and "--insecure" not in args
    assert call.call_args.kwargs.get("shell", False) is False
    assert "--data-binary" in args and call.call_args.kwargs["input"] == b"{}"
    assert json.loads(cache.read_text())["transport"] == "curl"


def test_curl_failure_cannot_cache_partial_stdout(tmp_path, monkeypatch):
    monkeypatch.setattr(p.shutil, "which", lambda _: "/usr/bin/curl")
    result = subprocess.CompletedProcess([], 18, stdout=b'{"data": []}', stderr=b"truncated")
    cache = tmp_path / "receipt.json"
    with patch.object(p.urllib.request, "urlopen", side_effect=http.client.IncompleteRead(b"")), \
            patch.object(p.subprocess, "run", return_value=result) as call, \
            patch.object(p.time, "sleep"), pytest.raises(p.ProviderError, match="truncated"):
        p.request_json("https://example.org/data", cache)
    assert call.call_count == 2 and not cache.exists()


def test_curl_http_403_stops_remaining_retries(tmp_path, monkeypatch):
    monkeypatch.setattr(p.shutil, "which", lambda _: "/usr/bin/curl")
    result = subprocess.CompletedProcess([], 22, stdout=b"",
                                         stderr=b"curl: (22) The requested URL returned error: 403")
    cache = tmp_path / "receipt.json"
    with patch.object(p.urllib.request, "urlopen", side_effect=http.client.IncompleteRead(b"")), \
            patch.object(p.subprocess, "run", return_value=result) as call, \
            patch.object(p.time, "sleep"), pytest.raises(p.ProviderError, match="403"):
        p.request_json("https://example.org/data", cache)
    assert call.call_count == 1 and not cache.exists()
    error = json.loads(cache.with_suffix(".json.error.json").read_text())
    assert len(error["attempts"]) == 2
