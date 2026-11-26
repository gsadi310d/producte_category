class Category:
    name: str
    description: str
    products: list

    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.product_count += len(products) if products else 0
        Category.category_count += 1
