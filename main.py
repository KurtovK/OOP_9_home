# Задача 1
#Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных операторов:
#Проверка на равенство радиусов двух окружностей (операция ==, !=);
#Проверка сравнения длин двух окружностей (операции >, <, <=,>=);
class Circle:
    def __init__(self, radius: float):
        self.__radius = radius

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