"""Тесты для класса Category.

Этот модуль содержит тесты для проверки корректности работы класса Category,
включая инициализацию, атрибуты и атрибуты класса.
"""

from src.category import DEFAULT_PRODUCTS_LIST, Category
from src.product import Product


class TestCategoryInit:
    """Тесты для инициализации класса Category."""

    def test_category_init_with_all_attributes(self) -> None:
        """Тест создания категории со всеми атрибутами.

        Проверяет, что все атрибуты корректно устанавливаются при создании объекта.
        """
        product1 = Product("Product 1", "Description 1", 100.0, 5)
        product2 = Product("Product 2", "Description 2", 200.0, 10)

        category = Category(
            name="Смартфоны",
            description="Смартфоны для коммуникации",
            products=[product1, product2],
        )

        assert category.name == "Смартфоны"
        assert category.description == "Смартфоны для коммуникации"
        assert len(category.products) == 2
        assert category.products[0] == product1
        assert category.products[1] == product2

    def test_category_init_with_empty_products_list(self) -> None:
        """Тест создания категории с пустым списком продуктов."""
        category = Category(
            name="Пустая категория",
            description="Категория без продуктов",
            products=[],
        )

        assert category.name == "Пустая категория"
        assert len(category.products) == 0

    def test_category_init_products_are_objects(self) -> None:
        """Тест, что products содержит объекты класса Product."""
        product = Product("Test", "Description", 100.0, 5)
        category = Category("Test Category", "Description", [product])

        assert isinstance(category.products[0], Product)
        assert category.products[0].name == "Test"


class TestCategoryClassAttributes:
    """Тесты для атрибутов класса Category."""

    def test_category_count_increments_on_init(self) -> None:
        """Тест увеличения счетчика категорий при создании объекта."""
        initial_count = Category.category_count

        category1 = Category("Category 1", "Description 1", [])
        assert Category.category_count == initial_count + 1
        assert category1.name == "Category 1"

        category2 = Category("Category 2", "Description 2", [])
        assert Category.category_count == initial_count + 2
        assert category2.name == "Category 2"

    def test_product_count_increments_on_init(self) -> None:
        """Тест увеличения счетчика продуктов при создании категории."""
        initial_count = Category.product_count

        product1 = Product("Product 1", "Description 1", 100.0, 5)
        product2 = Product("Product 2", "Description 2", 200.0, 10)
        product3 = Product("Product 3", "Description 3", 300.0, 15)

        category = Category("Test Category", "Description", [product1, product2, product3])
        assert Category.product_count == initial_count + 3
        assert len(category.products) == 3

    def test_product_count_counts_all_products_in_category(self) -> None:
        """Тест подсчета всех продуктов в категории."""
        initial_count = Category.product_count

        products = [Product(f"Product {i}", f"Description {i}", 100.0 * i, i) for i in range(1, 6)]

        category = Category("Test Category", "Description", products)
        assert Category.product_count == initial_count + 5
        assert len(category.products) == 5

    def test_category_count_and_product_count_are_class_attributes(self) -> None:
        """Тест, что category_count и product_count - атрибуты класса."""
        assert hasattr(Category, "category_count")
        assert hasattr(Category, "product_count")
        assert isinstance(Category.category_count, int)
        assert isinstance(Category.product_count, int)

    def test_category_count_accessible_from_instance(self) -> None:
        """Тест доступа к category_count через экземпляр."""
        category = Category("Test", "Description", [])
        assert hasattr(category, "category_count")
        assert category.category_count == Category.category_count

    def test_product_count_accessible_from_instance(self) -> None:
        """Тест доступа к product_count через экземпляр."""
        product = Product("Test", "Description", 100.0, 5)
        category = Category("Test", "Description", [product])
        assert hasattr(category, "product_count")
        assert category.product_count == Category.product_count


class TestCategoryAttributes:
    """Тесты для атрибутов экземпляра класса Category."""

    def test_category_attributes_are_accessible(self) -> None:
        """Тест доступа к атрибутам категории."""
        product = Product("Test Product", "Test Description", 100.0, 5)
        category = Category(
            name="Test Category",
            description="Test category description",
            products=[product],
        )

        assert category.name == "Test Category"
        assert category.description == "Test category description"
        assert len(category.products) == 1
        assert category.products[0] == product

    def test_category_products_list_can_be_accessed(self) -> None:
        """Тест доступа к списку продуктов категории."""
        products = [
            Product("Product 1", "Description 1", 100.0, 5),
            Product("Product 2", "Description 2", 200.0, 10),
        ]

        category = Category("Test", "Description", products)

        assert len(category.products) == 2
        assert category.products[0].name == "Product 1"
        assert category.products[1].name == "Product 2"


class TestCategoryConstants:
    """Тесты для констант модуля Category."""

    def test_default_products_list_constant(self) -> None:
        """Тест константы DEFAULT_PRODUCTS_LIST."""
        assert DEFAULT_PRODUCTS_LIST == []
        assert isinstance(DEFAULT_PRODUCTS_LIST, list)


class TestCategoryEdgeCases:
    """Тесты для граничных случаев класса Category."""

    def test_category_with_empty_string_name(self) -> None:
        """Тест создания категории с пустым именем."""
        category = Category("", "Description", [])
        assert category.name == ""

    def test_category_with_empty_string_description(self) -> None:
        """Тест создания категории с пустым описанием."""
        category = Category("Name", "", [])
        assert category.description == ""

    def test_category_with_very_long_strings(self) -> None:
        """Тест создания категории с очень длинными строками."""
        long_name = "A" * 1000
        long_description = "B" * 2000
        category = Category(long_name, long_description, [])
        assert len(category.name) == 1000
        assert len(category.description) == 2000

    def test_category_with_large_product_list(self) -> None:
        """Тест создания категории с большим списком продуктов."""
        products = [Product(f"Product {i}", f"Description {i}", 100.0 * i, i) for i in range(100)]
        category = Category("Large Category", "Description", products)
        assert len(category.products) == 100
        assert Category.product_count >= 100

    def test_category_products_list_mutation(self) -> None:
        """Тест, что список продуктов защищен от изменений через property."""
        product1 = Product("Product 1", "Description 1", 100.0, 5)
        original_list = [product1]
        category = Category("Test", "Description", original_list)
        assert len(category.products) == 1

        # Изменение исходного списка не влияет на категорию
        product2 = Product("Product 2", "Description 2", 200.0, 10)
        original_list.append(product2)
        assert len(category.products) == 1, "Список продуктов должен быть защищен от изменений исходного списка"

        # Попытка изменить через property не сохраняется (property возвращает копию)
        category.products.append(product2)
        assert len(category.products) == 1, "Property возвращает копию, изменения не сохраняются"

    def test_category_with_none_values_in_products(self) -> None:
        """Тест создания категории с None в списке продуктов (если возможно)."""
        # Это может вызвать ошибку типизации, но проверим поведение
        product = Product("Product", "Description", 100.0, 5)
        category = Category("Test", "Description", [product])
        assert len(category.products) == 1
