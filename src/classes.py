class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализирует новый продукт.

        :param name: Название продукта.
        :param description: Описание продукта.
        :param price: Цена продукта (должна быть положительной).
        :param quantity: Количество продукта на складе.
        """
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
        self.quantity = quantity

    def __repr__(self):
        """
        Возвращает строковое представление продукта.

        :return: Строка с информацией о продукте.
        """
        return (f"Product(name={self.name}, description={self.description}, price={self.price}, "
                f"quantity={self.quantity})")

    @property
    def price(self):
        """
        Возвращает цену продукта.

        :return: Цена продукта.
        """
        return self.__price

    @price.setter
    def price(self, value: float):
        """
        Устанавливает цену продукта.

        :param value: Новая цена продукта.
        :raises ValueError: Если цена меньше или равна нулю, выводится сообщение об ошибке.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Создает новый продукт на основе данных из словаря.

        :param product_data: Словарь с данными о продукте (name, description, price, quantity).
        :return: Новый экземпляр продукта.
        """
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    def __add__(self, other):
        """Возвращает сумму стоимости двух продуктов."""
        if not isinstance(other, Product):
            return NotImplemented
        if not isinstance(self, type(other)):
            raise TypeError("Нельзя складывать продукты разных типов")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __str__(self):
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return (f"Smartphone(name={self.name}, description={self.description}, price={self.price}, "
                f"quantity={self.quantity}, efficiency={self.efficiency}, model={self.model}, "
                f"memory={self.memory}, color={self.color})")


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return (f"LawnGrass(name={self.name}, description={self.description}, price={self.price}, "
                f"quantity={self.quantity}, country={self.country}, "
                f"germination_period={self.germination_period}, color={self.color})")


class Category:
    category_count = 0  # Статический атрибут для общего количества категорий
    product_count = 0   # Статический атрибут для общего количества продуктов

    def __init__(self, name: str, description: str, products: list = None):
        """
        Инициализирует новую категорию.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список продуктов в категории (по умолчанию пустой список).
        """
        self.name = name
        self.description = description
        self._products = products if products is not None else []  # Приватный атрибут для списка продуктов
        self.product_count = len(self._products)  # Локальный атрибут для количества продуктов в данной категории
        Category.category_count += 1
        Category.product_count += self.product_count  # Увеличиваем общее количество продуктов

    def add_product(self, product):
        """
        Добавляет продукт в категорию.

        :param product: Класс продукта, который нужно добавить.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты")
        self._products.append(product)  # Добавляем продукт в приватный атрибут
        Category.product_count += 1  # Увеличиваем общее количество продуктов

    @property
    def products(self):
        """
        Возвращает строку с информацией о продуктах в категории.

        :return: Строка с информацией о продуктах.
        """
        return ", ".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self._products])

    def __str__(self):
        """Возвращает строковое представление категории."""
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __del__(self):
        """Уменьшает счетчики категорий и продуктов при удалении экземпляра категории."""
        Category.category_count -= 1
        Category.product_count -= self.product_count  # Уменьшаем общее количество продуктов
