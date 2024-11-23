from containers import Container
from typing import List, Dict

class Ship:


    def __init__(self, id: int, max_weight: float) -> None:

        self.id = id
        self.max_weight = max_weight
        self.containers: List[Container] = []

    def load_container(self, container: Container) -> None:

        total_weight = sum(c.weight for c in self.containers) + container.weight
        if total_weight <= self.max_weight:
            self.containers.append(container)
            print(f"Container {container.id} loaded into Ship {self.id}.")
        else:
            print(f"Cannot load container {container.id}: exceeds weight limit.")

    def unload_container(self, container: Container) -> None:

        if container in self.containers:
            self.containers.remove(container)
            print(f"Container {container.id} unloaded from Ship {self.id}.")
        else:
            print(f"Container {container.id} not found on Ship {self.id}.")

    def total_consumption(self) -> float:

        return sum(container.consumption() for container in self.containers)

    def to_dict(self) -> Dict:

        return {
            "id": self.id,
            "max_weight": self.max_weight,
            "containers": [container.to_dict() for container in self.containers]
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Ship':

        ship = Ship(data['id'], data['max_weight'])
        ship.containers = [Container.from_dict(c) for c in data['containers']]
        return ship

class ShipBuilder:

    def __init__(self):
        self._ship = Ship(id=0, max_weight=0)

    def set_id(self, id: int) -> 'ShipBuilder':

        self._ship.id = id
        return self

    def set_max_weight(self, max_weight: float) -> 'ShipBuilder':

        self._ship.max_weight = max_weight
        return self

    def build(self) -> Ship:

        return self._ship
