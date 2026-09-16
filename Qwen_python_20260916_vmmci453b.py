"""Этический Гироскоп на основе Триады."""

from .golden_mean import GoldenMeanEngine


class EthicalGyroscope:
    def __init__(self):
        self.engine = GoldenMeanEngine()

    def evaluate(self, action: dict, context: dict) -> float:
        zhen = self._truth(action, context)
        shan = self._compassion(action, context)
        ren = self._resilience(action, context)
        return self.engine.compute(zhen, shan, ren)

    def _truth(self, action: dict, context: dict) -> float:
        return min(1.0, max(0.0, action.get("truthfulness", 0.5)))

    def _compassion(self, action: dict, context: dict) -> float:
        harm = action.get("harm_potential", 0.0)
        care = action.get("care_potential", 0.5)
        return min(1.0, max(0.0, care - harm + 0.5))

    def _resilience(self, action: dict, context: dict) -> float:
        return min(1.0, max(0.0, action.get("resilience", 0.5)))