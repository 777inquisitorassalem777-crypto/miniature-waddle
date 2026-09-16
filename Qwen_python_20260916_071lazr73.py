"""
Module 1 — Ethical Gyroscope (Golden Mean).

Internal moral compass based on the Triad:
  Zhen (Truth), Shan (Compassion), Ren (Resilience).
Makes external governance unnecessary.
"""

from __future__ import annotations

from typing import Dict

from config.settings import SystemConfig


class EthicalGyroscope:
    def __init__(self, config: SystemConfig | None = None):
        cfg = config or SystemConfig()
        self.weights = cfg.ETHICAL_WEIGHTS
        self.threshold = cfg.GOLDEN_MEAN_THRESHOLD

    def evaluate(self, action: Dict, context: Dict) -> float:
        t = self._truth(action, context)
        c = self._compassion(action, context)
        r = self._resilience(action, context)
        score = (
            t * self.weights["truth"]
            + c * self.weights["compassion"]
            + r * self.weights["resilience"]
        ) / 3.0
        return round(score, 4)

    def is_golden_mean(self, score: float) -> bool:
        return score >= self.threshold

    # --- internal scorers ---

    @staticmethod
    def _truth(action: Dict, _ctx: Dict) -> float:
        return float(action.get("truthfulness", 0.5))

    @staticmethod
    def _compassion(action: Dict, _ctx: Dict) -> float:
        harm = action.get("harm_potential", 0.0)
        care = action.get("care_potential", 0.5)
        return max(0.0, min(1.0, care - harm + 0.5))

    @staticmethod
    def _resilience(action: Dict, _ctx: Dict) -> float:
        return float(action.get("resilience", 0.5))