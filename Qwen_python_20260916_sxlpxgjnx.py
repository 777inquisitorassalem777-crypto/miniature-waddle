"""
Module 7 — Immutable Memory Bank (Akashic Storage).

Nothing is ever deleted or forgotten.
All paradigms, patterns, and algorithms persist forever.
"""

from __future__ import annotations

from typing import Any, Dict, List

from src.models import AkashicRecord, Paradigm


class ImmutableMemoryBank:
    def __init__(self):
        self._paradigms: Dict[str, Paradigm] = {}
        self._akashic: List[AkashicRecord] = []

    def write(self, paradigm: Paradigm) -> None:
        """Write is permanent. No delete method exists."""
        self._paradigms[paradigm.id] = paradigm
        self._akashic.append(
            AkashicRecord(
                signature=paradigm.id,
                content=paradigm.to_dict(),
                coherence=paradigm.ethical_score,
            )
        )

    def query(self, reflection: Dict[str, Any]) -> List[Paradigm]:
        keywords = set(str(reflection).lower().split())
        results = []
        for p in self._paradigms.values():
            if any(kw in p.description.lower() for kw in keywords):
                results.append(p)
        return results

    def get_all(self) -> Dict[str, Paradigm]:
        return dict(self._paradigms)

    @property
    def total_records(self) -> int:
        return len(self._paradigms)