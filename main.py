from typing import Dict
import json
import pickle
#Задание 1.
#К уже реализованному классу «Автомобиль» добавьте
#возможность упаковки и распаковки данных с использованием json и pickle.
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
#Задание 2
#К уже реализованному классу «Книга» добавьте возможность упаковки и распаковки данных
# с использованием json и pickle.
class Book:
    title: str
    author: str
    year: int
    genre: str
    price: float
    # Конструктор по умолчанию
    def __init__(self, title: str, author: str, year: int, genre: str, price: float):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.price = price

    # Метод для вывода данных
    def __str__(self):
        return f"Название книги: {self.title}\n" \
               f"Автор: {self.author}\n" \
               f"Год выпуска: {self.year}\n"\
               f"Жанр: {self.genre}\n" \
               f"Цена: {self.price}\n"

    # Метод для создания объекта класса на основе словаря
    @classmethod
    def from_dict(cls, book_dict: Dict[str, any]) -> 'Book':
        return cls(book_dict['title'], book_dict['author'], book_dict['year'],
                   book_dict['genre'], book_dict['price'])

    # Метод для преобразования объекта класса в словарь
    def to_dict(self) -> Dict[str, any]:
        return {"title": self.title,
                "author": self.author,
                "year": self.year,
                "genre": self.genre,
                "price": self.price}
def execute_application():
    pass





if __name__=="__main__":
    execute_application()