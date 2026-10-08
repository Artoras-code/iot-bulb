from .base import Bulb


class FakeBulb(Bulb):
    def set_rgb(self, r: int, g: int, b: int) -> None:
        # Bloque de color en terminales con soporte truecolor
        print(f"  \033[48;2;{r};{g};{b}m      \033[0m  RGB=({r}, {g}, {b})")