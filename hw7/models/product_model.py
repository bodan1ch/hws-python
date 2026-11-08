from product import Product


class ProductModel:
    def __init__(self):
        self.products = [
            Product(
                "Бездротові навушники",
                "https://images.unsplash.com/photo-1505740420928-5e560c06d30e"
                "?auto=format&fit=crop&w=800&q=80",
                2499,
                4.8,
                1,
            ),
            Product(
                "Смартгодинник",
                "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
                "?auto=format&fit=crop&w=800&q=80",
                3999,
                4.6,
                2,
            ),
            Product(
                "Фотоапарат",
                "https://images.unsplash.com/photo-1516035069371-29a1b244cc32"
                "?auto=format&fit=crop&w=800&q=80",
                12499,
                4.9,
                3,
            ),
        ]
        self._next_id = max((product.id for product in self.products), default=0) + 1

    def get_all_products(self):
        return list(self.products)

    def get_product_by_id(self, product_id):
        return next(
            (product for product in self.products if product.id == product_id),
            None,
        )

    def create_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Потрібно передати об'єкт класу Product.")
        if product.id is None:
            product.id = self._next_id
            self._next_id += 1
        elif self.get_product_by_id(product.id) is not None:
            raise ValueError(f"Товар з id {product.id} вже існує.")
        else:
            self._next_id = max(self._next_id, product.id + 1)

        self.products.append(product)
        return product
