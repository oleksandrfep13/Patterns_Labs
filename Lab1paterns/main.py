from customers import Customer
from operators import Operator
from bills import Bill


def main():
    operators = [Operator(0, 0.6, 0.1, 0.1, 10), Operator(1, 0.6, 0.2, 0.25, 5)]

    bills = [Bill(1000), Bill(500), Bill(700), Bill(1200)]

    customers = [
        Customer(0, 'Олексій', 'Лачен', 21, operators, bills[:2]),
        Customer(1, 'Миколай', 'Оберенко', 18, operators, bills[1:3]),
        Customer(2, 'Світлана', 'Ковальчук', 25, operators, bills[2:]),
        Customer(3, 'Іван', 'Гриценко', 30, operators, bills[:1]),
    ]

    customers[0].talk(10, customers[1], 0)
    customers[2].message(15, customers[3], 1)

    customers[0].connection(163, 0)
    customers[0].get_bill(0).pay(20)
    customers[0].get_bill(0).change_limit(10)


if __name__ == "__main__":
    main()
