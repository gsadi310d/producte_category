class Product:
    name: str
    description: str
    price: float
    quantity: list

    def __init__(self, name, description, price, quantity=None):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity if quantity else []
