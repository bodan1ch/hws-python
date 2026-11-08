import json


class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")


class JsonMixin:
    def to_json(self):
        return json.dumps(
            {"name": self.name, "price": self.price},
            ensure_ascii=False,
        )


class DiscountMixin:
    def apply_discount(self, percent):
        if not isinstance(percent, (int, float)):
            raise TypeError("Відсоток знижки має бути числом.")
        if not 0 <= percent <= 100:
            raise ValueError("Відсоток знижки має бути від 0 до 100.")

        self.price *= 1 - percent / 100
        return self.price


class Product:
    def __init__(self, name, price):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Назва товару не може бути порожньою.")
        if not isinstance(price, (int, float)):
            raise TypeError("Ціна товару має бути числом.")
        if price < 0:
            raise ValueError("Ціна товару не може бути від'ємною.")

        self.name = name
        self.price = price


class ProductManager(Product, LoggingMixin, JsonMixin, DiscountMixin):
    pass


def main():
    product = ProductManager("Навушники", 1000)
    product.log(f"Створено товар: {product.name}")
    print("Товар у форматі JSON:", product.to_json())
    print(f"Ціна після знижки 15%: {product.apply_discount(15):.2f} грн")
    print("Порядок пошуку методів ProductManager.mro():")
    for product_class in ProductManager.mro():
        print(product_class.__name__)
    print(
        "Спочатку перевіряється ProductManager, далі Product і міксини "
        "у порядку наслідування, а наприкінці — object."
    )


if __name__ == "__main__":
    main()
