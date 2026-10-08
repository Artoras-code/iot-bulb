import os

from dotenv import load_dotenv

load_dotenv()


def _flag(name: str, default: str = "1") -> bool:
    return os.getenv(name, default).strip() == "1"


SIMULATE_SENSOR = _flag("SIMULATE_SENSOR")
SIMULATE_BULB = _flag("SIMULATE_BULB")

DHT_GPIO = int(os.getenv("DHT_GPIO", "4"))
INTERVAL_SECONDS = float(os.getenv("INTERVAL_SECONDS", "5"))
COLOR_MODE = os.getenv("COLOR_MODE", "temperature")  # temperature | humidity

TUYA_DEVICE_ID = os.getenv("TUYA_DEVICE_ID", "")
TUYA_LOCAL_KEY = os.getenv("TUYA_LOCAL_KEY", "")
TUYA_IP = os.getenv("TUYA_IP", "")
TUYA_VERSION = float(os.getenv("TUYA_VERSION", "3.3"))

# Rangos para el mapeo a color
TEMP_MIN, TEMP_MAX = 15.0, 32.0  # °C: azul -> rojo
HUM_MIN, HUM_MAX = 20.0, 80.0    # %:  naranja -> azul

# Diferencia mínima de color para reenviar a la ampolleta
MIN_RGB_DELTA = 12