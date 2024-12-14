import doctest

class Fork:
    def __init__(self, tine_length = 1):
        """
        Создание и подготовка к работе объекта "Вилка"

        :param tine_length: Длина зубьев вилки

        Примеры:
        >>> fork = Fork(4)  # Инициализация экземпляра класса
        """
        self.tine_length = tine_length if tine_length < 25 else 1

    def use(self):
        """
        Использование объекта "Вилка"

        Примеры:
        >>> fork = Fork(4)  # Инициализация экземпляра класса
        >>> fork.use()  # Использование вилки
        It's time to grab something tasty!
        Food can be taken from a distance of 4 centimeters
        """
        print('It\'s time to grab something tasty!')
        print(f'Food can be taken from a distance of {self.tine_length} centimeters')

    def increase_tine_length(self):
        """
        Увеличить длину зубьев объекта "Вилка"

        Примеры:
        >>> fork = Fork(4)  # Инициализация экземпляра класса
        >>> fork.increase_tine_length()  # Увеличение зубьев вилки
        """
        if self.tine_length < 25:
            self.tine_length += 1
        else:
            print('The fork has the maximum allowable tine length')


class Spoon:
    def __init__(self, bottom_depth = 1):
        """
        Создание и подготовка к работе объекта "Ложка"

        :param bottom_depth: Глубина дна ложки

        Примеры:
        >>> spoon = Spoon(7)  # Инициализация экземпляра класса
        """
        self.bottom_depth = bottom_depth if bottom_depth < 10 else 1

    def use(self):
        """
        Использование объекта "Ложка"

        Примеры:
        >>> spoon = Spoon(7)  # Инициализация экземпляра класса
        >>> spoon.use()  # Использование ложки
        It's time to reduce the volume of borscht in the plate!
        Its volume will be reduced by about 7 milliliters
        """
        print('It\'s time to reduce the volume of borscht in the plate!')
        print(f'Its volume will be reduced by about {self.bottom_depth} milliliters')

    def enhance_depth(self):
        """
        Создание и подготовка к работе объекта "Нож"

        Примеры:
        >>> spoon = Spoon(4)  # Инициализация экземпляра класса
        >>> spoon.enhance_depth()  # Углубляем дно ложки
        """
        if self.bottom_depth < 10:
            self.bottom_depth += 1
        else:
            print('The spoon has a maximum level of depth')


class Table:
    def __init__(self):
        """
        Создание и подготовка к работе объекта "Стол"

        Примеры:
        >>> table = Table()  # Инициализация экземпляра класса
        """
        self.fork = Fork()  # Динамическая инициализация вилки
        self.spoon = Spoon()  # Динамическая инициализация ложки
        self.active_item = None  # Изначально активный предмет отсутствует

    def take_item(self, item_name) -> None:
        """
        Получение хранящегося объекта, зависящего от переданных параметров из объекта "Стол"

        :param item_name: Название объекта, который следует взять для использования

        Примеры:
        >>> table = Table()  # Инициализация экземпляра класса
        >>> table.take_item('spoon')
        """

        if not isinstance(item_name, str):
            raise TypeError("item_name must be a string")

        if item_name.lower() == 'fork':
            self.active_item = self.fork
        elif item_name.lower() == 'spoon':
            self.active_item = self.spoon
        else:
            raise ValueError(f'Unable to take {item_name}')

    def use_active_item(self) -> None:
        """
        Использование активного объекта из объекта "Стол"

        Примеры:
        >>> table = Table()  # Инициализация экземпляра класса
        >>> table.take_item('fork')  # Выбор вилки в качестве активного объекта
        >>> table.use_active_item()  # Использование вилки в качестве активного предмета
        It's time to grab something tasty!
        Food can be taken from a distance of 1 centimeters
        """
        self.active_item.use()

    def get_active_item(self):
        """
        Получение активного объекта из объекта "Стол"

        Примеры:
        >>> table = Table()  # Инициализация экземпляра класса
        >>> table.take_item('fork')  # Выбор вилки в качестве активного объекта
        >>> table.get_active_item().increase_tine_length()  # Использование вилки в качестве активного предмета
        """
        return self.active_item

if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров, которые находятся в документации