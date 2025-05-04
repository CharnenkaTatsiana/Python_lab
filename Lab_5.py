class Book:
    # Статическое поле
    total_books = 0

    def __init__(self, id, title, authors, publisher, year, pages, price, binding_type):
        # Динамические поля
        self.id = id
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self._price = price  # Инкапсулированное поле
        self.binding_type = binding_type
        Book.total_books += 1

    # Метод объекта
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

    # Статический метод
    @staticmethod
    def is_valid_year(year):
        return year > 0

    # Метод класса
    @classmethod
    def create_book(cls, id, title, authors, publisher, year, pages, price, binding_type):
        if not cls.is_valid_year(year):
            raise ValueError("Некорректный год издания")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        return cls(id, title, authors, publisher, year, pages, price, binding_type)

    # Getter и Setter для инкапсулированного поля price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value


# Создаем список объектов Book
books = [
    Book.create_book(1, "Война и мир", ["Лев Толстой"], "Эксмо", 1869, 1225, 1500, "Твердый"),
    Book.create_book(2, "Преступление и наказание", ["Федор Достоевский"], "АСТ", 1866, 608, 1200, "Мягкий"),
    Book.create_book(3, "1984", ["Джордж Оруэлл"], "Азбука", 1949, 320, 800, "Твердый"),
    Book.create_book(4, "Мастер и Маргарита", ["Михаил Булгаков"], "Эксмо", 1967, 480, 1100, "Твердый"),
    Book.create_book(5, "Гарри Поттер и философский камень", ["Джоан Роулинг"], "Росмэн", 1997, 400, 900, "Мягкий"),
]


# Функция для вывода списка книг заданного автора
def books_by_author(author):
    return [book for book in books if author.lower() in [a.lower() for a in book.authors]]


# Функция для вывода списка книг, выпущенных после заданного года
def books_after_year(year):
    return [book for book in books if book.year > year]


# Пример использования
print("Книги Льва Толстого:")
for book in books_by_author("Лев Толстой"):
    book.display_info()

print("\nКниги, выпущенные после 1900 года:")
for book in books_after_year(1900):
    book.display_info()

# Пример работы с инкапсуляцией
try:
    book = books[0]
    print(f"Текущая цена книги: {book.price}")
    book.price = 1600  # Корректное значение
    print(f"Новая цена книги: {book.price}")
    book.price = -100  # Некорректное значение
except ValueError as e:
    print(f"Ошибка: {e}")