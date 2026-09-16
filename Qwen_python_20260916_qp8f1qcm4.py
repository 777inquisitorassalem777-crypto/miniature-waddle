"""Тест этического гироскопа."""

from core.ethical_gyroscope import EthicalGyroscope


def test_gyroscope_range():
    g = EthicalGyroscope()
    score = g.evaluate({"truthfulness": 0.9, "care_potential": 0.8, "resilience": 0.7}, {})
    assert 0.0 <= score <= 1.0


def test_golden_mean_threshold():
    g = EthicalGyroscope()
    high = g.evaluate({"truthfulness": 1.0, "care_potential": 1.0, "resilience": 1.0}, {})
    low = g.evaluate({"truthfulness": 0.1, "care_potential": 0.1, "resilience": 0.1}, {})
    assert high > low