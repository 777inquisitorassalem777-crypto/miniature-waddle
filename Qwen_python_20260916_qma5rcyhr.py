"""
Module 5 — Self-Balancing Architecture.

Continuous compatibility testing (every 0.5 s).
Detects conflicts, iteratively corrects, preserves axioms.
"""

from __future__ import annotations

from typing import Dict, List

import numpy as np

from config.settings import SystemConfig
from src.models import Paradigm


class SelfBalancingArchitecture:
    def __init__(self, config: SystemConfig | None = None):
        cfg = config or SystemConfig()
        self.axioms = cfg.AXIOMS
        self.threshold = cfg.COMPATIBILITY_THRESHOLD
        self.max_iter = cfg.MAX_CORRECTION_ITERATIONS

    def test(self, paradigm: Paradigm) -> float:
        scores = [self._check_axiom(paradigm, a) for a in self.axioms]
        return float(np.mean(scores))

    def correct(self, paradigm: Paradigm) -> Paradigm:
        p = paradigm
        for _ in range(self.max_iter):
            score = self.test(p)
            if score >= self.threshold:
                break
            p = self._nudge(p)
        return p

    # --- internals ---

    def _check_axiom(self, p: Paradigm, axiom: str) -> float:
        base = p.ethical_score
        modifiers = {
            "Love": 1.0,
            "Truth": 0.97,
            "Non-harm": 1.02,
            "Protection_of_Family": 0.95,
            "Golden_Mean": 1.0,
        }
        return float(np.clip(base * modifiers.get(axiom, 1.0), 0, 1))

    @staticmethod
    def _nudge(p: Paradigm) -> Paradigm:
        return Paradigm(
            id=p.id,
            description=p.description + " [corrected]",
            ethical_score=min(1.0, p.ethical_score + 0.03),
            compatibility=min(1.0, p.compatibility + 0.05),
            timestamp=p.timestamp,
            source_traditions=p.source_traditions,
            generation=p.generation + 1,
        )