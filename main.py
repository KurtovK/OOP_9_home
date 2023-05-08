from typing import Dict
import json
import pickle
#Задание 1.
#Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
#название модели, год выпуска, производителя, объем двигателя, цвет машины,
#цену. Реализуйте конструктор по умолчанию и метод для вывода данных.
class Car:
    model: str
    year: int
    manufacturer: str
    engine_volume: float
    color: str
    price: float
    def __init__(self, model: str, year: int,manufacturer: str,
                 engine_volume: float, color: str, price: float):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.color = color
        self.price = price


    def __str__(self):
        return f"Модель: {self.model}\n" \
               f"Год выпуска: {self.year}\n" \
               f"Производитель: {self.manufacturer}\n"\
               f"Объем двигателя: {self.engine_volume}\n" \
               f"Цвет машины: {self.color}\n" \
               f"Цена: {self.price}\n"
    def to_dict(self):
        return {"model": self.model,
                "year": self.year,
                "manufacturer": self.manufacturer,
                "engine_volume": self.engine_volume,
                "color": self.color,
                "price": self.price}

    @classmethod
    def from_dict(cls, car_dict):
        return cls(model=car_dict['model'],
                   year=car_dict['year'],
                   manufacturer=car_dict['manufacturer'],
                   engine_volume=car_dict['engine_volume'],
                   color=car_dict['color'],
                   price=car_dict['price'])


def execute_application():
    pass





if __name__=="__main__":
    execute_application()