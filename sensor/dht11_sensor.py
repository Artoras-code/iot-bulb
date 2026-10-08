import time

from .base import Reading, Sensor


class DHT11Sensor(Sensor):
    def __init__(self, gpio_pin: int, retries: int = 5):
        import adafruit_dht
        import board

        self._retries = retries
        self._dev = adafruit_dht.DHT11(getattr(board, f"D{gpio_pin}"))

    def read(self) -> Reading:
        last_error = None
        for _ in range(self._retries):
            try:
                t = self._dev.temperature
                h = self._dev.humidity
                if t is not None and h is not None:
                    return Reading(float(t), float(h))
            except RuntimeError as e:  # lecturas fallidas son normales en el DHT11
                last_error = e
            time.sleep(2)
        raise RuntimeError(f"No se pudo leer el DHT11: {last_error}")

    def close(self) -> None:
        self._dev.exit()