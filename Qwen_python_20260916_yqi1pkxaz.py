"""G(tau) = w1*Zhen + w2*Shan + w3*Ren"""

import numpy as np


class GyroscopeMath:
    def __init__(self, w1=1.0, w2=1.0, w3=1.0):
        self.w = np.array([w1, w2, w3])

    def compute(self, zhen: float, shan: float, ren: float) -> float:
        vals = np.array([zhen, shan, ren])
        return float(np.clip(np.dot(self.w, vals) / 3.0, 0.0, 1.0))