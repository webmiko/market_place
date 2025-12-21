"""Тесты для класса Product.

Этот модуль содержит тесты для проверки корректности работы класса Product,
включая инициализацию и все атрибуты.
"""

from typing import TYPE_CHECKING

import pytest

from src.product import DEFAULT_PRICE, DEFAULT_QUANTITY, Product

if TYPE_CHECKING:
    from pytest import CaptureFixture, MonkeyPatch


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


class TestProductNewProduct:
    """Тесты для класс-метода new_product класса Product."""

    def test_new_product_from_dict(self) -> None:
        """Тест создания продукта из словаря."""
        product_data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": 100.0,
            "quantity": 5,
        }

        product = Product.new_product(product_data)

        assert isinstance(product, Product)
        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 100.0
        assert product.quantity == 5

    def test_new_product_without_existing_products(self) -> None:
        """Тест создания продукта без списка существующих продуктов."""
        product_data = {
            "name": "New Product",
            "description": "Description",
            "price": 200.0,
            "quantity": 10,
        }

        product = Product.new_product(product_data, existing_products=None)

        assert product.name == "New Product"
        assert product.price == 200.0
        assert product.quantity == 10

    def test_new_product_with_duplicate_name(self) -> None:
        """Тест создания продукта с дублирующимся именем."""
        existing_product = Product("Duplicate", "Description", 100.0, 5)
        product_data = {
            "name": "Duplicate",
            "description": "New Description",
            "price": 150.0,
            "quantity": 3,
        }

        result = Product.new_product(product_data, existing_products=[existing_product])

        # Должен вернуть существующий продукт с обновленными данными
        assert result is existing_product
        assert existing_product.quantity == 8  # 5 + 3
        assert existing_product.price == 150.0  # max(100.0, 150.0)

    def test_new_product_with_duplicate_name_lower_price(self) -> None:
        """Тест создания продукта с дублирующимся именем и меньшей ценой."""
        existing_product = Product("Duplicate", "Description", 200.0, 5)
        product_data = {
            "name": "Duplicate",
            "description": "New Description",
            "price": 150.0,
            "quantity": 3,
        }

        result = Product.new_product(product_data, existing_products=[existing_product])

        # Должен вернуть существующий продукт с максимальной ценой
        assert result is existing_product
        assert existing_product.quantity == 8  # 5 + 3
        assert existing_product.price == 200.0  # max(200.0, 150.0)

    def test_new_product_with_duplicate_name_updates_description(self) -> None:
        """Тест, что описание обновляется при дубликате продукта."""
        existing_product = Product("Duplicate", "Old Description", 100.0, 5)
        product_data = {
            "name": "Duplicate",
            "description": "Updated Description",
            "price": 150.0,
            "quantity": 3,
        }

        result = Product.new_product(product_data, existing_products=[existing_product])

        # Должен вернуть существующий продукт с обновленным описанием
        assert result is existing_product
        assert existing_product.description == "Updated Description"
        assert existing_product.quantity == 8  # 5 + 3
        assert existing_product.price == 150.0  # max(100.0, 150.0)


