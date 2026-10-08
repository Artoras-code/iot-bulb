import config

from .base import Reading, Sensor


def create_sensor() -> Sensor:
    if config.SIMULATE_SENSOR:
        from .fake_sensor import FakeSensor
        return FakeSensor()
    from .dht11_sensor import DHT11Sensor
    return DHT11Sensor(config.DHT_GPIO)


__all__ = ["Reading", "Sensor", "create_sensor"]