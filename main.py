#Задание 1.
#Используя механизм множественного наследования разработайте класс
#«Автомобиль». Создайте несколько классов-наследников согласно
#классификации. Используя классы-миксины «примешайте» к классам
#наследникам методы, которые выводят информацию об объекте из классов
#«Колесо», «Двигатель», «Двери» и т.п.


class Wheel:
    def __init__(self, size: int, material: str):
        self.size = size
        self.material = material
    def wheel_info(self):
        print(f"Размер: {self.size}\nМатериал: {self.material}")
class Engine:
    def __init__(self, power: int, fuel_type: str):
        self.power = power
        self.fuel_type = fuel_type

    def engine_info(self):
        print(f"Мощность: {self.power}\nТип топлива: {self.fuel_type}")
class Door:
    def __init__(self, number: int, isopen: bool):
        self.number = number
        self.isopen = isopen

    def door_info(self):
        if self.isopen:
            print(f"Дверь {self.number} открыта")
        else:
            print(f"Дверь {self.number} закрыта")
class Car:
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color
class SportCar(Car, Wheel, Engine):
    def __init__(self, brand: str, model: str, color: str, size: int, material: str, power: int, fuel_type: str):
        Car.__init__(self, brand, model, color)
        Wheel.__init__(self, size, material)
        Engine.__init__(self, power, fuel_type)

    def sportcar_info(self):
        print(f"Бренд: {self.brand}\nМодель: {self.model}\nЦвет: {self.color}")
        Wheel.wheel_info(self)
        Engine.engine_info(self)

class SUV(Car, Wheel, Door):
    def __init__(self, brand: str, model: str, color: str, size: int, material: str, number: int, isopen: bool):
        Car.__init__(self, brand, model, color)
        Wheel.__init__(self, size, material)
        Door.__init__(self, number, isopen)

    def suv_info(self):
        print(f"Бренд: {self.brand}\nМодель: {self.model}\nЦвет: {self.color}")
        Wheel.wheel_info(self)
        Door.door_info(self)

class Truck(Car, Wheel):
    def __init__(self, brand: str, model: str, color: str, size: int, material: str, max_load: int):
        Car.__init__(self, brand, model, color)
        Wheel.__init__(self, size, material)
        self.max_load = max_load

    def truck_info(self):
        print(f"Бренд: {self.brand}\nМодель: {self.model}\nЦвет: {self.color}")
        Wheel.wheel_info(self)
        print(f"Максимальная нагрузка: {self.max_load} кг")

class ElectricCar(Car, Wheel, Engine):
    def __init__(self, brand: str, model: str, color: str, size: int, material: str, power: int, fuel_type: str,
                 batterycapacity: int):
        Car.__init__(self, brand, model, color)
        Wheel.__init__(self, size, material)
        Engine.__init__(self, power, fuel_type)
        self.batterycapacity = batterycapacity

    def electriccar_info(self):
        print(f"Бренд: {self.brand}\nМодель: {self.model}\nЦвет: {self.color}")
        Wheel.wheel_info(self)
        Engine.engine_info(self)
        print(f"Емкость батареи: {self.batterycapacity} кВтч")
def execute_application():
    sportcar = SportCar("Ferrari", "488 GTB", "Красный", 20, "Углеродное волокно", 670, "Бензин")
    suv = SUV("Jeep", "Wrangler", "Зеленый", 18, "Сталь", 4, True)
    electriccar = ElectricCar("Tesla", "Model S", "Черный", 19, "Алюминий", 500, "Электричество", 100)
    truck = Truck("Volvo", "VNL 860", "Белый", 22.5, "Резина", 20000)

    # Вывод информации о каждом объекте
    print("Спортивная машина:")
    sportcar.sportcar_info()
    print("\nВнедорожник:")
    suv.suv_info()
    print("\nЭлектромобиль:")
    electriccar.electriccar_info()
    print("\nГрузовик:")
    truck.truck_info()

if __name__ =="__main__":
    execute_application()