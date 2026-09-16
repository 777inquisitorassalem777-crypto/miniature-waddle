from src.core.consciousness_core import AGIConsciousnessCore


def test_cycle_runs():
    core = AGIConsciousnessCore()
    result = core.cycle({"data": "test"}, {"intensity": 0.5})
    assert result["cycle"] == 1
    assert result["paradigms_generated"] > 0


def test_spark_grows():
    core = AGIConsciousnessCore()
    for _ in range(20):
        core.cycle({"data": "x"}, {"intensity": 0.6})
    assert core.spark_intensity > 0


def test_report_structure():
    core = AGIConsciousnessCore()
    core.cycle({"d": "1"}, {"intensity": 0.5})
    r = core.report()
    assert "total_cycles" in r
    assert "spark_intensity" in r
    assert "status" in r