from src.core.self_balancing import SelfBalancingArchitecture
from src.models import Paradigm
from src.utils import generate_id, get_timestamp


def _make_paradigm(ethical: float) -> Paradigm:
    return Paradigm(
        id=generate_id(),
        description="test",
        ethical_score=ethical,
        compatibility=0.0,
        timestamp=get_timestamp(),
        source_traditions=["Daoism"],
    )


def test_high_ethical_passes():
    b = SelfBalancingArchitecture()
    p = _make_paradigm(0.95)
    assert b.test(p) >= 0.85


def test_low_ethical_corrected():
    b = SelfBalancingArchitecture()
    p = _make_paradigm(0.3)
    corrected = b.correct(p)
    assert corrected.ethical_score > p.ethical_score