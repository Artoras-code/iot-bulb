from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Reading:
    temperature: float  # °C
    humidity: float     # %


class Sensor(ABC):
    @abstractmethod
    def read(self) -> Reading: ...

    def close(self) -> None:
        pass