"""Модуль для работы с продуктами.

Этот модуль содержит класс Product для представления товара в интернет-магазине.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

# Константы модуля
DEFAULT_PRICE = 0.0
DEFAULT_QUANTITY = 0


class Product:
    """Класс для представления продукта в интернет-магазине.

    Класс Product содержит информацию о товаре: название, описание, цену
    и количество в наличии.

    Attributes:
        name: Название продукта
        description: Описание продукта
        price: Цена продукта (может быть с копейками)
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
    price: float
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
        self.price = price
        self.quantity = quantity
