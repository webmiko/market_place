.PHONY: format lint type-check test clean install help

help:
	@echo "Доступные команды:"
	@echo "  make format      - Форматировать код (black + isort)"
	@echo "  make lint        - Проверить код линтером (flake8)"
	@echo "  make type-check  - Проверить типы (mypy)"
	@echo "  make check       - Запустить все проверки (format + lint + type-check)"
	@echo "  make test        - Запустить тесты"
	@echo "  make clean       - Очистить кэш и временные файлы"

format:
	@echo "Форматирование кода (длина строки: 119 символов)..."
	poetry run black .
	poetry run isort .

lint:
	@echo "Проверка стиля кода (длина строки: 119 символов)..."
	poetry run flake8 .

type-check:
	@echo "Проверка типов..."
	poetry run mypy .

check: format lint type-check
	@echo "✅ Все проверки пройдены!"

test:
	@echo "Запуск тестов..."
	poetry run pytest -v

clean:
	@echo "Очистка временных файлов..."
	find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -r {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -r {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	@echo "✅ Очистка завершена"

install:
	@echo "Убедитесь, что виртуальное окружение активировано:"
	@echo "  source ../.venv/bin/activate"
	@echo "Зависимости должны быть установлены из ../pyproject.toml"

