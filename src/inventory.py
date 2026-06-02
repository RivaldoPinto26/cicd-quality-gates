class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity, price):
        if not name:
            raise ValueError("Name cannot be empty")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if name in self.products:
            raise Exception("Product already exists")

        self.products[name] = {
            "quantity": quantity,
            "price": price
        }

    def update_stock(self, name, quantity):
        if name not in self.products:
            raise Exception("Product not found")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.products[name]["quantity"] += quantity

    def remove_stock(self, name, quantity):
        if name not in self.products:
            raise Exception("Product not found")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if self.products[name]["quantity"] < quantity:
            raise Exception("Not enough stock")

        self.products[name]["quantity"] -= quantity

    def get_low_stock(self, threshold=5):
        return {
            name: data
            for name, data in self.products.items()
            if data["quantity"] < threshold
        }

    def get_total_value(self):
        return sum(
            data["quantity"] * data["price"]
            for data in self.products.values()
        )

    # Função duplicada #1
    def get_total_value_detailed(self):
        total_value = 0
        for name, data in self.products.items():
            quantity = data["quantity"]
            price = data["price"]
            item_total = quantity * price
            total_value += item_total
        return total_value

    # Função duplicada #2
    def get_total_value_duplicate(self):
        total_value = 0
        for name, data in self.products.items():
            quantity = data["quantity"]
            price = data["price"]
            item_total = quantity * price
            total_value += item_total
        return total_value