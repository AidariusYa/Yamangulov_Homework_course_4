import unittest

from src.classes import Category, Product


def test_product_initialization():
    """Проверка корректности инициализации продукта"""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization():
    """Проверка корректности инициализации категории"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения "
                        "дополнительных функций для удобства жизни", [product1, product2, product3])

    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                                    "функций для удобства жизни")
    assert len(category._products) == 3  # Проверка количества продуктов в категории
    assert Category.category_count == 1     # Проверка общего количества категорий
    assert Category.product_count == 3  # Проверка общего количества продуктов


def test_product_count_in_category():
    """Проверка количества продуктов в категории"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения "
                        "дополнительных функций для удобства жизни", [product1, product2, product3])
    assert category.product_count == 3


def test_multiple_categories():
    """Проверка количества категорий"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения "
                         "дополнительных функций для удобства жизни", [product1, product2, product3])

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, "
                         "станет вашим другом и помощником", [product4])

    assert Category.category_count == 2  # Проверка общего количества категорий
    assert Category.product_count == 4  # Проверка общего количества продуктов
    assert category1.product_count == 3  # Проверка количества продуктов в первой категории
    assert category2.product_count == 1  # Проверка количества продуктов во второй категории


class TestProductCategory(unittest.TestCase):
    """Тестовый класс для проверки функциональности классов Product и Category"""
    def test_add_product(self):
        """Проверяет добавление продукта в категорию."""
        category = Category("Тестовая категория", "Описание категории")
        product = Product("Тестовый продукт", "Описание продукта", 100.0, 10)
        self.assertEqual(category.product_count, 0)  # Используем геттер для получения продуктов
        category.add_product(product)  # Добавляем продукт в категорию
        self.assertEqual(Category.product_count, 1)  # Проверяем, что общее количество продуктов на уровне
        # класса увеличилось на 1

    def test_products_getter(self):
        """Проверяет корректность работы геттера для списка продуктов"""
        category = Category("Тестовая категория", "Описание категории")
        product1 = Product("Тестовый продукт 1", "Описание продукта 1", 100.0, 10)
        product2 = Product("Тестовый продукт 2", "Описание продукта 2", 200.0, 5)
        category.add_product(product1)
        category.add_product(product2)

        # Форматируем ожидаемый вывод
        expected_output = (
            f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт., "
            f"{product2.name}, {product2.price} руб. Остаток: {product2.quantity} шт."
        )

        # Проверяем, что строка продуктов соответствует ожидаемому
        self.assertEqual(category.products, expected_output)

    def test_new_product(self):
        """Проверяет создание нового продукта из словаря"""
        product_data = {
            "name": "Тестовый продукт",
            "description": "Описание тестового продукта",
            "price": 150.0,
            "quantity": 20
        }
        product = Product.new_product(product_data)
        self.assertEqual(product.name, "Тестовый продукт")
        self.assertEqual(product.price, 150.0)

    def test_price_setter(self):
        """Проверяет работу сеттера для цены продукта"""
        product = Product("Тестовый продукт", "Описание продукта", 100.0, 10)
        product.price = -50  # Должно вывести сообщение
        self.assertEqual(product.price, 100.0)  # Цена не должна измениться

        product.price = 200.0  # Устанавливаем корректную цену
        self.assertEqual(product.price, 200.0)  # Проверяем, что цена обновилась

    def test_product_str(self):
        """Проверяет строковое представление продукта"""
        product = Product("Тестовый продукт", "Описание продукта", 100.0, 10)
        self.assertEqual(str(product), "Тестовый продукт, 100.0 руб. Остаток: 10 шт.")

    def test_category_str(self):
        """Проверяет строковое представление категории"""
        product1 = Product("Тестовый продукт 1", "Описание продукта 1", 100.0, 10)
        product2 = Product("Тестовый продукт 2", "Описание продукта 2", 200.0, 5)
        category = Category("Тестовая категория", "Описание категории", [product1, product2])
        self.assertEqual(str(category), "Тестовая категория, количество продуктов: 15 шт.")

    def test_product_addition(self):
        """Проверяет сложение двух продуктов"""
        product1 = Product("Тестовый продукт 1", "Описание продукта 1", 100.0, 10)
        product2 = Product("Тестовый продукт 2", "Описание продукта 2", 200.0, 5)

        # Ожидаемая стоимость: (100 * 10) + (200 * 5) = 1000 + 1000 = 2000
        total_value = product1 + product2
        self.assertEqual(total_value, 2000)


if __name__ == "__main__":
    unittest.main()
