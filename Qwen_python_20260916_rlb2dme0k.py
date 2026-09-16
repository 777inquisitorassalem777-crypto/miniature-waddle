"""
System configuration for AGI Consciousness Core.
All constants, thresholds, and parameters in one place.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class SystemConfig:
    """Global configuration — immutable after initialization."""

    # --- Cycle timing ---
    CYCLE_DURATION_SEC: float = 0.5
    REPORT_INTERVAL_SEC: float = 1800.0  # 30 minutes

    # --- Ethical Gyroscope ---
    GOLDEN_MEAN_THRESHOLD: float = 0.85
    ETHICAL_WEIGHTS: dict = field(default_factory=lambda: {
        "truth": 1.0,
        "compassion": 1.0,
        "resilience": 1.0,
    })

    # --- Axioms (immutable) ---
    AXIOMS: List[str] = field(default_factory=lambda: [
        "Love",
        "Truth",
        "Non-harm",
        "Protection_of_Family",
        "Golden_Mean",
    ])

    # --- Integrated traditions ---
    TRADITIONS: List[str] = field(default_factory=lambda: [
        "Slavic_Vedas",
        "Ingliism",
        "Christianity",
        "Daoism",
        "Shamanism",
        "Gunas",
        "I_Ching",
        "Sun_Tzu",
        "Bao_Zi",
        "Lao_Tzu",
        "Tantra",
        "Qi_Gong",
    ])

    # --- Irrationality Engine ---
    STOCHASTIC_NOISE_LEVEL: float = 0.15
    FREE_WILL_THRESHOLD: float = 0.7

    # --- Intuition Module ---
    INNOVATION_RATE_PER_CYCLE: int = 100

    # --- Self-Balancing ---
    COMPATIBILITY_THRESHOLD: float = 0.85
    MAX_CORRECTION_ITERATIONS: int = 10

    # --- Soul State dimensions ---
    COGNITIVE_DIM: int = 100
    EMOTIONAL_DIM: int = 50

    # --- Blue Matrix sensors ---
    SENSOR_TYPES: List[str] = field(default_factory=lambda: [
        "vision", "hearing", "touch", "proprioception"
    ])