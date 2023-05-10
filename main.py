from random import randint
#Задание 1.
#Используя механизм множественного наследования разработайте класс
#«Автомобиль». Создайте несколько классов-наследников согласно
#классификации. Используя классы-миксины «примешайте» к классам
#наследникам методы, которые выводят информацию об объекте из классов
#«Колесо», «Двигатель», «Двери» и т.п.

class Conditioner:
    def __init__(self):
        self.__status = False
    @property
    def status_conditioner(self):
        return self.__status
    @status_conditioner.setter
    def status_conditioner(self, status: bool):
        self.__status = status
    def conditioner_info(self):
        return "Кондиционер " + ("включён." if self.__status else "выключен.")
class StatusConditionerMixin:
    @staticmethod
    def get_status_conditioner(conditioner: Conditioner):
        print(conditioner.conditioner_info())


class Engine:
    def __init__(self):
        self.__status_engine = False
    @property
    def state(self):
        return self.__status_engine
    @state.setter
    def state(self, status: bool):
        self.__status_engine = status
    def engine_info(self):
        return "Двигатель " + ("заведен." if self.__status_engine else "не заведен.")
class EngineConditionMixin:
    @staticmethod
    def get_status_engine(engine: Engine):
        print(engine.engine_info())

class RadioWave:
    MIN = 87.5
    MAX = 108.0
    def __init__(self):
        self.__value = randint(875, 1080) / 10
    @classmethod
    def check_current_wave(cls, value: float = 0):
        if isinstance(value, float | int) and RadioWave.MIN <= value <= RadioWave.MAX:
            return "Нормальный диапазон FM радио"
        raise Exception(f"Некорректное значение FM радио: {value}")
class RadioWaveMixin:
    @staticmethod
    def check_current_wave(wave: RadioWave, value: float = RadioWave.MIN):
        return wave.check_current_wave(value)


class Car:
    def __init__(self, car_model: str, car_body: str, color: str, year: int):
        self.__car_model = car_model
        self.__car_body = car_body
        self.__color = color
        self.__year = year
    def info(self):
        print(f"Модель: {self.__car_model}, Кузов: {self.__car_body}, Цвет: {self.__color}, Год выпуска: {self.__year},"
              , end=" ")

class CarGasEngine(Car, EngineConditionMixin, RadioWaveMixin, StatusConditionerMixin):
    def __init__(self, car_model: str, car_body: str, color: str, year: int, power: str = None):
        super().__init__(car_model, car_body, color, year)
        self.__power = power
    def info(self):
        super().info()
        print(f"Марка бензина: {self.__power}")

class CarDieselEngine(Car, EngineConditionMixin, RadioWaveMixin, StatusConditionerMixin):
    def __init__(self, brand: str, model: str, color: str, year: int, power: str):
        super().__init__(brand, model, color, year)
        self.__power = power
    def info(self):
        super().info()
        print(f"Тип дизельного топлива: {self.__power}")

def execute_application():
    gas_car = CarGasEngine("Ferrari", "488 GTB", "Красный", 2015, "Бензин 95")
    gas_car.info()

    # Проверка двигателя
    gas_engine = Engine()
    gas_car.get_status_engine(gas_engine)

    # Проверка радио
    gas_car_tyre = RadioWave()
    try:
        print(gas_car.check_current_wave(gas_car_tyre, 66.6))
    except Exception as e:
        print(e)

    # Проверка кондиционера
    conditioner = Conditioner()
    gas_car.get_status_conditioner(conditioner)
    print()

    # Машина с дизельным двигателем
    diesel_car = CarDieselEngine("Jeep", "Wrangler", "Зеленый", 2021, "ДТЛ")
    diesel_car.info()

    # Проверка статуса двигателя
    diesel_engine = Engine()
    diesel_engine.state = True
    diesel_car.get_status_engine(diesel_engine)
    # Проверка радио
    diesel_car_radio = RadioWave()
    try:
        print(diesel_car.check_current_wave(diesel_car_radio, 87.9))
    except Exception as e:
        print(e)

    # Проверка кондиционера
    conditioner.status_conditioner = True
    diesel_car.get_status_conditioner(conditioner)

if __name__ == '__main__':
    execute_application()