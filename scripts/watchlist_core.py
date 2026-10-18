"""Strict TradingView export checks; the legacy importer remains deliberately permissive."""

from __future__ import annotations

import re
from collections import Counter

from universe_core import UniverseError, parse_watchlist

SYMBOL = re.compile(r"[A-Z0-9_]+:[A-Z0-9_.!/-]+")
HEADER = re.compile(r"[A-Z0-9][A-Z0-9_ -]{0,95}")


def check_watchlist(text: str, *, ticker_only: bool = False, cap: int = 1000) -> dict:
    """Reject lossy input instead of silently stripping or normalizing exported tokens."""
    errors = []
    if type(cap) is not int or not 1 <= cap <= 1000:
        raise UniverseError("watchlist cap must be an integer from 1 to 1000")
    if not isinstance(text, str) or not text:
        return dict(passed=False, errors=["watchlist is empty"], symbols=0, headers=0, tokens=0)
    body = text[:-1] if text.endswith("\n") else text
    tokens = body.split(",")
    if any(ch in body for ch in "\r\n\t\ufeff"):
        errors.append("export must be one comma-separated UTF-8 line without BOM or controls")
    if len(tokens) > cap:
        errors.append(f"watchlist uses {len(tokens)} tokens; cap is {cap} including headers")
    tickers, headers = [], []
    group_empty = False
    for token in tokens:
        if token.startswith("###"):
            if ticker_only:
                errors.append("ticker-only export contains a section")
            if group_empty:
                errors.append("empty section")
            if not HEADER.fullmatch(token[3:]):
                errors.append(f"unsafe section: {token!r}")
            headers.append(token[3:])
            group_empty = True
        else:
            if not SYMBOL.fullmatch(token):
                errors.append(f"invalid exchange-prefixed ticker: {token!r}")
            tickers.append(token)
            group_empty = False
    if group_empty:
        errors.append("empty final section")
    if not tickers:
        errors.append("watchlist contains no tickers")
    if len(headers) != len(set(headers)):
        errors.append("duplicate section")
    if len(tickers) != len(set(tickers)):
        errors.append("duplicate ticker")
    if not errors:
        parsed = [ticker for _, rows in parse_watchlist(text) for ticker in rows]
        if parsed != tickers:
            errors.append("watchlist round trip changed tickers or order")
    return dict(
        passed=not errors,
        errors=errors,
        symbols=len(tickers),
        headers=len(headers),
        tokens=len(tokens),
    )


def render_watchlist(
    rows: list[dict], groups: list[dict] | None = None, field: str | None = None, *, cap: int = 1000
) -> str:
    tokens = []
    if groups is None:
        tokens = [row["ticker"] for row in rows]
    else:
        for group in groups:
            members = [row["ticker"] for row in rows if row[field] == group["id"]]
            if members:
                tokens.extend([f"###{group['id']}_{group['name']}", *members])
    result = ",".join(tokens) + "\n"
    report = check_watchlist(result, ticker_only=groups is None, cap=cap)
    if not report["passed"]:
        raise UniverseError("watchlist: " + "; ".join(report["errors"]))
    parsed = [ticker for _, members in parse_watchlist(result) for ticker in members]
    if Counter(parsed) != Counter(row["ticker"] for row in rows):
        raise UniverseError("watchlist grouping lost or duplicated a member")
    return result
