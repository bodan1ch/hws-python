class Device:
    def __init__(self, name, manufacturer, power):
        self.name = name
        self.manufacturer = manufacturer
        self.power = power

    def display_info(self):
        print(
            f"{self.name} — производитель: {self.manufacturer}, "
            f"мощность: {self.power} Вт"
        )

    def turn_on(self):
        print(f"{self.name} включён.")


class CoffeeMachine(Device):
    def __init__(self, name, manufacturer, power, water_tank_volume):
        super().__init__(name, manufacturer, power)
        self.water_tank_volume = water_tank_volume

    def make_coffee(self):
        print(f"{self.name} готовит кофе.")

    def display_info(self):
        super().display_info()
        print(f"Объём резервуара для воды: {self.water_tank_volume} л")


class Blender(Device):
    def __init__(self, name, manufacturer, power, speed_levels):
        super().__init__(name, manufacturer, power)
        self.speed_levels = speed_levels

    def blend(self):
        print(f"{self.name} измельчает продукты.")

    def display_info(self):
        super().display_info()
        print(f"Количество скоростей: {self.speed_levels}")


class MeatGrinder(Device):
    def __init__(self, name, manufacturer, power, capacity):
        super().__init__(name, manufacturer, power)
        self.capacity = capacity

    def grind_meat(self):
        print(f"{self.name} перемалывает мясо.")

    def display_info(self):
        super().display_info()
        print(f"Производительность: {self.capacity} кг/мин")


class Ship:
    def __init__(self, name, displacement, max_speed):
        self.name = name
        self.displacement = displacement
        self.max_speed = max_speed

    def display_info(self):
        print(
            f"{self.name}: водоизмещение {self.displacement} т, "
            f"максимальная скорость {self.max_speed} узлов"
        )

    def sail(self):
        print(f"Корабль «{self.name}» вышел в море.")


class Frigate(Ship):
    def __init__(self, name, displacement, max_speed, missile_count):
        super().__init__(name, displacement, max_speed)
        self.missile_count = missile_count

    def display_info(self):
        super().display_info()
        print(f"Ракет на борту: {self.missile_count}")


class Destroyer(Ship):
    def __init__(self, name, displacement, max_speed, crew_size):
        super().__init__(name, displacement, max_speed)
        self.crew_size = crew_size

    def display_info(self):
        super().display_info()
        print(f"Экипаж: {self.crew_size} человек")


class Cruiser(Ship):
    def __init__(self, name, displacement, max_speed, helicopter_count):
        super().__init__(name, displacement, max_speed)
        self.helicopter_count = helicopter_count

    def display_info(self):
        super().display_info()
        print(f"Вертолётов на борту: {self.helicopter_count}")


class Money:
    def __init__(self, whole_part, fractional_part, currency="грн"):
        self.currency = currency
        self.set_amount(whole_part, fractional_part)

    def set_amount(self, whole_part, fractional_part):
        total_cents = whole_part * 100 + fractional_part
        sign = -1 if total_cents < 0 else 1
        self.whole_part, self.fractional_part = divmod(abs(total_cents), 100)
        self.whole_part *= sign
        self.fractional_part *= sign

    def total_cents(self):
        return self.whole_part * 100 + self.fractional_part

    def display(self):
        sign = "-" if self.total_cents() < 0 else ""
        print(
            f"{sign}{abs(self.whole_part)}."
            f"{abs(self.fractional_part):02d} {self.currency}"
        )

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Нельзя вычитать суммы в разных валютах.")

        difference = self.total_cents() - other.total_cents()
        sign = -1 if difference < 0 else 1
        whole_part, fractional_part = divmod(abs(difference), 100)
        return Money(sign * whole_part, sign * fractional_part, self.currency)


class Product:
    def __init__(self, name, price):
        if not isinstance(price, Money):
            raise TypeError("Цена товара должна быть объектом класса Money.")
        self.name = name
        self.price = price

    def reduce_price(self, amount):
        if not isinstance(amount, Money):
            raise TypeError("Сумма скидки должна быть объектом класса Money.")
        if self.price.currency != amount.currency:
            raise ValueError("Валюта скидки должна совпадать с валютой цены.")
        if amount.total_cents() < 0:
            raise ValueError("Скидка не может быть отрицательной.")
        if amount.total_cents() > self.price.total_cents():
            raise ValueError("Скидка не может быть больше цены товара.")
        self.price = self.price - amount

    def display(self):
        print(f"Товар: {self.name}")
        print("Цена:", end=" ")
        self.price.display()


def main():
    print("Устройства:")
    appliances = [
        CoffeeMachine("Aroma", "HomeTech", 1200, 1.5),
        Blender("MixPro", "KitchenPlus", 800, 5),
        MeatGrinder("GrindMax", "KitchenPlus", 1500, 2.0),
    ]
    for appliance in appliances:
        appliance.display_info()
        appliance.turn_on()

    print("\nКорабли:")
    fleet = [
        Frigate("Гетман Сагайдачный", 3500, 30, 8),
        Destroyer("Смелый", 8000, 32, 280),
        Cruiser("Адмирал", 12000, 29, 2),
    ]
    for vessel in fleet:
        vessel.display_info()
        vessel.sail()

    print("\nРабота с деньгами и товаром:")
    price = Money(250, 0, "грн")
    discount = Money(25, 50, "грн")
    product = Product("Электрический чайник", price)
    product.display()
    product.reduce_price(discount)
    print("После снижения цены:")
    product.display()


if __name__ == "__main__":
    main()
