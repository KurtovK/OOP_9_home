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
class Fraction:
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
    pass
if __name__=="__main__":
    execute_application()