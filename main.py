import math
#Задание 1.
#Создайте класс Обыкновенная дробь. Используя перегрузку операторов
#реализуйте для него арифметические операции и операции сравнения для
#работы с обыкновенными дробями.
#В классе должна быть реализована следующая функциональность:
# Сложение дробей;
# Вычитание дробей;
# Умножение дробей;
# Деление дробей.
# Сравнение дробей
#В т.ч. Перегрузка операций должна работать с целыми числам
class Fraction():
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
def  execute_application():
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    f3 = Fraction(2, 4)
    print(f"Операция сложения двух дробей: {f1} + {f2} = {f1 + f2}")
    print(f"Операция вычитания двух дробей: {f2} - {f1} = {f2 - f1}")
    print(f"Операция умножения двух дробей: {f1} * {f2} = {f1 * f2}")
    print(f"Операция деления двух дробей: {f1} / {f2} = {f1 / f2}")
    print(f"Сравнение двух дробей: {f1} == {f3} - {f1 == f3}")
    print(f"Сравнение двух дробей: {f1} < {f2} - {f1 < f2}")
    print(f"Сравнение двух дробей: {f2} > {f3} - {f2 > f3}")

    # Операции с целыми числами:
    f4 = Fraction(1, 2)
    print(f"Операция сложения дроби и целого числа: {f4} + 3 = {f4 + 3}")

    f5 = Fraction(25, 5)
    print(f"Сравнение дроби и целого числа: {f5} == 5 - {f5 == 5}")

    f6 = Fraction(8, 5)
    print(f"Сравнение дроби и целого числа: {f6} > 2 - {f6 > 2}")
if __name__=="__main__":
    execute_application()