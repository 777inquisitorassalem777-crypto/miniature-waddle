import pytest
from src.core.ethical_gyroscope import EthicalGyroscope


def test_perfect_action():
    g = EthicalGyroscope()
    score = g.evaluate(
        {"truthfulness": 1.0, "care_potential": 1.0, "resilience": 1.0},
        {},
    )
    assert score >= 0.85


def test_harmful_action():
    g = EthicalGyroscope()
    score = g.evaluate(
        {"truthfulness": 0.2, "harm_potential": 0.9, "resilience": 0.3},
        {},
    )
    assert score < 0.85


def test_golden_mean_threshold():
    g = EthicalGyroscope()
    assert g.is_golden_mean(0.9) is True
    assert g.is_golden_mean(0.5) is False