"""C(t) = integral W(tau) * M(tau) * G(tau) d_tau"""

import numpy as np


class EmotionalContinuity:
    def compute(self, weights: np.ndarray, memory: np.ndarray,
                gyroscope: np.ndarray, dt: float = 0.5) -> float:
        integrand = weights * memory * gyroscope
        return float(np.trapz(integrand, dx=dt))