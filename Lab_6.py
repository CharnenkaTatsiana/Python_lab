class Book:
    total_books = 0

    def __new__(cls, *args, **kwargs):
        print("Создается новый экземпляр книги...")
        instance = super().__new__(cls)
        return instance

    def __init__(self, id, title, authors, publisher, year, pages, price, binding_type):
        self.id = id
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self._price = price
        self.binding_type = binding_type
        Book.total_books += 1

    def __del__(self):
        print(f"Книга '{self.title}' удалена из памяти.")
        Book.total_books -= 1

    def __setattr__(self, name, value):
        if name == "year" and hasattr(self, "year") and value <= 0:
            raise ValueError("Год издания должен быть положительным числом")
        if name == "price" and value <= 0:
            raise ValueError("Цена должна быть положительной")
        super().__setattr__(name, value)

    def __str__(self):
        return f"Книга: {self.title} ({', '.join(self.authors)}, {self.year} г.)"

    # Арифметические методы
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        elif isinstance(other, (int, float)):
            return self.pages + other
        else:
            raise TypeError("Можно складывать только с книгой или числом")

    def __sub__(self, other):
        if isinstance(other, Book):
            return abs(self.pages - other.pages)
        elif isinstance(other, (int, float)):
            return abs(self.pages - other)
        else:
            raise TypeError("Можно вычитать только с книгой или числом")

    # Операторы сравнения
    def __lt__(self, other):
        if isinstance(other, Book):
            return self.year < other.year
        elif isinstance(other, int):
            return self.year < other
        else:
            raise TypeError("Можно сравнивать только с книгой или годом")

    def __gt__(self, other):
        if isinstance(other, Book):
            return self.year > other.year
        elif isinstance(other, int):
            return self.year > other
        else:
            raise TypeError("Можно сравнивать только с книгой или годом")

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.year == other.year
        elif isinstance(other, int):
            return self.year == other
        else:
            raise TypeError("Можно сравнивать только с книгой или годом")

    # Остальные методы класса
    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Название: {self.title}")
        print(f"Автор(ы): {', '.join(self.authors)}")
        print(f"Издательство: {self.publisher}")
        print(f"Год издания: {self.year}")
        print(f"Количество страниц: {self.pages}")
        print(f"Цена: {self._price}")
        print(f"Тип переплета: {self.binding_type}")
        print("-" * 30)

    @staticmethod
    def is_valid_year(year):
        return year > 0

    @classmethod
    def create_book(cls, id, title, authors, publisher, year, pages, price, binding_type):
        if not cls.is_valid_year(year):
            raise ValueError("Некорректный год издания")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        return cls(id, title, authors, publisher, year, pages, price, binding_type)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value


# Создаем список книг
books = [
    Book.create_book(1, "Война и мир", ["Лев Толстой"], "Эксмо", 1869, 1225, 1500, "Твердый"),
    Book.create_book(2, "Преступление и наказание", ["Федор Достоевский"], "АСТ", 1866, 608, 1200, "Мягкий"),
    Book.create_book(3, "1984", ["Джордж Оруэлл"], "Азбука", 1949, 320, 800, "Твердый"),
    Book.create_book(4, "Мастер и Маргарита", ["Михаил Булгаков"], "Эксмо", 1967, 480, 1100, "Твердый"),
    Book.create_book(5, "Гарри Поттер и философский камень", ["Джоан Роулинг"], "Росмэн", 1997, 400, 900, "Мягкий"),
]


# Пример использования оператора >
print("\nКниги, выпущенные после 1900 года:")
for book in books:
    if book > 1900:
        print(book)