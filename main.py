#Задача 1
#Создайте класс Device, который содержит информацию об устройстве.
#С помощью механизма наследования, реализуйте класс CoffeeMachine
#(содержит информацию о кофемашине), класс Blender (содержит информацию
#о блендере).
class Device:
    def __init__(self, name: str, brand: str, model: str):
        self.__name = name
        self.__brand = brand
        self.__model = model

def excute_application():
    pass
if __name__=="__main__":
    excute_application()