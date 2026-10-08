import colorsys

import config


def _clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def _hsv_to_rgb(hue_deg: float) -> tuple[int, int, int]:
    r, g, b = colorsys.hsv_to_rgb(hue_deg / 360.0, 1.0, 1.0)
    return int(r * 255), int(g * 255), int(b * 255)


def temperature_to_rgb(temp_c: float) -> tuple[int, int, int]:
    """Frío = azul (240°), templado = verde (120°), caliente = rojo (0°)."""
    t = _clamp01((temp_c - config.TEMP_MIN) / (config.TEMP_MAX - config.TEMP_MIN))
    return _hsv_to_rgb(240.0 * (1.0 - t))


def humidity_to_rgb(hum: float) -> tuple[int, int, int]:
    """Seco = naranja (30°), húmedo = azul (240°)."""
    h = _clamp01((hum - config.HUM_MIN) / (config.HUM_MAX - config.HUM_MIN))
    return _hsv_to_rgb(30.0 + 210.0 * h)


def reading_to_rgb(temp_c: float, hum: float) -> tuple[int, int, int]:
    if config.COLOR_MODE == "humidity":
        return humidity_to_rgb(hum)
    return temperature_to_rgb(temp_c)