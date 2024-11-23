import json
from typing import Protocol, Any, Tuple, List, Dict
from metro_cars import MetroCar


class IDepot(Protocol):
    """Interface for depot operations.

    This interface defines the methods that any depot class must implement
    to manage incoming and outgoing metro trains.
    """
    def incoming_train(self, train: Any) -> None:
        """Register an incoming train at the depot.

        Args:
            train (Any): The train that is arriving at the depot.
        """
        pass

    def outgoing_train(self, train: Any) -> None:
        """Register an outgoing train from the depot.

        Args:
            train (Any): The train that is leaving the depot.
        """
        pass


class Depot(IDepot):
    """Class representing a metro depot.

    Attributes:
        id (int): The unique identifier of the depot.
        coordinates (Tuple[float, float]): The geographical coordinates of the depot.
        cars (List[MetroCar]): A list of metro cars currently in the depot.
        trains (List[Any]): A list of trains currently at the depot.
        history (List[Any]): A list of trains that have previously been in the depot.
    """

    def __init__(self, id: int, coordinates: Tuple[float, float]) -> None:
        """Initialize a Depot instance.

        Args:
            id (int): The unique identifier of the depot.
            coordinates (Tuple[float, float]): The geographical coordinates of the depot.
        """
        self.id = id
        self.coordinates: Tuple[float, float] = coordinates
        self.cars: List[MetroCar] = []
        self.trains: List[Any] = []  # Список поточних поїздів
        self.history: List[Any] = []  # Список поїздів, що вже були в депо

    def incoming_train(self, train: Any) -> None:
        """Register an incoming train at the depot.

        Args:
            train (Any): The train that is arriving at the depot.

        Prints:
            A message indicating the arrival of the train.
        """
        self.trains.append(train)
        print(f"Train {train.id} has arrived at Depot {self.id}.")

    def outgoing_train(self, train: Any) -> None:
        """Register an outgoing train from the depot.

        Args:
            train (Any): The train that is leaving the depot.

        Prints:
            A message indicating the departure of the train or if the train was
            not found in the depot.
        """
        if train in self.trains:
            self.trains.remove(train)
            self.history.append(train)
            print(f"Train {train.id} has left Depot {self.id}.")
        else:
            print(f"Train {train.id} is not in Depot {self.id}.")

    def to_dict(self) -> Dict:
        """Convert the Depot instance to a dictionary representation.

        Returns:
            Dict: A dictionary containing the depot's attributes.
        """
        return {
            "id": self.id,
            "coordinates": self.coordinates,
            "cars": [car.to_dict() for car in self.cars],
            "trains": [train.to_dict() for train in self.trains],
            "history": [train.to_dict() for train in self.history],
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Depot':
        """Create a Depot instance from a dictionary representation.

        Args:
            data (Dict): A dictionary containing depot attributes.

        Returns:
            Depot: A new Depot instance populated with data from the dictionary.
        """
        depot = Depot(data['id'], tuple(data['coordinates']))
        # Set cars and trains if present
        return depot

    def save_to_json(self, filename: str) -> None:
        """Save the depot data to a JSON file.

        Args:
            filename (str): The name of the file to save the depot data.
        """
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @staticmethod
    def load_from_json(filename: str) -> 'Depot':
        """Load a Depot instance from a JSON file.

        Args:
            filename (str): The name of the file to load the depot data from.

        Returns:
            Depot: A Depot instance populated with data from the JSON file.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        return Depot.from_dict(data)
