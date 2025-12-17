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
    __products: list["Product"]

    def __init__(self, name: str, description: str, products: list["Product"]) -> None:
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
        self.__products = products[:] if products else []

        # Увеличиваем счетчик категорий
        Category.category_count += 1

        # Увеличиваем счетчик продуктов на длину списка продуктов
        Category.product_count += len(self.__products)

    def add_product(self, product: "Product") -> None:
        """Добавляет продукт в категорию.

        Метод добавляет объект класса Product в приватный список товаров категории
        и увеличивает счетчик общего количества продуктов.

        Args:
            product: Объект класса Product для добавления в категорию

        Example:
            >>> product = Product("Test", "Description", 100.0, 5)
            >>> category = Category("Test Category", "Description", [])
            >>> initial_count = Category.product_count
            >>> category.add_product(product)
            >>> assert len(category._Category__products) == 1
            >>> assert Category.product_count == initial_count + 1
            >>> assert "Test" in category.products
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает список продуктов категории в виде строки.

        Returns:
            Строка с информацией о продуктах в формате:
            "Название продукта, цена руб. Остаток: количество шт."
            Каждый продукт на новой строке.
        """
        if not self.__products:
            return ""
        return "\n".join(
            f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт." for product in self.__products
        )
