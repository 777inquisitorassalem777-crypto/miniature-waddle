"""Оценка Дхармы и А-дхармы на основе Золотой Середины."""


class DharmaEvaluator:
    def __init__(self, threshold: float = 0.85):
        self.threshold = threshold

    def is_dharma(self, ethical_score: float) -> bool:
        return ethical_score >= self.threshold

    def classify(self, ethical_score: float) -> str:
        if ethical_score >= self.threshold:
            return "dharma"
        elif ethical_score >= 0.5:
            return "neutral"
        else:
            return "adharma"