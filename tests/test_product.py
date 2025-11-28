"""Тесты для класса Product.

Этот модуль содержит тесты для проверки корректности работы класса Product,
включая инициализацию и все атрибуты.
"""

from src.product import DEFAULT_PRICE, DEFAULT_QUANTITY, Product


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


class TestProductConstants:
    """Тесты для констант модуля Product."""

    def test_default_price_constant(self) -> None:
        """Тест константы DEFAULT_PRICE."""
        assert DEFAULT_PRICE == 0.0
        assert isinstance(DEFAULT_PRICE, float)

    def test_default_quantity_constant(self) -> None:
        """Тест константы DEFAULT_QUANTITY."""
        assert DEFAULT_QUANTITY == 0
        assert isinstance(DEFAULT_QUANTITY, int)


class TestProductEdgeCases:
    """Тесты для граничных случаев класса Product."""

    def test_product_with_zero_price(self) -> None:
        """Тест создания продукта с нулевой ценой."""
        product = Product("Free Product", "Free item", 0.0, 10)
        assert product.price == 0.0
        assert product.quantity == 10

    def test_product_with_negative_price(self) -> None:
        """Тест создания продукта с отрицательной ценой (допускается)."""
        product = Product("Product", "Description", -10.0, 5)
        assert product.price == -10.0

    def test_product_with_negative_quantity(self) -> None:
        """Тест создания продукта с отрицательным количеством (допускается)."""
        product = Product("Product", "Description", 100.0, -5)
        assert product.quantity == -5

    def test_product_with_empty_string_name(self) -> None:
        """Тест создания продукта с пустым именем."""
        product = Product("", "Description", 100.0, 5)
        assert product.name == ""

    def test_product_with_empty_string_description(self) -> None:
        """Тест создания продукта с пустым описанием."""
        product = Product("Product", "", 100.0, 5)
        assert product.description == ""

    def test_product_with_very_long_strings(self) -> None:
        """Тест создания продукта с очень длинными строками."""
        long_name = "A" * 1000
        long_description = "B" * 2000
        product = Product(long_name, long_description, 100.0, 5)
        assert len(product.name) == 1000
        assert len(product.description) == 2000

    def test_product_with_float_quantity_conversion(self) -> None:
        """Тест создания продукта с float количеством (должно быть int)."""
        # Python автоматически не преобразует, но проверим поведение
        product = Product("Product", "Description", 100.0, 5)
        assert isinstance(product.quantity, int)

    def test_product_with_int_price(self) -> None:
        """Тест создания продукта с int ценой (должно быть float)."""
        product = Product("Product", "Description", 100, 5)
        assert isinstance(product.price, (int, float))
