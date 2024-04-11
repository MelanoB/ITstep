class ShoppingCart:
    def __init__(self):
        self.total = 0
        self.items = {}

    def add(self, item, quantity):
        self.total += quantity * produce_price[item]
        self.items.update({item: quantity})

    def remove(self, item, quantity):
        if quantity < self.items[item]:
            self.total -= quantity * produce_price[item]
        else:
            del self.items[item]

        self.items[item] = self.items[item] - quantity

    def current_items(self):
        return self.items

    def calculate_total(self):
        return f"ჯამი: {self.total} ლარი"


produce_price = {"puri": 2, "karaqi": 5, "wyali": 1, "zeti": 10}

cart = ShoppingCart()
cart.add("puri", 3)
cart.add("karaqi", 1)
cart.add("wyali", 4)
cart.add("zeti", 2)
print(cart.current_items())
print(cart.calculate_total())

cart.remove("zeti", 1)
print(cart.current_items())
print(cart.calculate_total())

