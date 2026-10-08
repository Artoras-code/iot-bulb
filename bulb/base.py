from abc import ABC, abstractmethod


class Bulb(ABC):
    @abstractmethod
    def set_rgb(self, r: int, g: int, b: int) -> None: ...

    def close(self) -> None:
        pass