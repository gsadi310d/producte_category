import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def product_first():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def product_second():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
    )


@pytest.fixture
def product_three():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )

@pytest.fixture
def category_first():
    return Category(
        name=,
        description=,
        products=,
    )

product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)

@pytest.fixture
def category_second():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=,
    )
    category1 = Category("Смартфоны",
                         ",
                         [product1, product2, product3])

    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])