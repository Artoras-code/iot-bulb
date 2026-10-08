from .base import Bulb


class TuyaBulb(Bulb):
    def __init__(self, device_id: str, ip: str, local_key: str, version: float):
        import tinytuya

        if not (device_id and ip and local_key):
            raise ValueError("Faltan TUYA_DEVICE_ID, TUYA_IP o TUYA_LOCAL_KEY en .env")

        self._dev = tinytuya.BulbDevice(device_id, ip, local_key)
        self._dev.set_version(version)
        self._dev.set_socketPersistent(True)

        status = self._dev.status()
        if "Error" in status:
            raise ConnectionError(f"No se pudo conectar a la ampolleta: {status}")

        self._dev.turn_on()

    def set_rgb(self, r: int, g: int, b: int) -> None:
        result = self._dev.set_colour(r, g, b)
        if isinstance(result, dict) and "Error" in result:
            raise ConnectionError(f"Error al enviar color: {result}")

    def close(self) -> None:
        try:
            self._dev.close()
        except Exception:
            pass