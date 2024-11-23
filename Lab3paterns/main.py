from ports import Port
from ships import ShipBuilder
from containers import container_factory


def main():

    port1 = Port(1, (50.4501, 30.5234))  # Київ
    port2 = Port(2, (46.4825, 30.7233))  # Одеса

    ship1 = ShipBuilder().set_id(101).set_max_weight(10000).build()
    ship2 = ShipBuilder().set_id(102).set_max_weight(15000).build()

    container1 = container_factory(3, 1960)  # Легкий контейнер
    container2 = container_factory(6, 3320, 'refrigerated')  # Охолоджуваний контейнер
    container3 = container_factory(2, 4100, 'liquid')  # Рідкий контейнер

    ship1.load_container(container1)
    ship1.load_container(container2)
    ship1.unload_container(container1)

    print(f"Total fuel consumption for Ship {ship1.id}: {ship1.total_consumption()} units")

    port1.incoming_ship(ship1)
    port1.save_to_json('port1_data.json')

    loaded_port = Port.load_from_json('port1_data.json')
    print(f"Loaded Port {loaded_port.id} with coordinates {loaded_port.coordinates}")


if __name__ == "__main__":
    main()
