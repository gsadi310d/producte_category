import pytest


@pytest.fixture
def product_one() -> list[int]:
    return [1, 2, 3, 4, 5]
