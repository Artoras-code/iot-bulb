import config

from .base import Bulb


def create_bulb() -> Bulb:
    if config.SIMULATE_BULB:
        from .fake_bulb import FakeBulb
        return FakeBulb()
    from .tuya_bulb import TuyaBulb
    return TuyaBulb(
        config.TUYA_DEVICE_ID,
        config.TUYA_IP,
        config.TUYA_LOCAL_KEY,
        config.TUYA_VERSION,
    )


__all__ = ["Bulb", "create_bulb"]