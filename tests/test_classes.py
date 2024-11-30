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
    assert len(category.products) == 3
    assert Category.category_count == 1
    assert category.product_count == 3  # Проверка количества продуктов в категории


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
        category.add_product(product)
        self.assertEqual(len(category.products), 1)  # Используем геттер для получения продуктов

    def test_products_getter(self):
        """Проверяет корректность работы геттера для списка продуктов"""
        category = Category("Тестовая категория", "Описание категории")
        product1 = Product("Тестовый продукт 1", "Описание продукта 1", 100.0, 10)
        product2 = Product("Тестовый продукт 2", "Описание продукта 2", 200.0, 5)
        category.add_product(product1)
        category.add_product(product2)

        # Форматируем ожидаемый вывод
        expected_output = [
            f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт.",
            f"{product2.name}, {product2.price} руб. Остаток: {product2.quantity} шт."
        ]

        # Проверяем, что список продуктов соответствует ожидаемому
        self.assertEqual([f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in category.products],
                         expected_output)

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


if __name__ == "__main__":
    unittest.main()
