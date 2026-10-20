class Book:
    def __init__(self, title, author, year, pages):
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год издания должен быть положительным целым числом.")
        if not isinstance(pages, int) or pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным.")

        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        return (
            f"«{self.title}», автор: {self.author}, "
            f"год издания: {self.year}, страниц: {self.pages}"
        )

    def __repr__(self):
        return (
            f"Book(title={self.title!r}, author={self.author!r}, "
            f"year={self.year!r}, pages={self.pages!r})"
        )

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages + other.pages

    def __contains__(self, word):
        if not isinstance(word, str):
            return False
        return word.casefold() in self.title.casefold()

    def __bool__(self):
        return self.pages > 0


library = [
    Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 480),
    Book("Белый Клык", "Джек Лондон", 1906, 240),
    Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, 320),
]

print("Книги в библиотеке:")
for item in library:
    print(item)

print("\nСортировка по количеству страниц:")
for item in sorted(library):
    print(f"{len(item)} страниц — {item.title}")

book1, book2 = library[0], library[1]
print(f"\nСуммарное количество страниц двух книг: {book1 + book2}")
print(f"Есть ли слово «поттер» в названии третьей книги? {'поттер' in library[2]}")
print(f"Книги с одинаковыми названием и автором: {book1 == book2}")
print(f"Книга «{book1.title}» непустая: {bool(book1)}")
print(f"Представление объекта для отладки: {book1!r}")
