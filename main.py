# Задача 2
#Создайте класс Point (точка). Для данного класса реализуйте ряд
#перегруженных операторов:
#Проверка на равенство пар координат по осям X и Y (операция ==, !=);
#Проверка сравнения пар координат (операции >, <, <=, >=);
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__x = self._validate_coordinate(x)
        self.__y = y
        self.__y = self._validate_coordinate(y)



    def _validate_coordinate(self, coord):
        if not isinstance(coord, int):
            raise TypeError(f"Координата должна быть целым числом, "
                            f"вместо этого получено значение: {coord}")


    def __eq__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"Сравнение выполнить невозможно "
                            f"между типом {type(self)} "
                            f"и {type(other)}")
        return self.__x == other.__x == self.__y == other.__y

    def __ne__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"Сравнение выполнить невозможно "
                            f"между типом {type(self)} "
                            f"и {type(other)}")
        return self.__x == other.__x != self.__y == other.__y

    def __lt__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"Сравнение выполнить невозможно "
                            f"между типом {type(self)} "
                            f"и {type(other)}")
        return (self.__x, self.__y) < (other.__x, other.__y)

    def __le__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"Сравнение выполнить невозможно "
                            f"между типом {type(self)} "
                            f"и {type(other)}")
        return (self.__x, self.__y) <= (other.__x, other.__y)

    def __gt__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"Сравнение выполнить невозможно "
                            f"между типом {type(self)} "
                            f"и {type(other)}")
        return (self.__x, self.__y) > (other.__x, other.__y)

    def __ge__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"Сравнение выполнить невозможно "
                            f"между типом {type(self)} "
                            f"и {type(other)}")
        return (self.__x, self.__y) >= (other.__x, other.__y)

    def __hash__(self):
        return hash((self.__x, self.__y))


def execute_application():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(1, 2)
    try:
        # проверка метода eq
        print("Проверка на равно (==):", p1 == p2)
        print("Проверка на равно (==):", p1 == p3)

        # проверка метода ne
        print("Проверка на не равно (!=):", p1 != p2)
        print("Проверка на не равно (!=):", p1 != p3)

        # проверка метода lt
        print("Проверка на меньше (<):", p1 < p2)
        print("Проверка на меньше (<):", p2 < p1)
        print("Проверка на меньше (<):", p1 < p3)

        # проверка метода le
        print("Проверка на меньше или равно (<=):", p1 <= p2)
        print("Проверка на меньше или равно (<=):", p2 <= p1)
        print("Проверка на меньше или равно (<=):", p1 <= p3)

        # проверка метода gt
        print("Проверка на больше (>):", p1 > p2)
        print("Проверка на больше (>):", p2 > p1)
        print("Проверка на больше (>):", p1 > p3)

        # проверка метода ge
        print("Проверка на больше или равно (>=):", p1 >= p2)
        print("Проверка на больше или равно (>=):", p2 >= p1)
        print("Проверка на больше или равно (>=):", p1 >= p3)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    execute_application()