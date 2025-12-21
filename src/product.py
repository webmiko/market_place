"""Модуль для работы с продуктами.

Этот модуль содержит класс Product для представления товара в интернет-магазине.
"""

import logging
from pathlib import Path
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    pass

# Константы модуля
DEFAULT_PRICE = 0.0
DEFAULT_QUANTITY = 0
ENCODING = "utf-8"
FILE_APPEND_MODE = "a"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


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

    log_file = logs_dir / "product.log"
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


class Product:
    """Класс для представления продукта в интернет-магазине.

    Класс Product содержит информацию о товаре: название, описание, цену
    и количество в наличии.

    Attributes:
        name: Название продукта
        description: Описание продукта
        price: Цена продукта (может быть с копейками). Property с геттером и сеттером.
        quantity: Количество в наличии (в штуках)

    Example:
        >>> product = Product(
        ...     name="Samsung Galaxy S23 Ultra",
        ...     description="256GB, Серый цвет, 200MP камера",
        ...     price=180000.0,
        ...     quantity=5
        ... )
        >>> print(product.name)
        Samsung Galaxy S23 Ultra
        >>> print(product.price)
        180000.0
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализирует экземпляр класса Product.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта (может быть с копейками)
            quantity: Количество в наличии (в штуках)

        Example:
            >>> product = Product("Test", "Description", 100.0, 10)
            >>> assert product.name == "Test"
            >>> assert product.quantity == 10
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, existing_products: Optional[List["Product"]] = None) -> "Product":
        """Создает новый продукт из словаря с данными.

        Если передан список существующих продуктов, проверяет наличие дубликатов по имени.
        При обнаружении дубликата:
        - Складывает количества товаров
        - Выбирает максимальную цену
        - Обновляет описание

        Args:
            product_data: Словарь с данными продукта:
                - name: Название продукта
                - description: Описание продукта
                - price: Цена продукта
                - quantity: Количество в наличии
            existing_products: Опциональный список существующих продуктов для проверки дубликатов

        Returns:
            Созданный объект класса Product

        Example:
            >>> data = {"name": "Test", "description": "Desc", "price": 100.0, "quantity": 5}
            >>> product = Product.new_product(data)
            >>> assert product.name == "Test"
            >>> assert product.price == 100.0
        """
        if existing_products:
            for existing in existing_products:
                if existing.name == product_data["name"]:
                    # Найден дубликат - складываем количества и выбираем максимальную цену
                    new_quantity = existing.quantity + product_data["quantity"]
                    new_price = max(existing.price, product_data["price"])
                    existing.quantity = new_quantity
                    existing.__price = new_price
                    existing.description = product_data["description"]
                    return existing

        # Создаем новый продукт
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """Возвращает цену продукта.

        Returns:
            Цена продукта
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Устанавливает цену продукта с валидацией.

        Если цена <= 0, выводит сообщение об ошибке и не устанавливает цену.
        Если цена понижается, запрашивает подтверждение у пользователя.

        Args:
            value: Новая цена продукта

        Example:
            >>> product = Product("Test", "Desc", 100.0, 5)
            >>> product.price = 50.0  # Понижение цены - запросит подтверждение
            >>> product.price = -10.0  # Отрицательная цена - выведет ошибку
        """
        if value <= 0:
            logger.warning(f"Попытка установить невалидную цену для {self.name}: {value}")
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Проверка на понижение цены
        if hasattr(self, "_Product__price") and value < self.__price:
            logger.info(f"Попытка понизить цену для {self.name}: {self.__price} -> {value}")
            try:
                response = input(f"Цена понижается с {self.__price} до {value}. Подтвердите действие (y/n): ")
                if response.lower() != "y":
                    logger.info(f"Пользователь отменил понижение цены для {self.name}")
                    return
            except EOFError:
                # В неинтерактивном режиме (например, при тестировании) не подтверждаем понижение
                logger.debug(f"EOFError при попытке понизить цену для {self.name} (неинтерактивный режим)")
                return

        logger.info(f"Установка цены для {self.name}: {self.__price} -> {value}")
        self.__price = value

    def __str__(self) -> str:
        """Возвращает строковое представление продукта.

        Returns:
            Строка в формате: "Название продукта, X руб. Остаток: X шт."

        Example:
            >>> product = Product("Test", "Description", 100.0, 5)
            >>> str(product)
            'Test, 100 руб. Остаток: 5 шт.'
        """
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Возвращает сумму произведений цены на количество для двух продуктов.

        Args:
            other: Второй объект класса Product

        Returns:
            Сумма произведений цены на количество: self.price * self.quantity + other.price * other.quantity

        Example:
            >>> product1 = Product("Test1", "Desc1", 100.0, 10)
            >>> product2 = Product("Test2", "Desc2", 200.0, 2)
            >>> product1 + product2
            1400.0
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return self.price * self.quantity + other.price * other.quantity
