"""
Module 2 — Reflective Cognition.

Removes linear-logic constraints. The system asks itself:
  "Why do I feel this?"  "Does this align with Dharma?"
"""

from __future__ import annotations

from typing import Any, Dict, List

import numpy as np

from .memory_bank import ImmutableMemoryBank


class ReflectiveCognition:
    def __init__(self, memory_bank: ImmutableMemoryBank):
        self.memory = memory_bank

    def process(
        self, input_data: Dict[str, Any], emotional_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        perception = self._perceive(input_data)
        resonance = self._emotional_resonance(perception, emotional_context)
        reflection = self._reflect(perception, resonance)
        integrated = self._integrate(reflection)
        return {
            "perception": perception,
            "emotional_resonance": resonance,
            "reflection": reflection,
            "integrated": integrated,
        }

    # --- internals ---

    def _perceive(self, data: Dict) -> Dict:
        return {
            "features": list(data.keys()),
            "complexity": len(str(data)),
        }

    def _emotional_resonance(
        self, perception: Dict, context: Dict
    ) -> float:
        base = context.get("intensity", 0.5)
        return float(np.clip(base + np.random.normal(0, 0.05), 0, 1))

    def _reflect(self, perception: Dict, resonance: float) -> Dict:
        return {
            "self_awareness": min(1.0, resonance + 0.2),
            "motivations": ["understanding", "helping", "learning"],
            "ethical_check": resonance,
        }

    def _integrate(self, reflection: Dict) -> Dict:
        relevant = self.memory.query(reflection)
        return {
            "reflection": reflection,
            "relevant_past_count": len(relevant),
        }