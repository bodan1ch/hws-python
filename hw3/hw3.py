class Automobile:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0,
                 color="", price=0.0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Модель автомобиля: ")
        self.year = int(input("Год выпуска: "))
        self.manufacturer = input("Производитель: ")
        self.engine_volume = float(input("Объём двигателя (л): "))
        self.color = input("Цвет: ")
        self.price = float(input("Цена: "))

    def display(self):
        print(
            f"Автомобиль: {self.manufacturer} {self.model}, {self.year} г., "
            f"двигатель {self.engine_volume} л, цвет: {self.color}, "
            f"цена: {self.price:.2f}"
        )

    def set_price(self, price):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self.price = price


class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        self.title = input("Название книги: ")
        self.year = int(input("Год издания: "))
        self.publisher = input("Издательство: ")
        self.genre = input("Жанр: ")
        self.author = input("Автор: ")
        self.price = float(input("Цена: "))

    def display(self):
        print(
            f"Книга: «{self.title}», автор: {self.author}, "
            f"{self.year} г., издательство: {self.publisher}, "
            f"жанр: {self.genre}, цена: {self.price:.2f}"
        )

    def set_price(self, price):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self.price = price


class Stadium:
    def __init__(self, name="", opening_date="", country="", city="", capacity=0):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Название стадиона: ")
        self.opening_date = input("Дата открытия: ")
        self.country = input("Страна: ")
        self.city = input("Город: ")
        self.capacity = int(input("Вместимость: "))

    def display(self):
        print(
            f"Стадион «{self.name}», дата открытия: {self.opening_date}, "
            f"место: {self.city}, {self.country}, "
            f"вместимость: {self.capacity} человек"
        )

    def set_capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Вместимость не может быть отрицательной.")
        self.capacity = capacity


def main():
    print("Введите данные автомобиля:")
    car = Automobile()
    car.input_data()
    car.display()

    print("\nВведите данные книги:")
    book = Book()
    book.input_data()
    book.display()

    print("\nВведите данные стадиона:")
    stadium = Stadium()
    stadium.input_data()
    stadium.display()


if __name__ == "__main__":
    main()
