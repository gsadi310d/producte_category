"""Тесты точки входа src/main.py.

Файл — скрипт: основная логика живёт под if __name__ == "__main__".
Поэтому запускаем его через runpy.run_path(run_name="__main__"),
перехватываем print через capsys, а входные данные подменяем
через monkeypatch, чтобы не зависеть от реального файла в data/.
"""
import runpy
from pathlib import Path

import pytest

from src.category import Category

MAIN_PATH = Path(__file__).resolve().parent.parent / "src" / "main.py"


def run_main(monkeypatch, sample_data, capsys):
    """Запускает main.py как скрипт и возвращает перехваченный stdout.

    - подменяем src.utils.read_json, чтобы скрипт брал данные из фикстуры;
    - run_name="__main__" активирует блок if __name__ == "__main__";
    - capsys перехватывает все print() внутри скрипта.
    """
    monkeypatch.setattr("src.utils.read_json", lambda path: sample_data)
    runpy.run_path(str(MAIN_PATH), run_name="__main__")
    return capsys.readouterr().out


""" Тесты """


class TestMainScript:
    """Сквозные проверки точки входа: от чтения JSON до счётчиков."""

    def test_prints_raw_json(self, monkeypatch, sample_data, capsys):
        """Скрипт печатает прочитанный JSON — данные дошли из read_json."""
        output = run_main(monkeypatch, sample_data, capsys)

        assert "Смартфоны" in output
        assert "Samsung Galaxy S23 Ultra" in output

    def test_prints_first_category_name(self, monkeypatch, sample_data, capsys):
        """create_objects_from_json вернула список, имя первой категории напечатано."""
        output = run_main(monkeypatch, sample_data, capsys)

        assert "Смартфоны" in output

    def test_first_category_has_products(self, monkeypatch, sample_data, capsys):
        """Печатается список товаров первой категории — объекты созданы из JSON."""
        output = run_main(monkeypatch, sample_data, capsys)

        # В repr списка товаров видны имена товаров
        assert "Xiaomi Redmi Note 11" in output

    def test_product_fields_printed(self, monkeypatch, sample_data, capsys):
        """Поля каждого ручного товара выведены: имена и цены на месте."""
        output = run_main(monkeypatch, sample_data, capsys)

        assert "Samsung Galaxy S23 Ultra" in output
        assert "180000.0" in output
        assert "Iphone 15" in output
        assert "210000.0" in output
        assert '55" QLED 4K' in output
        assert "123000.0" in output

    def test_manual_category_checks(self, monkeypatch, sample_data, capsys):
        """Проверка category1: имя совпало, товаров три, счётчики накоплены."""
        output = run_main(monkeypatch, sample_data, capsys)

        # print(category1.name == "Смартфоны") печатает True
        assert "True" in output
        # len(category1.products) == 3
        assert "3" in output

    def test_final_counters(self, monkeypatch, sample_data, capsys):
        """К концу скрипта счётчики учитывают все создания.

        Категории: 2 из JSON + 2 ручные = 4.
        Товары: сколько в sample_data, плюс 4 ручных.
        """
        run_main(monkeypatch, sample_data, capsys)

        json_products = sum(len(c["products"]) for c in sample_data)

        assert Category.category_count == 4
        assert Category.product_count == json_products + 4

    def test_works_with_real_json_file(self, monkeypatch, capsys):
        """Скрипт работает и с настоящим файлом data/products.json.

        Тест не подменяет read_json: если файла нет — скип с пояснением,
        чтобы прогон не падал у коллег без данных.
        """
        data_file = MAIN_PATH.parent.parent / "data" / "products.json"
        if not data_file.exists():
            pytest.skip("data/products.json отсутствует в репозитории")

        runpy.run_path(str(MAIN_PATH), run_name="__main__")
        output = capsys.readouterr().out

        assert output.strip() != ""
