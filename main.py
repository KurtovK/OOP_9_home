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
    def wheel_info(self):
        print(f"Размер: {self.__size}\nМатериал: {self.__material}")
class Engine:
    def __init__(self, power: int, fuel_type: str):
        self.__power = power
        self.__fuel_type = fuel_type

    def engine_info(self):
        print(f"Мощность: {self.__power}\nТип топлива: {self.__fuel_type}")
class Door:
    def __init__(self, number: int, isopen: bool):
        self.__number = number
        self.__isopen = isopen

    def door_info(self):
        if self.__isopen:
            print(f"Дверь {self.__number} открыта")
        else:
            print(f"Дверь {self.__number} закрыта")

def executer_application():
    pass
if __name__ =="__main__":
    executer_application()