"""Модуль для работы с заказами.

Этот модуль содержит класс Order для представления заказов в интернет-магазине.
"""

from typing import TYPE_CHECKING

from src.category import BaseEntity
from src.product import BaseProduct, ZeroQuantityError

if TYPE_CHECKING:
    pass

# Константы модуля
DEFAULT_QUANTITY = 1
MIN_QUANTITY = 1


class Order(BaseEntity):
    """Класс для представления заказа в интернет-магазине.

    Класс Order содержит информацию о заказе: номер заказа, описание,
    товар в заказе, количество купленного товара и итоговую стоимость.

    Attributes:
        name: Номер заказа
        description: Описание заказа
        product: Товар в заказе (объект класса Product или его наследников)
        quantity: Количество купленного товара
        total_price: Итоговая стоимость заказа

    Example:
        >>> from src.product import Product
        >>> product = Product("Test Product", "Description", 100.0, 10)
        >>> order = Order("ORD-001", "Тестовый заказ", product, 5)
        >>> print(order.name)
        ORD-001
        >>> print(order.total_price)
        500.0
        >>> print(order)
        Заказ ORD-001: Test Product, количество: 5, итого: 500.0 руб.
    """

    product: BaseProduct
    quantity: int
    total_price: float

    def __init__(
        self,
        name: str,
        description: str,
        product: BaseProduct,
        quantity: int,
    ) -> None:
        """Инициализирует экземпляр класса Order.

        Args:
            name: Номер заказа
            description: Описание заказа
            product: Товар в заказе (объект класса Product или его наследников)
            quantity: Количество купленного товара (должно быть >= MIN_QUANTITY)

        Raises:
            ValueError: Если quantity < MIN_QUANTITY
            TypeError: Если product не является объектом класса BaseProduct или его наследников
            ZeroQuantityError: Если товар имеет нулевое количество (обрабатывается внутри метода)

        Example:
            >>> from src.product import Product
            >>> product = Product("Test", "Desc", 100.0, 10)
            >>> order = Order("ORD-001", "Тестовый заказ", product, 5)
            >>> assert order.name == "ORD-001"
            >>> assert order.quantity == 5
            >>> assert order.total_price == 500.0

            >>> Order("ORD-001", "Тестовый заказ", product, 0)  # doctest: +SKIP
            Traceback (most recent call last):
            ...
            ValueError: Количество товара должно быть не менее 1
        """
        # ============================================================================
        # Начало разработки нового функционала в рамках работы над проектом homework_17_1
        # Дата: 2026-01-02
        # Обработка исключения ZeroQuantityError с использованием try/except/finally/else
        # ============================================================================
        super().__init__(name, description)
        try:
            if quantity < MIN_QUANTITY:
                raise ValueError(f"Количество товара должно быть не менее {MIN_QUANTITY}")
            if not isinstance(product, BaseProduct):
                raise TypeError("Товар должен быть объектом класса Product или его наследников")
            # Проверка на нулевое количество товара
            if product.quantity == 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен в заказ")
        except ZeroQuantityError as e:
            print(f"Ошибка при создании заказа: {e}")
            raise
        else:
            # Блок выполняется только если исключений не было
            self.product = product
            self.quantity = quantity
            self.total_price = round(product.price * quantity, 2)
            print(f"Заказ '{name}' успешно создан для товара '{product.name}'")
        finally:
            # Блок выполняется всегда, независимо от наличия исключений
            print(f"Обработка создания заказа '{name}' завершена")

    def __str__(self) -> str:
        """Возвращает строковое представление заказа.

        Returns:
            Строка в формате: "Заказ {name}: {product.name}, количество: {quantity}, итого: {total_price} руб."

        Example:
            >>> from src.product import Product
            >>> product = Product("Test Product", "Description", 100.0, 10)
            >>> order = Order("ORD-001", "Тестовый заказ", product, 5)
            >>> str(order)
            'Заказ ORD-001: Test Product, количество: 5, итого: 500.0 руб.'
        """
        return f"Заказ {self.name}: {self.product.name}, количество: {self.quantity}, итого: {self.total_price} руб."
