from metro_cars import MetroCar
from typing import List, Dict
from typing import Protocol


class ITrain(Protocol):
    """Interface for train operations.

    This interface defines the methods that any train class must implement
    to attach and detach metro cars.
    """
    def attach_car(self, car: MetroCar) -> None:
        """Attach a metro car to the train.

        Args:
            car (MetroCar): The metro car to be attached.
        """
        pass

    def detach_car(self, car: MetroCar) -> None:
        """Detach a metro car from the train.

        Args:
            car (MetroCar): The metro car to be detached.
        """
        pass


class Train:
    """Class representing a train.

    Attributes:
        id (int): The unique identifier of the train.
        max_weight (float): The maximum weight capacity of the train.
        cars (List[MetroCar]): A list of metro cars currently attached to the train.
    """

    def __init__(self, id: int, max_weight: float) -> None:
        """Initialize a Train instance.

        Args:
            id (int): The unique identifier of the train.
            max_weight (float): The maximum weight capacity of the train.
        """
        self.id = id
        self.max_weight = max_weight
        self.cars: List[MetroCar] = []

    def add_car(self, car: MetroCar) -> None:
        """Attach a metro car to the train.

        Args:
            car (MetroCar): The metro car to be attached.

        Prints:
            A message indicating whether the car was attached or if
            it exceeds the weight limit.
        """
        total_weight = sum(c.weight for c in self.cars) + car.weight
        if total_weight <= self.max_weight:
            self.cars.append(car)
            print(f"Metro car {car.id} attached to Train {self.id}.")
        else:
            print(f"Cannot attach metro car {car.id} to Train {self.id}: exceeds weight limit.")

    def remove_car(self, car: MetroCar) -> None:
        """Detach a metro car from the train.

        Args:
            car (MetroCar): The metro car to be detached.

        Prints:
            A message indicating whether the car was successfully detached
            or if it was not found on the train.
        """
        if car in self.cars:
            self.cars.remove(car)
            print(f"Metro car {car.id} detached from Train {self.id}.")
        else:
            print(f"Metro car {car.id} not found on Train {self.id}.")

    def total_energy_consumption(self) -> float:
        """Calculate the total energy consumption of the train.

        Returns:
            float: The total energy consumption based on the metro cars on board.
        """
        return sum(car.energy_consumption() for car in self.cars)

    def to_dict(self) -> Dict:
        """Convert the Train instance to a dictionary representation.

        Returns:
            Dict: A dictionary containing the train's attributes.
        """
        return {
            "id": self.id,
            "max_weight": self.max_weight,
            "cars": [car.to_dict() for car in self.cars]
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Train':
        """Create a Train instance from a dictionary representation.

        Args:
            data (Dict): A dictionary containing train attributes.

        Returns:
            Train: A new Train instance populated with data from the dictionary.
        """
        train = Train(data['id'], data['max_weight'])
        train.cars = [MetroCar.from_dict(c) for c in data['cars']]
        return train
