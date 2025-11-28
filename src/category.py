"""Модуль для работы с категориями.

Этот модуль содержит класс Category для представления категории товаров
в интернет-магазине.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.product import Product

# Константы модуля
DEFAULT_PRODUCTS_LIST: list["Product"] = []


class Category:
    """Класс для представления категории товаров в интернет-магазине.

    Класс Category содержит информацию о категории: название, описание
    и список товаров, принадлежащих этой категории.

    Attributes:
        name: Название категории
        description: Описание категории
        products: Список товаров категории (объекты класса Product).
                  Property, возвращает копию списка для защиты от изменений.

    Class Attributes:
        category_count: Количество созданных категорий
        product_count: Общее количество продуктов во всех категориях

    Example:
        >>> product1 = Product("Product 1", "Description 1", 100.0, 5)
        >>> product2 = Product("Product 2", "Description 2", 200.0, 10)
        >>> category = Category(
        ...     name="Смартфоны",
        ...     description="Смартфоны для коммуникации",
        ...     products=[product1, product2]
        ... )
        >>> print(category.name)
        Смартфоны
        >>> print(len(category.products))
        2
        >>> print(Category.category_count)
        1
    """

    # Атрибуты класса
    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    _products: list["Product"]

    def __init__(
        self, name: str, description: str, products: list["Product"]
    ) -> None:
        """Инициализирует экземпляр класса Category.

        При создании категории автоматически увеличиваются счетчики:
        - category_count - количество категорий
        - product_count - общее количество продуктов во всех категориях

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров категории (объекты класса Product)

        Example:
            >>> product = Product("Test", "Description", 100.0, 5)
            >>> category = Category("Test Category", "Description", [product])
            >>> assert category.name == "Test Category"
            >>> assert Category.category_count > 0
            >>> assert Category.product_count > 0
        """
        self.name = name
        self.description = description
        # Создаем копию списка, чтобы изменения исходного списка не влияли на категорию
        self._products = products[:] if products else []

        # Увеличиваем счетчик категорий
        Category.category_count += 1

        # Увеличиваем счетчик продуктов на длину списка продуктов
        Category.product_count += len(self._products)

    @property
    def products(self) -> list["Product"]:
        """Возвращает список продуктов категории.

        Returns:
            Список продуктов категории (копия для защиты от изменений)
        """
        return self._products[:]
