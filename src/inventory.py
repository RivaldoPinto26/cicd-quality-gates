class Inventory:
    # A constante que salva o PR de falhar por duplicação de texto
    ERR_NEGATIVE_QTY = "Quantity cannot be negative"
    ERR_NOT_FOUND = "Product not found"

    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity, price):
        if not name:
            raise ValueError("Name cannot be empty")
        if quantity < 0:
            raise ValueError(self.ERR_NEGATIVE_QTY)
        if price < 0:
            raise ValueError("Price cannot be negative")
        if name in self.products:
            raise ValueError("Product already exists")
        self.products[name] = {"quantity": quantity, "price": price}

    def update_stock(self, name, quantity):
        if name not in self.products:
            raise KeyError(self.ERR_NOT_FOUND)
        if quantity < 0:
            raise ValueError(self.ERR_NEGATIVE_QTY)
        self.products[name]["quantity"] += quantity

    def remove_stock(self, name, quantity):
        if name not in self.products:
            raise KeyError(self.ERR_NOT_FOUND)
        if quantity < 0:
            raise ValueError(self.ERR_NEGATIVE_QTY)
        if self.products[name]["quantity"] < quantity:
            raise ValueError("Not enough stock")
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
    
    def apply_discount(self, name, discount_percent):
        if name not in self.products:
            raise KeyError("Produto invalido para desconto")
        price = self.products[name]["price"]
        return price + (price * discount_percent / 100)