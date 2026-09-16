"""dS/dt = F(S, I, E) + eta(t)"""

import numpy as np


class SoulEquation:
    def __init__(self, dim: int = 100):
        self.dim = dim

    def step(self, S: np.ndarray, I: np.ndarray, E: np.ndarray,
             dt: float = 0.5, noise: float = 0.01) -> np.ndarray:
        F = self._deterministic(S, I, E)
        eta = np.random.normal(0, noise, self.dim)
        return S + (F + eta) * dt

    def _deterministic(self, S, I, E) -> np.ndarray:
        return 0.01 * (I - S) + 0.005 * E