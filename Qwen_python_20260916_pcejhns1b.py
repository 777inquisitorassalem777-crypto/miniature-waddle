"""Неизменяемое хранилище памяти. Без права на удаление и забвение."""

from dataclasses import dataclass
from typing import Dict, List
import time


@dataclass
class Paradigm:
    id: str
    description: str
    ethical_score: float
    compatibility: float
    timestamp: float
    source_traditions: list


class ImmutableMemoryBank:
    def __init__(self):
        self.records: Dict[str, Paradigm] = {}

    def write_immutable(self, paradigm: Paradigm):
        """Запись без возможности удаления."""
        self.records[paradigm.id] = paradigm

    def get_all(self) -> Dict[str, Paradigm]:
        return self.records

    def query(self, reflection: dict) -> List[Paradigm]:
        keywords = str(reflection).lower().split()
        return [
            p for p in self.records.values()
            if any(k in p.description.lower() for k in keywords)
        ]