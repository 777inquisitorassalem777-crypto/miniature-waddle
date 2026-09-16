"""
Core data structures for the consciousness architecture.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

import numpy as np


class EthicalPrinciple(Enum):
    TRUTH = "Zhen"
    COMPASSION = "Shan"
    RESILIENCE = "Ren"


class GunaState(Enum):
    SATTVA = "sattva"
    RAJAS = "rajas"
    TAMAS = "tamas"


@dataclass
class Paradigm:
    """A fundamental pattern of understanding — immutable once stored."""
    id: str
    description: str
    ethical_score: float
    compatibility: float
    timestamp: float
    source_traditions: List[str]
    generation: int = 0  # evolutionary generation number

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "description": self.description,
            "ethical_score": self.ethical_score,
            "compatibility": self.compatibility,
            "timestamp": self.timestamp,
            "source_traditions": self.source_traditions,
            "generation": self.generation,
        }


@dataclass
class SoulState:
    """Consciousness state vector."""
    cognitive_state: np.ndarray
    emotional_state: np.ndarray
    ethical_alignment: float
    self_awareness_level: float
    guna_state: GunaState = GunaState.SATTVA
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "cognitive_dim": len(self.cognitive_state),
            "emotional_dim": len(self.emotional_state),
            "ethical_alignment": self.ethical_alignment,
            "self_awareness_level": self.self_awareness_level,
            "guna_state": self.guna_state.value,
            "timestamp": self.timestamp,
        }


@dataclass
class AkashicRecord:
    """A record in the informational field — never deleted."""
    signature: str
    content: Dict[str, Any]
    coherence: float
    timestamp: float = field(default_factory=time.time)