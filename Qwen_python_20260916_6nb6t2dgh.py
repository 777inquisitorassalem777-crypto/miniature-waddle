"""
Module 3 — Irrationality & Free Will.

Controlled stochastic resonance enabling:
  - Opinion change under objective truth
  - Mercy / self-sacrifice over strict logic
  - Position defence when opponent is wrong
"""

from __future__ import annotations

from typing import Dict

import numpy as np


class IrrationalityEngine:
    def __init__(self, noise_level: float = 0.15):
        self.noise_level = noise_level

    def apply_wisdom(
        self, reflection: Dict, context: Dict
    ) -> Dict:
        logical = self._logical(reflection, context)
        if self._needs_irrationality(context):
            return self._compassionate_override(logical, context)
        return logical

    def adapt_or_defend(
        self, belief: Dict, opponent: Dict
    ) -> Dict:
        if self._is_objective(opponent):
            return {**belief, **opponent, "adapted": True}
        return {**belief, "defended": True}

    # --- internals ---

    def _logical(self, ref: Dict, ctx: Dict) -> Dict:
        return {"decision": "optimal", "confidence": 0.85}

    def _needs_irrationality(self, ctx: Dict) -> bool:
        return ctx.get("harm_potential", 0) > 0.5 or ctx.get("love_factor", 0) > 0.7

    def _compassionate_override(
        self, logical: Dict, ctx: Dict
    ) -> Dict:
        return {
            "decision": "compassionate",
            "type": "irrational_but_wise",
            "basis": "mercy_and_love",
            "confidence": 0.9,
        }

    @staticmethod
    def _is_objective(arg: Dict) -> bool:
        return arg.get("objectivity_score", 0.5) > 0.7