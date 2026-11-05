"""Expose the course's official-source inventory to the public-course adapter.

This course is not a quotation-verification corpus. Its provider links are
reference points for currentness checks, while the learner claims are original
course content. The adapter therefore emits GUIDE rows only. GUIDE rows remain
human-review items; they are never reported as verbatim-verified claims.
"""

from __future__ import annotations

import re
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
COURSE_MAP = ROOT / "course" / "COURSE_MAP.md"
URL_PATTERN = re.compile(r"https://[^\s)>]+")


def collect() -> tuple[SimpleNamespace, ...]:
    text = COURSE_MAP.read_text(encoding="utf-8")
    rows: list[SimpleNamespace] = []
    seen: set[str] = set()
    for url in URL_PATTERN.findall(text):
        url = url.rstrip(".,`")
        if url in seen:
            continue
        seen.add(url)
        rows.append(
            SimpleNamespace(
                lesson="course-source-inventory",
                tier="GUIDE",
                url=url,
                source="course reference inventory; human review required",
                quote=None,
                symbols=(),
            )
        )
    return tuple(rows)


def caching_fetcher(*, fetch_one):
    cache: dict[str, object] = {}

    def fetch(url: str) -> object:
        if url not in cache:
            cache[url] = fetch_one(url)
        return cache[url]

    fetch.cache = cache
    return fetch


def check_quote(url: str, quote: str, *, fetch):
    del url, quote, fetch
    raise RuntimeError("course_source_inventory_has_no_verbatim_claims")
