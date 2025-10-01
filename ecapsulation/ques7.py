class Laptop:
    def __init__(self, price):
        self.__price = price

    def set_price(self, p):
        if p > 0:
            self.__price = p
        else:
            print("Invalid price")

    def get_price(self):
        return self.__price

l = Laptop(50000)
print("Price:", l.get_price())
l.set_price(55000)
print("Updated Price:", l.get_price())
