git branch#Задание 1.
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
        if not isinstance(value, str):
            value = str(value)
        if not isinstance(value, str):
            raise ValueError("Значение должно быть строкой, содержащей число")
        if not isinstance(base, int) or base not in [2, 8, 10, 16]:
            raise ValueError("Недопустимая база")
        if base == 2 and any(digit not in ['0', '1'] for digit in value):
            raise ValueError(f"Недопустимый номер {value} для данной базы {base}")
        if base == 8 and any(digit not in ['0', '1', '2', '3', '4', '5', '6', '7'] for digit in value):
            raise ValueError(f"Недопустимый номер {value} для данной базы {base}")
        if base == 10 and any(digit not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] for digit in value):
            raise ValueError(f"Недопустимый номер {value} для данной базы {base}")
        if base == 16 and any(
                digit not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'] for digit
                in value.lower()):
            raise ValueError(f"Недопустимый номер {value} для данной базы {base}")
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
        if not isinstance(base, int) or base not in [2, 8, 10, 16]:
            raise ValueError("Недопустимая база")
        if base == number.base:
            return number
        try:
            decimal_value = int(number.value, number.base)
        except ValueError:
            raise ValueError(f"Недопустимый номер {number.value} для системы счисления {number.base}")
        digits = "0123456789abcdef"
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
        print(f'Число {number3.value} в системе счисления {number3.base} в шестнадцатеричной системе и обратно: {Calculator.with_base(Calculator.with_base(number3, 16), 10).value}')

        print(f'Число {number4.value} в системе счисления {number4.base} в восьмеричной системе: {Calculator.with_base(number4, 8).value}')
        print(f'Число {number4.value} в системе счисления {number4.base} в двоичной системе: {Calculator.with_base(number4, 2).value}')
        print(f'Число {number4.value} в системе счисления {number4.base} в десятичной системе: {Calculator.with_base(number4, 10).value}')



    except ValueError as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == '__main__':
    execute_application()