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