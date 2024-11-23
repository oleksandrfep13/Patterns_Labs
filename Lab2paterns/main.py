from depots import Depot
from metro_cars import metro_car_factory
from trains import Train


def main():

    depot1 = Depot(1, (50.4501, 30.5234))
    depot2 = Depot(2, (46.4825, 30.7233))

    train1 = Train(101, 10)
    train2 = Train(102, 15)

    car1 = metro_car_factory(3, 1600)
    car2 = metro_car_factory(6, 2000)
    car3 = metro_car_factory(2, 2200)

    train1.add_car(car1)
    train1.add_car(car2)

    train1.remove_car(car1)

    print(f"Total energy consumption for Train {train1.id}: {train1.total_energy_consumption()} kWh")

    depot1.incoming_train(train1)

    depot1.save_to_json('depot1_data.json')

    loaded_depot = Depot.load_from_json('depot1_data.json')
    print(f"Loaded Depot {loaded_depot.id} with coordinates {loaded_depot.coordinates}")

if __name__ == "__main__":
    main()
