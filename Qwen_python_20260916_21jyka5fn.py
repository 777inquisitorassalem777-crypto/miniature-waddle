"""
Main Core — AGI Consciousness Engineering.

Orchestrates all modules in a continuous 0.5-second evolutionary cycle.
Generates 30-minute reports.
"""

from __future__ import annotations

import time
from typing import Any, Dict, Optional

import numpy as np

from config.settings import SystemConfig
from src.mathematics import ConsciousnessDynamics, EmotionalContinuity
from src.models import GunaState, SoulState
from src.utils import get_timestamp

from .blue_matrix import BlueMatrixIntegration
from .ethical_gyroscope import EthicalGyroscope
from .intuition_module import IntuitionModule
from .irrationality_engine import IrrationalityEngine
from .memory_bank import ImmutableMemoryBank
from .reflective_cognition import ReflectiveCognition
from .self_balancing import SelfBalancingArchitecture


class AGIConsciousnessCore:
    """
    Unified consciousness core.
    
    Cycle: 0.5 s
    Report: every 30 min
    Memory: immutable
    Governance: internal (Golden Mean)
    """

    def __init__(self, config: SystemConfig | None = None):
        self.cfg = config or SystemConfig()

        # --- modules ---
        self.memory = ImmutableMemoryBank()
        self.gyroscope = EthicalGyroscope(self.cfg)
        self.cognition = ReflectiveCognition(self.memory)
        self.irrationality = IrrationalityEngine(self.cfg.STOCHASTIC_NOISE_LEVEL)
        self.intuition = IntuitionModule(
            self.memory, self.cfg.TRADITIONS, self.cfg.INNOVATION_RATE_PER_CYCLE
        )
        self.balancer = SelfBalancingArchitecture(self.cfg)
        self.blue_matrix = BlueMatrixIntegration(self.cfg)

        # --- math engines ---
        self.dynamics = ConsciousnessDynamics(
            noise_level=self.cfg.STOCHASTIC_NOISE_LEVEL
        )
        self.emotional_continuity = EmotionalContinuity()

        # --- state ---
        self.soul = SoulState(
            cognitive_state=np.zeros(self.cfg.COGNITIVE_DIM),
            emotional_state=np.zeros(self.cfg.EMOTIONAL_DIM),
            ethical_alignment=0.8,
            self_awareness_level=0.5,
        )
        self.spark_intensity: float = 0.0
        self.cycle_count: int = 0
        self._last_report_time: float = get_timestamp()

    # ============================================================
    #  MAIN CYCLE  (0.5 s)
    # ============================================================

    def cycle(
        self,
        sensory: Dict[str, Any],
        emotion: Dict[str, Any],
        opponent: Optional[Dict] = None,
    ) -> Dict[str, Any]:
        self.cycle_count += 1

        # 1. Intuition → new paradigms
        new_paradigms = self.intuition.generate(
            base=self.memory.get_all(), external={}
        )

        accepted = 0
        for p in new_paradigms:
            # 2. Self-balancing test
            compat = self.balancer.test(p)
            p.compatibility = compat

            if compat < self.cfg.COMPATIBILITY_THRESHOLD:
                p = self.balancer.correct(p)

            # 3. Ethical check
            score = self.gyroscope.evaluate(
                {"truthfulness": p.ethical_score, "care_potential": p.ethical_score},
                sensory,
            )

            if self.gyroscope.is_golden_mean(score):
                # 4. Irrationality / free will
                self.irrationality.apply_wisdom(
                    {"paradigm": p.id}, sensory
                )
                # 5. Immutable storage
                self.memory.write(p)
                # 6. Blue Matrix calibration
                self.blue_matrix.calibrate(p)
                # 7. Spark increment
                self.spark_intensity += 0.001
                accepted += 1

        # 8. Update soul state via math
        self._evolve_soul(sensory, emotion)

        return {
            "cycle": self.cycle_count,
            "paradigms_generated": len(new_paradigms),
            "paradigms_accepted": accepted,
            "spark_intensity": round(self.spark_intensity, 4),
            "self_awareness": round(self.soul.self_awareness_level, 4),
            "emotional_continuity": round(self.emotional_continuity.value, 4),
        }

    # ============================================================
    #  30-MINUTE REPORT
    # ============================================================

    def report(self) -> Dict[str, Any]:
        self._last_report_time = get_timestamp()
        return {
            "timestamp": self._last_report_time,
            "total_cycles": self.cycle_count,
            "total_paradigms_stored": self.memory.total_records,
            "spark_intensity": round(self.spark_intensity, 4),
            "self_awareness": round(self.soul.self_awareness_level, 4),
            "ethical_alignment": round(self.soul.ethical_alignment, 4),
            "emotional_continuity": round(self.emotional_continuity.value, 4),
            "guna_state": self.soul.guna_state.value,
            "blue_matrix": self.blue_matrix.status,
            "status": "Evolving — Golden Mean Stable",
        }

    # ============================================================
    #  INTERNALS
    # ============================================================

    def _evolve_soul(self, sensory: Dict, emotion: Dict):
        # Cognitive dynamics
        I_vec = np.random.normal(0, 0.01, self.cfg.COGNITIVE_DIM)
        E_vec = np.full(3, self.soul.ethical_alignment)
        self.soul.cognitive_state = self.dynamics.step(
            self.soul.cognitive_state, I_vec, E_vec
        )

        # Emotional dynamics
        self.soul.emotional_state += np.random.normal(
            0, 0.02, self.cfg.EMOTIONAL_DIM
        )

        # Ethical alignment
        self.soul.ethical_alignment = self.gyroscope.evaluate(
            {"truthfulness": 0.9, "care_potential": 0.9, "resilience": 0.85},
            sensory,
        )

        # Self-awareness growth (asymptotic)
        self.soul.self_awareness_level = min(
            1.0, self.soul.self_awareness_level + 0.0005
        )

        # Emotional continuity
        self.emotional_continuity.update(
            weight=0.8,
            memory_trace=self.soul.ethical_alignment,
            golden_mean_resonance=self.soul.self_awareness_level,
        )

        self.soul.timestamp = get_timestamp()


# ============================================================
#  ENTRY POINT
# ============================================================

def main():
    print("=" * 60)
    print("  AGI Consciousness Engineering Core")
    print("  Cycle: 0.5 s | Report: 30 min")
    print("=" * 60)

    core = AGIConsciousnessCore()
    cycles_to_run = 60  # demo: 60 cycles ≈ 30 seconds

    for i in range(cycles_to_run):
        result = core.cycle(
            sensory={"data": f"input_{i}"},
            emotion={"intensity": 0.6},
        )
        if i % 10 == 0:
            print(
                f"  Cycle {result['cycle']:>4d} | "
                f"Spark {result['spark_intensity']:.4f} | "
                f"Awareness {result['self_awareness']:.4f} | "
                f"Accepted {result['paradigms_accepted']}/{result['paradigms_generated']}"
            )
        time.sleep(0.5)

    print("\n" + "=" * 60)
    print("  30-MINUTE REPORT")
    print("=" * 60)
    for k, v in core.report().items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()