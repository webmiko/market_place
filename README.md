# Market Place

Проект для управления товарами и категориями в интернет-магазине.

## 📋 Описание

Market Place - это приложение для управления каталогом товаров с категориями. Проект позволяет работать с продуктами, категориями и их взаимосвязями.

### ✨ Основные возможности

- **Управление продуктами**: создание, редактирование и управление товарами
- **Категории товаров**: организация продуктов по категориям
- **Наследование классов**: специализированные классы `Smartphone` и `LawnGrass` как наследники `Product`
- **Валидация данных**: защита от отрицательных значений цены и количества, а также от нулевого количества
- **Защита от дубликатов**: предотвращение добавления продуктов с одинаковыми атрибутами
- **Обработка исключений**: пользовательский класс исключения `ZeroQuantityError` и обработка с использованием `try/except/finally/else`
- **Метод подсчета среднего ценника**: вычисление среднего ценника товаров в категории с обработкой деления на ноль
- **Магические методы**: строковое представление объектов, сложение продуктов, итерация по категориям
- **Загрузка данных**: импорт категорий и продуктов из JSON файлов
- **Тестирование**: полное покрытие кода тестами (212 тестов)

## 🚀 Быстрый старт

### Требования

- Python 3.9+
- Виртуальное окружение (общее для всех проектов в `Мои_проекты/.venv/`)

### Установка

1. Установите Poetry (если еще не установлен):
```bash
pip install poetry
```

2. Установите зависимости проекта:
```bash
cd market_place
poetry install
```

3. Активируйте виртуальное окружение Poetry:
```bash
poetry shell
```

4. Запустите проект:
```bash
cd market_place
python main.py
```

## 📁 Структура проекта

```
market_place/
├── src/                    # Исходный код приложения
│   ├── __init__.py
│   ├── product.py          # Классы Product, Smartphone, LawnGrass
│   ├── category.py         # Класс Category
│   └── data_loader.py      # Загрузка данных из JSON
├── tests/                  # Тесты
│   ├── __init__.py
│   ├── conftest.py         # Общие фикстуры
│   ├── test_product.py     # Тесты для Product, Smartphone, LawnGrass
│   ├── test_category.py    # Тесты для Category
│   └── test_data_loader.py # Тесты для загрузки данных
├── data/                   # Данные (JSON файлы)
│   └── products.json
├── docs/                   # Документация
│   ├── PLAN_INHERITANCE.md # План разработки наследования
│   └── PLAN_HOMEWORK_17_1.md # План разработки homework_17_1
├── 16.1_main.py            # Пример использования нового функционала
├── 17.1_main.py            # Пример использования функционала homework_17_1
├── main.py                 # Точка входа
└── README.md               # Документация
```

## 💡 Примеры использования

### Создание продуктов и категорий

```python
from src.product import Product
from src.category import Category

# Создание продуктов
product1 = Product(
    name="Samsung Galaxy S23 Ultra",
    description="256GB, Серый цвет, 200MP камера",
    price=180000.0,
    quantity=5
)

product2 = Product(
    name="Iphone 15",
    description="512GB, Gray space",
    price=210000.0,
    quantity=8
)

# Создание категории
category = Category(
    name="Смартфоны",
    description="Смартфоны для коммуникации",
    products=[product1, product2]
)

# Доступ к атрибутам
print(category.name)  # Смартфоны
print(Category.category_count)  # Количество созданных категорий
print(Category.product_count)  # Общее количество продуктов
```

### Строковое представление объектов

```python
from src.product import Product
from src.category import Category

# Строковое представление продукта
product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
print(str(product))
# Вывод: Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.

# Строковое представление категории
product1 = Product("Product 1", "Description 1", 100.0, 5)
product2 = Product("Product 2", "Description 2", 200.0, 10)
category = Category("Смартфоны", "Описание", [product1, product2])
print(str(category))
# Вывод: Смартфоны, количество продуктов: 15 шт.

# Использование в print (автоматически вызывает __str__)
print(product)  # То же самое, что print(str(product))
print(category)  # То же самое, что print(str(category))
```

