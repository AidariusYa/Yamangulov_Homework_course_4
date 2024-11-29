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
