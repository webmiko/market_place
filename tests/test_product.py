"""Тесты для класса Product.

Этот модуль содержит тесты для проверки корректности работы класса Product,
включая инициализацию и все атрибуты.
"""

from src.product import Product


class TestProductInit:
    """Тесты для инициализации класса Product."""

    def test_product_init_with_all_attributes(self) -> None:
        """Тест создания продукта со всеми атрибутами.

        Проверяет, что все атрибуты корректно устанавливаются при создании объекта.
        """
        product = Product(
            name="Samsung Galaxy S23 Ultra",
            description="256GB, Серый цвет, 200MP камера",
            price=180000.0,
            quantity=5,
        )

        assert product.name == "Samsung Galaxy S23 Ultra"
        assert product.description == "256GB, Серый цвет, 200MP камера"
        assert product.price == 180000.0
        assert product.quantity == 5

    def test_product_init_with_different_types(self) -> None:
        """Тест создания продукта с разными типами данных.

        Проверяет корректную работу с float для цены и int для количества.
        """
        product = Product(
            name="Test Product",
            description="Test description",
            price=99.99,
            quantity=1,
        )

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)

    def test_product_init_with_zero_quantity(self) -> None:
        """Тест создания продукта с нулевым количеством."""
        product = Product(
            name="Out of stock",
            description="No items available",
            price=100.0,
            quantity=0,
        )

        assert product.quantity == 0

    def test_product_init_with_high_price(self) -> None:
        """Тест создания продукта с высокой ценой."""
        product = Product(
            name="Expensive item",
            description="Very expensive",
            price=999999.99,
            quantity=1,
        )

        assert product.price == 999999.99


class TestProductAttributes:
    """Тесты для атрибутов класса Product."""

    def test_product_attributes_are_accessible(self, sample_product: Product) -> None:
        """Тест доступа к атрибутам продукта.

        Args:
            sample_product: Фикстура с тестовым продуктом
        """
        assert sample_product.name == "Test Product"
        assert sample_product.description == "Test description"
        assert sample_product.price == 1000.0
        assert sample_product.quantity == 10

    def test_product_attributes_can_be_read(self, sample_product: Product) -> None:
        """Тест чтения атрибутов продукта.

        Args:
            sample_product: Фикстура с тестовым продуктом
        """
        name = sample_product.name
        description = sample_product.description
        price = sample_product.price
        quantity = sample_product.quantity

        assert name == "Test Product"
        assert description == "Test description"
        assert price == 1000.0
        assert quantity == 10
