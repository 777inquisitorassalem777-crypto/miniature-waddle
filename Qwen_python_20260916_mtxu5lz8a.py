"""Математическая модель Золотой Середины."""

import numpy as np


class GoldenMeanEngine:
    """
    Вычисляет степень соответствия действия Золотой Середине.
    G(tau) = w1*Zhen + w2*Shan + w3*Ren
    """

    def __init__(self, w1: float = 1.0, w2: float = 1.0, w3: float = 1.0):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

    def compute(self, zhen: float, shan: float, ren: float) -> float:
        raw = self.w1 * zhen + self.w2 * shan + self.w3 * ren
        return np.clip(raw / 3.0, 0.0, 1.0)

    def is_harmonious(self, score: float, threshold: float = 0.85) -> bool:
        return score >= threshold