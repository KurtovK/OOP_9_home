from math import pi
# Задача 1
#Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных операторов:
#Проверка на равенство радиусов двух окружностей (операция ==, !=);
#Проверка сравнения длин двух окружностей (операции >, <, <=,>=);
class InitializationValueError(Exception):
    def __init__(self, text):
        self.__text = text

class Circle:
    def __init__(self, radius: float):
        self.validate_radius(radius)
        self.radius = radius
        self.__circumference = self.calculate_circumference()

    def validate_radius(self, radius: float):
        if radius <= 0:
            raise InitializationValueError("Радиус должен быть больше нуля.")

    def calculate_circumference(self):
        return 2 * pi * self.radius

    def __is_circle(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"Сравнение выполнить невозможно "
                            f"между типом {self.__class.name} "
                            f"а также {other.__class.name}")

from math import pi

class InitializationValueError(Exception):
    def __init__(self, text):
        self.text = text

class Circle:
    def __init__(self, radius: float):
        self.validate_radius(radius)
        self.radius = radius
        self.__circumference = self.calculate_circumference()

    def validate_radius(self, radius: float):
        if radius <= 0:
            raise InitializationValueError("Радиус должен быть больше нуля.")

    def calculate_circumference(self):
        return 2 * pi * self.radius

    def __is_circle(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"Сравнение выполнить невозможно "
                            f"между типом {self.__class.name} "
                            f"а также {other.__class.name}")

    def __eq__(self, other):
        self.__is_circle(other)
        return self.radius == other.radius

    def __ne__(self, other):
        self.__is_circle(other)
        return self.radius != other.radius

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
        return hash((self.radius,))

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

if __name__=="__main__":
    execute_application()
