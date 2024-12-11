import unittest

from src.classes import Category, LawnGrass, Product, Smartphone


class TestProductCategory(unittest.TestCase):
    """Тестовый класс для проверки функциональности классов Product и его подклассов и Category"""
    def setUp(self):
        """Сбрасываем счетчик перед каждым тестом"""
        Category.product_count = 0

    def test_product_initialization(self):
        """Проверка корректности инициализации продукта"""
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        assert product.name == "Samsung Galaxy S23 Ultra"
        assert product.description == "256GB, Серый цвет, 200MP камера"
        assert product.price == 180000.0
        assert product.quantity == 5

    def test_category_initialization(self):
        """Проверка корректности инициализации категории"""
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения "
                                         "дополнительных функций для удобства жизни", [product1, product2, product3])

        assert category.name == "Смартфоны"
        assert category.description == ("Смартфоны, как средство не только коммуникации, но и получения "
                                        "дополнительных функций для удобства жизни")
        assert len(category._products) == 3  # Проверка количества продуктов в категории
        assert Category.category_count == 1  # Проверка общего количества категорий
        assert Category.product_count == 3  # Проверка общего количества продуктов

    def test_product_count_in_category(self):
        """Проверка количества продуктов в категории"""
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения "
                                         "дополнительных функций для удобства жизни", [product1, product2, product3])
        assert category.product_count == 3

    def test_multiple_categories(self):
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

    def test_smartphone_initialization(self):
        """Тестирует инициализацию объекта класса Smartphone"""
        smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                                180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
        self.assertEqual(smartphone.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(smartphone.efficiency, 95.5)

    def test_lawn_grass_initialization(self):
        """Тестирует инициализацию объекта класса LawnGrass"""
        grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                          "Россия", "7 дней", "Зеленый")
        self.assertEqual(grass.country, "Россия")
        self.assertEqual(grass.germination_period, "7 дней")

    def test_product_addition_to_category(self):
        """Тестирует добавление продукта в категорию"""
        category = Category("Тестовая категория", "Описание категории")
        product = Product("Тестовый продукт", "Описание продукта", 100.0, 10)
        category.add_product(product)
        self.assertEqual(Category.product_count, 1)

    def test_product_addition_invalid_type(self):
        """Проверяет, что нельзя добавить объект, не являющийся продуктом."""
        category = Category("Тестовая категория", "Описание категории")
        with self.assertRaises(TypeError):
            category.add_product("Not a product")

    def test_add_smartphone(self):
        """Проверяет добавление смартфона в категорию."""
        category = Category("Смартфоны", "Описание категории")
        smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                                180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
        category.add_product(smartphone)  # Добавляем смартфон в категорию
        self.assertEqual(Category.product_count, 1)  # Проверяем, что общее количество продуктов увеличилось на 1

    def test_smartphone_addition(self):
        """Проверяет сложение двух смартфонов."""
        smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                                 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
        smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8,
                                 98.2, "15", 512, "Gray space")
        total_value = smartphone1 + smartphone2
        expected_value = (smartphone1.price * smartphone1.quantity) + (smartphone2.price * smartphone2.quantity)
        self.assertEqual(total_value, expected_value)

    def test_lawn_grass_addition(self):
        """Проверяет сложение двух газонов."""
        grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                           "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15,
                           "США", "5 дней", "Темно-зеленый")
        total_value = grass1 + grass2
        expected_value = (grass1.price * grass1.quantity) + (grass2.price * grass2.quantity)
        self.assertEqual(total_value, expected_value)

    def test_invalid_addition(self):
        """Проверяет, что нельзя сложить смартфон и газонную траву."""
        smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                                180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
        grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                          "Россия", "7 дней", "Зеленый")
        with self.assertRaises(TypeError):
            _ = smartphone + grass


def test_product_repr():
    """Проверяем, что строковое представление объекта product соответствует ожидаемому формату"""
    product = Product("Тестовый продукт", "Описание продукта", 100.0, 10)
    assert repr(product) == "Product(name=Тестовый продукт, description=Описание продукта, price=100.0, quantity=10)"


def test_smartphone_repr():
    """Проверяем, что строковое представление объекта smartphone соответствует ожидаемому формату"""
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                            180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    assert repr(smartphone) == ("Smartphone(name=Samsung Galaxy S23 Ultra, description=256GB, Серый цвет, "
                                "200MP камера, price=180000.0, quantity=5, efficiency=95.5, model=S23 Ultra, "
                                "memory=256, color=Серый)")


def test_lawn_grass_repr():
    """Проверяем, что строковое представление объекта LawnGrass соответствует ожидаемому формату"""
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                      "Россия", "7 дней", "Зеленый")
    assert repr(grass) == ("LawnGrass(name=Газонная трава, description=Элитная трава для газона, price=500.0, "
                           "quantity=20, country=Россия, germination_period=7 дней, color=Зеленый)")


if __name__ == "__main__":
    unittest.main()
