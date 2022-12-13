class Item:
    def __init__(self, name, price, quantity):

        self.__check(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def __check(name, price, quantity):
        if not isinstance(name, str):
            raise TypeError("Название товара должно быть строкой")

        if not isinstance(price, (int, float)):
            raise TypeError("Цена товара должна быть числом")

        if not isinstance(quantity, int):
            raise TypeError("Количество товара должно быть целым числом")

    def __str__(self):
        return f'{self.name} {self.price} {self.quantity}'


class Phone(Item):

    def __init__(self, name, price, quantity, broken_phones):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones


print(Phone("iPhone 10", 500, 5, 1))