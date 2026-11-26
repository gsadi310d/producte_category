import pytest
import json

from src.category import Category
from src.product import Product


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
def product_fore():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def product_five():
    return Product(
        name="LG",
        description="55\" QLED 4K, Фоновая подсветка",
        price=123000.0,
        quantity=7,
    )


@pytest.fixture
def category_first(product_five):
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром,"
                    + " станет вашим другом и помощником",
        products=[product_five],
    )


@pytest.fixture
def category_second(product_first, product_second, product_three, product_fore):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации,"
                    + " но и получения дополнительных функций для удобства жизни",
        products=[product_first, product_second, product_three, product_fore],
    )


""" Данные для тестов JSON """


@pytest.fixture
def sample_data():
    """Корректная структура данных: список категорий с товарами."""
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны для связи и задач",
            "products": [
                {
                    "name": "Samsung Galaxy S23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [
                {
                    "name": '55" QLED 4K',
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7,
                },
            ],
        },
    ]


@pytest.fixture
def sample_json_file(tmp_path, sample_data):
    """Временный файл с корректными данными.

    Используем tmp_path (встроенная фикстура pytest): она даёт уникальную
    временную папку для каждого теста, файлы не конфликтуют между тестами.
    """
    file_path = tmp_path / "products.json"
    file_path.write_text(
        json.dumps(sample_data, ensure_ascii=False),
        encoding="UTF-8",
    )
    return file_path


@pytest.fixture(autouse=True)
def reset_counters():
    """Сброс классовых счётчиков перед каждым тестом.

    category_count и product_count — атрибуты класса, они накапливаются
    между тестами в одной сессии pytest. Сброс делает проверки
    на финальные значения детерминированными.
    """
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0
