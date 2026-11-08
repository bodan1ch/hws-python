class Product:
    def __init__(self, title, image, price, rating, product_id=None):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Назва товару не може бути порожньою.")
        if not isinstance(image, str) or not image.strip():
            raise ValueError("Посилання на зображення не може бути порожнім.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Ціна має бути невід'ємним числом.")
        if not isinstance(rating, (int, float)) or not 0 <= rating <= 5:
            raise ValueError("Рейтинг має бути числом від 0 до 5.")

        self.id = product_id
        self.title = title
        self.image = image
        self.price = price
        self.rating = rating

    def __repr__(self):
        return (
            f"Product(id={self.id!r}, title={self.title!r}, "
            f"image={self.image!r}, price={self.price!r}, "
            f"rating={self.rating!r})"
        )
