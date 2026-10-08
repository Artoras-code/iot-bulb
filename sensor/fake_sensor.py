import math
import random
import time

from .base import Reading, Sensor


class FakeSensor(Sensor):
    """Onda lenta que recorre todo el rango de temperatura y humedad."""

    def __init__(self):
        self._t0 = time.time()

    def read(self) -> Reading:
        x = (time.time() - self._t0) / 20.0
        temp = 23.5 + 9.0 * math.sin(x) + random.uniform(-0.3, 0.3)
        hum = 50.0 + 30.0 * math.sin(x * 0.7 + 1) + random.uniform(-1, 1)
        return Reading(round(temp, 1), round(hum, 1))