class TestProductPriceProperty:
    """Тесты для property price класса Product."""

    def test_price_getter(self) -> None:
        """Тест получения цены через property."""
        product = Product("Test", "Description", 100.0, 5)
        assert product.price == 100.0

    def test_price_setter_valid_value(self) -> None:
        """Тест установки валидной цены через property."""
        product = Product("Test", "Description", 100.0, 5)
        product.price = 150.0
        assert product.price == 150.0

    def test_price_setter_zero_value(self, capsys: "CaptureFixture[str]") -> None:
        """Тест установки нулевой цены (должна быть отклонена)."""
        product = Product("Test", "Description", 100.0, 5)
        initial_price = product.price

        product.price = 0

        assert product.price == initial_price  # Цена не изменилась
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_negative_value(self, capsys: "CaptureFixture[str]") -> None:
        """Тест установки отрицательной цены (должна быть отклонена)."""
        product = Product("Test", "Description", 100.0, 5)
        initial_price = product.price

        product.price = -10.0

        assert product.price == initial_price  # Цена не изменилась
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_increase(self) -> None:
        """Тест увеличения цены (не требует подтверждения)."""
        product = Product("Test", "Description", 100.0, 5)

        product.price = 150.0

        assert product.price == 150.0

    def test_price_setter_decrease_without_confirmation(self, monkeypatch: "MonkeyPatch") -> None:
        """Тест понижения цены без подтверждения."""
        product = Product("Test", "Description", 100.0, 5)
        monkeypatch.setattr("builtins.input", lambda _: "n")

        product.price = 50.0

        assert product.price == 100.0  # Цена не изменилась

    def test_price_setter_decrease_with_confirmation(self, monkeypatch: "MonkeyPatch") -> None:
        """Тест понижения цены с подтверждением."""
        product = Product("Test", "Description", 100.0, 5)
        monkeypatch.setattr("builtins.input", lambda _: "y")

        product.price = 50.0

        assert product.price == 50.0  # Цена изменилась


class TestProductStr:
    """Тесты для метода __str__ класса Product."""

    def test_str_representation(self) -> None:
        """Тест строкового представления продукта."""
        product = Product("Samsung Galaxy S23 Ultra", "Description", 180000.0, 5)
        result = str(product)
        assert result == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."

    def test_str_with_zero_quantity(self) -> None:
        """Тест строкового представления продукта с нулевым количеством."""
        product = Product("Test Product", "Description", 100.0, 0)
        result = str(product)
        assert result == "Test Product, 100 руб. Остаток: 0 шт."

    def test_str_with_float_price(self) -> None:
        """Тест строкового представления продукта с ценой с копейками."""
        product = Product("Test Product", "Description", 99.99, 10)
        result = str(product)
        assert result == "Test Product, 99 руб. Остаток: 10 шт."

    def test_str_integration_with_category_products(self) -> None:
        """Тест использования __str__ в property products категории."""
        from src.category import Category

        product = Product("Test Product", "Description", 100.0, 5)
        category = Category("Test Category", "Description", [product])
        products_str = category.products
        assert "Test Product, 100 руб. Остаток: 5 шт." in products_str


class TestProductAdd:
    """Тесты для метода __add__ класса Product."""

    def test_add_two_products(self) -> None:
        """Тест сложения двух продуктов."""
        product1 = Product("Product 1", "Description 1", 100.0, 10)
        product2 = Product("Product 2", "Description 2", 200.0, 2)
        result = product1 + product2
        assert result == 1400.0  # 100 * 10 + 200 * 2 = 1400

    def test_add_products_with_zero_quantity(self) -> None:
        """Тест сложения продуктов с нулевым количеством."""
        product1 = Product("Product 1", "Description 1", 100.0, 0)
        product2 = Product("Product 2", "Description 2", 200.0, 5)
        result = product1 + product2
        assert result == 1000.0  # 100 * 0 + 200 * 5 = 1000

    def test_add_products_commutative(self) -> None:
        """Тест коммутативности сложения продуктов."""
        product1 = Product("Product 1", "Description 1", 100.0, 10)
        product2 = Product("Product 2", "Description 2", 200.0, 2)
        result1 = product1 + product2
        result2 = product2 + product1
        assert result1 == result2 == 1400.0

    def test_add_with_float_price(self) -> None:
        """Тест сложения продуктов с ценой с копейками."""
        product1 = Product("Product 1", "Description 1", 99.99, 10)
        product2 = Product("Product 2", "Description 2", 50.50, 5)
        result = product1 + product2
        assert result == pytest.approx(1252.4)  # 99.99 * 10 + 50.50 * 5 = 1252.4

    def test_add_with_different_types_raises_error(self) -> None:
        """Тест, что сложение с не-Product объектом вызывает TypeError."""
        product = Product("Product 1", "Description 1", 100.0, 10)
        with pytest.raises(TypeError, match="Можно складывать только объекты класса Product"):
            _ = product + 100  # type: ignore
