from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customers import Customer


class Operator:

    def __init__(self, id: int, talking_charge: float, message_cost: float,
                 network_charge: float, discount_rate: int) -> None:

        self.id = id
        self.talking_charge: float = talking_charge
        self.message_cost: float = message_cost
        self.network_charge: float = network_charge
        self.discount_rate: int = discount_rate

    def calc_talking_cost(self, minutes: float, customer: 'Customer') -> float:

        cost = self.talking_charge * minutes
        if customer.age < 18 or customer.age > 65:
            discount = cost * (self.discount_rate / 100)
            cost -= discount
        print(f"Дзвінок тривав {minutes} хвилин, що буде коштувати {cost}")
        return cost

    def calc_message_cost(self, quantity: int, customer: 'Customer', other: 'Customer') -> float:

        cost = self.message_cost * quantity
        if self.id == other.operators[self.id].id:
            discount = cost * (self.discount_rate / 100)
            cost -= discount
        print(f"Надсилає {quantity} повідомлень, що буде коштувати {cost}")
        return cost

    def calc_network_cost(self, amount: float) -> float:

        cost = self.network_charge * amount
        print(f"Використані {amount} MB інтернету будуть коштувати - {cost}")
        return cost


    def get_talking_charge(self) -> float:
        return self.talking_charge

    def set_talking_charge(self, charge: float) -> None:
        self.talking_charge = charge

    def get_message_cost(self) -> float:
        return self.message_cost

    def set_message_cost(self, cost: float) -> None:
        self.message_cost = cost

    def get_network_charge(self) -> float:
        return self.network_charge

    def set_network_charge(self, charge: float) -> None:
        self.network_charge = charge

    def get_discount_rate(self) -> int:
        return self.discount_rate

    def set_discount_rate(self, rate: int) -> None:
        self.discount_rate = rate