### Сложение продуктов

```python
from src.product import Product

# Создание продуктов
product_a = Product("Product A", "Description A", 100.0, 10)
product_b = Product("Product B", "Description B", 200.0, 2)

# Сложение продуктов (возвращает сумму произведений цены на количество)
total_value = product_a + product_b
print(total_value)  # 1400.0 (100 * 10 + 200 * 2 = 1400)

# Пример: расчет общей стоимости товаров на складе
product1 = Product("Товар 1", "Описание", 99.99, 10)
product2 = Product("Товар 2", "Описание", 50.50, 5)
total = product1 + product2
print(f"Общая стоимость товаров на складе: {total} руб.")
# Вывод: Общая стоимость товаров на складе: 1252.4 руб.
```

### Наследование классов: Smartphone и LawnGrass

```python
from src.product import Smartphone, LawnGrass
from src.category import Category

# Создание смартфона
smartphone = Smartphone(
    name="Samsung Galaxy S23 Ultra",
    description="256GB, Серый цвет, 200MP камера",
    price=180000.0,
    quantity=5,
    efficiency=95.5,  # Производительность
    model="S23 Ultra",  # Модель
    memory=256,  # Объем памяти в ГБ
    color="Серый"  # Цвет
)

# Создание газонной травы
grass = LawnGrass(
    name="Газонная трава",
    description="Элитная трава для газона",
    price=500.0,
    quantity=20,
    country="Россия",  # Страна-производитель
    germination_period="7 дней",  # Срок прорастания
    color="Зеленый"  # Цвет
)

# Оба класса наследуются от Product и имеют все его методы
print(smartphone.price)  # 180000.0
print(grass.quantity)  # 20

# Сложение работает только для одинаковых типов
smartphone1 = Smartphone("Phone1", "Desc", 100.0, 5, 95.5, "Model", 256, "Black")
smartphone2 = Smartphone("Phone2", "Desc", 200.0, 2, 98.0, "Model2", 512, "White")
total = smartphone1 + smartphone2  # Работает
print(total)  # 900.0

# Попытка сложить разные типы вызывает TypeError
try:
    invalid = smartphone1 + grass
except TypeError as e:
    print(f"Ошибка: {e}")  # Можно складывать только товары из одинаковых классов продуктов
```

### Валидация и защита от дубликатов

```python
from src.product import Product, ZeroQuantityError
from src.category import Category

# Валидация отрицательных значений
try:
    product = Product("Test", "Desc", -100.0, 5)  # Отрицательная цена
except ValueError as e:
    print(f"Ошибка: {e}")  # Цена не может быть отрицательной

try:
    product = Product("Test", "Desc", 100.0, -5)  # Отрицательное количество
except ValueError as e:
    print(f"Ошибка: {e}")  # Количество не может быть отрицательным

# Валидация нулевого количества
try:
    product = Product("Test", "Desc", 100.0, 0)  # Нулевое количество
except ZeroQuantityError as e:
    print(f"Ошибка: {e}")  # Товар с нулевым количеством не может быть добавлен

# Защита от дубликатов
category = Category("Test", "Desc", [])
product1 = Product("Test", "Desc", 100.0, 5)
category.add_product(product1)

# Попытка добавить продукт с теми же атрибутами
product2 = Product("Test", "Desc", 100.0, 5)  # Те же атрибуты
try:
    category.add_product(product2)
except ValueError as e:
    print(f"Ошибка: {e}")  # Продукт с такими же атрибутами уже существует в категории
```

### Итерация по товарам категории

