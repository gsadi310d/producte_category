import json
from pathlib import Path
from typing import Any

from src.category import Category
from src.product import Product

BASE_DIR = Path(__file__).resolve().parent.parent


def read_json(path: str) -> Any:
    full_path = Path(path)
    if not full_path.is_absolute():
        full_path = BASE_DIR / full_path
    with open(full_path, "r", encoding="UTF-8") as file:
        return json.load(file)


def create_objects_from_json(data: list[dict]) -> list[Category]:
    categories = []
    for category_data in data:
        products = [Product(**product) for product in category_data["products"]]
        categories.append(Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        ))
    return categories
