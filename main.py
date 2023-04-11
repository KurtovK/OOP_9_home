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



def excute_application():
    pass
if __name__=="__main__":
    excute_application()