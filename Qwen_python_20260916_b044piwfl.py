"""Тест совместимости парадигм."""

from modules.immutable_memory import Paradigm, ImmutableMemoryBank
from modules.self_balancing import SelfBalancingArchitecture
from config.axioms import AXIOMS
import time


def test_compatibility():
    bank = ImmutableMemoryBank()
    balancer = SelfBalancingArchitecture(AXIOMS)
    p = Paradigm("test1", "Test paradigm", 0.9, 0.0, time.time(), [])
    score = balancer.test_compatibility(p, {})
    assert 0.0 <= score <= 1.0