```python
from src.product import Product
from src.category import Category

# Создание категории с продуктами
product1 = Product("Product 1", "Description 1", 100.0, 5)
product2 = Product("Product 2", "Description 2", 200.0, 10)
product3 = Product("Product 3", "Description 3", 300.0, 15)

category = Category("Смартфоны", "Описание", [product1, product2, product3])

# Итерация по товарам категории в цикле for
for product in category:
    print(f"{product.name}: {product.price} руб. (остаток: {product.quantity} шт.)")

# Преобразование в список
products_list = list(category)
print(f"Всего товаров в категории: {len(products_list)}")

# Использование в генераторах и других конструкциях Python
product_names = [product.name for product in category]
print(product_names)  # ['Product 1', 'Product 2', 'Product 3']
```

### Комплексный пример использования всех возможностей

```python
from src.product import Product
from src.category import Category

# Создание продуктов
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

# Создание категории
category = Category("Смартфоны", "Смартфоны для коммуникации", [product1, product2, product3])

# 1. Использование строкового представления
print("=== Строковое представление ===")
print(product1)  # Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.
print(category)  # Смартфоны, количество продуктов: 27 шт.

# 2. Использование сложения продуктов
print("\n=== Сложение продуктов ===")
total_value = product1 + product2
print(f"Общая стоимость товаров 1 и 2: {total_value} руб.")
# Вывод: Общая стоимость товаров 1 и 2: 2328000.0 руб.

# 3. Итерация по товарам категории
print("\n=== Итерация по товарам ===")
for product in category:
    print(f"  - {product}")

# 4. Использование property products (использует __str__)
print("\n=== Список всех товаров ===")
print(category.products)
# Вывод:
# Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.
# Iphone 15, 210000 руб. Остаток: 8 шт.
# Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.
```

### Загрузка данных из JSON

```python
from src.data_loader import load_categories_from_json

# Загрузка категорий и продуктов из JSON файла
categories = load_categories_from_json("data/products.json")

# Работа с загруженными данными
for category in categories:
    print(f"Категория: {category.name}")
    print(f"Описание: {category.description}")
    print(f"Количество продуктов: {len(category.products)}")
    
    for product in category.products:
        print(f"  - {product.name}: {product.price} руб. (в наличии: {product.quantity})")
```

### Обработка ошибок при загрузке

```python
from src.data_loader import load_categories_from_json

# Функция автоматически обрабатывает ошибки
categories = load_categories_from_json("non_existent_file.json")
# Вернет пустой список [] при ошибке

# Проверка результата
if categories:
    print(f"Загружено категорий: {len(categories)}")
else:
    print("Не удалось загрузить данные")
```

## 🎯 Реализованные магические методы

Проект использует магические методы Python для удобной работы с объектами:

- **`Product.__str__`**: Строковое представление продукта в формате "Название продукта, X руб. Остаток: X шт."
- **`Category.__str__`**: Строковое представление категории с подсчетом общего количества товаров
- **`Product.__add__`**: Сложение продуктов с возвратом суммы произведений цены на количество (только для одинаковых типов)
- **`Product.__eq__`**: Сравнение продуктов по всем атрибутам
- **`Category.__iter__`**: Итерация по товарам категории в циклах `for`

## 🔒 Новый функционал (homework_17_1)

### Обработка исключений

#### Пользовательский класс исключения ZeroQuantityError

- **`ZeroQuantityError`**: Пользовательский класс исключения для обработки добавления товара с нулевым количеством
  - Наследуется от `ValueError`
  - Вызывается при попытке создать товар с `quantity == 0`
  - Используется в `BaseProduct.__init__` и `Product.new_product`

```python
from src.product import Product, ZeroQuantityError

# Попытка создать товар с нулевым количеством
try:
    product = Product("Товар", "Описание", 1000.0, 0)
except ZeroQuantityError as e:
    print(f"Ошибка: {e}")  # Товар с нулевым количеством не может быть добавлен
```

#### Обработка исключений в Category.add_product

Метод `add_product` использует `try/except/finally/else` для обработки исключений:

