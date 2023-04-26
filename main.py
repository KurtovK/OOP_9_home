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
        if radius <= 0:
            raise InitializationValueError("Радиус должен быть больше нуля.")
        self.__radius = radius
        self.__circumference = 2 * pi * self.__radius


    def __is_circle(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"Cравнение выполнить невозможно "
                            f"между типом {self.__class__.__name__} "
                            f"а также  {other.__class__.__name__}")

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
        return hash((self.__radius, self.__circumference))

def execute_application():
    pass
if __name__=="__main__":
    execute_application()