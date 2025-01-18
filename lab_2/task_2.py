BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Процедура инициализация книги

        :id_:   id книги
        :name:  название книги
        :pages: количество страниц в книге
        """

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строку с названием книги

        :return: Книга "название книги"
        """

        return str(f'Книга "{self.name}"')

    def __repr__(self):
        """
        Возвращает выражение, которое может быть использована для инициализации аналогичного класса

        :return: Выражение для инициализации аналогичного класса
        """

        return str(f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})')


# TODO написать класс Library
class Library:
    def __init__(self, books: list[Book] = None):
        """
        Процедура инициализации библиотеки

        :param books: Лист, состоящий из класса Book
        """

        self.books = books

        if books is None:
            self.max_id = 0
        else:
            self.max_id = max(books, key=lambda book: book.id).id

    def get_next_book_id(self):
        """
        Возвращает свободное id

        :return: Максимальное значение id, увеличенное на 1
        """

        return self.max_id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Проверяет на наличие книги с переданным в качестве параметра book_id и в случае её наличия возвращает индекс под которым книга хранится в листе
        В случае отсутствия книги генерируется ошибка с текстом "Книги с запрашиваемым id не существует"

        :param book_id:  Проверяемый id книги
        :return: Индекс, под которым хранится книга с переданным book_id
        """

        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index

        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
