#Задание 1.
#Используя механизм множественного наследования разработайте класс
#«Автомобиль». Создайте несколько классов-наследников согласно
#классификации. Используя классы-миксины «примешайте» к классам
#наследникам методы, которые выводят информацию об объекте из классов
#«Колесо», «Двигатель», «Двери» и т.п.
class Car:
    def __init__(self, brand: str, model: str , color: str):
        self.__brand = brand
        self.__model = model
        self.__color = color
class Wheel:
    def __init__(self, size: int, material: str):
        self.__size = size
        self.__material = material
def executer_application():
    pass
if __name__ =="__main__":
    executer_application()