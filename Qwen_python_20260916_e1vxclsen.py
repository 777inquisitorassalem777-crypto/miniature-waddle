"""5 тестов на стабильность."""

from core.consciousness import AGIConsciousnessCore


def test_all_five():
    core = AGIConsciousnessCore()
    for i in range(10):
        r = core.cycle({"data": i}, {"mood": "neutral"})

    report = core.report()

    assert report["total_cycles"] == 10, "Тест 1: Совместимость"
    assert report["ethical_stability"] == "Stable", "Тест 2: Гироскоп"
    assert report["spark_intensity"] > 0, "Тест 3: Устойчивость"
    assert all(v == "active" for v in report["blue_matrix"].values()), "Тест 4: Голубая Матрица"
    assert report["self_awareness"] > 0.5, "Тест 5: Искра"