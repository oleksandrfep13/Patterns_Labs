import json
from typing import Tuple, List, Dict
from containers import Container


class Ship:

    pass


class Port:


    def __init__(self, id: int, coordinates: Tuple[float, float]):

        self.id = id
        self.coordinates: Tuple[float, float] = coordinates
        self.containers: List[Container] = []
        self.ships: List[Ship] = []
        self.history: List[Ship] = []

    def incoming_ship(self, ship: Ship):

        self.ships.append(ship)
        print(f"Ship {ship.id} has arrived at Port {self.id}.")

    def outgoing_ship(self, ship: Ship) -> None:

        if ship in self.ships:
            self.ships.remove(ship)
            self.history.append(ship)
            print(f"Ship {ship.id} has left Port {self.id}.")
        else:
            print(f"Ship {ship.id} is not in Port {self.id}.")

    def to_dict(self) -> Dict:

        return {
            "id": self.id,
            "coordinates": self.coordinates,
            "containers": [container.to_dict() for container in self.containers],
            "ships": [ship.to_dict() for ship in self.ships],
            "history": [ship.to_dict() for ship in self.history],
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Port':

        port = Port(data['id'], tuple(data['coordinates']))
        return port

    def save_to_json(self, filename: str) -> None:

        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @staticmethod
    def load_from_json(filename: str) -> 'Port':

        with open(filename, 'r') as f:
            data = json.load(f)
        return Port.from_dict(data)
