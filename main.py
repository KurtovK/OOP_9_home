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
#Задание 3
#К уже реализованному классу «Стадион» добавьте
#возможность упаковки и распаковки данных с использованием json и pickle.
class Stadium:
    name: str
    opening_date: Dict[str, str]
    country: str
    city: str
    capacity: int
    def __init__(self, name: str, opening_date: Dict[str, str], country: str, city:str, capacity: int):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"Название: {self.name}\n"\
               f"Дата открытия:{self.opening_date}\n"\
               f"Страна: {self.country}\n"\
               f"Город:{self.city}\n"\
               f"Вместимость:{self.capacity}\n"



    # Метод для создания объекта класса на основе словаря
    @classmethod
    def from_dict(cls, stadium_dict):
        return cls(name=stadium_dict['name'],
                   opening_date=stadium_dict['opening_date'],
                   country=stadium_dict['country'],
                   city=stadium_dict['city'],
                   capacity=stadium_dict['capacity'])

    # Метод для преобразования объекта класса в словарь
    def to_dict(self):
        return {"name": self.name,
                "opening_date": self.opening_date,
                "country": self.country,
                "city": self.city,
                "capacity": self.capacity}
def execute_application():
    # Задание 1.
    car1 = Car('Sorento', 2021, 'KIA', 2.5, 'красный', 4079900)
    print(car1)
    # Упаковка и распаковка данных с использованием json
    car1_dict = car1.to_dict()
    car1_json = json.dumps(car1_dict)
    print(car1_json)
    car1_dict_from_json = json.loads(car1_json)
    car1_from_json = Car.from_dict(car1_dict_from_json)
    print(car1_from_json)
    # Упаковка и распаковка данных с использованием pickle
    car1_pickle = pickle.dumps(car1)
    car1_from_pickle = pickle.loads(car1_pickle)
    print(car1_from_pickle)
    # Задание 2.
    book1 = Book('Мастер и Маргарита', 'Михаил Булгаков', 1966, 'роман', 1500)
    print(book1)
    # Упаковка и распаковка данных с использованием json
    book1_dict = book1.to_dict()
    book1_json = json.dumps(book1_dict)
    print(book1_json)
    book1_dict_from_json = json.loads(book1_json)
    book1_from_json = Book.from_dict(book1_dict_from_json)
    print(book1_from_json)
    # Упаковка и распаковка данных с использованием pickle
    book1_pickle = pickle.dumps(book1)
    book1_from_pickle = pickle.loads(book1_pickle)
    print(book1_from_pickle)
    # Задание 3.
    stadium = Stadium('Шинник', {'день': '01', 'месяц': '01', 'год': '1957'}, 'Россия', 'Ярославль', 22990)
    print(stadium)
    # Упаковка и распаковка данных с использованием json
    stadium_dict = stadium.to_dict()
    stadium_json = json.dumps(stadium_dict)
    print(stadium_json)
    stadium_dict_from_json = json.loads(stadium_json)
    stadium_from_json = Stadium.from_dict(stadium_dict_from_json)
    print(stadium_from_json)
    # Упаковка и распаковка данных с использованием pickle
    stadium_pickle = pickle.dumps(stadium)
    stadium_from_pickle = pickle.loads(stadium_pickle)
    print(stadium_from_pickle)



if __name__=="__main__":
    execute_application()