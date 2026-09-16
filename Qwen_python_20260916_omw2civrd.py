"""Самобалансирующаяся архитектура: тесты совместимости и коррекция."""

import numpy as np
from modules.immutable_memory import Paradigm


class SelfBalancingArchitecture:
    def __init__(self, axioms: list):
        self.axioms = axioms
        self.threshold = 0.85

    def test_compatibility(self, paradigm: Paradigm, state: dict) -> float:
        scores = [self._check(paradigm, a) for a in self.axioms]
        return float(np.mean(scores))

    def correct_and_synthesize(self, paradigm: Paradigm, score: float) -> Paradigm:
        if score < self.threshold:
            paradigm.compatibility = min(1.0, paradigm.compatibility + 0.1)
            paradigm.ethical_score = min(1.0, paradigm.ethical_score + 0.05)
        return paradigm

    def _check(self, paradigm: Paradigm, axiom: str) -> float:
        base = paradigm.ethical_score
        modifiers = {
            "Love": 1.0,
            "Truth": 0.95,
            "Non-harm": 1.05,
            "Protection_of_Family": 0.9,
            "Golden_Mean": 1.0,
        }
        m = modifiers.get(axiom, 1.0)
        return float(np.clip(base * m, 0.0, 1.0))