"""Модуль для работы с категориями.

Этот модуль содержит класс Category для представления категории товаров
в интернет-магазине.
"""

from typing import TYPE_CHECKING, Iterator

from src.product import Product

if TYPE_CHECKING:
    pass

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

    # ============================================================================
    # Начало разработки нового функционала в рамках работы над проектом homework_16_1
    # ============================================================================

    def add_product(self, product: "Product") -> None:
        """Добавляет продукт в категорию.

        Метод добавляет объект класса Product или его наследников в приватный список
        товаров категории и увеличивает счетчик общего количества продуктов.

        Метод защищен от добавления объектов, не являющихся продуктами. При попытке
        добавить не-продукт выбрасывается TypeError.

        Args:
            product: Объект класса Product или его наследников (Smartphone, LawnGrass и т.д.)
                для добавления в категорию

        Raises:
            TypeError: Если product не является экземпляром класса Product или его наследников

        Example:
            >>> product = Product("Test", "Description", 100.0, 5)
            >>> category = Category("Test Category", "Description", [])
            >>> initial_count = Category.product_count
            >>> category.add_product(product)
            >>> assert len(category._Category__products) == 1
            >>> assert Category.product_count == initial_count + 1

            >>> from src.product import Smartphone
            >>> smartphone = Smartphone("Phone", "Desc", 100.0, 5, 95.5, "Model", 256, "Black")
            >>> category.add_product(smartphone)
            >>> assert len(category._Category__products) == 2

            >>> category.add_product("Not a product")  # doctest: +SKIP
            Traceback (most recent call last):
            ...
            TypeError: Можно добавлять только объекты класса Product и его наследников
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product и его наследников")
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
        return "\n".join(str(product) for product in self.__products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории.

        Returns:
            Строка в формате: "Название категории, количество продуктов: X шт."
            где X - общее количество всех товаров на складе (сумма quantity всех продуктов).

        Example:
            >>> product1 = Product("Test1", "Desc1", 100.0, 5)
            >>> product2 = Product("Test2", "Desc2", 200.0, 10)
            >>> category = Category("Test", "Description", [product1, product2])
            >>> str(category)
            'Test, количество продуктов: 15 шт.'
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self) -> Iterator["Product"]:
        """Возвращает итератор по продуктам категории.

        Позволяет перебирать товары категории в цикле for.

        Yields:
            Объекты класса Product из категории

        Example:
            >>> product1 = Product("Test1", "Desc1", 100.0, 5)
            >>> product2 = Product("Test2", "Desc2", 200.0, 10)
            >>> category = Category("Test", "Description", [product1, product2])
            >>> for product in category:
            ...     print(product.name)
            Test1
            Test2
        """
        for product in self.__products:
            yield product
