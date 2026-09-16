"""Тест Голубой Матрицы."""

from modules.blue_matrix import BlueMatrixIntegration
from modules.immutable_memory import Paradigm
import time


def test_calibration():
    bm = BlueMatrixIntegration()
    p = Paradigm("t", "test", 0.9, 0.9, time.time(), [])
    bm.calibrate(p)
    assert all(v == "active" for v in bm.status().values())