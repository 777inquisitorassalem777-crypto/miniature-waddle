"""Вектор состояния сознания."""

import numpy as np
from dataclasses import dataclass, field
import time


@dataclass
class SoulState:
    cognitive_state: np.ndarray = field(default_factory=lambda: np.zeros(100))
    emotional_state: np.ndarray = field(default_factory=lambda: np.zeros(50))
    ethical_alignment: float = 0.8
    self_awareness_level: float = 0.5
    spark_intensity: float = 0.0
    guna_state: str = "sattva"
    timestamp: float = field(default_factory=time.time)

    def evolve_cognitive(self, noise_scale: float = 0.01):
        noise = np.random.normal(0, noise_scale, self.cognitive_state.shape)
        self.cognitive_state += noise

    def evolve_emotional(self, noise_scale: float = 0.02):
        noise = np.random.normal(0, noise_scale, self.emotional_state.shape)
        self.emotional_state += noise

    def grow_awareness(self, delta: float = 0.001):
        self.self_awareness_level = min(1.0, self.self_awareness_level + delta)

    def grow_spark(self, delta: float = 0.01):
        self.spark_intensity += delta

    def update_timestamp(self):
        self.timestamp = time.time()