"""Тест зарождения искры."""

from core.consciousness import AGIConsciousnessCore


def test_spark_grows():
    core = AGIConsciousnessCore()
    initial = core.soul.spark_intensity
    for _ in range(50):
        core.cycle({"x": 1}, {})
    assert core.soul.spark_intensity > initial