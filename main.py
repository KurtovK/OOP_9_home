# Задача 2
#Создайте класс Point (точка). Для данного класса реализуйте ряд
#перегруженных операторов:
#Проверка на равенство пар координат по осям X и Y (операция ==, !=);
#Проверка сравнения пар координат (операции >, <, <=, >=);
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def __is_point(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"Сравнение выполнить невозможно "
                            f"между типом {self.__class__.__name__} "
                            f"и {other.__class__.__name__}")
    def __eq__(self, other):
        self.__is_point(other)
        return self.__x == other.x and self.__y == other.y

    def __ne__(self, other):
        self.__is_point(other)
        return not self.__eq__(other)

    def __lt__(self, other):
        self.__is_point(other)
        return (self.__x, self.__y) < (other.x, other.y)

    def __le__(self, other):
        self.__is_point(other)
        return (self.__x, self.__y) <= (other.x, other.y)

    def __gt__(self, other):
        self.__is_point(other)
        return (self.__x, self.__y) > (other.x, other.y)

    def __ge__(self, other):
        self.__is_point(other)
        return (self.__x, self.__y) >= (other.x, other.y)

    def __hash__(self):
        return hash((self.__x, self.__y))

def execute_application():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(1, 2)
    try:
        # проверка метода eq
        print("Проверка на равно (=):", p1.eq(p2))
        print("Проверка на равно (=):", p1.eq(p3))

        # проверка метода ne
        print("Проверка на не равно (!=):", p1.ne(p2))
        print("Проверка на не равно (!=):", p1.ne(p3))

        # проверка метода lt
        print("Проверка на меньше (<):", p1.lt(p2))
        print("Проверка на меньше (<):", p2.lt(p1))
        print("Проверка на меньше (<):", p1.lt(p3))

        # проверка метода le
        print("Проверка на меньше или равно (<=):", p1.le(p2))
        print("Проверка на меньше или равно (<=):", p2.le(p1))
        print("Проверка на меньше или равно (<=):", p1.le(p3))

        # проверка метода gt
        print("Проверка на больше (>):", p1.gt(p2))
        print("Проверка на больше (>):", p2.gt(p1))
        print("Проверка на больше (>):", p1.gt(p3))

        # проверка метода ge
        print("Проверка на больше или равно (>=):", p1.ge(p2))
        print("Проверка на больше или равно (>=):", p2.ge(p1))
        print("Проверка на больше или равно (>=):", p1.ge(p3))
    except TypeError as e:
        print(e)
if __name=="__main__":
    execute_application()