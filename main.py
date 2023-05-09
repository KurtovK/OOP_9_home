import pickle
#Задание 1
#Создайте класс «Самолет».Наполните его необходимыми характеристиками и методами. Реализуйте упаковку и
#распаковку объектов класса «Самолет» с использованием модуля pickle.
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
def  execute_application():
    pass
if __name__=="__main__":
    execute_application()