class Vehicle:
    """
    Базовый класс в который входят автобусы и грузовики.
    """

    def __init__(self, name: str, price: float, max_speed: float, weight: float) -> None:
        """
        Инициализация транспортного средства.

        :param name: Название транспортного средства.
        :param price: Стоимость транспортного средства в рублях.
        :param max_speed: Максимальная скорость транспортного средства в км/ч.
        :param weight: Вес транспортного средства в килограммах.

        Переменные инкапсулированны с целью предупреждения их прямого изменения.
        """
        self._name = name
        self._price = price
        self._max_speed = max_speed
        self._weight = weight
        self._is_started = False

    def turn_start_key(self) -> None:
        """
        Изменяет состояние транспортного средства на противоположное (т.е. включает/выключает)
        """
        self._is_started = not self._is_started

    def print_state(self) -> None:
        """
        Выводит информацию о том, в каком состоянии пребывает транспортное средство (т.е. включенное/ не выключенное)
        """
        print("Транспортное средство находится в " + ("включённом" if self._is_started else "выключенном") + "состоянии.")

    def __str__(self) -> str:
        """
        Рекламное сообщение в строковом формате.

        :return: Строка с информацией о транспортном средстве.
        """
        return f"Не упустите шанс приобрести новое транспортное средство под названием {self._name}, покупая его всего за какие-то {self._price} рублей, Вы получаете идеальное сочетание веса транспортного средства {self._weight} кг и его скорости {self._max_speed} км/ч."

    def __repr__(self) -> str:
        """
        Возвращает строку для инициализации подобного класса.

        :return: Строка для инициализации подобного класса.
        """
        return f"Vehicle(name='{self._name}', price={self._price}, max_speed={self._max_speed}, weight={self._weight})"

class Bus(Vehicle):
    """
    Класс для автобусов.
    """

    def __init__(self, name: str, price: float, max_speed: float, weight: float, passenger_capacity: int) -> None:
        """
        Инициализация автобуса.

        :param name: Название автобуса.
        :param price: Стоимость автобуса в рублях.
        :param max_speed: Максимальная скорость автобуса в км/ч.
        :param weight: Вес автобуса в килограммах.
        :param passenger_capacity: Вместимость автобуса по количеству пассажиров.
        """
        super().__init__(name, price, max_speed, weight)

        self._passenger_capacity = passenger_capacity
        self._number_of_passengers = 0

    def get_passenger(self) -> None:
        """
        Подобрать пассажира в автобус.
        """
        if self._number_of_passengers >= self._passenger_capacity:
            print("Тесниться более невозможно! В автобусе уже нет места для нового пассажира!")
        else:
            self._number_of_passengers += 1
            print("Ещё один пассажир был успешно принят на борт автобуса.")

    def eject_passenger(self) -> None:
        """
        Изгнать пассажира из автобуса.
        """
        if self._number_of_passengers <= 0:
            print("Кажется Вам показалось, что помимо Вас в автобусе кто-то присутствует...")
        else:
            self._number_of_passengers -= 1
            print("На одного пассажира в автобусе стало меньше...")

    def __repr__(self) -> str:
        """
        Возвращает строку для инициализации подобного класса.

        :return: Строка для инициализации подобного класса.
        """
        return f"Bus(name='{self._name}', price={self._price}, max_speed={self._max_speed}, weight={self._weight}, passenger_capacity={self._passenger_capacity})"


class Truck(Vehicle):
    """
    Класс для грузовиков.
    """

    def __init__(self, name: str, price: float, max_speed: float, weight: float, load_capacity: float) -> None:
        """
        Инициализация грузовика.

        :param name: Название грузовика.
        :param price: Стоимость грузовика в рублях.
        :param max_speed: Максимальная скорость грузовика в км/ч.
        :param weight: Вес грузовика в килограммах.
        :param load_capacity: Грузоподъемность грузовика в килограммах.
        """
        super().__init__(name, price, max_speed, weight)

        self._load_capacity = load_capacity
        self._current_load = 0

    def add_load(self, weight: float) -> None:
        """
        Добавить грузу в грузовик.

        :param weight: Вес добавляемого груза.
        """
        if self._current_load + weight > self._load_capacity:
            print(f"При попытке закинуть кирпич в кузов он прилетел к Вам обратно в руки...")
        elif weight < 0:
            print("Смешно, но вы не можете закинуть отрицательный вес!")
        else:
            self._current_load += weight
            print(f"Кирпичи успешно закинуты! Теперь в грузовике {self._name} {self._current_load} кг груза!")

    def remove_load(self, weight: float) -> None:
        """
        Снизить нагруженность грузовика.

        :param weight: Вес удаляемого груза.
        """
        if self._current_load - weight < 0:
            print(f"Судя по всему, вы пытаетесь вытащить больше, чем в кузове. Грузовик уже готов написать мемуары под названием 'Как я сбросил 500 килограммов'.")
        else:
            self._current_load -= weight
            print(f"Кирпичи успешно убраны! Теперь в грузовике {self._name} {self._current_load} кг груза!")

    def __repr__(self) -> str:
        """
        Возвращает строку для инициализации подобного класса.

        :return: Строка для инициализации подобного класса.
        """
        return f"Truck(name='{self._name}', price={self._price}, max_speed={self._max_speed}, weight={self._weight}, load_capacity={self._load_capacity}, current_load={self._current_load})"

if __name__ == "__main__":
    truck = Truck("Volvo FH", 8500500, 90, 8000, 20955)

    # Добавление груза
    truck.add_load(5000)
    truck.add_load(16000)  # Пробуем добавить еще 16000 кг, что превышает грузоподъемность
    truck.add_load(-1000)  # Пробуем закинуть отрицательный вес

    truck.remove_load(3000)
    truck.remove_load(25000)  # Пробуем удалить 25000 кг, когда их меньше

    print(truck)
    print(repr(truck))

    bus = Bus("Mercedes Sprinter", 5600200, 100, 3500, 20)

    bus.get_passenger()
    bus.get_passenger()
    bus.get_passenger()

    bus.eject_passenger()
    bus.eject_passenger()
    bus.eject_passenger()
    bus.eject_passenger() # Пробуем убрать пассажира из пустого автобуса

    print(bus)
    print(repr(bus))

    pass