```python
from src.product import Product, ZeroQuantityError
from src.category import Category

category = Category("Тест", "Описание", [])
product = Product("Товар", "Описание", 100.0, 5)

# Успешное добавление товара
category.add_product(product)
# Вывод:
# Товар 'Товар' успешно добавлен в категорию 'Тест'
# Обработка добавления товара 'Товар' завершена

# Попытка добавить товар с нулевым количеством
product_zero = Product("Товар", "Описание", 100.0, 5)
product_zero.quantity = 0  # Изменяем количество на 0

try:
    category.add_product(product_zero)
except ZeroQuantityError as e:
    print(f"Ошибка: {e}")
# Вывод:
# Ошибка при добавлении товара: Товар с нулевым количеством не может быть добавлен
# Обработка добавления товара 'Товар' завершена
```

#### Обработка исключений в Order.__init__

Конструктор `Order` также использует `try/except/finally/else`:

```python
from src.product import Product, ZeroQuantityError
from src.order import Order

product = Product("Товар", "Описание", 100.0, 5)

# Успешное создание заказа
order = Order("ORD-001", "Тестовый заказ", product, 3)
# Вывод:
# Заказ 'ORD-001' успешно создан для товара 'Товар'
# Обработка создания заказа 'ORD-001' завершена

# Попытка создать заказ с товаром с нулевым количеством
product_zero = Product("Товар", "Описание", 100.0, 5)
product_zero.quantity = 0

try:
    order = Order("ORD-002", "Заказ", product_zero, 3)
except ZeroQuantityError as e:
    print(f"Ошибка: {e}")
# Вывод:
# Ошибка при создании заказа: Товар с нулевым количеством не может быть добавлен в заказ
# Обработка создания заказа 'ORD-002' завершена
```

#### Метод подсчета среднего ценника

- **`Category.middle_price()`**: Метод для подсчета среднего ценника товаров в категории
  - Вычисляет среднее арифметическое цен всех товаров
  - Обрабатывает деление на ноль (возвращает 0 при отсутствии товаров)
  - Использует `try/except` для обработки исключений

```python
from src.product import Product
from src.category import Category

# Создание категории с товарами
product1 = Product("Товар 1", "Описание", 100.0, 5)
product2 = Product("Товар 2", "Описание", 200.0, 10)
product3 = Product("Товар 3", "Описание", 300.0, 15)

category = Category("Тест", "Описание", [product1, product2, product3])

# Подсчет среднего ценника
average_price = category.middle_price()
print(average_price)  # 200.0 (100 + 200 + 300) / 3 = 200

# Пустая категория
empty_category = Category("Пустая", "Описание", [])
print(empty_category.middle_price())  # 0.0 (обработка деления на ноль)
```

## 🔒 Новый функционал (homework_16_1 и homework_16_2)

### Абстрактный базовый класс

- **`BaseProduct`**: Абстрактный базовый класс для всех продуктов
  - Определяет общий интерфейс и функциональность для всех продуктов
  - Содержит абстрактные методы: `__str__`, `__add__`, `__eq__`
  - Реализует общую логику: инициализацию, валидацию, свойство `price`
  - Не может быть создан напрямую (абстрактный класс)

### Класс-миксин

- **`LogCreationMixin`**: Миксин для логирования создания объектов
  - При создании объекта автоматически выводит в консоль информацию о классе и параметрах
  - Добавлен в цепочку наследования класса `Product`
  - Используется для всех продуктов: `Product`, `Smartphone`, `LawnGrass`

### Наследование классов

- **`Product`**: Наследуется от `LogCreationMixin` и `BaseProduct`
  - Реализует все абстрактные методы базового класса
  - Использует миксин для логирования создания объектов

- **`Smartphone`**: Класс-наследник `Product` для смартфонов с дополнительными атрибутами:
  - `efficiency` (float) - производительность
  - `model` (str) - модель
  - `memory` (int) - объем памяти в ГБ
  - `color` (str) - цвет

