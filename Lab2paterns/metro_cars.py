from abc import ABC, abstractmethod
from typing import Dict, Self


class MetroCar(ABC):


    def __init__(self, id: int, weight: float) -> None:

        self.id = id
        self.weight = weight

    @abstractmethod
    def energy_consumption(self) -> float:

          pass

    def __eq__(self, other: Self) -> bool:

        return (self.__class__.__name__ == other.__class__.__name__ and
                self.weight == other.weight)

    def to_dict(self) -> Dict:

        return {
            "type": self.__class__.__name__,
            "id": self.id,
            "weight": self.weight
        }

    @staticmethod
    def from_dict(data: Dict) -> 'MetroCar':

        if data["type"] == "StandardMetroCar":
            return StandardMetroCar(data['id'], data['weight'])
        elif data["type"] == "HeavyMetroCar":
            return HeavyMetroCar(data['id'], data['weight'])
        else:
            raise ValueError("Unknown metro car type")


class StandardMetroCar(MetroCar):


    UNIT_CONSUMPTION = 1.8

    def __init__(self, id: int, weight: float) -> None:
        super().__init__(id, weight)

    def energy_consumption(self) -> float:

        return StandardMetroCar.UNIT_CONSUMPTION * self.weight


class HeavyMetroCar(MetroCar):


    UNIT_CONSUMPTION = 2.4

    def __init__(self, id: int, weight: float) -> None:

        super().__init__(id, weight)

    def energy_consumption(self) -> float:

        return HeavyMetroCar.UNIT_CONSUMPTION * self.weight


def metro_car_factory(id: int, weight: float) -> MetroCar:

    if weight <= 4000:
        return StandardMetroCar(id, weight)
    else:
        return HeavyMetroCar(id, weight)
