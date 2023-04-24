#Задание 1.
#Используя механизм множественного наследования разработайте класс
#«Автомобиль». Создайте несколько классов-наследников согласно
#классификации. Используя классы-миксины «примешайте» к классам
#наследникам методы, которые выводят информацию об объекте из классов
#«Колесо», «Двигатель», «Двери» и т.п.
def execute_application():
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

    class SportCar(Car, Wheel, Engine):
        def __init__(self, brand: str, model: str, color: str, size: int, material: str, power: int, fuel_type: str):
            Car.__init__(self, brand, model, color)
            Wheel.__init__(self, size, material)
            Engine.__init__(self, power, fuel_type)

        def sportcar_info(self):
            print(f"Бренд: {self.__brand}\nМодель: {self.__model}\nЦвет: {self.__color}")
            Wheel.wheel_info(self)
            Engine.engine_info(self)

    class SUV(Car, Wheel, Door):
        def __init__(self, brand: str, model: str, color: str, size: int, material: str, number: int, isopen: bool):
            Car.__init__(self, brand, model, color)
            Wheel.__init__(self, size, material)
            Door.__init__(self, number, isopen)

        def suvinfo(self):
            print(f"Бренд: {self.__brand}\nМодель: {self.__model}\nЦвет: {self.__color}")
            Wheel.wheel_info(self)
            Door.door_info(self)

    class Truck(Car, Wheel):
        def __init__(self, brand: str, model: str, color: str, size: float, material: str, max_load: int):
            Car.__init__(self, brand, model, color)
            Wheel.__init__(self, size, material)
            self.max_load = max_load

        def truck_info(self):
            print(f"Бренд: {self.__brand}\nМодель: {self.__model}\nЦвет: {self.__color}")
            Wheel.wheel_info(self)
            print(f"Максимальная нагрузка: {self.max_load} кг")
if __name__ =="__main__":
    execute_application()