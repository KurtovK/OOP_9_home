#Задание 1.
#Создайте класс «Число», которое хранит его значение и информацию о
#системе счисления. Создайте несколько экземпляров данного класса.
#Создайте класс «Калькулятор СС». В классе должна быть реализована
#следующая функциональность:
#Перевод числа в восьмеричную систему счисления.
#Перевод числа в шестнадцатеричную систему счисления.
#Перевод числа в двоичную систему счисления.
#Перевод числа в десятичную систему счисления.
class Number:
    def __init__(self, value, base):
        self.value = value
        self.base = base

class Calculator:
    def __init__(self, number):
        self.__number = number

    def to_octal(self):
        return oct(int(self.__number.value, self.__number.base))[2:]

    def to_hexadecimal(self):
        return hex(int(self.__number.value, self.__number.base))[2:]

    def to_binary(self):
        return bin(int(self.__number.value, self.__number.base))[2:]

    def to_decimal(self):
        return str(int(self.__number.value, self.__number.base))
def executer_application():
    number1 = Number('1101', 2)
    number2 = Number('ABC', 16)

    calculator1 = Calculator(number1)
    calculator2 = Calculator(number2)

    print(f'Число {number1.value} в системе счисления {number1.base} в восьмеричной системе: {calculator1.to_octal()}')
    print(
        f'Число {number1.value} в системе счисления {number1.base} в шестнадцатеричной системе: {calculator1.to_hexadecimal()}')
    print(f'Число {number1.value} в системе счисления {number1.base} в двоичной системе: {calculator1.to_binary()}')
    print(f'Число {number1.value} в системе счисления {number1.base} в десятичной системе: {calculator1.to_decimal()}')

    print(f'Число {number2.value} в системе счисления {number2.base} в восьмеричной системе: {calculator2.to_octal()}')
    print(
        f'Число {number2.value} в системе счисления {number2.base} в шестнадцатеричной системе: {calculator2.to_hexadecimal()}')
    print(f'Число {number2.value} в системе счисления {number2.base} в двоичной системе: {calculator2.to_binary()}')
    print(f'Число {number2.value} в системе счисления {number2.base} в десятичной системе: {calculator2.to_decimal()}')
if __name__ =="__main__":
    executer_application()