"""Модуль для загрузки данных из JSON файлов.

Этот модуль содержит функцию для загрузки категорий и продуктов из JSON файла
и создания соответствующих объектов Category и Product.
"""

import json
import logging
from pathlib import Path
from typing import List

from src.category import Category
from src.product import Product

# Константы модуля
ENCODING = "utf-8"
FILE_READ_MODE = "r"
FILE_APPEND_MODE = "a"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_RETURN_VALUE: List[Category] = []


def _setup_logger() -> logging.Logger:
    """
    Настраивает и возвращает логгер для модуля.

    Returns:
        Настроенный логгер для модуля
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    logs_dir = Path(__file__).parent.parent / "logs"
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "data_loader.log"
    file_handler = logging.FileHandler(log_file, mode=FILE_APPEND_MODE, encoding=ENCODING)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt=TIMESTAMP_FORMAT,
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


# Создаем логгер для модуля
logger = _setup_logger()


def load_categories_from_json(file_path: str) -> List[Category]:
    """
    Загружает категории и продукты из JSON-файла.

    Функция читает JSON-файл, содержащий список категорий с продуктами,
    и создает соответствующие объекты Category и Product.

    Args:
        file_path: Путь к JSON-файлу с данными о категориях и продуктах

    Returns:
        Список объектов Category. Возвращает пустой список при ошибке.

    Example:
        >>> categories = load_categories_from_json("data/products.json")
        >>> assert len(categories) > 0
        >>> assert isinstance(categories[0], Category)
    """
    logger.info(f"Загрузка категорий из файла: {file_path}")

    # Проверка существования файла
    if not Path(file_path).exists():
        logger.warning(f"Файл не найден: {file_path}")
        return DEFAULT_RETURN_VALUE[:]

    try:
        # Чтение JSON из файла
        with open(file_path, FILE_READ_MODE, encoding=ENCODING) as f:
            data = json.load(f)

        # Проверка типа данных
        if not isinstance(data, list):
            logger.warning("Файл содержит не список")
            return DEFAULT_RETURN_VALUE[:]

        # Обработка пустого файла
        if not data:
            logger.warning("Файл содержит пустой список")
            return DEFAULT_RETURN_VALUE[:]

        # Создание объектов Category и Product
        categories: List[Category] = []

        for category_data in data:
            # Создание продуктов для категории
            products: List[Product] = []

            for product_data in category_data.get("products", []):
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
                products.append(product)

            # Создание категории
            category = Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
            categories.append(category)

        logger.info(f"Успешно загружено {len(categories)} категорий")
        return categories

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON: {type(e).__name__} - {e}")
        return DEFAULT_RETURN_VALUE[:]
    except KeyError as e:
        logger.error(f"Отсутствует обязательное поле в JSON: {type(e).__name__} - {e}")
        return DEFAULT_RETURN_VALUE[:]
    except (OSError, IOError) as e:
        logger.error(f"Ошибка ввода-вывода при работе с файлом: {type(e).__name__} - {e}")
        return DEFAULT_RETURN_VALUE[:]
    except (ValueError, TypeError) as e:
        logger.error(f"Ошибка типа данных или значения: {type(e).__name__} - {e}")
        return DEFAULT_RETURN_VALUE[:]
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {type(e).__name__} - {e}")
        return DEFAULT_RETURN_VALUE[:]
