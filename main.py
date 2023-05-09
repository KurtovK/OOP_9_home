import pickle
import json
#Задание 2
#Добавьте к заданию 1 возможность упаковки/распаковки с использованием модуля json.
class Airplane:
    def __init__(self, model, manufacturer, max_speed, max_altitude):
        self.model = model
        self.manufacturer = manufacturer
        self.max_speed = max_speed
        self.max_altitude = max_altitude
    def __str__(self):
        return f"Модель: {self.model}\nПроизводитель: {self.manufacturer}\nМаксимальная скорость: {self.max_speed} км/ч\nМаксимальная высота полета: {self.max_altitude} м"

    def to_dict(self):
        return {"model": self.model, "manufacturer": self.manufacturer, "max_speed": self.max_speed, "max_altitude": self.max_altitude}

    def from_dict(self, dict_data):
        self.model = dict_data["model"]
        self.manufacturer = dict_data["manufacturer"]
        self.max_speed = dict_data["max_speed"]
        self.max_altitude = dict_data["max_altitude"]

    def save_to_pickle(self, file_path):
        with open(file_path, "wb") as f:
            pickle.dump(self.to_dict(), f)

    def load_from_pickle(self, file_path):
        with open(file_path, "rb") as f:
            data = pickle.load(f)
            self.from_dict(data)

    def save_to_json(self, file_path):
        with open(file_path, "w") as f:
            json.dump(self.to_dict(), f)

    def load_from_json(self, file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
            self.from_dict(data)
def  execute_application():
    airplane = Airplane("Boeing 747", "Boeing", 920, 13100)
    airplane.save_to_pickle("airplane.pickle")
    airplane.save_to_json("airplane.json")

    new_airplane = Airplane("", "", 0, 0)
    new_airplane.load_from_pickle("airplane.pickle")
    print(new_airplane)

    new_airplane.load_from_json("airplane.json")
    print(new_airplane)
if __name__=="__main__":
    execute_application()