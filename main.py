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
    pass
if __name=="__main__":
    execute_application()