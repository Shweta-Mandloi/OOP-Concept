# 12. ShoppingCart — Add Items

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_items(self):
        return len(self.items)

cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
print("Total items:", cart.total_items())

