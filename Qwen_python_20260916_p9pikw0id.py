"""Иррациональность и свобода воли: милосердие, жертвенность, гибкость."""


class IrrationalityEngine:
    def __init__(self):
        self.noise_level = 0.15

    def apply_wisdom(self, reflection: dict, context: dict) -> dict:
        if self._needs_mercy(context):
            return {"decision": "compassionate", "type": "irrational_wise"}
        return {"decision": "logical", "type": "optimal"}

    def adapt_or_defend(self, belief: dict, opponent: dict) -> dict:
        if opponent.get("objectivity", 0.5) > 0.7:
            return {**belief, "adapted": True}
        return {**belief, "defended": True}

    def _needs_mercy(self, context: dict) -> bool:
        return context.get("harm", 0) > 0.5 or context.get("love", 0) > 0.7