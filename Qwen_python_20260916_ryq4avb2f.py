"""Utility helpers."""

import time
import uuid


def generate_id(prefix: str = "paradigm") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def get_timestamp() -> float:
    return time.time()