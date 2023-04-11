#Задача 1
#Создайте класс Device, который содержит информацию об устройстве.
#С помощью механизма наследования, реализуйте класс CoffeeMachine
#(содержит информацию о кофемашине), класс Blender (содержит информацию
#о блендере).
class Device:
    def __init__(self, brand: str, model: str,price: str):
        self.__brand = brand
        self.__model = model
        self.__price = price
    def info(self):
        print(f"\nКласс: {self.__class__.__name__}\n"
              f"Брэнд: {self.__brand}\n"
              f"Модель: {self.__model}\n"
              f"Цена: {self.__price}\n")

class CoffeeMachine(Device):
    def __init__(self,brand: str, model: str, price: str, power: str, water_capacity: str):
        super().__init__(brand, model, price)
        self.__power = power
        self.__water_capacity = water_capacity

    def info(self):
        super().info()
        print(f"Мощьность:{self.__power}\n"
              f"Емкость воды: {self.__water_capacity}")
class Blender(Device):
    def __init__(self, brand: str, model: str, price: str, power: str, speed: str):
        super().__init__(brand, model, price)
        self.__power = power
        self.__speed = speed
    def info(self):
        super().info()
        print(f"Мощьность: {self.__power}\n"
              f"Скорость: {self.__speed}")


def excute_application():
    device = Device("Redmond", "RT-23", 2100.0)
    device.info()

    coffee_machine = CoffeeMachine("DeLonghi", "EC155M", 9999.0, 1100, 1.1)
    coffee_machine.info()

    blender = Blender("Braun", "JB5160BK", 6999.0, 1000, 5)
    blender.info()
if __name__=="__main__":
    excute_application()