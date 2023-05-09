import pickle
import json
#Задание 4
#К уже реализованному классу «Часы» добавьте возможность упаковки и распаковки данных с использованием json и pickle.
class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def to_dict(self):
        return {"hours": self.hours, "minutes": self.minutes, "seconds": self.seconds}
    def from_dict(self, dict_data):
        self.hours = dict_data["hours"]
        self.minutes = dict_data["minutes"]
        self.seconds = dict_data["seconds"]

    def save_to_json(self, file_path):
        with open(file_path, "w") as f:
            json.dump(self.to_dict(), f)

    def load_from_json(self, file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
            self.from_dict(data)

    def save_to_pickle(self, file_path):
        with open(file_path, "wb") as f:
            pickle.dump(self.to_dict(), f)

    def load_from_pickle(self, file_path):
        with open(file_path, "rb") as f:
            data = pickle.load(f)
            self.from_dict(data)
def  execute_application():
    clock = Clock(12, 30, 45)
    clock.save_to_json("clock.json")
    clock.save_to_pickle("clock.pickle")

    new_clock = Clock()
    new_clock.load_from_json("clock.json")
    print(new_clock)

    new_clock.load_from_pickle("clock.pickle")
    print(new_clock)
if __name__=="__main__":
    execute_application()