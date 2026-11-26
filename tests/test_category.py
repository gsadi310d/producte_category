def test_category(category_first, category_second):
    # Телевизоры: один товар
    assert category_first.name == "Телевизоры"
    assert category_first.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником"
    )
    assert len(category_first.products) == 1
    assert category_first.products[0].name == "LG"

    # Смартфоны: четыре товара
    assert category_second.name == "Смартфоны"
    assert category_second.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_second.products) == 4
    assert category_second.products[0].name == "Samsung Galaxy S23 Ultra"

    # Счётчики — общеклассные, накапливаются от обеих категорий
    assert category_first.product_count == 5
    assert category_first.category_count == 2
    assert category_second.product_count == 5
    assert category_second.category_count == 2
