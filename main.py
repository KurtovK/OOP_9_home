#Задание 3.
#Создайте класс Flat (квартира). Для данного класса реализуйте ряд
#перегруженных операторов:
#Проверка на равенство площадей квартир (операция ==);
#Проверка на неравенство площадей квартир (операция !=);
#Сравнение двух квартир по стоимости (операции >, <, <=, >=).
class Flat:
    def __init__(self, square: float, price_per_sq_m: float):
        self.__validate_square(square)
        self.__validate_price(price_per_sq_m)
        self.square = square
        self.__price_per_sq_m = price_per_sq_m

    def __validate_square(self, square: float):
        if not isinstance(square, (int, float)):
            raise TypeError("Площадь должна быть числом")
        if square <= 0:
            raise ValueError("Площадь должна быть положительной")

    def __validate_price(self, price_per_sq_m: float):
        if not isinstance(price_per_sq_m, (int, float)):
            raise TypeError("Цена за квадратный метр должна быть числом")
        if price_per_sq_m <= 0:
            raise ValueError("Цена за квадратный метр должна быть положительной")

    def is_flat(self, other):
        if not isinstance(other, Flat):
            raise TypeError(f"Сравнение выполнить невозможно "
                            f"между типом {self.__class__.__name__} "
                            f"и {other.__class__.__name__}")

    def __eq__(self, other):
        self.is_flat(other)
        return self.square == other.square

    def __ne__(self, other):
        self.is_flat(other)
        return self.square != other.square

    def __lt__(self, other):
        self.is_flat(other)
        return self.price < other.price

    def __gt__(self, other):
        self.is_flat(other)
        return self.price > other.price

    def __le__(self, other):
        self.is_flat(other)
        return self.price <= other.price

    def __ge__(self, other):
        self.is_flat(other)
        return self.price >= other.price

    @property
    def price(self):
        return self.square * self.__price_per_sq_m

    def __hash__(self):
        return hash((self.square, self.__price_per_sq_m))


def execute_application():
    f_1 = Flat(60, 20000)
    f_2 = Flat(50, 18000)
    try:
        print("Проверка на равно(=):", f_1 == f_2)
        print("Проверка на не равно (!=):", f_1 != f_2)
        print("Проверка на меньше (<):", f_1 < f_2)
        print("Проверка на больше (>):", f_1 > f_2)
        print("Проверка на меньше или равно (<=):", f_1 <= f_2)
        print("Проверка на больше или равно(>=):", f_1 >= f_2)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    execute_application()