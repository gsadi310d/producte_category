# Архитектура

## Схема

```
src/
├── main.py          точка входа: argparse, setup_logging, код возврата
├── constants.py     константы проекта
├── utils/           переиспользуемые функции
├── decorators/      логирование вызовов, retry
├── generators/      генераторы данных (dataclass + seed)
├── external_api/    обёртки над внешними API
└── logging/         единая точка настройки логирования

tests/               pytest: conftest + по папке на модуль
```

## Таблица модулей

| Модуль           | Ответственность                        | Зависимости        |
|------------------|----------------------------------------|--------------------|
| main             | CLI, сборка и запуск                   | utils, logging     |
| utils            | чистые функции без побочных эффектов   | —                  |
| decorators       | log_calls (таймер + логирование)       | logging            |
| generators       | детерминированные данные для тестов    | utils              |
| external_api     | ApiClient с config-датаклассом         | utils, logging     |
| logging          | setup_logging(verbose)                 | —                  |

## Принципы

- Код в src/, тесты в tests/, импорт через пакет (from src.utils import ...).
- Логи — через setup_logging, а не print.
- Каждый модуль проверяется своим тестом: tests/test_<модуль>/.
