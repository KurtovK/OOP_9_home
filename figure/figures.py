from.management_file import FigureManagementFile

class __Shape:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        self.__y = y
    def info(self):
        print(f"Координаты точки: ({self.__x}, {self.__y})")

class Sguare(__Shape, FigureManagementFile):
    NAME = "Квадрат"
    def __init__(self, x: int, y: int, side: float):
        super().__init__(x, y)
        self.__side = side

    @property
    def side(self):
        return self.__side
    @side.setter
    def side(self, side:float):
        self.__side = side


class Circle(Shape, FigureManagementFile):
    pass

class Ellipse (Shape,FigureManagementFile):
    pass

