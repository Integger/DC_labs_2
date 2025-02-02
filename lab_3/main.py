class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        self.__pages = pages

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, new_value):
        if not isinstance(new_value, int):
            raise ValueError("Значение, описывающее количество страниц книги должно быть представленно в виде целого числа.")

        if new_value <= 0:
            raise ValueError("Значение, описывающее количество страниц книги должно быть положительным.")

        self.__pages = new_value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, new_value):
        if not isinstance(new_value, float):
            raise ValueError("Значение, описывающее продолжительность книги должно быть представленно в виде типа float.")

        if new_value <= 0.0:
            raise ValueError("Значение, описывающее продолжительность книги должно быть положительным.")

        self.__duration = new_value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

# Пример использования
try:
    paper_book = PaperBook("1984", "Иоганн Вольфганг фон Гёте", 328)
    audio_book = AudioBook("Анна Каренина", "Лев Николаевич Толстой", 34.36)

    print(paper_book)
    print(audio_book)

    # Попробуем установить некорректные значения
    audio_book.duration = -0.1  # Это вызовет ValueError
except ValueError as e:
    print(e)