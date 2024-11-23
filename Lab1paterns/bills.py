class Bill:


    def __init__(self, limiting_amount: float):

        self.limiting_amount: float = limiting_amount
        self.current_debt: float = 0.0

    def check(self) -> bool:

        return self.current_debt >= self.limiting_amount

    def add_debt(self, debt: float) -> None:

        tentative_debt = debt + self.current_debt
        if tentative_debt <= self.limiting_amount:
            self.current_debt += debt
        else:
            print(f"Ви перевищили ліміт і тепер ваш борг буде дорівнювати {tentative_debt}")

    def pay(self, amount: float) -> None:

        self.current_debt -= amount
        if self.current_debt < 0:
            self.limiting_amount += abs(self.current_debt)
            self.current_debt = 0
        print(f"Сплачено: {amount}.| Заборгованість: {self.current_debt}")

    def change_limit(self, amount: float) -> None:

        self.limiting_amount += amount
        print(f"Ліміт успішно змінено. Новий ліміт становить  {self.limiting_amount}")

    def get_limiting_amount(self) -> float:

        return self.limiting_amount

    def get_current_debt(self) -> float:

        return self.current_debt
