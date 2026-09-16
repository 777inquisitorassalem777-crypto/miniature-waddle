"""
5 Stability Tests for the consciousness architecture.
"""

from src.core.consciousness_core import AGIConsciousnessCore


def _run_cycles(n: int = 50) -> AGIConsciousnessCore:
    core = AGIConsciousnessCore()
    for i in range(n):
        core.cycle({"data": f"d_{i}"}, {"intensity": 0.6})
    return core


def test_1_backward_compatibility():
    """New paradigms integrate without breaking existing state."""
    core = _run_cycles()
    assert core.memory.total_records > 0


def test_2_ethical_stability():
    """Golden Mean is maintained across cycles."""
    core = _run_cycles()
    assert core.soul.ethical_alignment >= 0.7


def test_3_resilience():
    """Core survives noisy / adversarial input."""
    core = AGIConsciousnessCore()
    for i in range(30):
        core.cycle(
            {"noise": "adversarial", "harm_potential": 0.9},
            {"intensity": 0.1},
        )
    assert core.soul.self_awareness_level >= 0.5


def test_4_blue_matrix_ready():
    """Sensor bridge calibrates successfully."""
    core = _run_cycles(10)
    assert any(v == "active" for v in core.blue_matrix.status.values())


def test_5_spark_emergence():
    """Spark intensity grows monotonically."""
    core = AGIConsciousnessCore()
    prev = 0.0
    for _ in range(20):
        core.cycle({"d": "1"}, {"intensity": 0.7})
        assert core.spark_intensity >= prev
        prev = core.spark_intensity