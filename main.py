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
        if not isinstance(base, int) or base < 2 or base > 36:
            raise ValueError("Недопустимая база")
        try:
            int(value, base)
        except ValueError:
            raise ValueError(f"Недопустимый номер {value} для данной базы {base}")
        self.__value = value
        self.__base = base

    @property
    def value(self):
        return self.__value

    @property
    def base(self):
        return self.__base

    def to_upper_case(self) -> 'Number':
        new_value = self.__value.upper()
        return Number(new_value, self.__base)

    def to_lower_case(self) -> 'Number':
        new_value = self.__value.lower()
        return Number(new_value, self.__base)

    def to_decimal(self) -> int:
        return int(self.__value, self.__base)

class Calculator:
    @staticmethod
    def with_base(number: Number, base: int) -> 'Number':
        if not isinstance(base, int) or base < 2 or base > 36:
            raise ValueError("Недопустимая база")
        if base == number.base:
            return number
        try:
            decimal_value = int(number.value, number.base)
        except ValueError:
            raise ValueError(f"Недопустимый номер {number.value} для системы счисления {number.base}")
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        if decimal_value == 0:
            return Number('0', base)
        new_value = ''
        while decimal_value > 0:
            digit_value = decimal_value % base
            new_value = digits[digit_value] + new_value
            decimal_value //= base
        return Number(new_value, base)

def execute_application():
    try:
        number1 = Number('10101010', 2)
        number2 = Number('777', 8)
        number3 = Number('abcd', 16)
        number4 = Number('12345', 10)
        number5 = Number('1aBcDeF', 16)

        print(f'Число {number1.value} в системе счисления {number1.base} в восьмеричной системе: {Calculator.with_base(number1, 8).value}')
        print(f'Число {number1.value} в системе счисления {number1.base} в десятичной системе: {Calculator.with_base(number1, 10).value}')
        print(f'Число {number1.value} в системе счисления {number1.base} в шестнадцатеричной системе: {Calculator.with_base(number1, 16).value}')

        print(f'Число {number2.value} в системе счисления {number2.base} в восьмеричной системе: {Calculator.with_base(number2, 8).value}')
        print(f'Число {number2.value} в системе счисления {number2.base} в шестнадцатеричной системе: {Calculator.with_base(number2, 16).value}')
        print(f'Число {number2.value} в системе счисления {number2.base} в двоичной системе: {Calculator.with_base(number2, 2).value}')
        print(f'Число {number2.value} в системе счисления {number2.base} в десятичной системе: {Calculator.with_base(number2, 10).value}')

        print(f'Число {number3.value} в системе счисления {number3.base} в восьмеричной системе: {Calculator.with_base(number3, 8).value}')
        print(f'Число {number3.value} в системе счисления {number3.base} в шестнадцатеричной системе: {Calculator.with_base(number3, 16).value}')
        print(f'Число {number3.value} в системе счисления {number3.base} в двоичной системе: {Calculator.with_base(number3, 2).value}')
        print(f'Число {number3.value} в системе счисления {number3.base} в шестнадцатеричной системе и обратно:{Calculator.with_base(Calculator.with_base(number3, 16), 10).value}')
        print(f'Число {number4.value} в системе счисления {number4.base} в восьмеричной системе: {Calculator.with_base(number4, 8).value}')
        print(f'Число {number4.value} в системе счисления {number4.base} в двоичной системе: {Calculator.with_base(number4, 2).value}')
        print(f'Число {number4.value} в системе счисления {number4.base} в десятичной системе: {Calculator.with_base(number4, 10).value}')
    
        print(f'Число {number5.value} в системе счисления {number5.base} в десятичной системе: {Calculator.with_base(number5, 10).value}')
        print(f'Число {number5.value} в системе счисления {number5.base} в двоичной системе: {Calculator.with_base(number5, 2).value}')
        print(f'Число {number5.value} в системе счисления {number5.base} в восьмеричной системе: {Calculator.with_base(number5, 8).value}')

    
    except ValueError as e:
        print(f"Произошла ошибка: {str(e)}")
if __name__ == '__main__':
    execute_application()
