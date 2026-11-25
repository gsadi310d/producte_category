# my-new-project

Базовый проект для разработки.

## Установка

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Запуск

```bash
make run
# или: python -m src.main
```

## Тесты и проверки

```bash
make test    # pytest с покрытием
make lint    # flake8
make type    # mypy
make check   # всё сразу (то же, что и в CI)
```

## Структура

Смотри docs/ARCHITECTURE.md.
