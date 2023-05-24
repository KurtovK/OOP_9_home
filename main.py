from math import pi

# Задача 1
#Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных операторов:
#Проверка на равенство радиусов двух окружностей (операция ==, !=);
#Проверка сравнения длин двух окружностей (операции >, <, <=,>=);
#Пропорциональное изменение размеров окружности, путем изменения
#ее радиуса (операции + - += -=)


class InitializationValueError(Exception):
    def __init__(self, text):
        self.text = text

class Circle:
    def __init__(self, radius: float):
        self.__radius = self.validate_radius(radius)
        self.__circumference = 2 * pi * self.__radius

    def validate_radius(self, radius: float):
        if radius <= 0:
            raise InitializationValueError("Радиус должен быть больше нуля.")
        return radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius (self, value):
        self.__radius = value

    def __is_circle(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"Сравнение выполнить невозможно "
                            f"между типом {self.__class__.__name__} "
                            f"а также {other.__class__.__name__}")

    def __eq__(self, other):
        self.__is_circle(other)
        return self.__radius == other.__radius

    def __ne__(self, other):
        self.__is_circle(other)
        return self.__radius != other.__radius

    def __lt__(self, other):
        self.__is_circle(other)
        return self.__circumference < other.__circumference

    def __gt__(self, other):
        self.__is_circle(other)
        return self.__circumference > other.__circumference

    def __le__(self, other):
        self.__is_circle(other)
        return self.__circumference <= other.__circumference

    def __ge__(self, other):
        self.__is_circle(other)
        return self.__circumference >= other.__circumference

    def __hash__(self):
        return hash(self.__radius, self.__circumference)
    def __add__(self, other):
        if isinstance(other, int | float):
            if other < 0 and abs(other) >= self.__radius:
                raise InvalidValueError(
                    f"Ошибка!!!Выполнить сложения с отрицательным числом невозможно, с большим числом чем радиус"
                    f" Радиус не может быть меньше или равен нулю")
            cir = self.__radius + other
            return Circle(cir)

        if isinstance(other, Circle):
            cir = self.__radius + other.__radius
            return Circle(cir)
        raise TypeError(
            f"Невозможно выполнить сложение между  {self.__class__.__name__} и {other.__class__.__name__}.")

    def __sub__(self, other):
        if isinstance(other, int | float):
            if abs(other) >= self.__radius and other < 0:
                raise InvalidValueError(
                    f"Ошибка!!!Модуль вычитаемого числа больше либо равен, чем число радиуса."
                    f" Радиус не может быть меньше или равен нулю")
            cir = self.__radius - other
            return Circle(cir)

        if isinstance(other, Circle):
            if other.__radius >= self.__radius:
                raise InvalidValueError(
                    f"Ошибка!!!Величина вычитаемого радиуса больше либо равна, чем число радиуса из которого вычитаем. "
                    f" Радиус не может быть меньше или равен нулю")
            cir = self.__radius - other.__radius
            return Circle(cir)
        raise TypeError(
            f"Невозможно выполнить вычитание между  {self.__class__.__name__} и {other.__class__.__name__}.")

    def __iadd__(self, other):
        if isinstance(other, int | float):
            if abs(other) >= self.__radius and other < 0:
                raise InvalidValueError(
                    f"Ошибка!!! Выполнить операцию сложения с отрицательным числом, большим по модулю невозможно "
                    f" Радиус не может быть меньше или равен нулю")
            self.__radius = self.__radius + other
            return self

        if isinstance(other, Circle):
            self.__radius = self.__radius + other.__radius
            return self
        raise TypeError(
            f"Невозможно выполнить сложение с присваиванием между  {self.__class__.__name__} и "
            f"{other.__class__.__name__}.")

    def __isub__(self, other):
        if isinstance(other, int | float):
            if abs(other) >= self.__radius:
                raise InvalidValueError(
                    f"Ошибка!! Выполнить операцию сложения с отрицательным числом, большим по модулю невозможно "
                    f" Радиус не может быть меньше или равен нулю")
            self.__radius = self.__radius - other
            return self

        if isinstance(other, Circle):
            if other.__radius >= self.__radius:
                raise InvalidValueError(
                    f"Ошибка!!!Число вычитаемого радиуса больше либо равна, чем число радиуса из которого вычитаем. "
                    f" Радиус не может быть меньше или равен нулю")
            self.__radius = self.__radius - other.__radius
            return self

        raise TypeError(
            f"Невозможно выполнить вычитание с присваиванием между {self.__class__.__name__} и "
            f"{other.__class__.__name__}.")


def execute_application():
    c1 = Circle(5)
    c2 = Circle(3)
    try:
        print("Проверка на равенство(=):", c1 == c2)
        print("Проверка на не равенство(!=):", c1 != c2)
        print("Проверка на меньше(<):", c1 < c2)
        print("Проверка на больше(>):", c1 > c2)
        print("Проверка на меньше или равно(<=):", c1 <= c2)
        print("Проверка на больше или равно(>=):", c1 >= c2)
    except TypeError as e:
        print(e)
    print()
    print(f"Изменение радиуса окружности:")

    c3 = Circle(3)
    c4 = Circle(5)

    try:
        circle_5 = c4 + 20
        print(f"\nОперация сложения: {circle_5.radius}.")

        circle_5 = c4 - 6
        print(f"Операция вычитания: {circle_5.radius}.")

        circle_5 += 3
        print(f"Операция сложения с присваиванием:  {circle_5.radius}.")

        circle_5 -= 1
        print(f"Операция вычитания с присваиванием: {circle_5.radius}.")

    except Exception as e:
        print(e)

if __name__=="__main__":
    execute_application()
