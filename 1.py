class Item:
    def __init__(self, name, price, quantity=0):

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


print(Item('phone', 18000, 5))

print(Item(18000, 'phone', 5))
# TypeError: Название товара должно быть строкой.

print(Item('phone', '18000', 5))
# TypeError: Цена товара должна быть числом.

print(Item('phone', 18000, 5.5))
# TypeError: Количество товара должно быть целым числом.