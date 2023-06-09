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
    def __init__(self, value: str, base: int):
        if base not in [2, 8, 10, 16]:
            raise ValueError("Недопустимая база")
        try:
            int(str(value), base)
        except ValueError:
            raise ValueError("Недопустимый номер для данной базы")
        self.__value = value
        self.__base = base
    @property
    def value(self):
        return self.__value

    @property
    def base(self):
        return self.__base

class Calculator:
    @staticmethod
    def to_octal(number: Number) -> Number:
        if number.base == 8:
            return number.value
        if number.base != 10:
            number = Number(int(number.value, number.base), 10)
        return oct(int(number.value))[2:]

    @staticmethod
    def to_hexadecimal(number: Number) -> Number:
        if number.base == 16:
            return number.value
        if number.base != 10:
            number = Number(int(number.value, number.base), 10)
        return hex(int(number.value))[2:]

    @staticmethod
    def to_binary(number: Number) -> Number:
        if number.base == 2:
            return number.value
        if number.base != 10:
            number = Number(int(number.value, number.base), 10)
        return bin(int(number.value))[2:]

    @staticmethod
    def to_decimal(number: Number) -> Number:
        if number.base == 10:
            return number.value
        return str(int(number.value, number.base))
def execute_application():
    try:
        number1 = Number('1101', 2)
        number2 = Number('ABC', 16)

        print(f'Число {number1.value} в системе счисления {number1.base} в восьмеричной системе: {Calculator.to_octal(number1)}')
        print(f'Число {number1.value} в системе счисления {number1.base} в шестнадцатеричной системе: {Calculator.to_hexadecimal(number1)}')
        print(f'Число {number1.value} в системе счисления {number1.base} в двоичной системе: {Calculator.to_binary(number1)}')
        print(f'Число {number1.value} в системе счисления {number1.base} в десятичной системе: {Calculator.to_decimal(number1)}')

        print(f'Число {number2.value} в системе счисления {number2.base} в восьмеричной системе: {Calculator.to_octal(number2)}')
        print(f'Число {number2.value} в системе счисления {number2.base} в шестнадцатеричной системе: {Calculator.to_hexadecimal(number2)}')
        print(f'Число {number2.value} в системе счисления {number2.base} в двоичной системе: {Calculator.to_binary(number2)}')
        print(f'Число {number2.value} в системе счисления {number2.base} в десятичной системе: {Calculator.to_decimal(number2)}')

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    execute_application()