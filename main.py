import pickle
import json
#Задание 3
#К уже реализованному классу «Дробь» добавьте возможность упаковки и распаковки данных с использованием json и pickle.
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                            self.denominator * other.denominator)
        else:
            raise TypeError("Операция поддерживается только для объектов класса 'Дробь'")
    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                            self.denominator * other.denominator)
        else:
            raise TypeError("Операция поддерживается только для объектов класса 'Дробь'")
    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        else:
            raise TypeError("Операция поддерживается только для объектов класса 'Дробь'")
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        else:
            raise TypeError("Операция поддерживается только для объектов класса 'Дробь'")
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == other.numerator * self.denominator
        else:
            return False
    def __ne__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator != other.numerator * self.denominator
        else:
            return True
    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        else:
            raise TypeError("Операция поддерживается только для объектов класса 'Дробь'")
    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        else:
            raise TypeError("Операция поддерживается только для объектов класса 'Дробь'")
    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        else:
            raise TypeError("Операция поддерживается только для объектов класса 'Дробь'")
    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        else:
            raise TypeError("Операция поддерживается только для объектов класса 'Дробь'")
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    def pack(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
    @staticmethod
    def unpack(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)
    def pack_json(self, filename):
        with open(filename, "w") as file:
            json.dump({"numerator": self.numerator, "denominator": self.denominator}, file)
    @staticmethod
    def unpack_json(filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return Fraction(data["numerator"], data["denominator"])
def  execute_application():
    pass
if __name__=="__main__":
    execute_application()