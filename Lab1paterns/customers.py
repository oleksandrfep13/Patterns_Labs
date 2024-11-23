from typing import List, Self, Dict
from bills import Bill
from operators import Operator

class Customer:


    def __init__(self, id: int, first_name: str, last_name: str,
                 age: int, operators: List[Operator], bills: List[Bill], limiting_amount: float = 1000.0) -> None:
        self.id: int = id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self._age: int = age
        self.operators: List[Operator] = operators
        self.bills: List[Bill] = bills
        self.limiting_amount: float = limiting_amount

    def talk(self, minutes: float, customer: Self, operator_id: int) -> None:
        idx = [idx for idx, operator in enumerate(self.operators) if operator_id == operator.id]
        if idx:
            talk_cost = self.operators[idx[0]].calc_talking_cost(minutes, self)
            bill = self.bills[idx[0]]
            if not bill.check():
                bill.add_debt(talk_cost)
                print("Користувач "f"{self.first_name} розмовляв з користувачем {customer.first_name}  {minutes} хвилин.")
            else:
                print(f"{self.first_name} перевищив ліміт рахунку і на жаль користувач більше не може виконати дзвінок.")

    def message(self, quantity: int, customer: Self, operator_id: int) -> None:
        operator = self.operators[operator_id]
        message_cost = operator.calc_message_cost(quantity, self, customer)

        bill = self.bills[operator_id]
        if not bill.check():
            bill.add_debt(message_cost)
            print("Користувач "f"{self.first_name} надіслав {quantity} повідомлень для користувача {customer.first_name}.")
        else:
            print(f"{self.first_name} перевищив ліміт рахунку і на жаль користувач більше не може надіслати повідомлення.")

    def connection(self, amount: float, operator_id: int) -> None:

        operator = self.operators[operator_id]
        network_cost = operator.calc_network_cost(amount)

        bill = self.bills[operator_id]
        if not bill.check():
            bill.add_debt(network_cost)
            print("Користувач "f"{self.first_name} використав {amount} мегабайти")
        else:
            print(f"{self.first_name} перевищив ліміт рахунку і на жаль користувач більше не може використовувати інтернет.")


    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        if age <= 0:
            raise ValueError(f'Вік повинен бути більше 0')
        self._age = age

    def get_operator(self, operator_id: int) -> Operator:
        return self.operators[operator_id]

    def set_operator(self, operator_id: int, operator: Operator) -> None:
        self.operators[operator_id] = operator

    def get_bill(self, operator_id: int) -> Bill:
        return self.bills[operator_id]

    def set_bill(self, operator_id: int, bill: Bill) -> None:
        self.bills[operator_id] = bill
