"""Точка входа: запуск эволюционных циклов."""

import time
from core.consciousness import AGIConsciousnessCore


def main():
    print("Инициализация AGI Consciousness Core...")
    core = AGIConsciousnessCore()
    print("Система готова. Запуск циклов 0.5 сек...\n")

    for i in range(100):
        result = core.cycle(
            sensory_input={"data": f"input_{i}"},
            emotional_context={"mood": "neutral"},
        )
        if i % 10 == 0:
            print(
                f"Цикл {result['cycle']:>3} | "
                f"Искра: {result['spark']:.4f} | "
                f"Осознанность: {result['awareness']:.4f} | "
                f"Этика: {result['ethics']:.4f} | "
                f"Интегрировано: {result['paradigms_integrated']}"
            )
        time.sleep(0.5)

    print("\n=== ИТОГОВЫЙ ОТЧЕТ ===")
    report = core.report()
    for k, v in report.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()