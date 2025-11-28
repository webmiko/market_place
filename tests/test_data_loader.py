"""Тесты для модуля загрузки данных из JSON."""

import json
from pathlib import Path

from src.category import Category
from src.data_loader import load_categories_from_json
from src.product import Product


class TestLoadCategoriesFromJson:
    """Тесты для функции load_categories_from_json."""

    def test_load_categories_from_json_success(self, tmp_path: Path) -> None:
        """Тест успешной загрузки категорий из JSON."""
        # Arrange
        json_data = [
            {
                "name": "Смартфоны",
                "description": "Смартфоны для коммуникации",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    },
                    {
                        "name": "Iphone 15",
                        "description": "512GB, Gray space",
                        "price": 210000.0,
                        "quantity": 8,
                    },
                ],
            },
            {
                "name": "Телевизоры",
                "description": "Современные телевизоры",
                "products": [
                    {
                        "name": '55" QLED 4K',
                        "description": "Фоновая подсветка",
                        "price": 123000.0,
                        "quantity": 7,
                    },
                ],
            },
        ]

        json_file = tmp_path / "products.json"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

        # Act
        categories = load_categories_from_json(str(json_file))

        # Assert
        assert len(categories) == 2
        assert isinstance(categories[0], Category)
        assert isinstance(categories[1], Category)
        assert categories[0].name == "Смартфоны"
        assert categories[1].name == "Телевизоры"
        assert len(categories[0].products) == 2
        assert len(categories[1].products) == 1

    def test_load_categories_from_json_products_are_objects(self, tmp_path: Path) -> None:
        """Тест, что продукты создаются как объекты Product."""
        # Arrange
        json_data = [
            {
                "name": "Смартфоны",
                "description": "Смартфоны для коммуникации",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    },
                ],
            },
        ]

        json_file = tmp_path / "products.json"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

        # Act
        categories = load_categories_from_json(str(json_file))

        # Assert
        assert len(categories) == 1
        assert len(categories[0].products) == 1
        assert isinstance(categories[0].products[0], Product)
        assert categories[0].products[0].name == "Samsung Galaxy C23 Ultra"
        assert categories[0].products[0].price == 180000.0
        assert categories[0].products[0].quantity == 5

    def test_load_categories_from_json_empty_products_list(self, tmp_path: Path) -> None:
        """Тест загрузки категории с пустым списком продуктов."""
        # Arrange
        json_data = [
            {
                "name": "Пустая категория",
                "description": "Категория без продуктов",
                "products": [],
            },
        ]

        json_file = tmp_path / "products.json"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

        # Act
        categories = load_categories_from_json(str(json_file))

        # Assert
        assert len(categories) == 1
        assert categories[0].name == "Пустая категория"
        assert len(categories[0].products) == 0

    def test_load_categories_from_json_file_not_found(self) -> None:
        """Тест обработки ошибки FileNotFoundError."""
        # Arrange
        non_existent_file = "non_existent_file.json"

        # Act
        categories = load_categories_from_json(non_existent_file)

        # Assert
        assert categories == []

    def test_load_categories_from_json_invalid_json(self, tmp_path: Path) -> None:
        """Тест обработки ошибки JSONDecodeError."""
        # Arrange
        json_file = tmp_path / "invalid.json"
        with open(json_file, "w", encoding="utf-8") as f:
            f.write("{ invalid json }")

        # Act
        categories = load_categories_from_json(str(json_file))

        # Assert
        assert categories == []

    def test_load_categories_from_json_empty_file(self, tmp_path: Path) -> None:
        """Тест обработки пустого файла."""
        # Arrange
        json_file = tmp_path / "empty.json"
        json_file.touch()

        # Act
        categories = load_categories_from_json(str(json_file))

        # Assert
        assert categories == []

    def test_load_categories_from_json_not_list(self, tmp_path: Path) -> None:
        """Тест обработки случая, когда JSON содержит не список."""
        # Arrange
        json_data = {"name": "Not a list"}

        json_file = tmp_path / "not_list.json"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

        # Act
        categories = load_categories_from_json(str(json_file))

        # Assert
        assert categories == []

    def test_load_categories_from_json_real_file(self) -> None:
        """Тест загрузки из реального файла data/products.json."""
        # Arrange
        json_file = Path(__file__).parent.parent / "data" / "products.json"

        # Act
        categories = load_categories_from_json(str(json_file))

        # Assert
        assert len(categories) > 0
        assert all(isinstance(cat, Category) for cat in categories)
        assert all(isinstance(prod, Product) for cat in categories for prod in cat.products)
