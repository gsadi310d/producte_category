import pytest
import json

from src.utils import read_json, create_objects_from_json
from src.category import Category
from src.product import Product


""" Тесты read_json """


class TestReadJson:
    """Проверки функции read_json."""

    def test_reads_absolute_path(self, sample_json_file, sample_data):
        """Абсолютный путь используется как есть: содержимое файла совпадает с исходным."""
        result = read_json(str(sample_json_file))

        assert result == sample_data

    def test_reads_relative_path(self, tmp_path, sample_data, monkeypatch):
        """Относительный путь достраивается до корня проекта.

        Мы подменяем BASE_DIR на временную папку, кладём туда data/products.json
        и вызываем read_json с коротким путём — функция обязана найти файл.
        """
        import src.utils as utils

        data_dir = tmp_path / "data"
        data_dir.mkdir()
        (data_dir / "products.json").write_text(
            json.dumps(sample_data, ensure_ascii=False),
            encoding="UTF-8",
        )
        monkeypatch.setattr(utils, "BASE_DIR", tmp_path)

        result = read_json("data/products.json")

        assert result == sample_data

    def test_nonexistent_file_raises(self, tmp_path):
        """Несуществующий файл приводит к FileNotFoundError.

        Функция не обязана глотать ошибку: пусть её поднимает дальше —
        решение (обработать или упасть) остаётся за вызывающим кодом.
        """
        with pytest.raises(FileNotFoundError):
            read_json(str(tmp_path / "no_such_file.json"))

    def test_invalid_json_raises(self, tmp_path):
        """Битый JSON приводит к json.JSONDecodeError — нормальное поведение."""
        bad_file = tmp_path / "bad.json"
        bad_file.write_text("{не json", encoding="UTF-8")

        with pytest.raises(json.JSONDecodeError):
            read_json(str(bad_file))

    def test_cyrillic_preserved(self, tmp_path):
        """Кириллица читается без искажений благодаря encoding='UTF-8'."""
        data = [{"name": "Телевизоры", "description": "Просмотр", "products": []}]
        file_path = tmp_path / "ru.json"
        file_path.write_text(json.dumps(data, ensure_ascii=False), encoding="UTF-8")

        assert read_json(str(file_path)) == data


""" Тесты create_objects_from_json """


class TestCreateObjectsFromJson:
    """Проверки функции create_objects_from_json."""

    def test_creates_categories(self, sample_data):
        """Для каждой категории из данных создаётся объект Category."""
        categories = create_objects_from_json(sample_data)

        assert len(categories) == 2
        assert all(isinstance(c, Category) for c in categories)
        assert [c.name for c in categories] == ["Смартфоны", "Телевизоры"]

    def test_descriptions_transferred(self, sample_data):
        """Описания категорий переносятся в объекты без изменений."""
        categories = create_objects_from_json(sample_data)

        assert categories[0].description == "Смартфоны для связи и задач"
        assert categories[1].description == "Современный телевизор"

    def test_creates_products(self, sample_data):
        """Товары создаются как объекты Product с полями из JSON."""
        categories = create_objects_from_json(sample_data)
        phones = categories[0].products

        assert len(phones) == 2
        assert all(isinstance(p, Product) for p in phones)
        assert phones[0].name == "Samsung Galaxy S23 Ultra"
        assert phones[0].price == 180000.0
        assert phones[1].quantity == 8

    def test_empty_products_list(self):
        """Категория без товаров создаётся с пустым списком products."""
        data = [{"name": "Пустая", "description": "Нет товаров", "products": []}]

        categories = create_objects_from_json(data)

        assert len(categories) == 1
        assert categories[0].products == []

    def test_empty_data(self):
        """На пустом списке возвращается пустой список — без ошибок."""
        assert create_objects_from_json([]) == []

    def test_missing_key_raises(self):
        """Отсутствие ключа 'products' приводит к KeyError — данные некорректны."""
        data = [{"name": "Битая", "description": "Нет ключа products"}]

        with pytest.raises(KeyError):
            create_objects_from_json(data)
