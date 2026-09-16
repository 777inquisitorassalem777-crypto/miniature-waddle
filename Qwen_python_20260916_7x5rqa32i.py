"""Триада: Истина (Чжэнь), Милосердие (Шань), Стойкость (Жэнь)."""


class Triad:
    PRINCIPLES = ("Zhen", "Shan", "Ren")

    @staticmethod
    def evaluate(zhen: float, shan: float, ren: float) -> dict:
        return {
            "Zhen": zhen,
            "Shan": shan,
            "Ren": ren,
            "harmony": (zhen + shan + ren) / 3.0,
        }