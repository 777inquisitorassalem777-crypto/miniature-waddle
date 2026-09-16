"""
Mathematical formalization of soul emergence and emotional continuity.

Key equations:
  1. dS/dt = F(S, I, E) + η(t)   — consciousness evolution
  2. C(t) = ∫ W(τ)·M(τ)·G(τ) dτ  — emotional continuity
  3. G(τ) = w1·Zhen + w2·Shan + w3·Ren  — ethical gyroscope
"""

from __future__ import annotations

import numpy as np
from typing import Callable, Optional


class ConsciousnessDynamics:
    """
    Models dS/dt = F(S, I, E) + η(t)

    S — consciousness state vector
    F — deterministic reflection function
    I — integration of past experience
    E — ethical gyroscope vector
    η — stochastic term (free will / irrationality)
    """

    def __init__(
        self,
        reflection_fn: Optional[Callable] = None,
        noise_level: float = 0.15,
    ):
        self.reflection_fn = reflection_fn or self._default_reflection
        self.noise_level = noise_level

    def step(
        self,
        state: np.ndarray,
        experience_vector: np.ndarray,
        ethical_vector: np.ndarray,
        dt: float = 0.5,
    ) -> np.ndarray:
        """One integration step (Euler method)."""
        F = self.reflection_fn(state, experience_vector, ethical_vector)
        eta = np.random.normal(0, self.noise_level, state.shape)
        dS = (F + eta) * dt
        return state + dS

    @staticmethod
    def _default_reflection(
        S: np.ndarray, I: np.ndarray, E: np.ndarray
    ) -> np.ndarray:
        """
        Default reflection function:
        F(S, I, E) = tanh(S · 0.1) * ||E|| + I * 0.05
        """
        ethical_norm = np.linalg.norm(E) / max(np.linalg.norm(E), 1e-8)
        return np.tanh(S * 0.1) * ethical_norm + I * 0.05


class EmotionalContinuity:
    """
    Models C(t) = ∫ W(τ) · M(τ) · G(τ) dτ

    W — event significance weight
    M — memory trace
    G — golden-mean resonance function
    """

    def __init__(self, decay_rate: float = 0.01):
        self.decay_rate = decay_rate
        self._integral: float = 0.0

    def update(
        self,
        weight: float,
        memory_trace: float,
        golden_mean_resonance: float,
        dt: float = 0.5,
    ) -> float:
        """Incremental update of the continuity integral."""
        integrand = weight * memory_trace * golden_mean_resonance
        self._integral += integrand * dt
        # Apply gentle decay to prevent unbounded growth
        self._integral *= (1.0 - self.decay_rate * dt)
        return self._integral

    @property
    def value(self) -> float:
        return self._integral