- **`LawnGrass`**: Класс-наследник `Product` для газонной травы с дополнительными атрибутами:
  - `country` (str) - страна-производитель
  - `germination_period` (str) - срок прорастания
  - `color` (str) - цвет

### Ограничения и валидация

- **Ограничение сложения**: Можно складывать только товары из одинаковых классов (используется `type()`)
- **Защита `add_product`**: Можно добавлять только объекты класса `Product` и его наследников (используется `isinstance()`)
- **Валидация отрицательных значений**: Цена и количество не могут быть отрицательными
- **Валидация нулевого количества**: Количество товара не может быть равно нулю (вызывается `ZeroQuantityError`)
- **Защита от дубликатов**: Нельзя добавить продукт с такими же атрибутами (используется `__eq__`)
- **Обработка деления на ноль**: Метод `middle_price()` возвращает 0 при отсутствии товаров в категории

## 🛠️ Разработка

### Форматирование кода

```bash
# Форматирование с помощью black (длина строки: 119 символов)
poetry run black .

# Сортировка импортов с помощью isort
poetry run isort .
```

### Линтинг

```bash
# Проверка стиля кода с помощью flake8 (длина строки: 119 символов)
poetry run flake8 .

# Проверка типов с помощью mypy
poetry run mypy .
```

### Тестирование

```bash
# Запуск тестов
poetry run pytest

# Запуск тестов с покрытием
poetry run pytest --cov=src tests/

# Запуск тестов с подробным выводом
poetry run pytest -v
```

**Статистика тестов:**
- Всего тестов: **212**
- Покрытие кода: **98%**
- Все тесты проходят успешно ✅

**Покрытие по модулям:**
- `src/__init__.py`: 100%
- `src/category.py`: 100%
- `src/data_loader.py`: 100%
- `src/product.py`: 97%

**Тесты для магических методов:**
- `Product.__str__`: 4 теста
- `Category.__str__`: 5 тестов
- `Product.__add__`: 8+ тестов (включая проверку типов)
- `Category.__iter__`: 5 тестов

**Тесты для нового функционала:**
- `Smartphone`: 10+ тестов (инициализация, наследование, методы)
- `LawnGrass`: 10+ тестов (инициализация, наследование, методы)
- `Product.__add__` с проверкой типов: 8 тестов
- `Category.add_product` с защитой: 17+ тестов
- Валидация отрицательных значений: 4 теста
- Проверка дубликатов: 6 тестов
- `ZeroQuantityError`: 5+ тестов (создание товара с нулевым количеством)
- `Category.middle_price()`: 6 тестов (с товарами и без товаров)
- Обработка исключений в `Category.add_product`: 1 тест
- Обработка исключений в `Order.__init__`: 1 тест

**Отчет о покрытии:**
- HTML-отчет генерируется автоматически при запуске тестов с покрытием

Для генерации отчета о покрытии:
```bash
# Терминальный отчет
poetry run pytest --cov=src --cov-report=term-missing tests/

# HTML отчет (создается в папке htmlcov/)
poetry run pytest --cov=src --cov-report=html tests/
```

## 📝 Зависимости

Проект использует Poetry для управления зависимостями. Все зависимости указаны в `pyproject.toml`:

**Основные зависимости:**
- Python 3.9+

**Зависимости для разработки:**
- `pytest` - для тестирования
- `pytest-cov` - для проверки покрытия кода тестами
- `black` - для форматирования кода
- `flake8` - для проверки стиля кода
- `isort` - для сортировки импортов
- `mypy` - для проверки типов

**Длина строки кода:** 119 символов (настроено в `pyproject.toml` для black, isort и flake8)

## 🔗 Связь с общим окружением

Этот проект использует:
- Общее виртуальное окружение: `../.venv/`
- Общие зависимости: `../pyproject.toml`
- Общую базу знаний: `Python-проекты/Универсальная-база-знаний/`

## 📄 Лицензия

См. файл [LICENSE](LICENSE)

## 👤 Автор

Проект разработан в рамках обучения Python и ООП

