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


    def __eq__(self, other):
        return self.__radius == other.__radius

    def __ne__(self, other):
        return self.__radius != other.__radius

    def __lt__(self, other):
        return self.__radius < other.__radius

    def __gt__(self, other):
        return self.__radius > other.__radius

    def __le__(self, other):
        return self.__radius <= other.__radius

    def __ge__(self, other):
        return self.__radius >= other.__radius

def execute_application():
    pass
if __name__=="__main__":
    execute_application()