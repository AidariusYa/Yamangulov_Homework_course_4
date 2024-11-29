class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (f"Product(name={self.name}, description={self.description}, price={self.price}, "
                f"quantity={self.quantity})")


class Category:
    category_count = 0  # Статический атрибут для общего количества категорий
    product_count = 0   # Статический атрибут для общего количества продуктов

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        self.product_count = len(products)  # Локальный атрибут для количества продуктов в данной категории
        Category.category_count += 1
        Category.product_count += self.product_count  # Увеличиваем общее количество продуктов

    def __del__(self):
        Category.category_count -= 1
        Category.product_count -= self.product_count  # Уменьшаем общее количество продуктов
