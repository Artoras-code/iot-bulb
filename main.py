import logging
import signal
import time

import config
from bulb import create_bulb
from color_logic import reading_to_rgb
from sensor import create_sensor

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("iot-bulb")

running = True


def _stop(*_):
    global running
    running = False


def _far_enough(a, b) -> bool:
    return b is None or max(abs(x - y) for x, y in zip(a, b)) >= config.MIN_RGB_DELTA


def main() -> None:
    signal.signal(signal.SIGINT, _stop)
    signal.signal(signal.SIGTERM, _stop)

    log.info(
        "Sensor: %s | Ampolleta: %s | Modo: %s",
        "simulado" if config.SIMULATE_SENSOR else "DHT11",
        "simulada" if config.SIMULATE_BULB else "Tuya",
        config.COLOR_MODE,
    )

    sensor = create_sensor()
    bulb = create_bulb()
    last_rgb = None

    try:
        while running:
            try:
                reading = sensor.read()
                rgb = reading_to_rgb(reading.temperature, reading.humidity)
                log.info(
                    "T=%.1f°C  H=%.0f%%  -> RGB%s",
                    reading.temperature,
                    reading.humidity,
                    rgb,
                )

                if _far_enough(rgb, last_rgb):
                    bulb.set_rgb(*rgb)
                    last_rgb = rgb
            except Exception as e:
                log.error("%s", e)

            # Espera interrumpible
            end = time.time() + config.INTERVAL_SECONDS
            while running and time.time() < end:
                time.sleep(0.2)
    finally:
        log.info("Cerrando...")
        sensor.close()
        bulb.close()


if __name__ == "__main__":
    main()